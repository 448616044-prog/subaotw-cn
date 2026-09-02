#!/usr/bin/env python3
"""Generate Phase 2 supplementary pages: moving cost, freight, commercial cargo"""

import os

TODAY = "2026-07-22"
BASE = "https://www.subaotw.cn"
D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(D, "blog")

PAGES = [
    {
        "slug": "tw-moving-cost-guide",
        "title": "台湾搬家到大陆费用2026 | 海运搬家报价明细 - 速豹集运",
        "h1": "台湾搬家到大陆费用全攻略2026：海运搬家报价明细一次看懂",
        "meta": "台湾搬家到大陆要花多少钱？海运搬家用具、行李、电器费用明细：拼柜800-1200元/m³，整柜3000-8000元。含台湾取件+海运+大陆清关派送全包价。免费估价→",
        "kw": "台湾搬家到大陆费用,台湾搬家大陆多少钱,台湾搬家运费,台湾海运搬家价格,从台湾搬家到大陆要多少钱",
        "body": """
        <h2>台湾搬家到大陆费用构成</h2>
        <p>台湾搬家到大陆的费用主要由以下几个部分组成：</p>
        <table><tr><th>费用项目</th><th>说明</th><th>参考价格</th></tr>
        <tr><td>上门取件/包装</td><td>台湾全岛上门，含专业家具拆装包装</td><td>500-2000元（视距离和货量）</td></tr>
        <tr><td>海运运费</td><td>拼柜按立方米，整柜按柜型</td><td>拼柜800-1200元/m³ / 整柜3000-8000元</td></tr>
        <tr><td>出口报关</td><td>台湾出口报关手续费</td><td>300-800元/票</td></tr>
        <tr><td>大陆清关</td><td>进口清关+检验检疫</td><td>500-1500元/票</td></tr>
        <tr><td>派送到家</td><td>大陆门到门派送</td><td>500-2000元（视距离和楼层）</td></tr>
        <tr><td>关税（如适用）</td><td>旧物品基本免税，新物品按品类</td><td>0-25%不等</td></tr></table>

        <h2>按搬家规模估算总费用</h2>
        <table><tr><th>搬家规模</th><th>货物量</th><th>推荐方式</th><th>预估总费用</th></tr>
        <tr><td>小搬家（单身/留学生）</td><td>1-2m³（5-15箱）</td><td>海运拼柜</td><td>2000-4000元</td></tr>
        <tr><td>中搬家（小家庭）</td><td>3-8m³（15-40箱+少量家具）</td><td>海运拼柜</td><td>5000-12000元</td></tr>
        <tr><td>大搬家（大家庭）</td><td>10-25m³（整套家具家电）</td><td>20GP整柜</td><td>8000-18000元</td></tr>
        <tr><td>超大搬家（别墅/公司）</td><td>25m³以上</td><td>40HQ整柜</td><td>15000-30000元</td></tr></table>

        <h2>省钱技巧</h2>
        <ul><li><strong>拼柜省60%+</strong>：与其他客户共用一个集装箱，分摊海运费</li>
        <li><strong>淡季出货</strong>：避开春节/暑假高峰期，运费可低10-20%</li>
        <li><strong>旧物品免税</strong>：个人使用超过半年的旧物品凭台胞证可免税清关</li>
        <li><strong>合理打包</strong>：尽量压缩体积，海运按m³计费，省体积=省钱</li>
        <li><strong>集合发货</strong>：朋友/同事一起搬家拼单，享受批量折扣</li></ul>
        """,
        "faq": [
            ("台湾搬家到大陆1立方米多少钱？","海运拼柜1立方米约800-1200元人民币（含台湾取件+海运+大陆清关+派送）。家具类因体积大，建议按整柜更划算。"),
            ("台湾搬家大陆可以免税吗？","个人使用超过半年的旧物品可以免税清关。需要提供：台胞证、物品清单、在台居住证明。新购买物品需按品类缴税。"),
            ("海运搬家要买保险吗？","建议买。海运搬家保险费率约为货物价值的1-3%。特别是有红木家具、钢琴、古董等高价值物品时，花几百元买安心很值得。"),
        ],
    },
    {
        "slug": "tw-to-cn-freight",
        "title": "台湾寄大陆货运专线2026 | 大件货物海运门到门 - 速豹集运",
        "h1": "台湾寄大陆货运专线2026：大件货物海运门到门全流程",
        "meta": "台湾寄大陆大件货物怎么运？工厂设备/建材/家具/大宗商品海运专线。整柜拼柜可选，台湾上门提货→海运→大陆清关派送一站式。7-15天门到门，免费报价→",
        "kw": "台湾寄大陆货运,台湾到大陆物流,台湾大件货物海运,台湾寄大陆专线,台湾货运大陆,台湾物流大陆",
        "body": """
        <h2>台湾寄大陆货运方式对比</h2>
        <table><tr><th>运输方式</th><th>适用货物</th><th>时效</th><th>参考价格</th><th>适合谁</th></tr>
        <tr><td>海运拼柜(LCL)</td><td>1-15m³货物</td><td>10-18天</td><td>800-1200元/m³</td><td>中小货主</td></tr>
        <tr><td>海运整柜(FCL) 20GP</td><td>15-28m³货物</td><td>8-12天</td><td>3000-5000元/柜</td><td>搬家/整批货</td></tr>
        <tr><td>海运整柜(FCL) 40HQ</td><td>55-68m³货物</td><td>8-12天</td><td>5000-8000元/柜</td><td>工厂搬迁/大宗</td></tr>
        <tr><td>空运快递</td><td>急用小件(<100kg)</td><td>2-5天</td><td>25-45元/kg</td><td>急件/样品</td></tr></table>

        <h2>台湾寄大陆大件货运流程</h2>
        <ol><li><strong>货物评估</strong>：提供货物清单（品名/数量/尺寸/重量），30分钟出方案</li>
        <li><strong>上门提货</strong>：台湾全岛上门，专业团队包装（木箱/托盘/缠绕膜）</li>
        <li><strong>出口报关</strong>：准备商业发票、装箱单、报关委托书</li>
        <li><strong>海运运输</strong>：台湾基隆/台中/高雄港→大陆上海/厦门/深圳/天津港</li>
        <li><strong>进口清关</strong>：大陆海关申报、缴税（如需）、检验检疫</li>
        <li><strong>派送到门</strong>：港口提货→陆运→送货到指定地址</li></ol>

        <h2>常见大件货物品类</h2>
        <table><tr><th>品类</th><th>可否运输</th><th>注意事项</th></tr>
        <tr><td>家具（实木/板材/沙发/床）</td><td>✅</td><td>需防潮包装，实木家具建议木箱</td></tr>
        <tr><td>机械设备（注塑机/CNC/生产线）</td><td>✅</td><td>需专业固定+防锈处理+木箱</td></tr>
        <tr><td>建材（瓷砖/卫浴/门窗/石材）</td><td>✅</td><td>易碎品需木箱+气泡膜多层保护</td></tr>
        <tr><td>电子设备（服务器/仪器）</td><td>✅</td><td>防震包装+防静电+温控（如需）</td></tr>
        <tr><td>汽车零部件</td><td>✅</td><td>需商业报关，提供产品目录</td></tr></table>
        """,
        "faq": [
            ("台湾寄大件货物到大陆怎么最省钱？","海运拼柜最省钱。1-5m³的货物走拼柜，和其他货主共用一个集装箱分摊费用。20m³以上建议整柜，单价更低。具体方案可免费评估。"),
            ("台湾到大陆货运需要哪些文件？","基本文件：①商业发票 ②装箱单（品名/数量/重量/尺寸）③报关委托书。特殊货物可能还需要：原产地证、商检证书、许可证等。速豹协助准备全套报关文件。"),
            ("台湾寄设备到大陆需要多久？","海运8-12天（门到门全程约12-18天）。具体取决于起运港和目的港：基隆→厦门最快（3-5天海运），基隆→天津最慢（7-10天海运）。空运2-5天但费用高。"),
        ],
    },
    {
        "slug": "tw-commercial-cargo-to-cn",
        "title": "台湾商业货物寄大陆2026 | 商品/库存/样品海运报关 - 速豹集运",
        "h1": "台湾商业货物寄大陆全攻略2026：商品/库存/样品海运报关一条龙",
        "meta": "台湾商业货物（商品/库存/样品/展品）寄大陆全流程。商业报关、关税计算、原产地证、检验检疫一次讲清楚。台湾取件→海运→大陆清关→送货上门。免费获取报关方案→",
        "kw": "台湾商业货物寄大陆,台湾商品寄大陆报关,台湾库存寄大陆,台湾样品寄大陆,台湾商业报关大陆,台湾出口大陆关税",
        "body": """
        <h2>个人物品 vs 商业货物：关键区别</h2>
        <table><tr><th>维度</th><th>个人物品</th><th>商业货物</th></tr>
        <tr><td>报关方式</td><td>个人物品申报（简易）</td><td>正式商业报关</td></tr>
        <tr><td>关税</td><td>旧物品基本免税</td><td>按HS编码税率缴纳</td></tr>
        <tr><td>所需文件</td><td>台胞证+物品清单</td><td>合同/发票/箱单/报关委托书</td></tr>
        <tr><td>检验检疫</td><td>一般不涉及</td><td>部分品类需商检</td></tr>
        <tr><td>数量限制</td><td>合理自用范围</td><td>无限制</td></tr></table>

        <h2>商业货物报关流程</h2>
        <ol><li><strong>准备文件</strong>：商业发票、装箱单、外贸合同、报关委托书（速豹提供模板）</li>
        <li><strong>HS编码归类</strong>：根据产品类别确定海关编码，查询适用税率</li>
        <li><strong>出口报关</strong>：台湾出口申报，如涉及优惠税率需提供原产地证</li>
        <li><strong>海运/空运</strong>：根据货量和紧急程度选择运输方式</li>
        <li><strong>进口报关</strong>：大陆海关申报、缴税、检验检疫（如需）</li>
        <li><strong>送货到仓</strong>：清关完成后送达指定仓库/门店</li></ol>

        <h2>常见商业货物关税参考</h2>
        <table><tr><th>品类</th><th>关税</th><th>增值税</th><th>综合税率</th></tr>
        <tr><td>电子产品</td><td>0-10%</td><td>13%</td><td>13-25%</td></tr>
        <tr><td>纺织品/服装</td><td>8-14%</td><td>13%</td><td>22-30%</td></tr>
        <tr><td>塑料制品</td><td>6-10%</td><td>13%</td><td>20-25%</td></tr>
        <tr><td>机械设备零件</td><td>3-8%</td><td>13%</td><td>16-22%</td></tr>
        <tr><td>食品（加工包装）</td><td>5-15%</td><td>13%</td><td>18-30%</td></tr></table>
        <p><em>注：以上为参考税率，实际以海关核定为准。ECFA框架下部分台湾产品享有优惠税率。</em></p>

        <h2>商业货物寄大陆常见问题</h2>
        """,
        "faq": [
            ("台湾商业货物寄大陆，需要公司资质吗？","需要。发货方需要台湾公司（有统一编号），收货方需要大陆公司（有进出口经营权）。如果收货方没有进出口权，速豹可以协助提供代理报关服务。"),
            ("少量样品寄大陆算商业货物吗？","样品价值低于5000元人民币且数量合理（每款1-2件），可以按样品申报，流程更简单。超过此范围按正式商业报关处理。具体可以传产品信息到微信确认。"),
            ("台湾商品寄大陆可以用ECFA优惠关税吗？","可以。如果产品在ECFA早收清单内（如部分石化产品、机械零件、纺织品等），凭台湾签发的ECFA原产地证可以享受零关税或低关税。速豹协助办理ECFA证书。"),
        ],
    },
]


