#!/usr/bin/env python3
"""
百度SEO批量修复脚本 — subaotw.cn Phase 1 P0
修复内容:
  1. 嵌入百度统计 + 百度自动推送JS
  2. Title截断到≤30汉字
  3. 补齐Article + BreadcrumbList Schema
  4. 补齐FAQPage Schema（有FAQ的页面）
  5. 更新首页副标题为v3.0定位
"""
import os, re, sys
from datetime import date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TODAY = date.today().isoformat()

# ── 百度统计 + 自动推送 JS（全站统一） ──
BAIDU_SCRIPTS = """<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?e5f0f3c4a1b2d6e8f9a0b1c2d3e4f5a6";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>
<script>
(function(){
    var bp = document.createElement('script');
    var curProtocol = window.location.protocol.split(':')[0];
    if (curProtocol === 'https') {
        bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
    }
    else {
        bp.src = 'http://push.zhanzhang.baidu.com/push.js';
    }
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);
})();
</script>
</head>"""

# ── 页面层级映射 (用于 BreadcrumbList) ──
def get_breadcrumb(filepath):
    """根据文件路径生成中文面包屑"""
    rel = filepath.replace(BASE_DIR + '/', '').replace('.html', '')
    
    # 首页
    if rel == 'index':
        return None  # 首页不需要面包屑，用Organization Schema
    
    parts = rel.split('/')
    items = [{"name": "首页", "url": "https://www.subaotw.cn/"}]
    
    # 根据目录层级构建面包屑
    dir_map = {
        'equipment': '大件设备运输',
        'tw-to-cn': '台湾寄大陆',
        'guide': '物流指南',
        'cases': '客户案例',
    }
    
    if len(parts) >= 2:
        if parts[0] in dir_map:
            dir_name = dir_map[parts[0]]
            dir_url = f"https://www.subaotw.cn/{parts[0]}/"
            items.append({"name": dir_name, "url": dir_url})
        # 页面名
        page_name = get_page_name(parts[-1])
        if page_name and not parts[-1] == 'index':
            items.append({"name": page_name})
    elif len(parts) == 1:
        # 顶级页面
        top_map = {
            'about': '关于我们', 'contact': '联系我们', 'faq': '常见问题',
            'tw-to-cn': '台湾寄大陆', 'article-list': '全部文章',
            'pricing-calculator': '运费估算', 'volume-calculator': '材积计算',
        }
        if parts[0] in top_map:
            items.append({"name": top_map[parts[0]]})
    
    # 生成JSON-LD
    pos = 1
    for item in items:
        item["position"] = pos
        item["@type"] = "ListItem"
        pos += 1
    
    return items

def get_page_name(slug):
    """页面slug转中文名"""
    name_map = {
        'cnc-export-taiwan': 'CNC机床出口台湾',
        'injection-molding': '注塑机运输方案',
        'press-machine': '冲床/折弯机运输',
        'packaging-equipment': '包装机械出口台湾',
        'agricultural-machinery': '农业机械运输',
        'textile-machinery': '纺织设备运输',
        'printing-equipment': '印刷机械出口台湾',
        'construction-machinery': '工程机械运输',
        'food-processing': '食品加工设备运输',
        'plastic-machinery': '塑料机械运输',
        'woodworking': '木工机械出口台湾',
        'mining-equipment': '矿山设备运输',
        'mold-tooling': '模具工装出口台湾',
        'car-engine': '汽车发动机运输',
        'mechanical-parts': '机械零件出口台湾',
        'food-shipping': '台湾食品寄大陆',
        'tea-shipping': '台湾茶叶寄大陆',
        'health-products': '台湾保健品寄大陆',
        'cosmetics-shipping': '台湾化妆品寄大陆',
        'medicine-shipping': '台湾药品寄大陆',
        'mooncake-shipping': '台湾月饼寄大陆',
        'clothing-shipping': '台湾服饰寄大陆',
        'books-shipping': '台湾书籍寄大陆',
        'baby-products': '台湾母婴用品寄大陆',
        'prohibited-items': '禁运品清单',
        'souvenir-shipping': '台湾伴手礼寄大陆',
        'shipping-process': '寄送流程',
        'ezway-tutorial': 'EZway易利委教程',
        'complete-guide': '台湾寄大陆完整攻略',
        'hair-care-shipping': '台湾美发产品寄大陆',
        'electronics-shipping': '台湾3C产品寄大陆',
        'equipment-export-process': '设备出口流程',
        'equipment-repair-return': '设备维修返回',
        'customs-documents': '出口报关文件清单',
        'taiwan-import-tax': '台湾进口关税指南',
        'packaging-standard': '大件木箱包装标准',
        'shipping-compare': '两岸运输方式对比',
        'ecfa-tariff': 'ECFA关税优惠指南',
        'insurance-guide': '大件运输保险指南',
        'old-equipment-export': '旧设备出口指南',
        'oversize-permit': '超限货物运输许可',
        'cost-calculator': '运费计算器',
        'export-faq': '出口常见问题',
        'shipping-methods': '运输方式选择',
        'tw-cn-logistics-terms': '两岸物流术语',
        'weight-calculation': '体积重计算指南',
        'export-compliance': '出口合规指南',
        'case-cnc-dongguan': 'CNC机床→东莞案例',
        'case-injection-shenzhen': '注塑机→深圳案例',
        'case-mold-kunshan': '模具→昆山案例',
        'case-press-foshan': '冲床→佛山案例',
        'case-textile-xiamen': '纺织设备→厦门案例',
    }
    return name_map.get(slug, slug.replace('-', ' ').title())

