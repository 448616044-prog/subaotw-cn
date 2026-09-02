#!/usr/bin/env python3
"""Generate Phase 2 TW-to-CN moving scenario pages for subaotw.cn"""

import os

TODAY = "2026-07-22"
BASE_URL = "https://www.subaotw.cn"

PAGES = [
    {
        "slug": "student-moving-taiwan-to-mainland",
        "title": "台湾留学生搬家回大陆攻略2026 | 行李海运+清关全流程 - 速豹集运",
        "h1": "台湾留学生搬家回大陆全攻略2026：行李海运、清关避坑",
        "meta": "台湾留学生毕业搬家回大陆怎么办？行李海运、书籍托运、电器寄送全流程。凭学生签证个人物品免税清关，海运7-15天门到门。免费估运行李运费→",
        "keywords": "台湾留学生搬家,留学生搬家回大陆,台湾留学生行李海运,留学生行李寄大陆,毕业搬家台湾大陆",
        "faq": [
            ("台湾留学生搬家回大陆，行李怎么运最便宜？", "海运拼柜最便宜。留学生个人旧物品（衣服、书籍、生活用品）1-2立方米约2000-4000元人民币。建议和其他留学生拼一个柜，分摊运费更划算。"),
            ("留学生毕业回大陆，家电可以海运吗？", "可以。旧家电（电脑、显示器、小冰箱、电饭煲等）凭学生签证可免税清关。建议用原包装或木箱加固，海运7-15天送达。新购买的家电需补税。"),
            ("留学生个人物品清关需要什么证件？", "主要需要：① 护照（含有效签证页）② 台胞证/大陆通行证 ③ 毕业证书或在学证明 ④ 物品清单（中英文）。个人自用旧物品基本免税。"),
            ("台湾寄书回大陆怎么寄？几箱书运费多少？", "书籍属于普货，海运最划算。10箱书（约100kg）海运拼柜约800-1500元人民币。需注意：敏感政治类书籍禁运，教材和普通读物没问题。"),
            ("留学生离台搬家，提前多久安排？", "建议提前2-3周联系物流公司。预留1周打包+1周海运+1周清关派送。毕业季（6-7月、12-1月）是高峰期，提前安排可避开排队。"),
        ],
        "desc": "每年数千名大陆留学生在台湾完成学业后需要将行李、书籍、生活用品搬回大陆。个人物品海运是最经济的选择。",
    },
    {
        "slug": "businessman-moving-taiwan-to-mainland",
        "title": "台商搬家回大陆2026 | 工厂设备+家具海运门到门 - 速豹集运",
        "h1": "台商搬家回大陆全攻略2026：工厂设备+家具海运一条龙",
        "meta": "台商回大陆发展，工厂设备、办公室家具、个人家当怎么搬？整柜/拼柜海运方案，协助出口报关+大陆清关。设备/家具/库存一站式门到门，免费上门评估→",
        "keywords": "台商搬家回大陆,台商回大陆搬家,台湾工厂搬迁大陆,台商设备海运,台湾搬厂到大陆,台商海运搬家",
        "faq": [
            ("台商从台湾搬厂回大陆，设备怎么运？", "工厂设备走海运整柜或拼柜。重型设备需专业木箱包装+固定，用40HQ高柜运输。速豹提供台湾上门拆卸→包装→海运→大陆清关→派送到厂全程服务。"),
            ("台商搬设备回大陆需要交关税吗？", "旧设备凭公司文件和资产评估报告可申请免税进口。新设备需按品类缴纳关税（一般5-15%）。建议提前准备：公司营业执照、设备清单、购买发票、资产评估报告。"),
            ("台商搬家回大陆，家具和私人物品怎么处理？", "家具走海运拼柜最经济。私人物品（衣物、书籍、收藏品）可随家具一起装箱运输。建议分类打包：家具类、电器类、私人物品类分开标注，清关更顺畅。"),
            ("台湾搬厂到大陆整个流程需要多久？", "从上门评估到大陆派送完成，全程约15-25天：上门拆卸包装3-5天 + 海运7-10天 + 大陆清关3-5天 + 派送2-3天。具体时长取决于货物量和清关复杂度。"),
            ("台商回大陆，库存商品可以一起运吗？", "可以。库存商品需按商业货物报关，缴纳进口关税和增值税。建议和私人物品分票报关，私人物品走个人物品通道、商品走商业报关，税率更优。"),
        ],
        "desc": "台商回大陆发展是近年趋势。从工厂设备搬迁到个人家当搬运，需要专业的跨境物流方案。海运门到门是最省心的选择。",
    },
    {
        "slug": "furniture-taiwan-to-mainland",
        "title": "台湾家具寄大陆2026 | 家具海运门到门费用+流程 - 速豹集运",
        "h1": "台湾家具寄大陆全攻略2026：实木家具/红木家具海运费用流程",
        "meta": "台湾家具寄大陆怎么运？实木家具、红木家具、新购家具海运门到门全流程。台湾上门包装→海运→大陆清关派送。1立方米800-1200元起，整柜更省。免费估运费→",
        "keywords": "台湾家具寄大陆,台湾家具海运,台湾实木家具寄大陆,台湾红木家具海运,家具台湾寄大陆运费,家具海运大陆",
        "faq": [
            ("台湾家具寄大陆怎么运？运费多少？", "家具走海运拼柜最划算。1立方米约800-1200元人民币，整柜20GP约3000-5000元。费用含台湾上门取件+包装+海运+大陆清关+派送到家。红木/实木家具体积大，建议走整柜。"),
            ("台湾红木家具可以寄大陆吗？需要什么手续？", "可以。红木家具属于普通货物，海运可正常运输。需提供：购买凭证（发票或收据）、木材品种说明。旧红木家具（个人使用过的）可免税清关；新购红木家具需按品类缴税。"),
            ("台湾新买的家具寄大陆要交税吗？", "新购家具需缴纳进口关税+增值税。木质家具关税约5-10%，加上增值税13%，综合税率约18-25%。个人自用旧家具凭台胞证可免税。购买凭证保留好，报关更顺利。"),
            ("家具海运到大陆需要多长时间？", "台湾到大陆海运7-10天，加上两头上门取件+清关+派送，全程约12-18天门到门。福建/广东等沿海省份清关更快，内陆城市（如成都/重庆）需额外2-3天陆运。"),
            ("家具海运怎么包装才不会损坏？", "实木家具必须多层保护：① 边角用泡沫护角 ② 表面覆PE膜防刮 ③ 整体缠绕气泡膜 ④ 定制木箱固定。速豹提供专业家具包装服务，运输损坏包赔。红木/古董家具建议买运输保险。"),
        ],
        "desc": "台湾家具工艺精湛，实木家具和红木家具在大陆市场需求旺盛。无论是搬家自带还是商业采购，海运门到门是最稳妥的方式。",
    },
]


