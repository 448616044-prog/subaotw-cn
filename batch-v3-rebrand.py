#!/usr/bin/env python3
"""
全站定位升级脚本：大件设备 → 大件物流
应用于 subaotw.cn 全部74个HTML页面
"""

import os, re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ═════════════════════════════════════════════════════════
# 全局替换规则（按顺序执行）
# ═════════════════════════════════════════════════════════

GLOBAL_REPLACEMENTS = [
    # 1. Logo文字
    ('<span>大件设备·两岸快递</span>', '<span>两岸大件物流专家</span>'),
    
    # 2. Footer 标签行（多种变体）
    ('大件设备两岸专线 · 台湾寄大陆快递<br>6年经验，500+工厂信赖', 
     '两岸大件物流 · 搬家/设备/货运/建材<br>6年经验，500+企业信赖'),
    ('大件设备两岸专线 · 台湾寄大陆快递<br>6年经验，500+企业信赖',
     '两岸大件物流 · 搬家/设备/货运/建材<br>6年经验，500+企业信赖'),
    
    # 3. 导航保持不变 — "设备运输" 在导航中是正确的子类别
    # 但部分上下文需要调整
    
    # 4. 页面Title中的旧定位（保留设备关键词但换描述）
    # 这些由每页单独处理
]

# ═════════════════════════════════════════════════════════
# 页面级精确修复
# ═════════════════════════════════════════════════════════

