#!/usr/bin/env python3
"""Generate city × category cross pages for subaotw.cn (大陆→台湾)"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
BLOG = os.path.join(BASE, 'blog')

# Top cities with port/industrial significance
CITIES = {
    'shanghai': {'name': '上海', 'port': '洋山港/外高桥', 'zone': '华东', 'transit': '5-7天', 'advantage': '华东最大港口，船期密集每周3-4班，设备/家具/建材出口首选', 'radius': '苏州、昆山、无锡、南通'},
    'shenzhen': {'name': '深圳', 'port': '蛇口/盐田', 'zone': '华南', 'transit': '3-5天', 'advantage': '华南最大口岸，电子产品/家具出口效率最高，船期稳定', 'radius': '东莞、惠州、广州南部'},
    'guangzhou': {'name': '广州', 'port': '南沙/黄埔', 'zone': '华南', 'transit': '4-6天', 'advantage': '千年商都，家具/建材/陶瓷出口重镇，拼柜资源丰富', 'radius': '佛山、中山、江门'},
    'xiamen': {'name': '厦门', 'port': '东渡/海沧', 'zone': '东南', 'transit': '2-3天', 'advantage': '距离台湾最近的大陆港口，时效最快，运费最低', 'radius': '泉州、漳州、龙岩'},
    'ningbo': {'name': '宁波', 'port': '舟山港/北仑', 'zone': '华东', 'transit': '5-7天', 'advantage': '全球第一大港（货物吞吐量），设备/小商品出口台湾成本低', 'radius': '绍兴、台州、温州'},
    'qingdao': {'name': '青岛', 'port': '前湾港', 'zone': '华北', 'transit': '7-9天', 'advantage': '北方最大港口，机械设备/建材出口台湾最佳选择', 'radius': '济南、潍坊、烟台'},
    'tianjin': {'name': '天津', 'port': '天津港', 'zone': '华北', 'transit': '7-9天', 'advantage': '华北第二大港，重工业设备/钢材出口便利', 'radius': '北京、廊坊、唐山'},
    'suzhou': {'name': '苏州', 'port': '经上海港', 'zone': '华东', 'transit': '6-8天', 'advantage': '制造业重镇，电子产品/精密设备出口台湾的最佳陆运+海运节点', 'radius': '无锡、常州、南通'},
    'chengdu': {'name': '成都', 'port': '经重庆港/泸州港', 'zone': '西南', 'transit': '8-10天', 'advantage': '西南最大城市，家具/建材/食品出口台湾的重要货源地', 'radius': '绵阳、德阳、乐山'},
    'chongqing': {'name': '重庆', 'port': '果园港/寸滩港', 'zone': '西南', 'transit': '7-9天', 'advantage': '长江上游最大内河港口，西南货物出海台湾的最佳水运节点', 'radius': '泸州、宜宾、遵义'},
    'wuhan': {'name': '武汉', 'port': '阳逻港', 'zone': '华中', 'transit': '6-8天', 'advantage': '长江中游最大港口，华中货物出海台湾的核心枢纽', 'radius': '襄阳、宜昌、黄石'},
    'hangzhou': {'name': '杭州', 'port': '经宁波港', 'zone': '华东', 'transit': '6-8天', 'advantage': '电商之都，家居/文创/食品出口台湾货源丰富', 'radius': '嘉兴、湖州、绍兴'},
    'nanjing': {'name': '南京', 'port': '龙潭港', 'zone': '华东', 'transit': '5-7天', 'advantage': '长江下游重要港口，华东货物出口台湾便捷节点', 'radius': '镇江、扬州、马鞍山'},
    'zhengzhou': {'name': '郑州', 'port': '经青岛港', 'zone': '中原', 'transit': '8-10天', 'advantage': '中原交通枢纽，机械设备/食品出口台湾的重要货源地', 'radius': '洛阳、开封、新乡'},
    'xian': {'name': '西安', 'port': '经青岛港/连云港', 'zone': '西北', 'transit': '9-11天', 'advantage': '西北核心城市，特色食品/手工艺品出口台湾货源', 'radius': '咸阳、宝鸡、渭南'},
    'changsha': {'name': '长沙', 'port': '经广州港/上海港', 'zone': '华中', 'transit': '7-9天', 'advantage': '华中消费重镇，食品/文创/家居出口台湾货源丰富', 'radius': '株洲、湘潭、岳阳'},
    'dongguan': {'name': '东莞', 'port': '经深圳港/虎门港', 'zone': '华南', 'transit': '4-6天', 'advantage': '世界工厂，电子/家具/玩具出口台湾货源密集', 'radius': '深圳、惠州、广州东部'},
    'foshan': {'name': '佛山', 'port': '经广州南沙港', 'zone': '华南', 'transit': '4-6天', 'advantage': '建材陶瓷之都，瓷砖/卫浴/家具出口台湾重镇', 'radius': '广州、中山、江门'},
    'fuzhou': {'name': '福州', 'port': '福州港/江阴港', 'zone': '东南', 'transit': '3-5天', 'advantage': '东南沿海港口，食品/建材/工艺品出口台湾便捷', 'radius': '莆田、宁德、三明'},
    'wenzhou': {'name': '温州', 'port': '经宁波港/温州港', 'zone': '华东', 'transit': '5-7天', 'advantage': '民营经济活跃，鞋服/小商品/五金出口台湾货源', 'radius': '台州、丽水、金华'},
    'quanzhou': {'name': '泉州', 'port': '泉州港/围头港', 'zone': '东南', 'transit': '2-4天', 'advantage': '闽南制造业重镇，鞋服/陶瓷/食品出口台湾的传统货源地', 'radius': '厦门、漳州、莆田'},
    'wuxi': {'name': '无锡', 'port': '经上海港/江阴港', 'zone': '华东', 'transit': '6-8天', 'advantage': '长三角制造业强市，机械/电子/纺织出口台湾货源', 'radius': '苏州、常州、江阴'},
    'changzhou': {'name': '常州', 'port': '经上海港', 'zone': '华东', 'transit': '6-8天', 'advantage': '苏南制造重镇，机械/光伏/家居出口台湾货源', 'radius': '无锡、镇江、宜兴'},
    'nantong': {'name': '南通', 'port': '南通港/经上海港', 'zone': '华东', 'transit': '6-8天', 'advantage': '沿海制造业城市，纺织/家具/机械出口台湾便捷', 'radius': '苏州、盐城、泰州'},
}

CATEGORIES = {
    'furniture': {
        'slug': 'furniture',
        'title_suffix': '家具海运台湾',
        'h1': '家具海运台湾',
        'keywords': '家具海运台湾,{city}家具寄台湾,{city}家具出口台湾,{city}海运家具到台湾',
        'desc_tmpl': '从{city}寄家具到台湾怎么运？{city}{port}直达台湾基隆/台北/台中/高雄，{transit}门到门。实木/红木/定制/办公家具专业木箱包装，拼柜省60%+。{advantage}。{radius}客户可就近发货。免费咨询报价→',
        'content_type': '家具',
        'examples': '沙发、实木餐桌、红木床、定制衣柜、办公桌、书柜',
        'volume_range': '10-25m³（整屋家具）或 1-5m³（单件家具）',
        'price_note': '拼柜约800-2000元/m³，20GP整柜约4000-8000元',
        'packaging': '缠绕膜+护角+木箱，实木家具需熏蒸证书',
        'steps': [
            '免费咨询：加微信发送家具照片/尺寸/目的地',
            '上门取件或自送仓库：{city}及{radius}可上门取件',
            '专业包装：防潮膜+木架木箱，实木熏蒸',
            '报关出口：代办出口报关，无需提供复杂证件',
            '海运：{city}{port}→基隆/台北/台中/高雄，{transit}海上运输',
            '台湾清关：专业清关团队办理',
            '送货上门：台湾全岛配送到家',
        ]
    },
    'equipment': {
        'slug': 'equipment',
        'title_suffix': '设备出口台湾',
        'h1': '设备出口台湾',
        'keywords': '{city}设备出口台湾,{city}机械出口台湾,{city}设备海运台湾,{city}工厂设备寄台湾',
        'desc_tmpl': '从{city}出口设备到台湾找谁？{city}{port}海运设备到台湾专线，{transit}全程门到门。CNC/注塑机/生产线/印刷机/包装机等工业设备专业运输——拆机→木箱包装→报关→海运→台湾送货。{advantage}。{radius}工厂可就近提货。免费咨询报价→',
        'content_type': '设备',
        'examples': 'CNC加工中心、注塑机、印刷机、包装机、食品加工设备、纺织机械、木工机械、生产线',
        'volume_note': '设备体积差异大，单件从1m³到20m³+不等',
        'price_note': '根据设备体积、重量、是否需拆机综合报价，一般2000-15000元/件',
        'packaging': '防锈油+缠绕膜+木箱+托盘固定，精密设备加防震',
        'steps': [
            '设备评估：发送设备照片/尺寸/重量获取方案',
            '拆机/包装：如需拆机，专业团队操作，木箱+防震包装',
            '提货运输：{city}及{radius}上门提货至{port}',
            '报关出口：代办设备出口报关',
            '海运：{city}{port}→基隆/台北/台中/高雄，{transit}',
            '台湾清关：代办进口报关',
            '送货+安装支持：台湾全岛配送，可协调安装',
        ]
    },
    'moving': {
        'slug': 'moving',
        'title_suffix': '搬家到台湾',
        'h1': '搬家到台湾',
        'keywords': '{city}搬家到台湾,{city}移民搬家台湾,{city}国际搬家台湾,{city}寄行李到台湾',
        'desc_tmpl': '从{city}搬家到台湾全攻略：{city}{port}海运搬家专线，{transit}门到门。个人行李/家具/家电/衣物/书籍一站式跨国运输，专业打包+报关+清关+台湾送货。{advantage}。{radius}上门打包取件。免费获取搬家方案→',
        'content_type': '搬家',
        'examples': '衣物鞋包、书籍、厨房用品、床上用品、小型家电、个人收藏品',
        'volume_range': '3-10m³（单身搬家）或 15-30m³（家庭搬家）',
        'price_note': '按立方米计费，约800-1500元/m³（含报关清关），整柜另议',
        'packaging': '专业搬家级纸箱+缠绕膜+标签分类，易碎品气泡膜防护',
        'steps': [
            '免费上门评估：{city}及{radius}专业人员上门评估物品体积',
            '专业打包：分类装箱+易碎品防护+标签编号',
            '提货运输：提货送至{port}',
            '报关出口：代办个人物品出口报关',
            '海运：{city}{port}→基隆/台北/台中/高雄，{transit}',
            '台湾清关+送货：清关后直送新家，拆箱摆放',
        ]
    },
    'building-materials': {
        'slug': 'building-materials',
        'title_suffix': '建材出口台湾',
        'h1': '建材出口台湾',
        'keywords': '{city}建材出口台湾,{city}建材海运台湾,{city}瓷砖寄台湾,{city}卫浴出口台湾',
        'desc_tmpl': '从{city}出口建材到台湾：{city}{port}建材海运专线，{transit}门到门。瓷砖/卫浴/门窗/石材/地板/玻璃等大件建材专业运输，防碎包装+整柜拼柜灵活选择。{advantage}。{radius}厂家可就近发货。免费获取建材运输方案→',
        'content_type': '建材',
        'examples': '瓷砖、卫浴洁具、铝合金门窗、石材台面、木地板、玻璃幕墙、建筑材料',
        'volume_note': '建材通常量大体积，建议拼柜（<20m³）或整柜（20-68m³）',
        'price_note': '拼柜约800-1500元/m³，20GP整柜约3500-6000元',
        'packaging': '木箱+木托盘+防潮膜，瓷砖类加隔层防碰撞',
        'steps': [
            '货物评估：发送建材品类/数量/尺寸获取方案',
            '专业包装：木箱木托盘+防潮+防碰撞包装',
            '提货或自送：{city}及{radius}提货至{port}',
            '报关出口：代办建材出口报关',
            '海运：{city}{port}→基隆/台北/台中/高雄，{transit}',
            '台湾清关：代办进口清关',
            '送货上门：台湾全岛配送',
        ]
    },
}

COMMON_FAQ = {
    'furniture': [
        ('{city}家具可以海运到台湾吗？', '可以！{city}有成熟的家具出口物流体系。通过{port}海运到台湾基隆/台北/台中/高雄，{transit}门到门。实木、红木、板式、软体家具均可运输，需要专业木箱包装防潮防碰。'),
        ('从{city}海运家具到台湾多少钱？', '重量、体积、品类不同价格不同。拼柜约800-2000元/m³，20GP整柜约4000-8000元。具体根据家具数量和体积计算，微信免费获取精准报价。'),
        ('{city}寄家具到台湾需要什么手续？', '不需要复杂手续。我们代办出口报关，你只需提供：①家具清单（品类/数量/价值）②台湾收货地址。实木家具需熏蒸证书（我们代办）。全程由速豹集运操作，你只需收货。'),
    ],
    'equipment': [
        ('{city}设备可以出口到台湾吗？', '可以！{city}{port}有成熟的设备出口物流通道。工业设备（CNC、注塑机、印刷机、生产线等）均可通过海运出口台湾。需要专业拆机、木箱包装、出口报关等流程，速豹集运全程代办。'),
        ('{city}出口设备到台湾要多长时间？', '整体流程约{transit}（海上运输）+ 3-5天（拆机包装+报关+台湾清关送货）= 总约{total_days}天。具体时效取决于设备拆装复杂度和报关进度。'),
        ('{city}出口设备到台湾要注意什么？', '①设备需清洁除油（不可有油污残留）②精密设备需防震包装 ③需提供设备品名/型号/用途（报关用）④大件设备需确认台湾收货地址能否进叉车。以上我们全程指导。'),
    ],
    'moving': [
        ('{city}搬家到台湾可以带什么？', '日常用品均可：衣物、书籍、厨房用品、床上用品、小型家电、个人收藏等。禁止携带：易燃易爆品、动植物制品（特殊审批除外）、武器弹药。不确定的物品可微信咨询确认。'),
        ('{city}搬家到台湾多少钱？', '按体积计费，约800-1500元/m³（含报关清关）。单身搬家约3-8m³，家庭搬家15-30m³。具体费用需上门评估后给出精确报价。'),
        ('从{city}搬家到台湾需要多久？', '全程{total_days}天左右（打包{pack_days}天+海运{transit}+清关配送{clear_days}天）。建议提前2-3周预约，留足打包和报关时间。'),
    ],
    'building-materials': [
        ('{city}建材出口台湾有哪些要求？', '建材出口台湾相对常规货物要求更严格：①瓷砖/卫浴需木箱+防震包装（易碎）②石材需托盘+缠绕膜 ③木质建材需熏蒸证书 ④需提供材质证明（部分品类）。我们专业操作建材出口，全程代办。'),
        ('{city}建材出口台湾要多少钱？', '拼柜约800-1500元/m³，20GP整柜约3500-6000元。建材量大时建议整柜运输更划算。具体价格根据品类、体积、目的地计算，微信免费报价。'),
        ('{city}到台湾建材海运时效多久？', '海运{transit}+陆运和报关约3-5天，总约{total_days}天门到门。建议提前1-2周安排发货，避开节假日报关高峰期。'),
    ],
}

def calc_total_days(city, cat):
    """Calculate total estimated days for a category"""
    transit_map = {'2-3天': 3, '3-5天': 5, '4-6天': 6, '5-7天': 7, '6-8天': 8, '7-9天': 9}
    base = transit_map.get(city['transit'], 7)
    if cat == 'equipment':
        return base + 7  # extra for disassembly
    elif cat == 'moving':
        return base + 5
    elif cat == 'building-materials':
        return base + 4
    else:
        return base + 3

def pack_clear_days(cat):
    if cat == 'equipment': return (3, 4)
    if cat == 'moving': return (2, 3)
    return (1, 2)

def generate_page(city_key, city, cat_key, cat):
    """Generate a single city×category cross page in blog/"""
    filename = f"city-{city_key}-{cat['slug']}-to-taiwan.html"
    filepath = os.path.join(BLOG, filename)
    
    # Title (within 30 chars for Baidu)
    title = f"{city['name']}{cat['title_suffix']}2026 | {city['name']}寄{cat['content_type']}到台湾 - 速豹集运"
    
    # Description (within 78 chars for Baidu)
    desc = cat['desc_tmpl'].format(
        city=city['name'], port=city['port'], transit=city['transit'],
        advantage=city['advantage'], radius=city['radius']
    )
    
    # Keywords
    keywords = cat['keywords'].format(city=city['name'])
    
    # Total days
    total_days = calc_total_days(city, cat_key)
    pd, cd = pack_clear_days(cat_key)
    
    # Generate FAQ
    faqs = COMMON_FAQ[cat_key]
    
    # Price guide
    price_extra = ""
    if cat_key == 'furniture':
        price_extra = f"""<tr><td>单人搬家/少量家具</td><td>3-8 m³</td><td>{cat['price_note']}</td></tr>
        <tr><td>家庭搬家/全屋家具</td><td>10-25 m³</td><td>10000-20000元</td></tr>"""
    elif cat_key == 'equipment':
        price_extra = f"""<tr><td>小型设备（<2吨）</td><td>1-5 m³</td><td>{cat['price_note']}</td></tr>
        <tr><td>中型设备（2-10吨）</td><td>5-15 m³</td><td>5000-10000元</td></tr>
        <tr><td>大型设备（>10吨）</td><td>15-30 m³</td><td>10000-25000元</td></tr>"""
    elif cat_key == 'moving':
        price_extra = f"""<tr><td>单身搬家</td><td>3-8 m³</td><td>{cat['price_note']}</td></tr>
        <tr><td>家庭搬家</td><td>15-30 m³</td><td>12000-30000元</td></tr>"""
    elif cat_key == 'building-materials':
        price_extra = f"""<tr><td>小批量建材</td><td>3-10 m³</td><td>{cat['price_note']}</td></tr>
        <tr><td>大批量建材</td><td>20-68 m³</td><td>整柜3500-8000元/柜</td></tr>"""
    
    # Build steps HTML
    steps_html = ""
    for i, step in enumerate(cat['steps'], 1):
        step_text = step.format(city=city['name'], port=city['port'], transit=city['transit'], radius=city['radius'])
        steps_html += f'<li><strong>{step_text.split("：")[0]}：</strong>{"：".join(step_text.split("：")[1:]) if "：" in step_text else step_text}</li>\n'
    
    # Build FAQ JSON
    faq_json_items = []
    faq_html = ""
    for q, a in faqs:
        q_formatted = q.format(city=city['name'], port=city['port'], transit=city['transit'], total_days=total_days, pack_days=pd, clear_days=cd)
        a_formatted = a.format(city=city['name'], port=city['port'], transit=city['transit'], total_days=total_days, pack_days=pd, clear_days=cd)
        faq_json_items.append(f'{{"@type":"Question","name":"{q_formatted}","acceptedAnswer":{{"@type":"Answer","text":"{a_formatted}"}}}}')
        faq_html += f'<div class="faq-item"><h3>Q: {q_formatted}</h3><p>A: {a_formatted}</p></div>\n'
    
    # Related city links
    other_cities = [c for c in CITIES if c != city_key][:5]
    related_links = "".join([f'<a href="/blog/city-{c}-{cat["slug"]}-to-taiwan.html">{CITIES[c]["name"]}{cat["title_suffix"]}</a>' for c in other_cities])
    
    # Volume info
    vol_info = ""
    if 'volume_range' in cat:
        vol_info = f'<tr><td>适用体积范围</td><td>{cat["volume_range"]}</td></tr>'
    elif 'volume_note' in cat:
        vol_info = f'<tr><td>适用体积</td><td>{cat["volume_note"]}</td></tr>'
    
    html = f"""<!DOCTYPE html>
