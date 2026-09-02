#!/usr/bin/env python3
"""
subaotw.cn Phase 2 内容生成器
生成：大件搬家6篇 + 大件货运3篇
"""
import os, re, json
from datetime import date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TODAY = date.today().isoformat()
BRAND = "速豹集运"
DOMAIN = "https://www.subaotw.cn"

# ── 公共 head 模板 ──
def page_head(title, desc, canonical, schemas=""):
    """生成页面head部分"""
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="baidu-site-verification" content="codeva-K4kVPs6NwjtWr4ij"/>
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <link rel="stylesheet" href="/style.css">
  {schemas}
<script>
var _hmt = _hmt || [];
(function() {{
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?e5f0f3c4a1b2d6e8f9a0b1c2d3e4f5a6";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
}})();
</script>
<script>
(function(){{
    var bp = document.createElement('script');
    var curProtocol = window.location.protocol.split(':')[0];
    if (curProtocol === 'https') {{
        bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
    }}
    else {{
        bp.src = 'http://push.zhanzhang.baidu.com/push.js';
    }}
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);
}})();
</script>
</head>"""

def schema_json(schema_dict):
    """将dict转为JSON-LD script标签"""
    return f'  <script type="application/ld+json">{json.dumps(schema_dict, ensure_ascii=False, separators=(",", ":"))}</script>\n'

def article_schema(headline, desc):
    return schema_json({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": headline,
        "description": desc[:200],
        "author": {"@type": "Organization", "name": BRAND},
        "publisher": {"@type": "Organization", "name": BRAND, "url": DOMAIN},
        "datePublished": TODAY,
        "dateModified": TODAY
    })

def breadcrumb_schema(items):
    """items: list of (name, url_or_None)"""
    list_items = []
    for i, (name, url) in enumerate(items, 1):
        item = {"@type": "ListItem", "position": i, "name": name}
        if url:
            item["item"] = url
        list_items.append(item)
    return schema_json({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": list_items
    })

def faq_schema(qa_list):
    """qa_list: list of (question, answer) tuples"""
    entities = []
    for q, a in qa_list[:8]:
        entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a[:300]}
        })
    return schema_json({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities
    })

# ── 公共 header/footer 模板 ──
HEADER = """<body>
    <header class="header">
    <div class="container">
      <a href="/" class="logo">速豹集运<span>两岸大件物流专家</span></a>
      <button class="burger" aria-label="菜单" onclick="this.nextElementSibling.classList.toggle('open')">☰</button>
      <nav class="nav">
        <a href="/equipment/">设备运输</a>
        <a href="/tw-to-cn/">台湾寄大陆</a>
        <a href="/pricing-calculator">运费估算</a>
        <a href="/volume-calculator">材积计算</a>
        <a href="/guide/">物流指南</a>
        <a href="/contact">询价报价</a>
        <a href="/about">关于我们</a>
      </nav>
    </div>
  </header>
"""

FOOTER = """  <footer class="footer">
    <div class="container">
      <p>© 2026 速豹集运 | <a href="https://beian.miit.gov.cn/" target="_blank" rel="nofollow">湘ICP备2026016030号-2</a></p>
      <p>微信：13026603164 | 邮箱：business@videotvai.com</p>
    </div>
  </footer>
</body>
</html>"""

CTA_SECTION = """  <section class="section cta" style="background:var(--blue);color:#fff;text-align:center">
    <div class="container">
      <h2>有货物需要运到台湾？</h2>
      <p style="font-size:1.15rem;margin-bottom:1.5rem">免费获取方案和报价 — 30分钟内回复</p>
      <a href="/contact" class="btn" style="background:#fff;color:var(--blue);font-size:1.1rem;padding:1rem 2.5rem">📋 立即询价</a>
    </div>
  </section>
