#!/usr/bin/env python3
"""Generate competitor alternative pages for subaotw.cn — 截流竞品搜索流量"""

import os

TODAY = "2026-07-23"
BASE = "https://www.subaotw.cn"
D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(D, "blog")

ALTERNATIVES = [
    {
        "slug": "kafeisi-alternative",
        "title": "卡菲斯替代方案2026 | 大陆寄台湾物流对比：速豹 vs 卡菲斯",
        "h1": "卡菲斯替代方案2026：速豹 vs 卡菲斯 大陆寄台湾物流对比",
        "meta": "找卡菲斯替代方案？速豹集运vs卡菲斯全维度对比：价格、时效、可寄品类、客服响应。大陆寄台湾大件物流，家具/设备/建材专线。免费获取报价→",
        "kw": "卡菲斯替代,卡菲斯物流对比,大陆寄台湾物流哪家好,卡菲斯vs速豹,台湾物流公司推荐",
        "competitor": "卡菲斯",
        "body": """
        <h2>卡菲斯 vs 速豹：核心对比</h2>
        <table><tr><th>对比维度</th><th>卡菲斯</th><th>速豹集运</th></tr>
        <tr><td>主营方向</td><td>大陆→台湾 一般货物</td><td>大陆→台湾 大件物流 + 台湾→大陆 敏感货</td></tr>
        <tr><td>大件物流</td><td>有，但非核心</td><td>核心业务，家具/设备/建材专线</td></tr>
        <tr><td>台湾寄大陆</td><td>服务有限</td><td>双向服务，敏感货专线</td></tr>
        <tr><td>客服响应</td><td>工作日回复</td><td>微信/电话即时回复</td></tr>
        <tr><td>城市覆盖</td><td>主要港口城市</td><td>20+城市专线直达</td></tr></table>

        <h2>如果你正在找卡菲斯替代方案</h2>
        <p>很多客户因为以下原因寻找卡菲斯的替代方案：</p>
        <ul><li>需要更大件货物（家具/设备）的门到门服务</li>
        <li>需要台湾寄回大陆的敏感货渠道</li>
        <li>需要更快的客服响应和全程跟踪</li>
        <li>需要覆盖更多内陆城市（成都/重庆/武汉等）</li></ul>
        <p>速豹集运专注两岸大件物流6年，服务大陆20+城市直达台湾，含家具/设备/建材/搬家全品类。同时提供台湾寄大陆敏感货专线（食品/化妆品/保健品/茶叶/3C）。</p>

        <h2>运费参考</h2>
        <table><tr><th>货物类型</th><th>运输方式</th><th>参考价格</th><th>时效</th></tr>
        <tr><td>家具搬家</td><td>海运拼柜/整柜</td><td>800-1200元/m³</td><td>7-15天</td></tr>
        <tr><td>机械设备</td><td>海运整柜</td><td>3000-8000元/柜</td><td>5-10天</td></tr>
        <tr><td>建材大货</td><td>海运拼柜</td><td>800-2000元/m³</td><td>7-15天</td></tr></table>
        """,
        "faq": [
            ("卡菲斯和速豹哪个好？","取决于需求。如果寄一般小件货物，两家都可以。如果需要大件物流（家具/设备/建材）或台湾寄大陆的敏感货，速豹更专业。建议根据具体货物类型和目的地获取报价对比。"),
            ("卡菲斯可以寄家具到台湾吗？","卡菲斯有物流服务但大件家具不是其核心业务。速豹集运专注大件物流，提供家具拆卸包装+海运+台湾清关+上门安装一条龙服务。"),
            ("找卡菲斯替代，速豹有什么优势？","三大优势：①大件物流专精（家具/设备/建材）②20+城市直达台湾 ③双向服务（大陆→台湾 + 台湾→大陆 敏感货专线）。免费咨询微信/电话。"),
        ],
    },
    {
        "slug": "feijin-alternative",
        "title": "飞晋物流替代方案2026 | 大陆寄台湾快递对比 - 速豹集运",
        "h1": "飞晋物流替代方案2026：速豹 vs 飞晋 大陆寄台湾对比",
        "meta": "找飞晋物流替代？速豹集运vs飞晋全维度对比：大件货运、设备出口、搬家服务、城市覆盖。20+城市专线直达台湾，家具/建材/机械门到门。免费获取对比报价→",
        "kw": "飞晋物流替代,飞晋物流对比,大陆到台湾物流,飞晋替代方案,台湾海运物流",
        "competitor": "飞晋物流",
        "body": """
        <h2>飞晋物流 vs 速豹集运：核心对比</h2>
        <table><tr><th>对比维度</th><th>飞晋物流</th><th>速豹集运</th></tr>
        <tr><td>主营</td><td>大陆→台湾 快递/货运</td><td>大陆→台湾 大件物流 + 台湾→大陆</td></tr>
        <tr><td>大件设备</td><td>有货运服务</td><td>核心专长，专业设备包装运输</td></tr>
        <tr><td>城市专线</td><td>主要港口</td><td>20+城市独立专线页</td></tr>
        <tr><td>双向服务</td><td>以大陆→台湾为主</td><td>双向全品类，含台湾敏感货</td></tr>
        <tr><td>在线工具</td><td>基础</td><td>运费计算器+材积计算+商品查询</td></tr></table>

        <h2>速豹集运的优势</h2>
        <ul><li><strong>大件物流专精</strong>：家具拆卸、设备木箱包装、建材运输——不是顺带做，是核心业务</li>
        <li><strong>20+城市直达</strong>：厦门/深圳/上海/广州等每个城市有独立专线页面，含时效+运费</li>
        <li><strong>双向全品类</strong>：大陆寄台湾 + 台湾寄大陆（含食品/化妆品/保健品等敏感货）</li>
        <li><strong>免费在线工具</strong>：运费计算器、材积计算器、200+商品"能不能寄"查询</li></ul>
        """,
        "faq": [
            ("飞晋物流可靠吗？有什么替代？","飞晋是大陆到台湾的老牌物流商，但如果需要更专业的大件物流服务（家具/设备/建材）或台湾寄大陆的敏感货渠道，速豹集运是更好的替代方案。"),
            ("速豹和飞晋哪个便宜？","具体价格取决于货物类型、体积、目的地。大件货物方面，速豹的拼柜方案可以省60%以上。建议同时获取两家报价做对比，微信免费咨询。"),
        ],
    },
    {
        "slug": "hangying-alternative",
        "title": "航鹰物流替代方案2026 | 两岸物流公司对比 - 速豹集运",
        "h1": "航鹰物流替代方案2026：速豹 vs 航鹰 两岸大件物流对比",
        "meta": "找航鹰物流替代？速豹集运vs航鹰全维度对比：大件设备运输、搬家服务、台湾敏感货专线。20+城市直达台湾，免费材积计算+运费估算→",
        "kw": "航鹰物流替代,航鹰对比,两岸物流公司,航鹰替代方案,台湾物流比较",
        "competitor": "航鹰物流",
        "body": """
        <h2>航鹰物流 vs 速豹集运</h2>
        <table><tr><th>对比维度</th><th>航鹰物流</th><th>速豹集运</th></tr>
        <tr><td>定位</td><td>两岸综合物流</td><td>两岸大件物流专家</td></tr>
        <tr><td>大件专长</td><td>一般货运</td><td>家具/设备/建材专线</td></tr>
        <tr><td>台湾→大陆</td><td>一般物品</td><td>敏感货专线（食品/化妆品/保健品）</td></tr>
        <tr><td>城市覆盖</td><td>主要城市</td><td>20+城市独立专线</td></tr>
        <tr><td>在线工具</td><td>有限</td><td>运费/材积/商品查询3个工具</td></tr></table>
        <p>速豹集运定位「两岸大件物流专家」，在设备出口、家具搬运、建材运输方面有更深积累。同时提供台湾寄大陆敏感货专线，这是多数两岸物流公司不具备的能力。</p>
        """,
        "faq": [
            ("航鹰物流和速豹哪个好？","航鹰是综合物流商，速豹是大件物流专家。如果你寄的是家具/设备/建材等大件货物，速豹更专业。如果只是小件快递，两家都可以。建议根据具体货物咨询对比。"),
        ],
    },
]