def fix_about(filepath):
    """重写关于页面的定位"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fixes = [
        ('<title>关于我们 | 速豹集运 — 大件设备两岸专线</title>',
         '<title>关于速豹集运 | 两岸大件物流专家</title>'),
        
        ('<meta name="description" content="速豹集运专注两岸大件设备运输，6年经验，500+工厂信赖。CNC机床、注塑机、医疗仪器出口台湾专线。 免费获取大件设备出口台湾运费报价及运输方案，30分钟内回复。">',
         '<meta name="description" content="速豹集运 — 两岸大件物流专家。搬家/家具/设备/建材/大货大陆⇄台湾双向专线，6年经验，500+企业信赖。免费获取运输方案和报价，30分钟回复。">'),
        
        ('"description":"专业两岸物流服务商 — 大件设备运输专线 + 台湾寄大陆快递"',
         '"description":"两岸大件物流专家 — 搬家/家具/设备/建材/大货专线 + 台湾寄大陆快递"'),
        
        ('<meta property="og:title" content="关于我们 | 速豹集运 — 大件设备两岸专线">',
         '<meta property="og:title" content="关于速豹集运 | 两岸大件物流专家 | 搬家/设备/货运专线">'),
        
        ('<meta property="og:description" content="速豹集运专注两岸大件设备运输，6年经验，500+工厂信赖。CNC机床、注塑机、医疗仪器出口台湾专线。 免费获取大件设备出口台湾运费报价及运输方案，30分钟内回复。">',
         '<meta property="og:description" content="速豹集运 — 两岸大件物流专家。大陆⇄台湾搬家、家具、设备、建材、大货双向运输专线，6年经验500+企业信赖，免费方案报价。">'),
        
        ('6年专注两岸物流，500+工厂的信赖之选',
         '两岸大件物流专家，搬家·家具·设备·建材·大货全覆盖'),
        
        ('速豹集运成立于2020年，总部位于深圳，是国内领先的两岸物流服务商。我们专注于大陆至台湾的大件设备运输和台湾至大陆的快递服务，已累计服务500+工厂客户。',
         '速豹集运成立于2020年，是国内领先的两岸大件物流服务商。我们专注大陆⇄台湾双向大件运输：搬家、家具、设备、建材、商业大货，以及台湾寄大陆敏感货快递。6年累计服务500+企业客户，处理超过50,000件跨境货物。'),
        
        ('<h3>大件设备运输</h3>',
         '<h3>大陆→台湾 大件物流</h3>'),
        
        ('发设备参数，30分钟内收到运输方案和精准报价',
         '发送货物信息，30分钟内收到运输方案和精准报价'),
        
        ('<div><strong>30分钟出方案</strong><p>发设备参数，30分钟内收到运输方案和精准报价</p></div>',
         '<div><strong>30分钟出方案</strong><p>发货物信息，30分钟内收到运输方案和精准报价</p></div>'),
        
        ('准备好发设备到台湾了吗？',
         '准备好发货到台湾了吗？'),
        
        ('发送设备信息，30分钟内获取运输方案和报价',
         '发送货物信息，30分钟内获取运输方案和报价'),
    ]
    
    for old, new in fixes:
        if old in content:
            content = content.replace(old, new)
        else:
            print(f"  ⚠️ about.html: pattern not found: {old[:60]}...")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("  ✅ about.html 定位重写完成")

def fix_contact(filepath):
    """重写联系/询价页面"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fixes = [
        ('<title>联系我们 | 大件设备运输询价 | 速豹集运</title>',
         '<title>联系我们 | 大件物流询价 | 两岸搬家/设备/货运 | 速豹集运</title>'),
        
        ('<meta name="description" content="大件设备出口台湾实时报价：发送货物尺寸/重量/目的地，30分钟内获取含全部费用的精确报价。最低消费、偏远费、超材费、叉车费透明公开。 偏远费、超材费、叉车费、报关费全透明，无隐藏收费，速豹集运6年两岸物流经验。">',
         '<meta name="description" content="两岸大件物流实时报价：搬家/家具/设备/建材/大货运输。发送货物尺寸和目的地，30分钟内获取含全部费用的精确报价。速豹集运6年两岸物流经验，透明收费。">'),
        
        ('<meta property="og:title" content="联系我们 | 大件设备运输询价 | 速豹集运">',
         '<meta property="og:title" content="联系我们 | 两岸大件物流询价 | 速豹集运">'),
        
        ('<meta property="og:description" content="大件设备出口台湾实时报价：发送货物尺寸/重量/目的地，30分钟内获取含全部费用的精确报价。最低消费、偏远费、超材费、叉车费透明公开。 偏远费、超材费、叉车费、报关费全透明，无隐藏收费，速豹集运6年两岸物流经验。">',
         '<meta property="og:description" content="两岸大件物流实时报价：搬家/家具/设备/建材/大货。发送货物详情，30分钟出含全部费用的精确报价。速豹集运，透明收费。">'),
        
        ('<h1>大件设备运输 — 实时报价</h1>',
         '<h1>大件物流 — 实时报价</h1>'),
        
        ('<p style="color:var(--l)">大件海运按实际货物计费，发送以下信息即可获得<strong>含全部费用的精确报价</strong>。</p>',
         '<p style="color:var(--l)">搬家/家具/设备/建材/大货，按实际货物计费。发送以下信息即可获得<strong>含全部费用的精确报价</strong>。</p>'),
    ]
    
    for old, new in fixes:
        if old in content:
            content = content.replace(old, new)
        else:
            print(f"  ⚠️ contact.html: pattern not found: {old[:60]}...")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("  ✅ contact.html 定位重写完成")