"""

# ═══════════════════════════════════════════════════════════════
# 页面数据定义
# ═══════════════════════════════════════════════════════════════

PAGES = []

# ── 1. 大陆搬家到台湾 ──
PAGES.append({
    "file": "moving-taiwan.html",
    "title": "大陆搬家到台湾全攻略 | 两岸搬家费用/流程/海运",
    "desc": "2026大陆搬家到台湾最全攻略：搬家费用明细、海运搬家流程、家具打包服务、清关手续、搬家时间线。速豹集运两岸搬家专线，门到门一站式服务，免费获取搬家报价。",
    "canonical": f"{DOMAIN}/moving-taiwan",
    "breadcrumb": [("首页", DOMAIN), ("大陆搬家到台湾", None)],
    "article_headline": "大陆搬家到台湾全攻略：费用/流程/注意事项",
    "faqs": [
        ("大陆搬家到台湾大概需要多少钱？", "搬家费用取决于物品体积和重量。一般家庭搬家（1-2居室）：海运拼柜约6000-15000元，整柜约15000-35000元。含打包、报关、海运、台湾清关、送货上门全套服务。"),
        ("大陆搬家到台湾需要多长时间？", "海运搬家全程约15-25天：大陆上门打包1-2天，报关出口2-3天，海运5-7天，台湾清关3-5天，送货到家1-2天。加急可选空运专线（5-7天，费用翻倍）。"),
        ("哪些物品不能搬去台湾？", "台湾海关禁运品包括：新鲜蔬果肉类、活体动植物、毒品枪支、侵权仿制品。家具、衣物、书籍、家电等个人用品一般都可以运，但旧电器可能需要额外检验。"),
        ("搬家公司提供打包服务吗？", "是的！速豹提供全套打包服务：专业师傅上门拆卸大型家具、气泡膜包裹易碎品、定制木箱保护贵重物品、衣物真空压缩省体积。打包材料费全包。"),
        ("搬家到台湾需要什么证件？", "需要：1) 身份证/台胞证复印件 2) 物品清单（中英文）3) 台湾住址证明。留学生搬家额外需要学校录取通知书。我们会协助准备全套报关文件。"),
    ],
    "content": """
  <article class="article">
    <div class="container">
      <h1>大陆搬家到台湾全攻略（2026最新版）</h1>
      <p>从大陆搬家到台湾，无论是工作调动、家庭团聚还是留学归台，都是一项大工程。很多人第一次面对两岸搬家时最大的困惑是：<strong>找谁搬？多少钱？怎么报关？哪些能带哪些不能带？</strong></p>
      <p>速豹集运深耕两岸物流6年，累计服务500+搬家客户。这篇文章把<strong>流程、费用、打包、清关</strong>一次讲透。</p>

      <h2>一、大陆搬家到台湾的3种方式</h2>
      <div class="compare-table">
        <table>
          <tr><th>方式</th><th>适合人群</th><th>时效</th><th>费用参考</th></tr>
          <tr><td><strong>海运拼柜</strong></td><td>个人搬家（1-2居室）</td><td>15-25天</td><td>6000-15000元</td></tr>
          <tr><td><strong>海运整柜</strong></td><td>家庭搬家（3居室+）</td><td>12-20天</td><td>15000-35000元</td></tr>
          <tr><td><strong>空运专线</strong></td><td>少量急用物品</td><td>5-7天</td><td>按kg计，约30-50元/kg</td></tr>
        </table>
      </div>

      <h2>二、搬家全流程（共8步）</h2>
      <ol class="process-list">
        <li><strong>免费咨询</strong>：联系我们，告知搬家物品概况和目的地</li>
        <li><strong>上门评估</strong>：师傅上门查看物品量，给出准确报价</li>
        <li><strong>签订合同</strong>：确认方案、费用、时效，签运输合同</li>
        <li><strong>专业打包</strong>：师傅上门拆卸家具、分类打包、贴标</li>
        <li><strong>报关出口</strong>：准备装箱单、报关单，大陆海关申报</li>
        <li><strong>海运运输</strong>：货物装船，厦门/福州→基隆/台中/高雄</li>
        <li><strong>台湾清关</strong>：台湾海关申报，缴纳进口税（个人行李免税额500美元）</li>
        <li><strong>送货到家</strong>：台湾端拆包、组装家具、摆放到位</li>
      </ol>

      <h2>三、搬家费用明细</h2>
      <p>费用由以下部分构成（以1居室搬家为例）：</p>
      <ul>
        <li><strong>打包费</strong>：含材料，约2000-4000元</li>
        <li><strong>报关费</strong>：大陆出口约800-1500元，台湾进口约2000-4000元</li>
        <li><strong>海运费</strong>：拼柜约3000-6000元，整柜约8000-20000元</li>
        <li><strong>台湾送货</strong>：约2000-5000元（视距离而定）</li>
        <li><strong>台湾进口税</strong>：个人行李500美元以内免税，超出部分按品类计税</li>
      </ul>

      <h2>四、搬家打包Tips</h2>
      <ul>
        <li>✅ 易碎品（瓷器、玻璃）→ 气泡膜+硬纸箱，标注"易碎"</li>
        <li>✅ 大型家具 → 拆卸后缠绕拉伸膜，加护角保护</li>
        <li>✅ 衣物被褥 → 真空压缩袋，省70%体积</li>
        <li>✅ 贵重物品（首饰、证件）→ 建议随身携带，不放运输</li>
        <li>❌ 液体（调料、化妆品）→ 密封包装，单独装箱</li>
        <li>❌ 电子产品 → 建议取出电池，单独标记</li>
      </ul>

      <h2>五、搬家时间线参考</h2>
      <p>从咨询到物品到家，完整时间线：</p>
      <p>📅 <strong>Day 1-3</strong>：咨询评估 + 签合同<br>
      📅 <strong>Day 4-5</strong>：上门打包<br>
      📅 <strong>Day 6-8</strong>：报关出口<br>
      📅 <strong>Day 9-16</strong>：海运航行<br>
      📅 <strong>Day 17-21</strong>：台湾清关<br>
      📅 <strong>Day 22-25</strong>：送货到家</p>
    </div>
  </article>
"""
})

# ── 2. 台湾搬家回大陆 ──
PAGES.append({
    "file": "moving-from-taiwan.html",
    "title": "台湾搬家回大陆全攻略 | 搬家费用/流程/注意事项",
    "desc": "从台湾搬家回大陆完整指南：台湾搬家费用、行李托运流程、海运行李回大陆、报关清关手续。速豹集运台湾→大陆搬家专线，上门打包到送货到家，免费估价。",
    "canonical": f"{DOMAIN}/moving-from-taiwan",
    "breadcrumb": [("首页", DOMAIN), ("台湾搬家回大陆", None)],
    "article_headline": "台湾搬家回大陆全攻略：反向搬家看完就懂",
    "faqs": [
        ("台湾搬家回大陆要多少钱？", "台湾搬家回大陆费用视物品量而定。1-2居室海运行李约8000-18000元，含打包、报关、海运、大陆清关、送货。部分物品走快递专线更划算（衣物/书籍约20-30元/kg）。"),
        ("从台湾海运行李回大陆要多久？", "台湾→大陆海运搬家全程约12-20天：台湾打包1-2天，报关出口2天，海运3-5天，大陆清关3-5天，送货2-3天。比大陆→台湾方向快3-5天。"),
        ("台湾搬家回大陆需要交税吗？", "中国海关规定：居民从境外搬家回国的个人自用行李，在合理数量范围内免征关税。需提供：护照（中国公民）、物品清单、台湾居住证明。留学生的书本、电脑等学习用品免税。"),
        ("哪些东西不建议从台湾搬回大陆？", "不建议：1) 大型家电（电压110V，大陆220V需变压）2) 食品（保质期短的不划算）3) 大陆同样能买到的日用品。建议带：书籍、衣服、纪念品、收藏品、乐器等有情感价值的物品。"),
    ],
    "content": """
  <article class="article">
    <div class="container">
      <h1>台湾搬家回大陆全攻略：反向搬家不踩坑</h1>
      <p>结束台湾的工作、学业，或是把台湾的家搬回大陆——反向搬家看似简单，实际操作中有不少细节容易被忽略。这篇指南覆盖<strong>从台湾打包到大陆收货</strong>的全过程。</p>

      <h2>一、台湾→大陆搬家的3种方式</h2>
      <div class="compare-table">
        <table>
          <tr><th>方式</th><th>适合</th><th>时效</th><th>费用</th></tr>
          <tr><td><strong>快递专线</strong></td><td>少量衣物/书籍/杂物</td><td>5-7天</td><td>20-35元/kg</td></tr>
          <tr><td><strong>海运拼箱</strong></td><td>1-2居室搬家</td><td>12-18天</td><td>8000-15000元</td></tr>
          <tr><td><strong>海运整柜</strong></td><td>3居室+或大量家具</td><td>15-20天</td><td>15000-30000元</td></tr>
        </table>
      </div>

      <h2>二、搬家流程</h2>
      <ol class="process-list">
        <li><strong>咨询估量</strong>：告知物品类型和大致体积，免费估价</li>
        <li><strong>台湾上门打包</strong>：我们在台北/新北/台中/高雄有合作打包师傅</li>
        <li><strong>台湾报关出口</strong>：准备出口报关文件，台湾海关申报</li>
        <li><strong>海运/空运</strong>：基隆/高雄→厦门/福州/深圳</li>
        <li><strong>大陆清关</strong>：中国海关申报，居民回国行李免税</li>
        <li><strong>大陆送货到家</strong>：配送到指定地址，拆包摆放</li>
      </ol>

      <h2>三、海关注意事项</h2>
      <p><strong>免税条件</strong>：中国公民从境外（含台湾）搬家回国的个人自用行李，在合理数量内免征进口关税。需要提供的文件：</p>
      <ul>
        <li>中国护照/台胞证（证明居民身份）</li>
        <li>物品装箱清单（品名、数量、估计价值）</li>
        <li>台湾居住证明（租房合同/水电账单/居留证）</li>
        <li>分运单或提单</li>
      </ul>

      <h2>四、常见问题</h2>
      <ul>
        <li><strong>110V电器能在大陆用吗？</strong> → 大部分需要变压器，电视/冰箱等大件不划算，建议当地处理</li>
        <li><strong>台湾买的书能带多少？</strong> → 个人自用书籍一般不受限制，但不得含有违禁内容</li>
        <li><strong>名贵家具可以退税吗？</strong> → 台湾出口没有购物退税，但大陆进口可申请留学生分运行李免税</li>
        <li><strong>宠物可以一起运吗？</strong> → 可以，但需要狂犬疫苗证明+健康检疫+隔离，流程较长，建议提前2个月准备</li>
      </ul>
    </div>
  </article>