def gen(p):
    s = p["slug"]
    fname = f"{s}.html"
    faq_json = ",".join([
        '{"@type":"Question","name":"' + q + '","acceptedAnswer":{"@type":"Answer","text":"' + a + '"}}'
        for q, a in p["faq"]
    ])

    html = f'''<!DOCTYPE html>
<html lang="zh-CN"><head>
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
<link rel="canonical" href="{BASE}/blog/{s}">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"速豹集运","url":"{BASE}"}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"首页","item":"{BASE}/"}},{{"@type":"ListItem","position":2,"name":"{p["h1"][:20]}","item":"{BASE}/blog/{s}"}}]}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_json}]}}</script>
<script type="application/ld+json">{{"@context":"https://ziyuan.baidu.com/contexts/cambrian.jsonld","@type":"WebPage","title":"{p["h1"]}","description":"{p["meta"][:120]}","pubDate":"{TODAY}","upDate":"{TODAY}"}}</script>
<link rel="stylesheet" href="../style.css">
<meta name="format-detection" content="telephone=no">
</head><body>
<header class="site-header"><div class="container"><div class="header-inner">
<a href="/" class="brand"><img src="../images/logo.webp" alt="速豹集运" style="height:40px"></a>
<nav class="main-nav"><a href="/equipment/">大件物流</a><a href="/city-shipping-guide">城市指南</a><a href="/pricing-calculator">运费估算</a><a href="/tw-to-cn/">台湾寄大陆</a><a href="/article-list">文章攻略</a><a href="/contact">询价</a></nav>
</div></div></header>
<main><article class="blog-post"><div class="container">
<header class="post-header"><h1>{p["h1"]}</h1><p class="post-meta">速豹集运 · {TODAY} · 阅读约5分钟</p></header>
<div class="post-content">
<div style="background:#FFF3CD;padding:20px;border-radius:8px;border-left:4px solid #FFC107;margin-bottom:24px">
<strong>📌 快速结论：</strong>如果你在寻找{p["competitor"]}的替代方案，速豹集运在大件物流（家具/设备/建材）和台湾寄大陆敏感货方面有显著优势。免费咨询获取对比报价：<strong>13026603164</strong>（微信同号）
</div>
{p["body"]}
<div style="text-align:center;padding:32px;background:linear-gradient(135deg,#0052D9,#003DA5);color:#fff;border-radius:12px;margin:32px 0">
<h2 style="color:#fff;margin:0">正在对比{p["competitor"]}和速豹？</h2>
<p style="margin:8px 0 16px">告知货物类型和目的地，30分钟出对比方案</p>
<a href="tel:13026603164" style="display:inline-block;background:#fff;color:#0052D9;padding:14px 32px;border-radius:8px;font-weight:700;font-size:16px;text-decoration:none">📞 立即咨询</a>
</div>
</div></div></article></main>
<footer class="site-footer"><div class="container">
<p>© 2026 速豹集运 — 两岸大件物流专家</p>
<p><a href="https://beian.miit.gov.cn/" target="_blank" rel="noopener">湘ICP备2026016030号-2</a></p>
</div></footer>
</body></html>'''

    return fname, html


def main():
    for p in ALTERNATIVES:
        fname, html = gen(p)
        with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ {fname}")

    print(f"\n📊 {len(ALTERNATIVES)} 个竞品替代页")


if __name__ == "__main__":
    main()