def gen(p):
    s = p["slug"]
    fname = f"{s}.html"
    faq_json = ",".join([
        '{"@type":"Question","name":"'+q+'","acceptedAnswer":{"@type":"Answer","text":"'+a+'"}}'
        for q, a in p["faq"]
    ])

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta http-equiv="Cache-Control" content="no-siteapp">
  <meta name="applicable-device" content="pc,mobile">
  <meta charset="UTF-8">
  <meta name="robots" content="index,follow">
  <meta name="lastmod" content="{TODAY}">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <meta name="baidu-site-verification" content="codeva-K4kVPs6NwjtWr4ij" />
  <title>{p["title"]}</title>
  <meta name="description" content="{p["meta"]}">
  <meta name="keywords" content="{p["kw"]}">
  <meta property="og:title" content="{p["h1"]}">
  <meta property="og:description" content="{p["meta"]}">
  <meta property="og:url" content="{BASE}/blog/{s}">
  <meta property="og:type" content="article">
  <link rel="canonical" href="{BASE}/blog/{s}">
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"速豹集运","url":"{BASE}","logo":"{BASE}/images/logo.png","contactPoint":{{"@type":"ContactPoint","telephone":"13026603164","contactType":"customer service"}}}}</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"首页","item":"{BASE}/"}},{{"@type":"ListItem","position":2,"name":"文章攻略","item":"{BASE}/article-list"}},{{"@type":"ListItem","position":3,"name":"{p["h1"]}","item":"{BASE}/blog/{s}"}}]}}</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_json}]}}</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{p["h1"]}","description":"{p["meta"]}","author":{{"@type":"Organization","name":"速豹集运"}},"publisher":{{"@type":"Organization","name":"速豹集运","url":"{BASE}"}},"datePublished":"{TODAY}","dateModified":"{TODAY}"}}</script>
  <script type="application/ld+json">{{"@context":"https://ziyuan.baidu.com/contexts/cambrian.jsonld","@type":"WebPage","title":"{p["h1"]} | 速豹集运","description":"{p["meta"]}","pubDate":"{TODAY}","upDate":"{TODAY}"}}</script>
  <link rel="stylesheet" href="../style.css">
  <meta name="format-detection" content="telephone=no">