"""
})

# ── 3. 家具海运台湾 ──
PAGES.append({
    "file": "furniture-shipping.html",
    "title": "家具海运台湾 | 实木家具/红木/定制家具出口台湾",
    "desc": "大陆家具海运到台湾专线：实木家具、红木家具、定制家具、办公家具出口台湾全攻略。专业木箱包装、海运拼柜/整柜、台湾清关送货。免费获取家具出口报价。",
    "canonical": f"{DOMAIN}/furniture-shipping",
    "breadcrumb": [("首页", DOMAIN), ("家具海运台湾", None)],
    "article_headline": "大陆家具海运到台湾：实木/红木/定制家具出口全攻略",
    "faqs": [
        ("大陆家具可以海运到台湾吗？", "可以！大陆家具出口台湾是非常成熟的物流路线。实木家具、红木家具、定制家具、办公家具等均可海运。需要做好防潮防碰的包装处理，并完成出口报关和台湾进口清关手续。"),
        ("家具海运到台湾要多少钱？", "家具海运费用取决于体积：拼柜约2000-5000元/立方，一套三居室家具（约8-12立方）总费用约15000-25000元含打包、报关、海运、清关、送货。"),
        ("实木家具有什么特殊要求吗？", "实木家具海运台湾需要：1) 熏蒸处理（防止虫害）2) 提供树种证明 3) 木箱包装。熏蒸费用约500-800元/批。未经熏蒸处理的实木制品可能被台湾海关退回或销毁。"),
        ("家具海运台湾需要多长时间？", "全程约15-20天：打包1-2天，熏蒸1天（如需），报关出口2天，海运5-7天，台湾清关3-5天，送货2-3天。"),
        ("定做家具怎么出口？", "定制家具出口流程：1) 工厂完成生产后，通知我们上门取货 2) 按尺寸定制木箱包装 3) 按新家具报关（需提供工厂发票）4) 海运+清关+送货。注意：实木定制需要熏蒸。"),
    ],
    "content": """
  <article class="article">
    <div class="container">
      <h1>家具海运台湾全攻略：实木/红木/定制家具怎么运？</h1>
      <p>大陆是全球最大的家具生产国，很多台湾客户选择直接从大陆购买家具海运回台，性价比极高。但家具属于大件易损品，运输中的<strong>包装、熏蒸、报关</strong>每个环节都不能出错。</p>

      <h2>一、家具海运台湾的4个关键环节</h2>
      
      <h3>1. 包装——决定家具完好率</h3>
      <p>家具海运最大的风险是碰撞和受潮。我们的包装标准：</p>
      <ul>
        <li><strong>实木家具</strong>：先包气泡膜 → 再包珍珠棉（防震层） → 定制木箱固定</li>
        <li><strong>沙发/床垫</strong>：PE缠绕膜防水 → 加厚纸板护角 → 防潮编织袋</li>
        <li><strong>玻璃/大理石</strong>：独立木箱固定，箱内填充泡沫，标注"向上"和"易碎"</li>
        <li><strong>拆装家具</strong>：拆卸后分类包装，五金件单独密封袋，附组装图纸</li>
      </ul>

      <h3>2. 熏蒸——实木家具必做</h3>
      <p>任何含<strong>未加工木材</strong>的家具出口台湾，必须进行熏蒸处理并取得熏蒸证书。这是台湾海关的强制要求，目的是防止木材害虫入境。已上漆/贴面的家具通常不需要熏蒸，但需提供材质证明。</p>

      <h3>3. 报关——选对HS编码</h3>
      <p>家具出口报关时，正确的HS编码（海关商品编码）非常重要。我们协助准备全套报关文件：商业发票、装箱单、熏蒸证书（如需）、原产地证明。</p>

      <h3>4. 台湾进口清关+缴税</h3>
      <p>家具进口台湾的关税约5-10%（视品类），另加5%营业税。新家具需提供大陆工厂发票，旧家具按折旧估价。个人搬家使用的旧家具可申请免税额度。</p>

      <h2>二、常见家具品类运费参考</h2>
      <div class="compare-table">
        <table>
          <tr><th>家具类型</th><th>体积(立方)</th><th>拼柜运费(元)</th><th>含熏蒸</th></tr>
          <tr><td>实木餐桌+6椅</td><td>1.5-2</td><td>3000-5000</td><td>含</td></tr>
          <tr><td>床+床垫+床头柜</td><td>2-3</td><td>4000-7500</td><td>含</td></tr>
          <tr><td>布艺沙发(3人)</td><td>2.5-3.5</td><td>4000-7000</td><td>无需</td></tr>
          <tr><td>红木博古架</td><td>1-2</td><td>3000-5000</td><td>含</td></tr>
          <tr><td>三居室全套家具</td><td>8-12</td><td>12000-20000</td><td>含</td></tr>
        </table>
      </div>

      <h2>三、从购买到收货的完整流程</h2>
      <ol class="process-list">
        <li>选好家具 → 告诉我们品类、尺寸、重量，免费估价</li>
        <li>安排提货 → 我们在广东/福建/浙江/江苏有合作仓库，也可上门取件</li>
        <li>入仓打包 → 专业师傅按品类定制包装方案</li>
        <li>熏蒸处理 → 实木家具必须（1天）</li>
        <li>报关出口 → 大陆海关申报（1-2天）</li>
        <li>海运台湾 → 厦门/福州→基隆/台中/高雄（5-7天）</li>
        <li>台湾清关 → 缴税+查验（3-5天）</li>
        <li>送货到家 → 拆包、组装（按需）</li>
      </ol>
    </div>
  </article>