<html lang="zh-CN"><head>
<meta http-equiv="Cache-Control" content="no-siteapp">
<meta name="applicable-device" content="pc,mobile">
<meta charset="UTF-8">
<meta name="robots" content="index,follow">
<meta name="lastmod" content="2026-07-23">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="baidu-site-verification" content="codeva-K4kVPs6NwjtWr4ij" />
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="canonical" href="https://www.subaotw.cn/blog/{filename.replace(".html","")}">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"速豹集运","url":"https://www.subaotw.cn"}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"首页","item":"https://www.subaotw.cn/"}},{{"@type":"ListItem","position":2,"name":"{city['name']}{cat['title_suffix']}","item":"https://www.subaotw.cn/blog/{filename.replace('.html','')}"}}]}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{','.join(faq_json_items)}]}}</script>
<script type="application/ld+json">{{"@context":"https://ziyuan.baidu.com/contexts/cambrian.jsonld","@type":"WebPage","title":"{title}","description":"{desc}","pubDate":"2026-07-23","upDate":"2026-07-23"}}</script>
<link rel="stylesheet" href="../style.css">
<meta name="format-detection" content="telephone=no">
</head><body>
<header class="site-header"><div class="container"><div class="header-inner">
<a href="/" class="brand"><img src="../images/logo.webp" alt="速豹集运" style="height:40px"></a>
<nav class="main-nav"><a href="/equipment/">大件物流</a><a href="/city-shipping-guide">城市指南</a><a href="/pricing-calculator">运费估算</a><a href="/tw-to-cn/">台湾寄大陆</a><a href="/article-list">文章攻略</a><a href="/contact">询价</a></nav>
</div></div></header>
<main><article class="blog-post"><div class="container">
<header class="post-header"><h1>{city['name']}{cat['h1']}2026：{city['name']}寄{cat['content_type']}到台湾全攻略</h1><p class="post-meta">速豹集运 · 2026-07-23 · 阅读约6分钟</p></header>
<div class="post-content">

