#!/usr/bin/env python3
"""Programmatic SEO: generate 20 city→taiwan shipping pages for subaotw.cn"""

import os
from datetime import date

TODAY = "2026-07-22"
BASE_URL = "https://www.subaotw.cn"

CITIES = [
    {"name": "厦门", "pinyin": "xiamen", "port": "厦门港", "region": "福建/华东", "distance": "最近",
     "eta": "3-5天", "price": "最低", "ship_freq": "每周3-5班",
     "industries": "家具、石材、卫浴、电子产品", "nearby": "泉州、漳州、龙岩",
     "desc": "厦门是大陆距离台湾最近的港口，厦门港到基隆港/台北港仅需3-5天门到门。"},
    {"name": "深圳", "pinyin": "shenzhen", "port": "深圳蛇口港/盐田港", "region": "华南", "distance": "近",
     "eta": "4-6天", "price": "中等", "ship_freq": "每周3-5班",
     "industries": "电子产品、家具、机械设备、服装", "nearby": "东莞、惠州、中山",
     "desc": "深圳蛇口港是华南最大的对台口岸之一，船期密集，每周3-5班。"},
    {"name": "上海", "pinyin": "shanghai", "port": "上海港（洋山/外高桥）", "region": "华东", "distance": "中等",
     "eta": "5-7天", "price": "中等", "ship_freq": "每周2-3班",
     "industries": "机械设备、化工品、电子元器件、精密仪器", "nearby": "苏州、昆山、无锡、南通",
     "desc": "上海港是华东最大港口，洋山深水港和外卖高桥港区均有对台航线。"},
    {"name": "广州", "pinyin": "guangzhou", "port": "广州南沙港/黄埔港", "region": "华南", "distance": "近",
     "eta": "4-6天", "price": "中等", "ship_freq": "每周2-3班",
     "industries": "家具、建材、陶瓷、卫浴、五金", "nearby": "佛山、中山、江门、清远",
     "desc": "广州南沙港和黄埔港均可出货到台湾，集装箱码头设施完善。"},
    {"name": "东莞", "pinyin": "dongguan", "port": "东莞虎门港（经深圳/广州出）", "region": "华南", "distance": "近",
     "eta": "4-6天", "price": "中等", "ship_freq": "每周3-5班",
     "industries": "电子产品、模具、塑料制品、玩具、鞋类", "nearby": "深圳、惠州、广州",
     "desc": "东莞是世界工厂，制造业发达。货物通常经深圳蛇口港或广州南沙港出运。"},
    {"name": "苏州", "pinyin": "suzhou", "port": "苏州港（经上海港出）", "region": "华东", "distance": "中等",
     "eta": "6-8天", "price": "中等", "ship_freq": "每周2-3班",
     "industries": "电子元器件、精密机械、纺织面料、光伏产品", "nearby": "上海、无锡、常州、南通",
     "desc": "苏州工业园区和昆山是台商聚集地，货物经由上海港出运至台湾。"},
    {"name": "福州", "pinyin": "fuzhou", "port": "福州港（马尾/江阴）", "region": "福建/华东", "distance": "最近",
     "eta": "3-5天", "price": "最低", "ship_freq": "每周2-3班",
     "industries": "石材、茶叶、水产品加工、工艺品、电子产品", "nearby": "宁德、莆田、南平",
     "desc": "福州港与厦门港并列为福建两大对台口岸，马尾港区对台航线成熟。"},
    {"name": "宁波", "pinyin": "ningbo", "port": "宁波舟山港", "region": "华东", "distance": "近",
     "eta": "4-6天", "price": "中等", "ship_freq": "每周1-2班",
     "industries": "小家电、塑料制品、五金工具、文具", "nearby": "杭州、绍兴、台州、舟山",
     "desc": "宁波舟山港是全球货物吞吐量第一大港，对台航线逐步扩展中。"},
    {"name": "南京", "pinyin": "nanjing", "port": "南京港（经上海港出）", "region": "华东", "distance": "中等",
     "eta": "6-8天", "price": "中等", "ship_freq": "每周1-2班",
     "industries": "化工品、汽车零部件、钢铁制品、电子元器件", "nearby": "镇江、扬州、马鞍山、滁州",
     "desc": "南京是长三角重要工业城市，货物经上海港转运至台湾。"},
    {"name": "天津", "pinyin": "tianjin", "port": "天津港", "region": "华北", "distance": "远",
     "eta": "7-10天", "price": "较高", "ship_freq": "每周1班",
     "industries": "重型机械、钢材、化工设备、汽车零部件", "nearby": "北京、唐山、廊坊、沧州",
     "desc": "天津港是华北最大港口，京津地区的设备和建材通过天津港出运。"},
    {"name": "青岛", "pinyin": "qingdao", "port": "青岛港", "region": "山东/华北", "distance": "较远",
     "eta": "7-10天", "price": "较高", "ship_freq": "每周1班",
     "industries": "家电、轮胎、机械设备、海产品加工", "nearby": "烟台、潍坊、日照、威海",
     "desc": "青岛港是山东半岛核心港口，山东制造业发达，对台货运需求逐年增长。"},
    {"name": "北京", "pinyin": "beijing", "port": "北京（经天津港出）", "region": "华北", "distance": "远",
     "eta": "7-10天", "price": "较高", "ship_freq": "每周1班",
     "industries": "精密仪器、医疗器械、工艺品、图书资料", "nearby": "天津、廊坊、保定、雄安",
     "desc": "北京货物需先陆运至天津港再装船出海，适合高价值、非紧急货物。"},
    {"name": "杭州", "pinyin": "hangzhou", "port": "杭州（经宁波/上海港出）", "region": "华东", "distance": "中等",
     "eta": "5-7天", "price": "中等", "ship_freq": "每周2-3班",
     "industries": "电商产品、服装、丝绸、茶叶、电子产品", "nearby": "宁波、绍兴、嘉兴、湖州",
     "desc": "杭州是电商之都，跨境电商和小商品出口活跃。货物经宁波港或上海港出运。"},
    {"name": "成都", "pinyin": "chengdu", "port": "成都（经上海/深圳港出）", "region": "西南", "distance": "远",
     "eta": "8-12天", "price": "较高", "ship_freq": "每周1班",
     "industries": "电子元器件、汽车零部件、食品加工设备", "nearby": "德阳、绵阳、眉山、资阳",
     "desc": "成都是西南制造业重镇，货物先陆运至沿海港口（上海/深圳）再装船，适合非紧急大件货物。"},
    {"name": "重庆", "pinyin": "chongqing", "port": "重庆（经上海/深圳港出）", "region": "西南", "distance": "远",
     "eta": "8-12天", "price": "较高", "ship_freq": "每周1班",
     "industries": "摩托车零部件、汽车配件、机械设备", "nearby": "成都、贵阳、达州、涪陵",
     "desc": "重庆是西南工业重镇，摩托车和汽车零部件出口需求大。货物通常经上海或深圳转运。"},
    {"name": "武汉", "pinyin": "wuhan", "port": "武汉（经上海港出）", "region": "华中", "distance": "较远",
     "eta": "7-10天", "price": "中等偏高", "ship_freq": "每周1班",
     "industries": "钢铁制品、汽车零部件、光电子产品", "nearby": "黄石、孝感、鄂州、黄冈",
     "desc": "武汉是华中最大工业城市，光谷的电子产品和高新区制造业是主要货主。"},
    {"name": "佛山", "pinyin": "foshan", "port": "佛山（经广州港出）", "region": "华南", "distance": "近",
     "eta": "4-6天", "price": "中等", "ship_freq": "每周2-3班",
     "industries": "家具、陶瓷、卫浴、铝型材、家电", "nearby": "广州、中山、江门、肇庆",
     "desc": "佛山是中国家具之都和陶瓷之都，乐从家具市场和南庄陶瓷基地对台出口量大。"},
    {"name": "泉州", "pinyin": "quanzhou", "port": "泉州港（石湖/围头/深沪）", "region": "福建/华东", "distance": "最近",
     "eta": "3-5天", "price": "最低", "ship_freq": "每周2-3班",
     "industries": "石材、鞋服、陶瓷、茶叶、食品", "nearby": "厦门、漳州、莆田",
     "desc": "泉州是海上丝绸之路起点，对台小额贸易活跃。石湖港区有成熟的对台货运航线。"},
    {"name": "合肥", "pinyin": "hefei", "port": "合肥（经上海/南京港出）", "region": "华东", "distance": "中等",
     "eta": "7-9天", "price": "中等", "ship_freq": "每周1-2班",
     "industries": "家电、汽车零部件、新型显示面板、集成电路", "nearby": "南京、芜湖、蚌埠、安庆",
     "desc": "合肥是新兴制造业城市，京东方、蔚来等企业带动电子和汽车零部件出口。"},
    {"name": "长沙", "pinyin": "changsha", "port": "长沙（经上海/深圳港出）", "region": "华中", "distance": "较远",
     "eta": "7-10天", "price": "中等偏高", "ship_freq": "每周1班",
     "industries": "工程机械、轨道交通设备、新材料", "nearby": "株洲、湘潭、岳阳、衡阳",
     "desc": "长沙是工程机械之都，中联重科和三一重工是全球领先的工程机械制造商。"},
]