def fix_faq(filepath):
    """重写FAQ页面"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fixes = [
        ('<title>常见问题 | 大件设备运输FAQ | 速豹集运</title>',
         '<title>常见问题 | 两岸大件物流FAQ | 搬家/设备/货运 | 速豹集运</title>'),
        
        ('<meta name="description" content="大件设备出口台湾常见问题：运输费用、报关文件、时效、保险、包装标准。CNC机床/注塑机/医疗仪器运输FAQ。 提供运费报价、报关方案、包装指导、保险咨询。速豹集运6年两岸物流经验，免费咨询。">',
         '<meta name="description" content="两岸大件物流常见问题：搬家/家具/设备/建材运输费用、报关文件、时效、保险、包装标准。搬家FAQ、设备运输FAQ、货运FAQ一站式解答。速豹集运6年两岸物流经验。">'),
        
        ('<meta property="og:title" content="常见问题 | 大件设备运输FAQ | 速豹集运">',
         '<meta property="og:title" content="常见问题 | 两岸大件物流FAQ | 速豹集运">'),
        
        ('<meta property="og:description" content="大件设备出口台湾常见问题：运输费用、报关文件、时效、保险、包装标准。CNC机床/注塑机/医疗仪器运输FAQ。 提供运费报价、报关方案、包装指导、保险咨询。速豹集运6年两岸物流经验，免费咨询。">',
         '<meta property="og:description" content="两岸大件物流常见问题：搬家/家具/设备/建材运输FAQ一站式解答。速豹集运6年两岸物流经验，免费咨询。">'),
    ]
    
    for old, new in fixes:
        if old in content:
            content = content.replace(old, new)
        else:
            print(f"  ⚠️ faq.html: pattern not found: {old[:60]}...")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("  ✅ faq.html 定位重写完成")

def fix_equipment_index(filepath):
    """重写设备总览页 — 保持内容但调整定位框"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fixes = [
        ('<title>台湾大件设备运输 | 机械/仪器/设备出口台湾专线 | 速豹集运</title>',
         '<title>大件设备运输台湾 | CNC/注塑机/机械出口台湾专线 | 速豹集运</title>'),
        
        ('"description": "专注台湾大件设备运输，CNC机床、注塑机、冲床、农业机械等15大品类出口台湾专线。整柜/拼柜/散货均可，提供木箱包装、报关清关、门到门服务。 速豹集运6年两岸设备运输经验，覆盖CNC/注塑机/冲床/纺织/印刷/木工/食品加工等品类，免费获取运费报价。">',
         '速豹集运大件设备运输台湾专线：CNC机床、注塑机、冲床、纺织机械等15大品类出口台湾。整柜/拼柜、木箱包装、报关清关、门到门一站式。免费获取设备出口报价。'),
        
        ('"headline": "大件设备运输服务"',
         '"headline": "大陆大件设备出口台湾运输服务"'),
        
        ('<meta property="og:title" content="台湾大件设备运输 | 机械/仪器/设备出口台湾专线 | 速豹集运">',
         '<meta property="og:title" content="大件设备运输台湾 | CNC/注塑机/机械出口台湾专线 | 速豹集运">'),
        
        ('<meta property="og:description" content="专注台湾大件设备运输，CNC机床、注塑机、冲床、农业机械等15大品类出口台湾专线。整柜/拼柜/散货均可，提供木箱包装、报关清关、门到门服务。 速豹集运6年两岸设备运输经验，覆盖CNC/注塑机/冲床/纺织/印刷/木工/食品加工等品类，免费获取运费报价。">',
         '<meta property="og:description" content="速豹集运大件设备运输台湾专线：CNC机床、注塑机、冲床、纺织机械等15大品类。整柜拼柜、木箱包装、报关清关、门到门。免费获取设备出口报价。">'),
        
        ('<h1>大件设备运输台湾专线</h1>',
         '<h1>大件设备出口台湾专线</h1>'),
    ]
    
    for old, new in fixes:
        if old in content:
            content = content.replace(old, new)
        else:
            print(f"  ⚠️ equipment/index.html: pattern not found: {old[:60]}...")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("  ✅ equipment/index.html 定位调整完成")