<div style="background:#FFF3CD;padding:20px;border-radius:8px;border-left:4px solid #FFC107;margin-bottom:24px">
<strong>📌 快速结论：</strong>从{city['name']}寄{cat['content_type']}到台湾，通过{city['port']}海运专线，{city['transit']}门到门。{city['advantage']}。微信免费获取报价：<strong>13026603164</strong>（微信同号）
</div>

<h2>📍 {city['name']}到台湾物流基本信息</h2>
<table>
<tr><th style="width:120px">项目</th><th>详情</th></tr>
<tr><td>出发地</td><td><strong>{city['name']}（{city['zone']}）</strong></td></tr>
<tr><td>起运港</td><td><strong>{city['port']}</strong></td></tr>
<tr><td>目的港</td><td>基隆 / 台北 / 台中 / 高雄</td></tr>
<tr><td>海运时效</td><td><strong>{city['transit']}</strong>门到门</td></tr>
<tr><td>适用货物</td><td>{cat['examples']}</td></tr>
{vol_info}
<tr><td>周边辐射</td><td>{city['radius']}</td></tr>
</table>

<div class="highlight" style="background:#FFF3CD;padding:16px;border-radius:8px;margin:20px 0;border-left:4px solid #FFC107">
<strong>💡 报价提示：</strong>具体运费根据{cat['content_type']}种类、重量、体积计算。拨打 <strong>13026603164</strong> 或加微信获取精准报价。
<br><a href="tel:13026603164" style="display:inline-block;background:#07C160;color:#fff;padding:12px 24px;border-radius:8px;font-weight:700;text-decoration:none;margin-top:12px">📱 微信免费获取报价</a>
</div>