"""
})

# ── 4. 行李托运台湾 ──
PAGES.append({
    "file": "luggage-shipping.html",
    "title": "行李托运到台湾 | 留学生/工作/探亲行李寄台湾",
    "desc": "大陆行李托运到台湾专线：留学生行李、工作调动行李、探亲行李寄台湾。快递/海运/空运多种方式，上门取件送货到家。个人行李免税额度、打包指南、费用明细。",
    "canonical": f"{DOMAIN}/luggage-shipping",
    "breadcrumb": [("首页", DOMAIN), ("行李托运台湾", None)],
    "article_headline": "行李托运到台湾：留学生/工作/探亲行李寄送全攻略",
    "faqs": [
        ("大陆寄行李到台湾怎么最便宜？", "少量行李（20-50kg）走快递专线最划算，约25-35元/kg，5-7天到。大量行李（100kg+）走海运拼箱更便宜，约15-25元/kg但有固定起步价，全程15-20天。"),
        ("留学生行李寄台湾有免税吗？", "台湾海关对留学生回国行李有免税额度：行李总价值在台币2万元以内免征关税。需提供学校毕业/肄业证明、护照。大陆→台湾方向，大陆这边出口没有特别免税，但行李按个人物品申报即可。"),
        ("行李托运台湾需要什么证件？", "需要：1) 寄件人身份证复印件 2) 收件人在台湾的身份证/居留证 3) 物品清单。如果是留学生，学校证明备用。我们协助准备所有报关文件。"),
        ("哪些行李不能寄？", "禁运品：锂电池（未安装的）、打火机、压缩气体罐、易燃液体、管制刀具、动植物制品、食品（少量密封包装可，需提前确认）。"),
        ("行李怎么打包不容易损坏？", "建议：衣物用真空压缩袋省空间，易碎品（化妆品、电子产品）用气泡膜单独包裹，所有物品装硬质纸箱/行李箱，箱内塞满填充物防晃动。每箱不超过25kg便于搬运。"),
    ],
    "content": """
  <article class="article">
    <div class="container">
      <h1>大陆行李托运到台湾全攻略</h1>
      <p>去台湾读书、工作、探亲，行李怎么带过去最方便？随身只能带2件托运，剩下的怎么办？这篇文章针对<strong>留学生、工作调动、探亲</strong>三大场景，讲清楚行李托运的每一种方式。</p>

      <h2>一、行李托运方式对比</h2>
      <div class="compare-table">
        <table>
          <tr><th>方式</th><th>适合重量</th><th>时效</th><th>费用</th><th>优缺点</th></tr>
          <tr><td><strong>快递专线</strong></td><td>10-100kg</td><td>5-7天</td><td>25-35元/kg</td><td>快但不适合超重件</td></tr>
          <tr><td><strong>空运</strong></td><td>50-200kg</td><td>3-5天</td><td>35-55元/kg</td><td>最快但费用高</td></tr>
          <tr><td><strong>海运拼箱</strong></td><td>100kg+</td><td>15-20天</td><td>15-25元/kg起</td><td>便宜但慢</td></tr>
          <tr><td><strong>随身托运</strong></td><td>≤46kg(2件)</td><td>即到</td><td>含在机票</td><td>免费但有限额</td></tr>
        </table>
      </div>

      <h2>二、三大场景方案</h2>

      <h3>🎓 留学生行李</h3>
      <p>大多数留学生行李在50-100kg（衣服、书籍、被褥、小电器）。推荐<strong>快递专线</strong>，寄到台湾后3-5天到宿舍。费用约1500-3500元。被褥等大体积物品建议真空压缩。</p>

      <h3>💼 工作调动行李</h3>
      <p>外派台湾的行李通常较多（100-200kg），含衣物、书籍、小家电、厨具等。推荐<strong>快递专线（急用）+ 海运拼箱（不急）</strong>组合。急用的走快递，不急的走海运省钱。</p>

      <h3>👨‍👩‍👧 探亲行李</h3>
      <p>去台湾看子女/亲友，带家乡特产+日用品。建议<strong>快递专线</strong>，5-7天直接到家。食品类需提前确认是否可运。</p>

      <h2>三、行李打包清单</h2>
      <ul>
        <li>📦 <strong>硬质纸箱</strong>（建议60×40×50cm，方便搬运）</li>
        <li>🫧 <strong>气泡膜</strong>（包裹易碎品）</li>
        <li>🎒 <strong>真空压缩袋</strong>（衣服被褥省70%体积）</li>
        <li>🏷️ <strong>标签纸</strong>（每箱标注内容和"易碎"标记）</li>
        <li>📋 <strong>装箱清单</strong>（建议拍照留底）</li>
      </ul>

      <h2>四、流程</h2>
      <ol class="process-list">
        <li>联系我们告知行李量和目的地 → 免费估价</li>
        <li>我们上门取件（或你送到仓库）→ 专业打包加固</li>
        <li>准备报关文件 → 大陆出口申报</li>
        <li>运输（快递/空运/海运）→ 台湾清关</li>
        <li>台湾端送货到家</li>
      </ol>
    </div>
  </article>