</head>
<body>
<header class="site-header"><div class="container"><div class="header-inner">
  <a href="/" class="brand"><img src="../images/logo.webp" alt="速豹集运" loading="lazy" style="height:40px"></a>
  <nav class="main-nav">
    <a href="/equipment/">大件物流</a>
    <a href="/city-shipping-guide">城市指南</a>
    <a href="/pricing-calculator">运费估算</a>
    <a href="/tw-to-cn/">台湾寄大陆</a>
    <a href="/article-list">文章攻略</a>
    <a href="/contact">询价</a>
  </nav>
</div></div></header>
<main><article class="blog-post"><div class="container">
  <header class="post-header">
    <h1>{p["h1"]}</h1>
    <p class="post-meta">速豹集运 · 发布于 {TODAY} · 阅读约8分钟</p>
  </header>
  <div class="post-content">
    <div class="highlight-box">
      <strong>📌 核心摘要：</strong>{p["meta"]}
      <br>📞 <strong>免费咨询：13026603164</strong>（微信同号）
    </div>
    {p["body"]}
    <div class="faq-section">'''

    for q, a in p["faq"]:
        html += f'<div style="margin-bottom:16px"><strong style="color:#1a1a2e">❓ {q}</strong><p style="color:#555;margin-top:4px">{a}</p></div>'

    html += f'''</div>
    <div style="text-align:center;padding:32px;background:linear-gradient(135deg,#0052D9,#003DA5);color:#fff;border-radius:12px;margin:32px 0">
      <h2 style="color:#fff;margin:0 0 8px">📞 免费获取方案+报价</h2>
      <p style="margin:0 0 16px">30分钟出专属方案</p>
      <p style="font-size:20px"><strong>13026603164</strong></p>
      <a href="tel:13026603164" style="display:inline-block;background:#fff;color:#0052D9;padding:12px 28px;border-radius:6px;font-weight:700;text-decoration:none;margin-top:8px">立即电话咨询</a>
    </div>
  </div>
</div></article></main>
<footer class="site-footer"><div class="container">
  <p>© 2026 速豹集运 — 两岸大件物流专家</p>
  <p><a href="https://beian.miit.gov.cn/" target="_blank" rel="noopener">湘ICP备2026016030号-2</a></p>
</div></footer>
</body></html>'''

    return fname, html


def main():
    for p in PAGES:
        fname, html = gen(p)
        with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ {fname}")

    print(f"\n📊 {len(PAGES)} 个新页面已生成")

if __name__ == "__main__":
    main()