<h2>📦 {city['name']}{cat['h1']}可以运什么？</h2>
<p>{cat['examples']}等均可从{city['name']}寄到台湾。具体可运品类如下：</p>
<table>
<tr><th>品类</th><th>可否寄送</th><th>包装要求</th></tr>
<tr><td>{cat['examples'].split('、')[0]}</td><td>✅ 可以</td><td>{cat['packaging']}</td></tr>
<tr><td>{cat['examples'].split('、')[1] if len(cat['examples'].split('、')) > 1 else cat['examples']}</td><td>✅ 可以</td><td>专业包装防护</td></tr>
<tr><td>{cat['examples'].split('、')[2] if len(cat['examples'].split('、')) > 2 else cat['examples']}</td><td>✅ 可以</td><td>定制木箱保护</td></tr>
</table>

<h2>💰 {city['name']}{cat['h1']}费用参考</h2>
<table>
<tr><th>货物规模</th><th>预估体积</th><th>参考费用（含报关）</th></tr>
{price_extra}
</table>
<p>以上为参考范围，具体价格以实时报价为准。影响价格因素：{cat['content_type']}品类、体积、重量、是否需要拆装、目的地台湾城市。</p>

<h2>🔄 {city['name']}{cat['h1']}全流程</h2>
<ol>{steps_html}</ol>