def generate_page(city):
    name = city["name"]
    pinyin = city["pinyin"]
    slug = f"city-{pinyin}-to-taiwan"
    filename = f"{slug}.html"

    title = f"{name}寄台湾专线2026 | 海运{name}→台湾时效+费用 - 速豹集运"
    desc = f"{name}寄台湾怎么寄？{city['desc']}{city['industries']}均可海运/陆运+海运门到门。{city['eta']}送达到基隆/台北/台中/高雄，{city['nearby']}货物也可经{name}港出运。免费咨询报价→"

    keywords = f"{name}寄台湾,{name}到台湾物流,{name}寄台湾运费,{name}到台湾海运"

    html = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">
  <meta name="lastmod" content="{TODAY}"><meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{keywords}">
  <link rel="canonical" href="{BASE_URL}/city/{slug}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{BASE_URL}/city/{slug}">
  <meta property="og:type" content="website">
  <style>body{{font-family:PingFang SC,Microsoft YaHei,sans-serif;color:#333;line-height:1.8;margin:0;background:#f5f7fa}}.container{{max-width:900px;margin:0 auto;padding:0 20px}}header{{background:#0052D9;color:#fff;padding:16px 0}}.hero{{background:linear-gradient(135deg,#0052D9,#003DA5);color:#fff;padding:48px 0 32px;text-align:center}}.hero h1{{font-size:28px;margin:0}}.content{{background:#fff;padding:32px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,.08);margin:-20px auto 40px}}h2{{color:#0052D9;font-size:22px;margin:32px 0 16px;border-bottom:2px solid #E8F2FF;padding-bottom:8px}}h3{{color:#333;font-size:18px;margin:24px 0 12px}}table{{width:100%;border-collapse:collapse;margin:20px 0}}th,td{{padding:12px 16px;border-bottom:1px solid #E0E0E0;text-align:left}}th{{background:#0052D9;color:#fff}}tr:nth-child(even){{background:#f5f7fa}}.highlight{{background:#FFF3CD;padding:16px;border-radius:8px;margin:20px 0;border-left:4px solid #FFC107}}.cta{{background:#0052D9;color:#fff;text-align:center;padding:48px 0}}.cta a{{display:inline-block;background:#fff;color:#0052D9;padding:14px 32px;border-radius:30px;font-weight:700;text-decoration:none}}footer{{background:#1a1a2e;color:rgba(255,255,255,.5);padding:40px 0;text-align:center;font-size:14px}}.btn{{display:inline-block;background:#07C160;color:#fff;padding:12px 24px;border-radius:8px;font-weight:700;text-decoration:none;margin:8px}}.btn-tel{{background:#0052D9}}@media(max-width:768px){{.content{{padding:20px}}.hero h1{{font-size:22px}}}}</style>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebPage","name":"{title}","description":"{desc}","url":"{BASE_URL}/city/{slug}","dateModified":"{TODAY}"}}</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"首页","item":"{BASE_URL}/"}},{{"@type":"ListItem","position":2,"name":"{name}寄台湾专线"}}]}}</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"速豹集运","url":"{BASE_URL}","description":"大陆寄台湾大件物流专线 — 搬家/家具/设备/建材/大货专线 + 台湾寄大陆快递","foundingDate":"2020","contactPoint":{{"@type":"ContactPoint","contactType":"customer service","telephone":"13026603164"}}}}</script>
  <meta name="format-detection" content="telephone=no">
</head><body>
<header><div class="container">
  <nav class="nav" style="display:flex;gap:20px;flex-wrap:wrap">
    <a href="/" style="color:#fff;font-weight:700;text-decoration:none;font-size:18px">速豹集运</a>
    <a href="/equipment/" style="color:rgba(255,255,255,.85);text-decoration:none">大件物流</a>
    <a href="/pricing-calculator" style="color:rgba(255,255,255,.85);text-decoration:none">运费估算</a>
    <a href="/volume-calculator" style="color:rgba(255,255,255,.85);text-decoration:none">材积计算</a>
    <a href="/city-shipping-guide" style="color:rgba(255,255,255,.85);text-decoration:none">城市指南</a>
    <a href="/tw-to-cn/" style="color:rgba(255,255,255,.85);text-decoration:none">台湾寄大陆</a>
    <a href="/contact" style="color:rgba(255,255,255,.85);text-decoration:none">询价</a>
  </nav>
</div></header>

<section class="hero"><div class="container">
  <h1>{name}寄台湾专线2026：海运+门到门全程服务</h1>
  <p style="opacity:.9;font-size:16px">{city['desc']}.{city['industries']}等均可海运。</p>
</div></section>

<div class="container"><div class="content">

<h2>🚢 {name}到台湾物流基本信息</h2>
<table>
  <tr><th style="width:120px">项目</th><th>详情</th></tr>
  <tr><td>起运港</td><td><strong>{city['port']}</strong></td></tr>
  <tr><td>目的港</td><td>基隆 / 台北 / 台中 / 高雄</td></tr>
  <tr><td>海运时效</td><td><strong>{city['eta']}</strong>门到门</td></tr>
  <tr><td>船期频率</td><td>{city['ship_freq']}</td></tr>
  <tr><td>适合货物</td><td>{city['industries']}</td></tr>
  <tr><td>周边辐射</td><td>{city['nearby']}</td></tr>
</table>

<div class="highlight">
  <strong>💡 报价提示：</strong>{name}属于{city['region']}区域，海运价格{city['price']}。具体运费根据货物重量、体积、品类计算，拨打 <strong>13026603164</strong> 或 <strong>微信13026603164</strong> 获取精准报价。
  <br><a href="tel:13026603164" class="btn btn-tel" style="margin-top:12px">📞 立即咨询报价</a>
</div>

<h2>📦 {name}寄台湾可以寄什么？</h2>
<table>
  <tr><th>品类</th><th>可否寄送</th><th>说明</th></tr>
  <tr><td>家具（沙发/床/柜子/桌椅）</td><td>✅ 可以</td><td>海运门到门，整柜/拼柜均可</td></tr>
  <tr><td>建材（瓷砖/卫浴/门窗/石材）</td><td>✅ 可以</td><td>大件建材海运专线</td></tr>
  <tr><td>机械设备（注塑机/CNC/生产线）</td><td>✅ 可以</td><td>专业设备包装+固定+运输</td></tr>
  <tr><td>电子产品/家电</td><td>✅ 可以</td><td>需木箱包装防护</td></tr>
  <tr><td>个人搬家行李</td><td>✅ 可以</td><td>搬家专线，门到门</td></tr>
  <tr><td>服装/纺织品</td><td>✅ 可以</td><td>布料/成衣均可海运</td></tr>
  <tr><td>食品/茶叶</td><td>⚠️ 需确认</td><td>密封包装可，具体品类咨询</td></tr>
</table>

<h2>💰 {name}到台湾运费多少钱？</h2>
<p>运费由多个因素决定，无法统一报价，但可以参考以下范围：</p>
<table>
  <tr><th>货物类型</th><th>参考价格区间</th><th>计费方式</th></tr>
  <tr><td>家具搬家（整柜）</td><td>3,000-8,000 元/柜</td><td>20GP/40HQ整柜</td></tr>
  <tr><td>建材大货（拼柜）</td><td>800-2,000 元/m³</td><td>按立方米计费</td></tr>
  <tr><td>机械设备（单件）</td><td>2,000-10,000 元/件</td><td>按重量+体积综合</td></tr>
  <tr><td>小件货物（快递）</td><td>15-35 元/kg</td><td>按重量计费</td></tr>
</table>
<p>以上为参考范围，具体价格以实时报价为准。影响价格的因素：货物重量、体积、品类、目的地（台湾哪个城市）、是否需报关、是否含保险等。</p>

<div class="highlight">
  <strong>🎯 省钱技巧：</strong>
  ① 拼柜比整柜便宜60%+（与其他客户共享一个柜子）<br>
  ② 淡季（非节前）运费通常低10-20%<br>
  ③ 周边城市（{city['nearby']}）集合发货可以省陆运费<br>
  ④ 长期合作客户可享阶梯价格
</div>

<h2>📋 {name}寄台湾流程</h2>
<table>
  <tr><th style="width:30px">步骤</th><th>内容</th><th>时间</th></tr>
  <tr><td>1️⃣</td><td><strong>联系报价</strong>：告知货物信息（品类/重量/体积/目的地）</td><td>30分钟出方案</td></tr>
  <tr><td>2️⃣</td><td><strong>上门提货/送货到仓</strong>：{name}及周边（{city['nearby']}）均可上门</td><td>1-2天</td></tr>
  <tr><td>3️⃣</td><td><strong>装箱/报关</strong>：专业包装+出口报关手续</td><td>1-2天</td></tr>
  <tr><td>4️⃣</td><td><strong>海运</strong>：{name}港→台湾基隆/台北/台中/高雄</td><td>{city['eta']}</td></tr>
  <tr><td>5️⃣</td><td><strong>清关+派送</strong>：台湾进口清关+门到门派送</td><td>1-2天</td></tr>
</table>

<h2>🏭 {name}主要出口货物品类</h2>
<p>{city['industries']}是{name}寄台湾的主要品类。{name}的制造业基础雄厚，对台出口活跃。{city['nearby']}等周边地区的货物也可以经过{name}集中出运，降低物流成本。</p>

<h2>📞 {name}寄台湾，怎么联系？</h2>
<p>速豹集运提供{name}到台湾全程门到门物流服务：上门提货 → 海运/陆海联运 → 台湾清关 → 门到门派送。一口价含报关+海运+清关+派送。</p>

<div style="text-align:center;padding:24px;background:#E8F2FF;border-radius:12px;margin:24px 0">
  <strong style="font-size:20px">📞 {name}寄台湾物流专线</strong>
  <p style="font-size:16px;margin:12px 0">免费咨询 · 30分钟出方案 · 门到门一口价</p>
  <a href="tel:13026603164" class="btn btn-tel">📞 13026603164</a>
  <a href="/pricing-calculator" class="btn" style="background:#0052D9">💰 在线估价</a>
  <p style="font-size:13px;color:#666;margin-top:8px">或添加微信：13026603164</p>
</div>

<h2>🔗 其他城市寄台湾</h2>
<div style="display:flex;flex-wrap:wrap;gap:8px;margin:16px 0">'''

    # Add links to all other city pages
    for other in CITIES:
        if other["pinyin"] != pinyin:
            html += f'\n  <a href="/city/city-{other["pinyin"]}-to-taiwan" style="display:inline-block;padding:6px 12px;background:#E8F2FF;color:#0052D9;text-decoration:none;border-radius:6px;font-size:14px;margin:4px">{other["name"]}寄台湾</a>'

    html += '''
</div>
<p style="color:#666;font-size:14px">不确定哪个城市出货最划算？<a href="/contact" style="color:#0052D9">联系我们</a>，货代帮你规划最优路线。</p>

</div></div>

<section class="cta"><div class="container">
  <h2 style="margin:0;font-size:24px">''' + f'{name}到台湾，30分钟出方案' + '''</h2>
  <p style="margin:12px 0;font-size:16px">大件物流专线 · 门到门一口价 · 含报关清关</p>
  <a href="tel:13026603164" style="display:inline-block;background:#fff;color:#0052D9;padding:14px 40px;border-radius:30px;font-weight:700;text-decoration:none;font-size:18px">📞 立即咨询</a>
  <p style="font-size:14px;margin-top:12px;opacity:.8">微信同号：13026603164 | 免费报价</p>
</div></section>

<footer><div class="container">
  <p style="margin:4px 0">© 2026 速豹集运 — 大陆寄台湾大件物流专线</p>
  <p style="margin:4px 0"><a href="https://beian.miit.gov.cn/" style="color:rgba(255,255,255,.5);text-decoration:none" target="_blank" rel="noopener">湘ICP备2026016030号-2</a></p>
</div></footer>

</body></html>'''

    return filename, html


def main():
    out_dir = os.path.join(os.path.dirname(__file__), "city")
    os.makedirs(out_dir, exist_ok=True)

    generated = []
    for city in CITIES:
        filename, html = generate_page(city)
        path = os.path.join(out_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        generated.append(filename)
        print(f"✅ {filename}")

    # Generate index page for the city directory
    index_html = '''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">
  <meta name="lastmod" content="''' + TODAY + '''"><meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>大陆各城市寄台湾专线 | 20+城市直达台湾物流 - 速豹集运</title>
  <meta name="description" content="大陆各城市寄台湾专线汇总：厦门、深圳、上海、广州、东莞等20+城市到台湾海运门到门。各城市时效费用对比、起运港、周边辐射区域。免费报价→">
  <meta name="keywords" content="大陆寄台湾,城市寄台湾,寄台湾物流,寄台湾专线">
  <link rel="canonical" href="''' + BASE_URL + '''/city/">
  <style>body{font-family:PingFang SC,Microsoft YaHei,sans-serif;color:#333;line-height:1.8;margin:0;background:#f5f7fa}.container{max-width:900px;margin:0 auto;padding:0 20px}header{background:#0052D9;color:#fff;padding:16px 0}.hero{background:linear-gradient(135deg,#0052D9,#003DA5);color:#fff;padding:48px 0 32px;text-align:center}.hero h1{font-size:28px;margin:0}.content{background:#fff;padding:32px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,.08);margin:-20px auto 40px}h2{color:#0052D9;font-size:22px;margin:32px 0 16px;border-bottom:2px solid #E8F2FF;padding-bottom:8px}footer{background:#1a1a2e;color:rgba(255,255,255,.5);padding:40px 0;text-align:center;font-size:14px}@media(max-width:768px){.content{padding:20px}}</style>
</head><body>
<header><div class="container">
  <nav class="nav" style="display:flex;gap:20px;flex-wrap:wrap">
    <a href="/" style="color:#fff;font-weight:700;text-decoration:none;font-size:18px">速豹集运</a>
    <a href="/equipment/" style="color:rgba(255,255,255,.85);text-decoration:none">大件物流</a>
    <a href="/pricing-calculator" style="color:rgba(255,255,255,.85);text-decoration:none">运费估算</a>
    <a href="/tw-to-cn/" style="color:rgba(255,255,255,.85);text-decoration:none">台湾寄大陆</a>
  </nav>
</div></header>
<section class="hero"><div class="container">
  <h1>大陆各城市寄台湾专线</h1>
  <p style="opacity:.9">20+城市直达台湾 · 门到门一口价 · 免费报价</p>
</div></section>
<div class="container"><div class="content">
<h2>选择你的起运城市</h2>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px;margin:24px 0">'''

    for city in CITIES:
        index_html += f'\n  <a href="/city/city-{city["pinyin"]}-to-taiwan" style="display:block;padding:16px;background:#E8F2FF;color:#0052D9;text-decoration:none;border-radius:8px;font-weight:500">{city["name"]}寄台湾</a>'

    index_html += '''
</div></div></div>
<footer><div class="container">
  <p>© 2026 速豹集运 <a href="https://beian.miit.gov.cn/" style="color:rgba(255,255,255,.5);text-decoration:none" target="_blank" rel="noopener">湘ICP备2026016030号-2</a></p>
</div></footer>
</body></html>'''

    index_path = os.path.join(out_dir, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_html)
    print(f"\n✅ city/index.html（目录页）")
    print(f"\n📊 总计生成: {len(generated) + 1} 个文件")
    print(f"📂 输出目录: {out_dir}")


if __name__ == "__main__":
    main()