def generate_page(p):
    slug = p["slug"]
    filename = f"{slug}.html"

    faq_json = ",".join([
        '{"@type":"Question","name":"' + q + '","acceptedAnswer":{"@type":"Answer","text":"' + a + '"}}'
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
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="baidu-site-verification" content="codeva-K4kVPs6NwjtWr4ij" />
  <title>{p["title"]}</title>
  <meta property="og:title" content="{p["h1"]}">
  <meta property="og:description" content="{p["meta"]}">
  <meta property="og:image" content="{BASE_URL}/images/og-image.jpg">
  <meta property="og:url" content="{BASE_URL}/blog/{slug}">
  <meta property="og:type" content="article">
  <meta name="description" content="{p["meta"]}">
  <meta name="keywords" content="{p["keywords"]}">
  <link rel="canonical" href="{BASE_URL}/blog/{slug}">
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"速豹集运","url":"{BASE_URL}","logo":"{BASE_URL}/images/logo.png","contactPoint":{{"@type":"ContactPoint","telephone":"13026603164","contactType":"customer service"}},"address":{{"@type":"PostalAddress","addressCountry":"中国","addressRegion":"湖南省"}},"sameAs":["{BASE_URL}"]}}</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"首页","item":"{BASE_URL}/"}},{{"@type":"ListItem","position":2,"name":"文章攻略","item":"{BASE_URL}/article-list"}},{{"@type":"ListItem","position":3,"name":"{p["h1"]}","item":"{BASE_URL}/blog/{slug}"}}]}}</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_json}]}}</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{p["h1"]}","description":"{p["meta"]}","author":{{"@type":"Organization","name":"速豹集运"}},"publisher":{{"@type":"Organization","name":"速豹集运","url":"{BASE_URL}"}},"datePublished":"{TODAY}","dateModified":"{TODAY}"}}</script>
  <script type="application/ld+json">{{"@context":"https://ziyuan.baidu.com/contexts/cambrian.jsonld","@type":"WebPage","title":"{p["h1"]} | 速豹集运","description":"{p["meta"]}","pubDate":"{TODAY}","upDate":"{TODAY}"}}</script>
  <link rel="stylesheet" href="../style.css">
  <meta name="format-detection" content="telephone=no">
</head>
<body>
<header class="site-header">
  <div class="container">
    <div class="header-inner">
      <a href="/" class="brand"><img src="../images/logo.webp" alt="速豹集运" loading="lazy" style="height:40px"></a>
      <nav class="main-nav">
        <a href="/equipment/">大件物流</a>
        <a href="/city-shipping-guide">城市指南</a>
        <a href="/pricing-calculator">运费估算</a>
        <a href="/tw-to-cn/">台湾寄大陆</a>
        <a href="/article-list">文章攻略</a>
        <a href="/contact">询价</a>
      </nav>
    </div>
  </div>
</header>