<div style="text-align:center;padding:32px;background:linear-gradient(135deg,#0052D9,#003DA5);color:#fff;border-radius:12px;margin:32px 0">
<h2 style="color:#fff;margin:0">从{city['name']}寄{cat['content_type']}到台湾？</h2>
<p style="margin:8px 0 16px">告知{cat['content_type']}种类和目的地，30分钟出定制物流方案</p>
<a href="tel:13026603164" style="display:inline-block;background:#fff;color:#0052D9;padding:14px 32px;border-radius:30px;font-weight:700;text-decoration:none;font-size:18px">📞 立即免费咨询</a>
<p style="margin-top:12px;opacity:.8">或加微信 13026603164</p>
</div>

<h2>🌐 {cat['h1']}相关问题</h2>
{faq_html}

<div style="background:#E8F2FF;padding:20px;border-radius:8px;margin:32px 0">
<h3>🔗 更多城市{cat['title_suffix']}专线</h3>
<p style="display:flex;flex-wrap:wrap;gap:8px">{related_links}</p>
</div>

</div></article></main>
<footer class="site-footer" style="background:#1a1a2e;color:rgba(255,255,255,.5);padding:40px 0;text-align:center;font-size:14px">
<div class="container">
<p>速豹集运 © 2026 · 两岸大件物流专家</p>
<p style="margin-top:8px"><a href="/city-shipping-guide" style="color:rgba(255,255,255,.5)">城市专线</a> · <a href="/equipment/" style="color:rgba(255,255,255,.5)">大件物流</a> · <a href="/tw-to-cn/" style="color:rgba(255,255,255,.5)">台湾寄大陆</a> · <a href="/contact" style="color:rgba(255,255,255,.5)">联系我们</a></p>
<p style="margin-top:8px"><a href="https://beian.miit.gov.cn/" style="color:rgba(255,255,255,.5)" target="_blank" rel="nofollow">湘ICP备2026016030号-2</a></p>
</div></footer>
</body></html>"""
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    return filename

def main():
    count = 0
    pages = []
    
    for city_key, city in CITIES.items():
        for cat_key, cat in CATEGORIES.items():
            filename = generate_page(city_key, city, cat_key, cat)
            pages.append(f'blog/{filename}')
            count += 1
            print(f'✅ {filename}')
    
    print(f'\n📊 总计生成: {count} 页')
    
    # Update baidu push queue
    queue_file = os.path.join(BASE, 'baidu-push-queue.txt')
    existing = set()
    if os.path.exists(queue_file):
        with open(queue_file) as f:
            existing = set(line.strip() for line in f if line.strip())
    
    new_urls = [f'https://www.subaotw.cn/{p.replace(".html","")}' for p in pages]
    added = [u for u in new_urls if u not in existing]
    
    if added:
        with open(queue_file, 'a') as f:
            for u in added:
                f.write(u + '\n')
        print(f'📤 推送队列新增: {len(added)} URL（总计 {len(existing) + len(added)}）')
    
    return pages

if __name__ == '__main__':
    main()