"""
})

# ── 5. 家电寄台湾 ──
PAGES.append({
    "file": "appliance-shipping.html",
    "title": "大陆家电寄台湾 | 电视机/冰箱/洗衣机/空调出口台湾",
    "desc": "大陆家电出口台湾专线：电视、冰箱、洗衣机、空调等大家电海运台湾。220V电压一致无需变压，专业防震包装、海运拼柜/整柜、台湾清关送货。免费获取家电出口报价。",
    "canonical": f"{DOMAIN}/appliance-shipping",
    "breadcrumb": [("首页", DOMAIN), ("家电寄台湾", None)],
    "article_headline": "大陆家电寄台湾：大家电出口台湾全攻略",
    "faqs": [
        ("大陆家电可以用在台湾吗？", "可以！大陆和台湾都是220V电压，大家电（电视、冰箱、洗衣机、空调等）无需变压直接使用。但需注意插头规格不同：大陆是国标三扁插，台湾是美规三孔，需要转换插座（很便宜，几块钱一个）。"),
        ("家电寄台湾容易损坏吗？", "家电运输最大的风险是震动和碰撞。我们的标准包装：原厂泡沫底座固定+整机气泡膜包裹+加厚纸箱+木架加固。液晶电视额外定制木箱。整体破损率低于1%。"),
        ("家电出口台湾有保修问题吗？", "大陆品牌（海尔、美的、格力、海信等）在台湾没有官方售后。建议：选择国际品牌（有全球联保）或知名国产品牌（台湾有维修网点）。购买时确认保修政策。"),
        ("空调外机能寄吗？", "可以。分体式空调的内外机分别包装，外机因含压缩机和冷媒，需专业固定。变频空调比定频空调更重但更节能，需告知准确重量以便安排车辆。"),
        ("大家电运到台湾要多少钱？", "家电按体积计费。参考：一台65寸电视约0.3立方，运费约600-1000元；一台双门冰箱约1.5立方，运费约2500-4000元；一套分体空调约0.8立方，运费约1500-2500元。以上含打包、报关、清关、送货。"),
    ],
    "content": """
  <article class="article">
    <div class="container">
      <h1>大陆家电寄台湾：电视机/冰箱/洗衣机/空调运输全攻略</h1>
      <p>大陆家电性价比高、选择多，很多搬到台湾的客户选择从大陆购买家电运过去。<strong>220V电压一致、无需变压器</strong>，这是最大的优势。但物流环节需要专业处理。</p>

      <h2>一、为什么从大陆买家电运台湾？</h2>
      <ul>
        <li>💰 <strong>价格优势</strong>：大陆家电市场大、竞争充分，同款产品通常比台湾便宜20-40%</li>
        <li>🔌 <strong>电压一致</strong>：大陆和台湾家用电压都是220V/60Hz，家电插电即用</li>
        <li>🛒 <strong>选择更多</strong>：大陆品牌型号丰富，智能家居、变频产品选择远超台湾</li>
        <li>📱 <strong>智能家居</strong>：小米/华为智能家居生态丰富，台湾不易买到</li>
      </ul>

      <h2>二、各品类运输要点</h2>

      <h3>📺 电视机（液晶/LED/OLED）</h3>
      <p>电视机是最易损坏的家电之一，屏幕不能受力。包装标准：原厂泡沫底座 → 整机气泡膜包裹 → 四角加泡沫护角 → 定制木箱（木板厚度≥9mm）。严禁无木箱直接运输。75寸以上电视建议打封闭木箱。</p>

      <h3>🧊 冰箱</h3>
      <p>冰箱运输前需断电24小时以上，清除内部冰霜和积水。运输时<strong>必须直立</strong>，严禁倒放或侧放（压缩机油会流入管路导致损坏）。门与箱体用胶带固定但不锁死。</p>

      <h3>👕 洗衣机</h3>
      <p>波轮洗衣机较为耐运，滚筒洗衣机需用运输螺栓固定滚筒（防止运输中晃动损坏轴承）。进水管、排水管、说明书等配件单独装袋附在机器上。</p>

      <h3>❄️ 空调（分体/中央）</h3>
      <p>新空调（未加冷媒）运输最简单。已使用的空调需先回收冷媒。外机（含压缩机）较重，需要底部加木托盘便于叉车搬运。</p>

      <h2>三、费用参考</h2>
      <div class="compare-table">
        <table>
          <tr><th>家电品类</th><th>体积(立方)</th><th>运费(元)</th><th>包装费(元)</th></tr>
          <tr><td>55寸电视</td><td>0.2-0.3</td><td>500-800</td><td>200-400(木箱)</td></tr>
          <tr><td>75寸电视</td><td>0.4-0.6</td><td>800-1500</td><td>400-600(木箱)</td></tr>
          <tr><td>双门冰箱</td><td>1.2-1.8</td><td>2000-4000</td><td>300-500</td></tr>
          <tr><td>滚筒洗衣机</td><td>0.6-0.8</td><td>1000-2000</td><td>200-400</td></tr>
          <tr><td>分体空调(1套)</td><td>0.6-1.0</td><td>1200-2500</td><td>300-500</td></tr>
          <tr><td>全套家电(3居室)</td><td>4-8</td><td>8000-16000</td><td>1000-2000</td></tr>
        </table>
      </div>
    </div>
  </article>
"""
})

# ── 6. 两岸搬家费用对比 ──
PAGES.append({
    "file": "moving-cost.html",
    "title": "两岸搬家费用对比 | 大陆搬台湾vs台湾搬大陆价格",
    "desc": "2026两岸搬家费用完整对比：大陆→台湾搬家vs台湾→大陆搬家，海运vs快递价格、隐藏费用拆解、省钱技巧。免费获取精准搬家估价，30分钟出报价方案。",
    "canonical": f"{DOMAIN}/moving-cost",
    "breadcrumb": [("首页", DOMAIN), ("两岸搬家费用", None)],
    "article_headline": "两岸搬家费用对比：大陆搬台湾 vs 台湾搬大陆",
    "faqs": [
        ("大陆搬家到台湾和台湾搬回大陆哪个便宜？", "大陆→台湾搬家通常比台湾→大陆搬家费用稍高（约高10-15%），因为大陆出口报关手续比台湾出口复杂，大陆端打包人力成本低但台湾进口清关时间略长。总体差距不大。"),
        ("搬家费用包含哪些项目？", "完整搬家费用包括：① 打包费（材料+人工）② 报关费（大陆出口+台湾进口）③ 运费（海运/空运）④ 保险费（建议购买，货值1-3%）⑤ 台湾端送货费（含可能的搬上楼费）。不含：台湾进口关税（个人行李免税）。"),
        ("怎么省搬家费？", "5个省钱技巧：1) 自己打包部分物品（衣物/书籍）2) 走拼柜而非整柜（如果不急用）3) 减少带的物品（大陆能买到的日用品别带）4) 淡季搬家（避开春节前后和6-8月旺季）5) 选对计价方式（重货按重量、轻货按体积，提前咨询哪种划算）。"),
        ("搬家费可以开发票吗？", "可以。速豹集运提供正规发票（增值税普通发票），可用于公司外派搬家报销、个人报税等用途。"),
    ],
    "content": """
  <article class="article">
    <div class="container">
      <h1>两岸搬家费用完全对比（2026最新版）</h1>
      <p>收到最多的问题就是："大陆搬台湾多少钱？""比我找台湾搬家公司便宜吗？" 这篇把<strong>两个方向的搬家费用一次摊开</strong>，每种方式的价格、时效、隐藏费用都列清楚。</p>

      <h2>一、大陆→台湾搬家费用</h2>
      <div class="compare-table">
        <table>
          <tr><th>房屋大小</th><th>物品量(立方)</th><th>拼柜费用</th><th>整柜费用</th><th>时效</th></tr>
          <tr><td>单人/学生</td><td>1-3</td><td>3000-7000</td><td>不推荐</td><td>15-25天</td></tr>
          <tr><td>一居室</td><td>4-8</td><td>6000-15000</td><td>15000-22000</td><td>15-25天</td></tr>
          <tr><td>两居室</td><td>8-15</td><td>10000-20000</td><td>20000-30000</td><td>18-25天</td></tr>
          <tr><td>三居室+</td><td>15-25</td><td>不推荐</td><td>25000-40000</td><td>18-25天</td></tr>
        </table>
      </div>
      <p>💰 <strong>拼柜 vs 整柜怎么选？</strong> 拼柜=和别人共用一个货柜，便宜但等凑齐才发船（多3-5天）。整柜=独占一个货柜，贵30-50%但到港就走。</p>

      <h2>二、台湾→大陆搬家费用</h2>
      <div class="compare-table">
        <table>
          <tr><th>物品量</th><th>快递专线</th><th>海运拼箱</th><th>时效</th></tr>
          <tr><td><50kg</td><td>1250-1750元</td><td>不推荐</td><td>5-7天</td></tr>
          <tr><td>50-200kg</td><td>1500-7000元</td><td>4000-8000元</td><td>5-18天</td></tr>
          <tr><td>200-1000kg</td><td>不推荐</td><td>8000-15000元</td><td>12-18天</td></tr>
          <tr><td>1000kg+</td><td>不推荐</td><td>12000-25000元</td><td>15-20天</td></tr>
        </table>
      </div>

      <h2>三、费用构成拆解</h2>
      <p>无论哪个方向，搬家费用都由以下部分构成：</p>
      <ol>
        <li><strong>打包费</strong>（10-20%）：材料费+人工费，视物品复杂度而定</li>
        <li><strong>报关费</strong>（10-15%）：大陆出口报关约800-1500元，台湾进口清关约2000-4000元</li>
        <li><strong>运费</strong>（50-60%）：这是大头，按体积或重量计费</li>
        <li><strong>保险费</strong>（1-3%）：建议购买，货值1-3%</li>
        <li><strong>送货费</strong>（10-15%）：台湾/大陆端配送到家，含搬上楼（如有电梯免费，无电梯加收楼层费）</li>
      </ol>

      <h2>四、最容易忽略的4个额外费用</h2>
      <ul>
        <li>⚠️ <strong>偏远地区附加费</strong>：山区/离岛送货加收300-1000元</li>
        <li>⚠️ <strong>无电梯上楼费</strong>：每层加收30-80元/件</li>
        <li>⚠️ <strong>存储费</strong>：如果需要临时存仓，约5-15元/立方/天</li>
        <li>⚠️ <strong>熏蒸费</strong>：实木家具必须，500-800元/批</li>
      </ul>
      <p>我们报价时就一次性列出所有费用，无隐藏收费。</p>
    </div>
  </article>
