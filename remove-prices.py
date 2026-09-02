#!/usr/bin/env python3
"""全站删除大陆→台湾运费价格引用"""
import os, re, json

BASE = '/Users/mac/WorkBuddy/Claw/物流項目/sites/subaotw-cn'

# 大陆→台湾方向页面（排除tw-to-cn台湾→大陆方向）
TARGET_DIRS = ['equipment/', 'guide/', 'cases/', '.']  # . 是根目录新页面
EXCLUDE = ['tw-to-cn/', 'pricing-calculator.html', 'contact.html', 'nav-preview.html']

def is_target(path):
    rel = os.path.relpath(path, BASE)
    for e in EXCLUDE:
        if e in rel:
            return False
    for d in TARGET_DIRS:
        if d == '.' and '/' not in rel:
            return True
        if rel.startswith(d):
            return True
    return False

def remove_price_tables(html):
    """删除含价格数据的完整table块"""
    # 匹配<table>...</table>包含价格关键词的
    patterns = [
        r'<table[^>]*>.*?(NT\$|元/|约.*元|费用.*参考|价格|运费.*元).*?</table>',
    ]
    for p in patterns:
        html = re.sub(p, '<p style="color:#64748b;text-align:center">💰 具体运费请<a href="/contact">联系我们</a>获取实时报价</p>', html, flags=re.DOTALL)
    return html

def remove_price_lists(html):
    """删除费用明细列表"""
    # 匹配 <ul> 或 <ol> 包含价格数据的
    patterns = [
        r'(打包费|报关费|海运费|送货费|存储费|熏蒸费|附加费|上楼费).*?</[uo]l>',
    ]
    for p in patterns:
        match = re.search(p, html, re.DOTALL)
        if match:
            block = match.group(0)
            # 检查是否包含金额
            if re.search(r'\d+[元块]', block):
                html = html.replace(block, '<p style="color:#64748b">💰 具体费用请<a href="/contact">联系我们</a>获取实时报价</p>')
    return html

def fix_price_faq_text(html):
    """修正正文中的FAQ价格问答"""
    # Q: XX多少钱/费用 → A: 联系我们获取报价
    replacements = [
        # 家具海运
        (r'<h3>家具海运到台湾要多少钱\?', '<h3>家具海运台湾怎么收费？'),
        (r'<p>家具海运费用取决于体积：拼柜约.*?送货。</p>',
         '<p>家具海运费用根据品类、体积、数量综合计算。实木家具需熏蒸，布艺家具不涉及。我们提供免费估价，<a href="/contact">点击咨询</a>获取精准报价。</p>'),
        
        # 搬家
        (r'<h3>大陆搬家到台湾大概需要多少钱\?', '<h3>大陆搬家到台湾怎么收费？'),
        (r'<p>搬家费用取决于物品体积和重量.*?送货上门全套服务。</p>',
         '<p>搬家费用根据物品体积、重量、服务内容综合计算。我们提供免费上门估价，<a href="/contact">点击咨询</a>获取精准搬家报价。</p>'),
        
        # 实木熏蒸
        (r'<p>实木家具海运台湾需要.*?退回或销毁。</p>',
         '<p>实木家具海运台湾需要：1) 熏蒸处理（防止虫害）2) 提供树种证明 3) 木箱包装。未经熏蒸处理的实木制品可能被台湾海关退回或销毁。熏蒸及包装费用请联系我们获取实时报价。</p>'),
        
        # 家电
        (r'<h3>大陆家电可以用在台湾吗\?', None),  # keep
        (r'<h3>大家电运到台湾要多少钱\?', None),  # handled below
        
        # 建材
        (r'<h3>卫浴洁具.*怎么运输\?', None),  # keep
    ]
    
    for old, new in replacements:
        if new and old in html:
            html = html.replace(old, new)
    
    return html