def fix_guide_index(filepath):
    """重写指南总览页"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fixes = [
        ('<title>设备出口台湾指南 | 大件设备两岸物流全攻略 | 速豹集运</title>',
         '<title>大件物流指南 | 两岸运输全攻略 | 搬家/设备/货运 | 速豹集运</title>'),
        
        ('<meta name="description" content="大陆设备出口台湾一站式指南：全流程、报关文件、关税计算、包装标准、运输方式对比、ECFA优惠、保险、旧设备出口、费用预估。6年两岸设备运输经验，500+工厂信赖。">',
         '<meta name="description" content="两岸大件物流知识库：搬家流程、设备出口、家具运输、建材海运、报关文件、包装标准、运费计算。速豹集运6年经验，一站式物流指南。">'),
        
        ('"headline": "设备出口台湾指南 | 大件设备两岸物流全攻略 | 速豹集运"',
         '"headline": "两岸大件物流全攻略 | 搬家/设备/货运/建材运输指南"'),
        
        ('"description": "大陆设备出口台湾一站式指南：全流程、报关文件、关税计算、包装标准、运输方式对比、ECFA优惠、保险、旧设备出口、费用预估。6年两岸设备运输经验，500+工厂信赖。"',
         '"description": "两岸大件物流知识库：搬家流程、设备出口、货运拼柜、建材运输、报关文件、包装标准、运费计算。速豹集运6年经验。"'),
        
        ('"title": "设备出口台湾指南 | 大件设备两岸物流全攻略"',
         '"title": "两岸大件物流全攻略 | 搬家/设备/货运/建材运输指南"'),
    ]
    
    for old, new in fixes:
        if old in content:
            content = content.replace(old, new)
        else:
            print(f"  ⚠️ guide/index.html: pattern not found: {old[:60]}...")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("  ✅ guide/index.html 定位重写完成")

def fix_pricing_calculator(filepath):
    """修复定价页面"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # pricing-calculator footer is handled by global replacement
    # Just check logo
    if '大件设备·两岸快递' in content:
        print("  ⚠️ pricing-calculator.html: old logo found, should be fixed by global replacement")
    print("  ✅ pricing-calculator.html (handled by global replacements)")

def fix_404(filepath):
    """修复404页面的footer"""
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Global replacements handle footer/logo
    print("  ✅ 404.html (handled by global replacements)")

# ═════════════════════════════════════════════════════════
# 主流程
# ═════════════════════════════════════════════════════════

def main():
    html_files = []
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in ('.git',)]
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))
    
    # Phase 1: Global replacements
    print("📝 Phase 1: 全局替换...")
    global_fixes = 0
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        for old, new in GLOBAL_REPLACEMENTS:
            if old in content:
                content = content.replace(old, new)
                global_fixes += 1
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
    
    print(f"  ✅ 全局替换完成：{global_fixes} 处修改\n")
    
    # Phase 2: Page-specific fixes
    print("📝 Phase 2: 页面级精确修复...")
    
    fix_about(os.path.join(BASE_DIR, 'about.html'))
    fix_contact(os.path.join(BASE_DIR, 'contact.html'))
    fix_faq(os.path.join(BASE_DIR, 'faq.html'))
    fix_equipment_index(os.path.join(BASE_DIR, 'equipment/index.html'))
    fix_guide_index(os.path.join(BASE_DIR, 'guide/index.html'))
    
    # Verify logo and footer replacements
    print("\n📝 Phase 3: 验证...")
    remaining_old_logo = 0
    remaining_old_footer = 0
    for filepath in html_files:
        with open(filepath, 'r') as f:
            c = f.read()
        if '大件设备·两岸快递' in c:
            remaining_old_logo += 1
        if '大件设备两岸专线' in c:
            remaining_old_footer += 1
    
    if remaining_old_logo > 0:
        print(f"  ⚠️  还有 {remaining_old_logo} 个文件保留旧Logo文字")
    if remaining_old_footer > 0:
        print(f"  ⚠️  还有 {remaining_old_footer} 个文件保留旧Footer文字")
    
    if remaining_old_logo == 0 and remaining_old_footer == 0:
        print("  ✅ Logo和Footer已全部更新")
    
    print(f"\n📊 全站定位升级完成：{len(html_files)} 个文件已处理")

if __name__ == "__main__":
    main()