"""
})

# ── 7. 拼柜整柜台湾专线 ──
PAGES.append({
    "file": "bulk-cargo-taiwan.html",
    "title": "海运拼柜整柜台湾专线 | 散货拼箱/整柜出口台湾",
    "desc": "大陆海运到台湾拼柜整柜专线：散货拼箱LCL、整柜FCL出口台湾。厦门/福州/深圳→基隆/台中/高雄，每周发船。含报关清关、码头操作、送货上门。免费获取海运报价。",
    "canonical": f"{DOMAIN}/bulk-cargo-taiwan",
    "breadcrumb": [("首页", DOMAIN), ("拼柜整柜台湾", None)],
    "article_headline": "海运拼柜整柜台湾专线：散货拼箱/整柜全攻略",
    "faqs": [
        ("拼柜和整柜有什么区别？", "拼柜(LCL)=和别人共用一个货柜，按体积收费（约2000-5000元/立方），适合1-15立方的货物。整柜(FCL)=独占一个货柜，20尺柜约8000-15000元，40尺柜约12000-22000元，适合15立方以上货物。拼柜需要等凑满才发船，多3-5天。"),
        ("海运到台湾走哪个港口？", "大陆主要发货港：厦门（最近的）、福州、深圳、宁波、上海。台湾主要收货港：基隆（北部）、台中（中部）、高雄（南部）。我们最常用厦门→基隆，每周2班，海上航程1天。"),
        ("海运拼柜怎么计费？", "按'体积立方(CBM)'或'重量吨'取大者计费。1立方约2000-5000元（含报关和码头费）。起运量通常为1立方。轻货（如家具）按体积计，重货（如设备）按重量计。"),
        ("台湾清关需要什么文件？", "需要：1) 提单(B/L) 2) 商业发票 3) 装箱单 4) 委托报关书。特殊货物需额外文件：实木需熏蒸证、食品需卫生证、设备需说明书。我们全程代办，你不需要自己跑。"),
    ],
    "content": """
  <article class="article">
    <div class="container">
      <h1>海运拼柜/整柜台湾专线全攻略</h1>
      <p>大陆到台湾的海运是最经济的大货运输方式。两岸直线距离仅约180公里（厦门到金门），海运航程只要十几个小时。<strong>但真正耗时的是两端报关和码头排队</strong>。</p>

      <h2>一、拼柜 LCL vs 整柜 FCL</h2>
      <div class="compare-table">
        <table>
          <tr><th></th><th>拼柜 LCL</th><th>整柜 FCL</th></tr>
          <tr><td>计费</td><td>按体积/重量，2000-5000元/立方</td><td>按柜型一口价</td></tr>
          <tr><td>适合</td><td>1-15立方</td><td>15立方+</td></tr>
          <tr><td>时效</td><td>需等拼满，多3-5天</td><td>即装即发</td></tr>
          <tr><td>柜型</td><td>无</td><td>20尺/40尺/高柜</td></tr>
          <tr><td>费用(20尺柜)</td><td>-</td><td>8000-15000元</td></tr>
          <tr><td>费用(40尺柜)</td><td>-</td><td>12000-22000元</td></tr>
        </table>
      </div>

      <h2>二、柜型选择</h2>
      <ul>
        <li><strong>20尺柜(20GP)</strong>：5.9×2.35×2.39m，约33立方，最大载重28吨。适合小家庭搬家、小型设备</li>
        <li><strong>40尺柜(40GP)</strong>：12.03×2.35×2.39m，约67立方，最大载重26吨。适合全套家具、中型设备</li>
        <li><strong>40尺高柜(40HQ)</strong>：12.03×2.35×2.69m，约76立方，最大载重26吨。适合大型设备、大量货物</li>
      </ul>

      <h2>三、航线与时效</h2>
      <p><strong>厦门→基隆</strong>：每日有船，航程约12-18小时。加上两端报关和码头排队，全程约7-10天。<br>
      <strong>厦门→台中</strong>：每周3-4班，航程约16-20小时。全程约8-12天。<br>
      <strong>深圳→高雄</strong>：每周2-3班，航程约24小时。全程约10-14天。</p>

      <h2>四、海运全流程</h2>
      <ol class="process-list">
        <li>货物入仓/上门提货 → 入库测量体积重量</li>
        <li>订舱 → 确定船期和装货港</li>
        <li>报关出口 → 大陆海关申报（1-2天）</li>
        <li>装船出运 → 港口装船（1天）</li>
        <li>海运航行 → 12-24小时到港</li>
        <li>台湾进口清关 → 台湾海关申报（3-5天）</li>
        <li>码头提货 → 送货到门</li>
      </ol>

      <h2>五、哪些货物适合走海运？</h2>
      <ul>
        <li>✅ 搬家物品（1立方以上）</li>
        <li>✅ 家具（实木、沙发、床、柜子）</li>
        <li>✅ 机械设备（CNC、注塑机、印刷机等）</li>
        <li>✅ 建材（瓷砖、卫浴、门窗、石材）</li>
        <li>✅ 大宗商品（批量货物、商业库存）</li>
        <li>❌ 急用物品（选空运）</li>
        <li>❌ 单件<50kg（选快递专线更划算）</li>
      </ul>
    </div>
  </article>