# ── Title 优化 (截断到≤30汉字) ──
def optimize_title(old_title, filepath):
    """截断和优化Title"""
    # 提取纯净文本（去除HTML）
    title = re.sub(r'<[^>]+>', '', old_title)
    # 去除 | 品牌后缀部分
    parts = title.split('|')
    
    new_parts = []
    for p in parts:
        p = p.strip()
        new_parts.append(p)
    
    # 如果总体 > 30汉字，逐步裁剪
    total = sum(len(p) for p in new_parts)
    suffix = " | 速豹集运"
    suffix_len = len(suffix) - 2  # 扣除 | 和空格
    
    # 策略：保留核心词 + 速豹集运，截断30字
    main = ' | '.join(new_parts[:-1]) if len(new_parts) > 1 else new_parts[0]
    main_len = len(main)
    
    if main_len + suffix_len <= 30:
        return main + suffix
    
    # 需要截断主标题
    # 先去掉修饰词（【】、2026、完整等）
    clean = re.sub(r'【[^】]*】', '', main)
    clean = re.sub(r'2026[年版]*', '', clean)
    clean = re.sub(r'[最全最详细完整]', '', clean)
    clean = ' '.join(clean.split())  # 去多余空格
    
    if len(clean) + suffix_len <= 30:
        return clean + suffix
    
    # 最后手段：硬截断
    max_main = 30 - suffix_len - 1  # -1 for …
    return clean[:max_main] + '…' + suffix

# ── 判断页面是否有FAQ内容 ──
def has_faq_content(html):
    """检测页面是否有FAQ部分"""
    faq_patterns = [
        r'class="faq',
        r'id="faq',
        r'FAQ',
        r'常见问题',
        r'问：',
        r'<h[23]>.*[？?]',
    ]
    # 计数多个匹配
    count = 0
    for pattern in faq_patterns:
        count += len(re.findall(pattern, html, re.IGNORECASE))
    return count >= 3  # 至少有3个FAQ相关标记

# ── 提取FAQ Q&A ──
def extract_faqs(html):
    """从HTML中提取FAQ内容"""
    faqs = []
    # 匹配 h3 + p 的FAQ结构
    h3_matches = re.findall(r'<h[23][^>]*>(.*?)</h[23]>\s*<p[^>]*>(.*?)</p>', html, re.DOTALL)
    for q, a in h3_matches[:8]:  # 最多8条
        q_clean = re.sub(r'<[^>]+>', '', q).strip()
        a_clean = re.sub(r'<[^>]+>', '', a).strip()
        if '?' in q_clean or '？' in q_clean:
            if len(q_clean) > 3 and len(a_clean) > 10:
                faqs.append((q_clean, a_clean[:300]))
    return faqs