<main>
  <article class="blog-post">
    <div class="container">
      <header class="post-header">
        <h1>{p["h1"]}</h1>
        <p class="post-meta">速豹集运 · 发布于 {TODAY} · 阅读约8分钟</p>
      </header>

      <div class="post-content">
        <div class="highlight-box">
          <strong>📌 核心摘要：</strong>{p["desc"]}
          <br>📞 <strong>免费咨询：13026603164</strong>（微信同号）
        </div>

        <h2>一、{p["h1"].split("：")[0] if "：" in p["h1"] else p["h1"]} — 整体流程</h2>
        <p>{p["desc"]}从台湾到大陸的物流流程主要分为五个步骤：</p>
        <ol>
          <li><strong>联系评估</strong>：告知货物信息（品类/体积/重量/目的地城市），30分钟内获取专属方案和报价</li>
          <li><strong>上门包装/取件</strong>：台湾全岛上门取件（含包装服务），按货物类型选择木箱/纸箱/气泡膜包装</li>
          <li><strong>出口报关</strong>：协助准备出口文件，报关放行</li>
          <li><strong>海运/空运</strong>：海上运输7-10天（空运2-5天），实时追踪物流轨迹</li>
          <li><strong>大陆清关+派送</strong>：进口清关后门到门派送，全程12-18天</li>
        </ol>

        <h2>二、费用参考</h2>
        <p>具体费用根据货物类型、体积、重量、目的地综合计算。以下为参考范围：</p>
        <table>
          <tr><th>运输方式</th><th>适用场景</th><th>参考价格</th><th>时效</th></tr>
          <tr><td>海运拼柜</td><td>1-5立方米货物</td><td>800-1200元/立方米</td><td>12-18天</td></tr>
          <tr><td>海运整柜 20GP</td><td>搬家/整批货物</td><td>3000-5000元/柜</td><td>10-15天</td></tr>
          <tr><td>海运整柜 40HQ</td><td>大件设备/工厂搬迁</td><td>5000-8000元/柜</td><td>10-15天</td></tr>
          <tr><td>空运快递</td><td>急用小件</td><td>25-45元/kg</td><td>2-5天</td></tr>
        </table>
        <p><em>以上为参考价格，实际报价以货物评估为准。费用包含台湾取件+海运+大陆清关+派送。</em></p>

        <h2>三、清关与证件要求</h2>
        <p>根据货物性质不同，清关要求也不同：</p>
        <table>
          <tr><th>货物类型</th><th>所需证件</th><th>关税情况</th></tr>
          <tr><td>个人旧物品（搬家）</td><td>台胞证/护照 + 物品清单</td><td>基本免税</td></tr>
          <tr><td>新购商品</td><td>购买发票 + 物品清单</td><td>按品类缴关税+增值税</td></tr>
          <tr><td>商业货物</td><td>合同/发票/箱单/报关委托书</td><td>按海关税则缴税</td></tr>
        </table>

        <h2>四、包装要求与注意事项</h2>
        <ul>
          <li><strong>易碎品</strong>：必须用气泡膜+泡沫+木箱三层保护，标注"易碎"</li>
          <li><strong>电器</strong>：原包装优先，无原包装需定制木箱固定</li>
          <li><strong>实木家具</strong>：边角护角+PE膜+气泡膜+木箱，四层保护</li>
          <li><strong>衣物/书籍</strong>：纸箱打包，标注"衣物"或"书籍"，单箱不超过25kg</li>
          <li><strong>禁运品</strong>：动植物、新鲜食品、易燃易爆品、政治敏感物品不可寄</li>
        </ul>

        <h2>五、常见问题</h2>
        <div class="faq-section">
'''

    for q, a in p["faq"]:
        html += f'''          <div class="faq-item">
            <h3>❓ {q}</h3>
            <p>{a}</p>
          </div>
'''

    html += f'''        </div>

        <div class="cta-box">
          <h2>📞 {p["h1"].split("：")[0] if "：" in p["h1"] else p["h1"]} — 免费获取方案</h2>
          <p>告知货物信息，30分钟出专属物流方案+精准报价</p>
          <p style="font-size:20px"><strong>📞 13026603164</strong>（微信同号）</p>
          <a href="tel:13026603164" class="btn-primary">立即电话咨询</a>
        </div>

      </div>
    </div>
  </article>
</main>

<footer class="site-footer">
  <div class="container">
    <p>© 2026 速豹集运 — 两岸大件物流专家</p>
    <p><a href="https://beian.miit.gov.cn/" target="_blank" rel="noopener">湘ICP备2026016030号-2</a></p>
  </div>
</footer>
</body>
</html>'''

    return filename, html


def main():
    out_dir = os.path.join(os.path.dirname(__file__), "blog")
    generated = []
    for p in PAGES:
        filename, html = generate_page(p)
        path = os.path.join(out_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        generated.append(filename)
        print(f"✅ {filename}")

    print(f"\n📊 生成: {len(generated)} 个页面")
    print(f"📂 输出: {out_dir}")


if __name__ == "__main__":
    main()