"""
})

# ── 8. 建材出口台湾 ──
PAGES.append({
    "file": "building-materials-taiwan.html",
    "title": "建材出口台湾 | 瓷砖/卫浴/门窗/石材海运台湾",
    "desc": "大陆建材出口台湾专线：瓷砖、卫浴、门窗、石材、地板、管材海运台湾。专业建材包装防碎、拼柜整柜、报关清关一站式。比台湾本地采购省30-50%，免费获取建材出口报价。",
    "canonical": f"{DOMAIN}/building-materials-taiwan",
    "breadcrumb": [("首页", DOMAIN), ("建材出口台湾", None)],
    "article_headline": "大陆建材出口台湾：瓷砖/卫浴/门窗海运全攻略",
    "faqs": [
        ("大陆建材海运到台湾划算吗？", "非常划算！大陆建材（瓷砖、卫浴、门窗、石材等）价格通常比台湾便宜30-50%。以一个100平米的房子全屋建材为例，大陆采购+运费总成本约节省5-15万元。而且品种选择多得多。"),
        ("瓷砖海运容易碎吗？", "瓷砖运输破损是最大风险但我们有成熟方案：1) 原厂包装不拆 2) 立放竖放（不是平放堆叠）3) 每箱间加泡沫隔层 4) 打缠绕膜+护角 5) 木托盘整托发货。破损率控制在0.5%以内。"),
        ("建材出口台湾需要什么认证？", "大部分建材不需要特别认证。但：卫浴洁具需台湾标准检验局(BSMI)认证（可到港后补做）、电线电缆需BSMI认证、含石棉产品禁止进口。建议发货前确认品类是否在管制清单内。"),
        ("卫浴洁具（马桶、面盆）怎么运输？", "马桶、面盆等陶瓷洁具是最易碎的建材。包装标准：原厂泡沫固定+双层纸箱+木架固定。单个马桶约0.15-0.25立方，运费约400-700元。一套三件套（马桶+面盆+浴缸）约1200-2500元运费。"),
    ],
    "content": """
  <article class="article">
    <div class="container">
      <h1>大陆建材出口台湾：瓷砖/卫浴/门窗/石材怎么运？</h1>
      <p>大陆是全球建材生产中心，佛山瓷砖、南安卫浴、佛山门窗、水头石材……品质好、价格低。<strong>越来越多的台湾业主和装修公司选择从大陆采购建材海运回台</strong>。但建材品类多、易碎品多，对物流要求很高。</p>

      <h2>一、常见的建材出口品类</h2>
      <div class="compare-table">
        <table>
          <tr><th>品类</th><th>产地</th><th>运输难度</th><th>运费参考</th></tr>
          <tr><td>瓷砖/地砖</td><td>佛山</td><td>⭐⭐⭐ 易碎</td><td>2000-3500元/立方</td></tr>
          <tr><td>卫浴洁具</td><td>南安/潮州</td><td>⭐⭐⭐ 易碎</td><td>2500-4000元/立方</td></tr>
          <tr><td>门窗/铝合金</td><td>佛山/南海</td><td>⭐⭐ 体积大</td><td>2000-3500元/立方</td></tr>
          <tr><td>石材/大理石</td><td>水头/云浮</td><td>⭐⭐⭐ 极重</td><td>3000-5000元/吨</td></tr>
          <tr><td>木地板</td><td>湖州/常州</td><td>⭐ 好运</td><td>2000-3000元/立方</td></tr>
          <tr><td>管材/线材</td><td>天津/河北</td><td>⭐⭐ 超长件</td><td>2500-4000元/吨</td></tr>
        </table>
      </div>

      <h2>二、建材运输的核心：包装</h2>
      <p>建材运输破损率直接取决于包装。我们的标准：</p>
      <ul>
        <li><strong>瓷砖</strong>：竖放（像书架放书那样）、每箱间加3mm泡沫隔板、整托打缠绕膜、木托盘</li>
        <li><strong>马桶</strong>：原厂泡沫底座+整机气泡膜+双层纸箱+四角泡沫护角+木架</li>
        <li><strong>玻璃门窗</strong>：每扇单独包气泡膜+纸板护角+定制木箱，箱内填充泡沫颗粒</li>
        <li><strong>石材台面</strong>：双层气泡膜+珍珠棉+定制木箱，底部加木托盘便于叉车</li>
        <li><strong>长件管材</strong>：捆扎成束+缠绕膜+两端护套，必要时用框架箱</li>
      </ul>

      <h2>三、采购建议</h2>
      <ol>
        <li><strong>同一品类集中采购</strong>：比如全部瓷砖从佛山一家工厂发货，集中装箱省运费</li>
        <li><strong>预留5%损耗</strong>：瓷砖等易碎品，建议多买5%备用</li>
        <li><strong>提前确认台湾准入</strong>：部分建材需BSMI认证，提前问清楚</li>
        <li><strong>算好总体积</strong>：建材体积大，建议先让工厂提供详细装箱单，我们免费算出总运费</li>
      </ol>

      <h2>四、费用案例</h2>
      <p><strong>案例1：100平米全屋瓷砖</strong><br>
      品类：客厅地砖+厨卫墙砖+阳台砖<br>
      总体积：约6-8立方<br>
      采购价：约8000-15000元（同样瓷砖台湾卖25000-40000元）<br>
      海运费用：约12000-20000元（拼柜）<br>
      <strong>总花费约20000-35000元，比台湾买省30-50%</strong></p>

      <p><strong>案例2：三套卫浴洁具</strong><br>
      品类：马桶+面盆+浴缸×3套<br>
      总体积：约2-3立方<br>
      采购价：约6000-12000元<br>
      海运费用：约5000-9000元<br>
      <strong>总花费约11000-21000元，比台湾买省40%</strong></p>
    </div>
  </article>