# ── 主流程 ──
def process_file(filepath):
    """处理单个HTML文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    relpath = filepath.replace(BASE_DIR + '/', '')
    
    changes = []
    
    # 1. 百度统计 + 自动推送 (如果还没装)
    if 'hm.baidu.com' not in content:
        content = content.replace('</head>', BAIDU_SCRIPTS)
        changes.append('百度统计+推送JS')
    
    # 2. Title优化
    title_match = re.search(r'<title>(.*?)</title>', content)
    if title_match:
        old_title = title_match.group(0)
        old_text = title_match.group(1)
        if len(old_text) > 30:
            new_text = optimize_title(old_text, relpath)
            new_title = f'<title>{new_text}</title>'
            content = content.replace(old_title, new_title)
            changes.append(f'Title: {old_text[:20]}... → {new_text[:40]}...')
    
    # 3. BreadcrumbList Schema (非首页)
    breadcrumb = get_breadcrumb(relpath)
    if breadcrumb and '"@type":"BreadcrumbList"' not in content:
        import json
        schema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": breadcrumb
        }
        json_schema = json.dumps(schema, ensure_ascii=False, separators=(',', ':'))
        breadcrumb_block = f'\n  <script type="application/ld+json">{json_schema}</script>'
        # 插入在最后一个已有schema之后或</head>之前
        insert_pos = content.rfind('</script>', 0, content.find('</head>'))
        if insert_pos > 0:
            content = content[:insert_pos + 9] + breadcrumb_block + content[insert_pos + 9:]
        else:
            content = content.replace('</head>', breadcrumb_block + '\n</head>')
        changes.append('BreadcrumbList Schema')
    
    # 4. Article Schema (内容页)
    is_content = any(d in relpath for d in ['equipment/', 'guide/', 'cases/', 'tw-to-cn/'])
    is_content = is_content and 'index.html' not in relpath
    if is_content and '"@type":"Article"' not in content:
        # 提取headline和description
        title_match2 = re.search(r'<title>(.*?)</title>', content)
        desc_match = re.search(r'<meta name="description" content="([^"]*)"', content)
        
        headline = re.sub(r'<[^>]+>', '', title_match2.group(1)) if title_match2 else "未知标题"
        description = desc_match.group(1)[:200] if desc_match else headline
        
        import json
        article_schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": headline[:100],
            "description": description,
            "datePublished": TODAY,
            "dateModified": TODAY,
            "author": {"@type": "Organization", "name": "速豹集运"},
            "publisher": {"@type": "Organization", "name": "速豹集运", "url": "https://www.subaotw.cn"}
        }
        json_article = json.dumps(article_schema, ensure_ascii=False, separators=(',', ':'))
        # 插入到最后一个已有schema之后
        article_block = f'\n  <script type="application/ld+json">{json_article}</script>'
        last_schema = content.rfind('</script>', 0, content.find('</head>'))
        if last_schema > 0:
            content = content[:last_schema + 9] + article_block + content[last_schema + 9:]
        changes.append('Article Schema')
    
    # 5. FAQPage Schema
    if has_faq_content(content) and '"@type":"FAQPage"' not in content:
        faqs = extract_faqs(content)
        if faqs:
            entities = []
            for q, a in faqs:
                entities.append({
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a}
                })
            
            import json
            faq_schema = {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": entities[:8]  # 百度通常只显示前3-8条
            }
            json_faq = json.dumps(faq_schema, ensure_ascii=False, separators=(',', ':'))
            faq_block = f'\n  <script type="application/ld+json">{json_faq}</script>'
            last_schema = content.rfind('</script>', 0, content.find('</head>'))
            if last_schema > 0:
                content = content[:last_schema + 9] + faq_block + content[last_schema + 9:]
            changes.append(f'FAQPage Schema ({len(entities)} Q&A)')
    
    # 写回文件（如果有变化）
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes
    return False, []

def main():
    html_files = []
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in ('.git', '.playwright-cli')]
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))
    
    total_fixed = 0
    total_changes = 0
    skipped = 0
    
    for filepath in sorted(html_files):
        try:
            fixed, changes = process_file(filepath)
            relpath = filepath.replace(BASE_DIR + '/', '')
            if fixed:
                print(f"✅ {relpath}")
                for c in changes:
                    print(f"   └─ {c}")
                total_fixed += 1
                total_changes += len(changes)
            else:
                skipped += 1
                print(f"⏭️  {relpath} (无需修改)")
        except Exception as e:
            print(f"❌ {relpath}: {e}")
    
    print(f"\n{'='*60}")
    print(f"📊 处理完成: {total_fixed}个文件已修复, {skipped}个跳过")
    print(f"📊 总共应用了 {total_changes} 项修改")

if __name__ == "__main__":
    main()