def clean_price_table_rows(html):
    """删除表格中含"费用"或"元"的行"""
    # 找到所有 <tr> 包含价格的数据行，替换为提示
    rows = re.findall(r'<tr>.*?(元|NT\$).*?</tr>', html, re.DOTALL)
    if rows:
        for row in rows[:1]:  # 只对第一个匹配替换
            replacement = '<tr><td colspan="4" style="text-align:center;color:#1a56db;padding:16px">💰 <a href="/contact" style="color:#1a56db;font-weight:700">联系我们</a> 获取实时报价（费用因货物类型/体积/时效而异）</td></tr>'
            html = html.replace(row, replacement)
        # 删除其余价格行
        for row in rows[1:]:
            html = html.replace(row, '')
    
    # 也清理整行独立的 <tr> 价格行
    price_rows = re.findall(r'<tr>.*?\d+[-~]\d+.*?</tr>', html)
    for row in price_rows[1:]:  # keep one, delete rest
        html = html.replace(row, '')
    
    return html

def clean_schema_faqs(html):
    """清理FAQPage Schema中的价格问答"""
    faq_match = re.search(r'"@type":"FAQPage".*?"mainEntity":(\[.*?\])', html, re.DOTALL)
    if not faq_match:
        return html
    
    try:
        entities = json.loads(faq_match.group(1))
    except:
        return html
    
    new_entities = []
    removed = 0
    for e in entities:
        q = e.get('name', '')
        a = e.get('acceptedAnswer', {}).get('text', '')
        combined = q + a
        
        # 跳过含价格的FAQ
        price_patterns = [
            r'\d+[-~]\d+元', r'NT\$', r'台币', r'多少[钱费]', r'费用.*元',
            r'约\d+', r'\d+元/', r'元/立方', r'元/kg', r'保费',
            r'货值.*元', r'\d+[-~]\d+.*元', r'\d+万',
        ]
        skip = False
        for pp in price_patterns:
            if re.search(pp, combined):
                skip = True
                break
        
        if skip:
            removed += 1
            continue
        
        # 修正"联系人获取报价"类FAQ（不去掉但修正措辞）
        if '联系' in combined or '报价' in combined:
            new_entities.append(e)
        else:
            new_entities.append(e)
    
    if removed > 0:
        # 替换FAQ Schema
        new_json = json.dumps(new_entities, ensure_ascii=False, separators=(',', ':'))
        html = html.replace(faq_match.group(1), new_json)
    
    return html

def remove_section_prices(html):
    """删除各级标题和相关价格段落"""
    # 匹配 <h2>费用</h2> 到下一个 <h2> 之间的内容
    sections = re.findall(r'<h[23][^>]*>(费用|价格|运费).*?</h[23]>.*?(?=<h[23]|</article>|</section>)', html, re.DOTALL)
    for sec in sections:
        if re.search(r'\d+[-~]\d+', sec):
            html = html.replace(sec, '<p style="color:#64748b;text-align:center;padding:16px">💰 <a href="/contact">联系我们获取实时报价</a></p>')
    
    return html

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()
    
    html = original
    
    # 应用所有清理
    html = remove_price_tables(html)
    html = remove_price_lists(html)
    html = fix_price_faq_text(html)
    html = clean_price_table_rows(html)
    html = clean_schema_faqs(html)
    html = remove_section_prices(html)
    
    # 清理残留的零散价格数字（在HTML内容中，不破坏Schema JSON）
    # 替换"约XXX元" → "联系我们获取报价"
    html = re.sub(r'约\d{3,6}[-~]\d{3,6}元', '联系我们获取报价', html)
    html = re.sub(r'NT\$[\d,]+[-~][\d,]+', '联系我们获取报价', html)
    
    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return True
    return False

def main():
    html_files = []
    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in ('.git',)]
        for f in files:
            if f.endswith('.html') and f != '404.html':
                html_files.append(os.path.join(root, f))
    
    cleaned = 0
    for fp in sorted(html_files):
        if is_target(fp):
            if process_file(fp):
                rel = os.path.relpath(fp, BASE)
                print(f'✅ {rel}')
                cleaned += 1
    
    print(f'\n📊 已清理 {cleaned} 个文件的价格引用')

if __name__ == '__main__':
    main()