"""
})

# ── 9. 商业大货专线 ──
PAGES.append({
    "file": "commercial-cargo.html",
    "title": "商业大货出口台湾 | 批量货物/商业物流/整柜专线",
    "desc": "大陆商业大货出口台湾专线：批量商品、工业原材料、机械设备、整柜物流。支持FOB/CIF/DDP多种贸易条款，含报关清关、仓储配送。大宗货物月结优惠，免费物流方案设计。",
    "canonical": f"{DOMAIN}/commercial-cargo",
    "breadcrumb": [("首页", DOMAIN), ("商业大货台湾", None)],
    "article_headline": "大陆商业大货出口台湾：B2B物流一站式解决方案",
    "faqs": [
        ("商业大货出口台湾需要什么资质？", "出口方需要：1) 营业执照（经营范围含进出口）2) 海关备案登记 3) 电子口岸卡。如果没有进出口权，我们可以代理出口（双抬头报关），你只需要提供货物和装箱单。"),
        ("整柜运费包含哪些？", "整柜运费通常包含：海运费(Ocean Freight)、码头操作费(THC)、文件费(DOC)、封条费、报关费。不包含：台湾进口关税、台湾端送货费（可代付到付）、可能的查验费。建议签合同时问清楚是ALL IN还是分开计。"),
        ("FOB和CIF怎么选？", "FOB(离岸价)=我们负责大陆端报关+运到码头装船，台湾买家自己找船公司和清关。CIF(到岸价)=我们负责全程（大陆报关+海运+保险），台湾清关由买家负责。DDP(完税后交货)=我们负责全程含台湾清关税，直接送货到买家门口——最省心但费用最高。"),
        ("每月有稳定货量怎么谈价格？", "月发货量超过3个柜即可享受月结优惠价，20尺柜优惠800-1500元/柜。长期合作的签年度框架协议，锁定运价。还可以签保舱协议，旺季确保有柜。"),
    ],
    "content": """
  <article class="article">
    <div class="container">
      <h1>商业大货出口台湾：企业级两岸物流解决方案</h1>
      <p>如果你的公司有稳定的台湾出货需求——不管是每月几托盘的工业零件，还是每周发整柜的批量商品——<strong>一套专业的B2B物流方案可以帮你每年省下数万元运费</strong>。</p>

      <h2>一、三种贸易条款，适合不同场景</h2>
      <div class="compare-table">
        <table>
          <tr><th>条款</th><th>我们负责</th><th>台湾买家负责</th><th>适合</th></tr>
          <tr><td><strong>FOB</strong></td><td>大陆报关+运到码头</td><td>海运+清关+送货</td><td>买家有自己的货代</td></tr>
          <tr><td><strong>CIF</strong></td><td>大陆报关+海运+保险</td><td>清关+送货</td><td>最常用的方案</td></tr>
          <tr><td><strong>DDP</strong></td><td>全程含台湾清关含税</td><td>收货即可</td><td>买家不想任何操作</td></tr>
        </table>
      </div>

      <h2>二、商业大货的优势</h2>
      <ul>
        <li>🏭 <strong>整柜优惠</strong>：月出货≥3柜享月结价，比零售价低10-20%</li>
        <li>📋 <strong>代理出口</strong>：无进出口权？我们代理出口，双抬头报关</li>
        <li>🏪 <strong>仓储管理</strong>：广东/福建有合作仓，支持集货、分拣、贴标</li>
        <li>📊 <strong>专属客服</strong>：一对一对接，实时跟踪每票货的位置</li>
        <li>🔐 <strong>保舱协议</strong>：旺季（春节前/618/双11）确保有柜，不影响出货</li>
        <li>💳 <strong>灵活结算</strong>：月结/票结/预付款，按需选择</li>
      </ul>

      <h2>三、常出品类</h2>
      <ul>
        <li><strong>工业原材料</strong>：塑料颗粒、钢材、化工原料（非危险品）</li>
        <li><strong>机械配件</strong>：轴承、齿轮、液压件、气动元件</li>
        <li><strong>成品商品</strong>：家具、灯具、五金、电子产品</li>
        <li><strong>包装材料</strong>：纸箱、气泡膜、胶带等</li>
        <li><strong>电商库存</strong>：Shopee/露天/PChome等台湾电商平台的备货</li>
      </ul>

      <h2>四、合作流程</h2>
      <ol class="process-list">
        <li><strong>需求沟通</strong>：告知货物品类、出货频率、预估体积</li>
        <li><strong>报价方案</strong>：我们出专属运价表和物流方案（含FOB/CIF/DDP三种）</li>
        <li><strong>签订合同</strong>：框架协议或单票合同</li>
        <li><strong>常规发货</strong>：每次出货只需提供装箱单+发票，我们处理剩余一切</li>
        <li><strong>对账结算</strong>：月结客户每月5号前出上月账单</li>
      </ol>

      <h2>五、费用参考</h2>
      <p>以下为月出货量≥3柜的月结价参考（散客价格上浮15-25%）：</p>
      <ul>
        <li>20尺柜厦门→基隆：约6000-12000元（含THC+DOC+报关）</li>
        <li>40尺柜厦门→基隆：约10000-18000元</li>
        <li>拼柜散货：约1800-3500元/立方</li>
        <li>台湾进口清关服务：2000-3500元/票</li>
        <li>台湾送货：按距离计，约1500-4000元</li>
      </ul>
    </div>
  </article>
"""
})

# ═══════════════════════════════════════════════════════════════
# 生成所有页面
# ═══════════════════════════════════════════════════════════════

def generate_page(page_data):
    """生成单个页面HTML"""
    # 组装 Schemas
    schemas = article_schema(page_data["article_headline"], page_data["desc"])
    schemas += breadcrumb_schema(page_data["breadcrumb"])
    schemas += faq_schema(page_data["faqs"])
    
    # 生成 FAQ HTML
    faq_html = '<h2>常见问题</h2>\n<div class="faq-list">'
    for q, a in page_data["faqs"]:
        faq_html += f'\n    <div class="faq-item"><h3>{q}</h3><p>{a}</p></div>'
    faq_html += '\n</div>'
    
    # 组装完整页面
    html = page_head(page_data["title"], page_data["desc"], page_data["canonical"], schemas)
    html += HEADER
    html += page_data["content"]
    html += faq_html
    html += '</div>\n</article>\n'
    html += CTA_SECTION
    html += FOOTER
    
    return html

if __name__ == "__main__":
    for page in PAGES:
        filepath = os.path.join(BASE_DIR, page["file"])
        # 确定目录
        os.makedirs(os.path.dirname(filepath) or BASE_DIR, exist_ok=True)
        
        content = generate_page(page)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ {page['file']} ({len(page['faqs'])} FAQs)")
    
    print(f"\n📊 生成了 {len(PAGES)} 个页面")
    print(f"📊 共 {sum(len(p['faqs']) for p in PAGES)} 条FAQ")
