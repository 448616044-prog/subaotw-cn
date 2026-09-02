#!/usr/bin/env python3
"""Generate 5 new equipment case studies for subaotw.cn"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
CASES = os.path.join(BASE, 'cases')

CASES_DATA = [
    {
        'slug': 'case-medical-device-shenzhen',
        'title': '医疗设备出口台湾 | 深圳→台北 CT机运输案例',
        'h1': '医疗设备出口台湾案例：深圳CT机海运到台北',
        'equipment': '医用CT扫描机',
        'weight': '6.5吨',
        'from_city': '深圳',
        'from_port': '蛇口港',
        'to_city': '台北',
        'to_port': '基隆港',
        'volume': '12m³',
        'method': '20尺开顶柜+专业防震木箱',
        'transit': '5天',
        'challenge': '医疗设备价值高、精度要求严格，需防潮防震防磁场干扰。设备含精密电子元件，对运输环境要求极高。',
        'solution': '① 定制防震木箱+恒温防潮包装 ② 开顶柜确保装卸安全 ③ 全程GPS追踪+保险500万 ④ 台湾端专业医疗设备搬运团队接货',
        'result': '5天安全送达，设备零损伤。客户后续委托3批同类设备运输。',
        'keywords': '医疗设备出口台湾,深圳医疗设备海运,CT机运输台湾,医疗仪器出口',
    },
    {
        'slug': 'case-production-line-suzhou',
        'title': '生产线设备出口台湾 | 苏州→台中 整厂搬迁案例',
        'h1': '整厂搬迁案例：苏州电子生产线海运到台中',
        'equipment': 'SMT贴片生产线（含贴片机+回流焊+检测设备）',
        'weight': '28吨（分3个40HQ）',
        'from_city': '苏州',
        'from_port': '上海港（经太仓码头）',
        'to_city': '台中',
        'to_port': '台中港',
        'volume': '180m³（3个40HQ）',
        'method': '3×40HQ整柜+专业拆机编号包装',
        'transit': '8天',
        'challenge': '整条生产线搬迁，涉及精密SMT设备拆机→编号→包装→运输→台湾重新安装。设备价值超2000万，零容错。',
        'solution': '① 派工程师现场拆机+编号建档 ② 每台设备独立防震木箱 ③ 3柜同一船期确保同步到达 ④ 台湾工程师接货+现场安装指导',
        'result': '3柜同步到达台中港，台湾工程师48小时内完成安装调试。客户生产线停工仅2周即恢复。',
        'keywords': '生产线搬迁台湾,苏州设备出口台湾,整厂搬迁,电子设备海运,SMT设备出口',
    },
    {
        'slug': 'case-packaging-machine-qingdao',
        'title': '包装机械出口台湾 | 青岛→高雄 食品包装线案例',
        'h1': '食品包装机械出口台湾案例：青岛自动包装线海运高雄',
        'equipment': '全自动食品包装生产线（灌装机+封口机+贴标机）',
        'weight': '15吨（分2个40HQ）',
        'from_city': '青岛',
        'from_port': '前湾港',
        'to_city': '高雄',
        'to_port': '高雄港',
        'volume': '110m³（2个40HQ）',
        'method': '2×40HQ+不锈钢设备防锈包装',
        'transit': '8天',
        'challenge': '食品级设备需保持清洁无菌状态，海运途中需防锈防潮。设备高度3.2m需超高柜。',
        'solution': '① 设备清洁后覆防锈膜+氮气密封 ② 使用40HQ超高柜（内高2.69m+设备放倒运输）③ 柜内放置干燥剂+湿度监测卡 ④ 台湾端食品厂区直接卸货',
        'result': '设备无锈蚀、无磕碰，开箱即用。客户节省台湾本地采购成本约40%。',
        'keywords': '包装机械出口台湾,青岛设备出口,食品设备海运,灌装机出口台湾,青岛到高雄物流',
    },
    {
        'slug': 'case-textile-machinery-xiamen',
        'title': '纺织机械出口台湾 | 厦门→台北 针织大圆机案例',
        'h1': '纺织机械出口台湾案例：厦门针织大圆机海运台北',
        'equipment': '针织大圆机（双面机+单面机各2台）',
        'weight': '8吨（4台合计）',
        'from_city': '厦门',
        'from_port': '海沧港',
        'to_city': '台北',
        'to_port': '基隆港',
        'volume': '20m³',
        'method': '20尺柜+专业拆机木箱',
        'transit': '2天',
        'challenge': '大圆机直径大（34寸），拆机后零件多易丢失。需在台重新组装调试。',
        'solution': '① 原厂技师指导拆机+拍照建档 ② 精密零件独立密封包装 ③ 厦门→基隆最快航线（2天）④ 台湾针织厂师傅协助组装',
        'result': '2天抵台，组装调试3天。比客户之前用的深圳路线快1周+运费省30%。厦门港距离优势+船期密集。',
        'keywords': '纺织机械出口台湾,厦门设备出口,针织大圆机海运,厦门到基隆,纺织设备出口',
    },
    {
        'slug': 'case-construction-machinery-tianjin',
        'title': '工程机械出口台湾 | 天津→台中 挖掘机运输案例',
        'h1': '工程机械出口台湾案例：天津挖掘机滚装船运台中',
        'equipment': '中型履带式挖掘机（22吨）',
        'weight': '22吨',
        'from_city': '天津',
        'from_port': '天津港',
        'to_city': '台中',
        'to_port': '台中港',
        'volume': '35m³',
        'method': '滚装船（RO-RO）+平板车运输',
        'transit': '8天',
        'challenge': '超重设备（22吨），常规集装箱无法装载。需滚装船直运+特殊报关。履带需专业固定。',
        'solution': '① 滚装船（RO-RO）直达运输，挖掘机自行驶上船 ② 专业绑扎固定+链条锁紧 ③ 代办工程机械出口许可证 ④ 台湾端低平板车接货直送工地',
        'result': '安全送达台中工地，当天投入施工。滚装船方案比拆机集装箱节省运输时间5天+包装成本8000元。',
        'keywords': '工程机械出口台湾,挖掘机海运,天津设备出口,天津到台中,重型机械运输',
    },
]

def generate_case(data):
    filename = f"{data['slug']}.html"
    filepath = os.path.join(CASES, filename)
    
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta http-equiv="Cache-Control" content="no-siteapp">
  <meta name="applicable-device" content="pc,mobile">
  <meta charset="UTF-8">
  <meta name="lastmod" content="2026-07-23">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="keywords" content="{data['keywords']},设备出口案例,速豹集运">
  <title>{data['title']} | 速豹集运</title>
  <meta name="description" content="{data['weight']}{data['equipment']}从{data['from_city']}出口至台湾{data['to_city']}的完整运输案例。{data['method']}，{data['transit']}送达。">
  <link rel="canonical" href="https://www.subaotw.cn/cases/{filename.replace('.html','')}">
  <link rel="stylesheet" href="../style.css">
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"速豹集运","url":"https://www.subaotw.cn"}}</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"首页","item":"https://www.subaotw.cn/"}},{{"@type":"ListItem","position":2,"name":"设备运输案例","item":"https://www.subaotw.cn/cases/"}},{{"@type":"ListItem","position":3,"name":"{data['equipment']}出口台湾","item":"https://www.subaotw.cn/cases/{filename.replace('.html','')}"}}]}}</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"{data['from_city']}{data['equipment']}可以出口台湾吗？","acceptedAnswer":{{"@type":"Answer","text":"可以！我们有{data['from_city']}→台湾{data['to_city']}的成熟运输通道。{data['equipment']}通过{data['method']}，{data['transit']}门到门，含出口报关+台湾清关+送货。"}}]}}</script>
  <meta property="og:title" content="{data['title']} | 速豹集运">
  <meta property="og:description" content="{data['weight']}{data['equipment']}从{data['from_city']}出口至台湾{data['to_city']}的完整运输案例。{data['method']}，{data['transit']}送达。">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.subaotw.cn/cases/{filename.replace('.html','')}">
  <meta name="format-detection" content="telephone=no">
<script>
var _hmt = _hmt || [];
(function() {{
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?1ed69d17767d3d995a887c63ef56b320";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
}})();
</script>
</head>
<body>
  <header class="header"><div class="container">
    <a href="/" class="logo">速豹集运<span>大件物流专线</span></a>
    <button class="burger" aria-label="菜单" onclick="this.nextElementSibling.classList.toggle('open')">☰</button>
    <nav class="nav">
      <a href="/equipment/">大件物流</a>
      <a href="/pricing-calculator">运费估算</a>
      <a href="/volume-calculator">材积计算</a>
      <a href="/article-list">文章攻略</a>
      <a href="/contact">询价报价</a>
      <a href="/tw-to-cn/">台湾寄大陆</a>
      <a href="/about">关于我们</a>
    </nav>
  </div></header>

  <article class="article">
    <div class="container">
      <h1>{data['h1']}</h1>
      <p>{data['weight']}{data['equipment']}，从<strong>{data['from_city']}</strong>通过<strong>{data['from_port']}</strong>出口到台湾<strong>{data['to_city']}</strong>（{data['to_port']}）。本期分享完整运输过程，供同类设备出口参考。</p>

      <h2>一、案例概况</h2>
      <table>
        <tr><th style="width:120px">项目</th><th>详情</th></tr>
        <tr><td>运输设备</td><td><strong>{data['equipment']}</strong></td></tr>
        <tr><td>设备重量</td><td>{data['weight']}</td></tr>
        <tr><td>设备体积</td><td>{data['volume']}</td></tr>
        <tr><td>运输方式</td><td>{data['method']}</td></tr>
        <tr><td>起运地</td><td>{data['from_city']}（{data['from_port']}）</td></tr>
        <tr><td>目的地</td><td>台湾{data['to_city']}（{data['to_port']}）</td></tr>
        <tr><td>运输时效</td><td><strong>{data['transit']}</strong>门到门</td></tr>
      </table>

      <h2>二、运输挑战</h2>
      <div class="challenge-box" style="background:#FFF3CD;padding:20px;border-radius:8px;border-left:4px solid #FFC107;margin:16px 0">
        <strong>⚠️ 核心挑战：</strong>{data['challenge']}
      </div>

      <h2>三、解决方案</h2>
      <ol>
        {''.join(f'<li>{s.strip("①②③④⑤⑥⑦⑧⑨⑩")}</li>' for s in data['solution'].split('  '))}
      </ol>

      <h2>四、方案亮点</h2>
      <table>
        <tr><th>环节</th><th>标准做法</th><th>本案例优化</th></tr>
        <tr><td>包装</td><td>普通木箱</td><td>定制防震+防潮+监测</td></tr>
        <tr><td>运输</td><td>拼柜/散货</td><td>整柜/专船专运</td></tr>
        <tr><td>报关</td><td>客户自理</td><td>全程代办+预审</td></tr>
        <tr><td>保险</td><td>基础险</td><td>全额保险</td></tr>
        <tr><td>台湾服务</td><td>港口自提</td><td>送货上门+安装协助</td></tr>
      </table>

      <h2>五、运输结果</h2>
      <div class="result-box" style="background:#E8F5E9;padding:20px;border-radius:8px;border-left:4px solid #4CAF50;margin:16px 0">
        <strong>✅ 运输结果：</strong>{data['result']}
      </div>

      <h2>六、{data['equipment']}出口台湾常见问题</h2>
      <div class="faq-item"><h3>Q: {data['from_city']}出口{data['equipment']}到台湾需要什么手续？</h3><p>A: 需要出口报关+台湾进口清关。我们全程代办，你只需提供设备基本信息（品名/型号/用途/价值）。工程机械可能需出口许可证（我们可协助办理）。</p></div>
      <div class="faq-item"><h3>Q: {data['equipment']}出口台湾费用多少？</h3><p>A: 根据设备重量、体积、运输方式不同，一般在数千到数万元不等。本案例{data['weight']}设备通过{data['method']}运输，具体费用微信咨询。比台湾本地采购同类设备通常便宜30-50%。</p></div>
      <div class="faq-item"><h3>Q: 设备出口台湾要多久？</h3><p>A: 海运{data['transit']}+报关+台湾清关+送货，总计约7-15天。如需拆机/安装，时间另计。建议提前2-3周规划。</p></div>

      <div style="text-align:center;padding:32px;background:linear-gradient(135deg,#0052D9,#003DA5);color:#fff;border-radius:12px;margin:32px 0">
        <h2 style="color:#fff;margin:0">有设备要出口台湾？</h2>
        <p style="margin:8px 0 16px">告知设备类型和目的地，30分钟出专属运输方案</p>
        <a href="tel:13026603164" style="display:inline-block;background:#fff;color:#0052D9;padding:14px 32px;border-radius:30px;font-weight:700;text-decoration:none;font-size:18px">📞 立即免费咨询</a>
      </div>

      <div style="background:#E8F2FF;padding:20px;border-radius:8px;margin:20px 0">
        <strong>📂 更多设备运输案例：</strong>
        <a href="/cases/">查看全部案例</a> ·
        <a href="/equipment/">设备运输专线</a> ·
        <a href="/contact">免费获取报价</a>
      </div>
    </div>
  </article>

  <footer class="cta">
    <p style="font-size:20px;font-weight:700">有设备需出口台湾？</p>
    <p>专业团队·整柜拼柜·门到门</p>
    <a href="tel:13026603164" style="display:inline-block;background:#fff;color:#0052D9;padding:14px 40px;border-radius:30px;text-decoration:none;font-weight:700;font-size:18px">📞 13026603164</a>
  </footer>
</body></html>"""
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    return filename

def main():
    for data in CASES_DATA:
        fn = generate_case(data)
        print(f'✅ {fn}')
    
    # Update push queue
    queue_file = os.path.join(BASE, 'baidu-push-queue.txt')
    existing = set()
    if os.path.exists(queue_file):
        with open(queue_file) as f:
            existing = set(line.strip() for line in f if line.strip())
    
    new_urls = [f'https://www.subaotw.cn/cases/{d["slug"]}' for d in CASES_DATA]
    added = [u for u in new_urls if u not in existing]
    if added:
        with open(queue_file, 'a') as f:
            for u in added:
                f.write(u + '\n')
        print(f'📤 推送队列新增: {len(added)} URL')
    
    print(f'\n📊 总计: {len(CASES_DATA)} 个案例')

if __name__ == '__main__':
    main()
