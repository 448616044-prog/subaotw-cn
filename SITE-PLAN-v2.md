# subaotw.cn 建站计划 v2.0 — 大件设备+敏感货双线

> 更新时间：2026-05-31
> 备案状态：预计本周通过

---

## 一、品牌定位

| 维度 | subao.tw | **subaotw.cn** |
|------|----------|---------------|
| 品牌名 | 速豹集運 | 速豹集运 |
| 副标题 | 台灣寄大陸敏感貨專線 | 大件设备两岸专线 |
| 核心业务 | 台湾→大陆 敏感货 | 两岸 大件设备 + 台湾→大陆 敏感货 |
| 主客户 | 台湾个人/小商家 | 大陆工厂 + 在大陆的台湾人 |
| 最小单重 | 1kg | 50kg（设备）/ 1kg（敏感货） |
| SEO引擎 | Google | **百度** |
| 搜索语言 | 繁体中文 | **简体中文** |

### 长期三线架构
```
Phase 1（现在）：大件设备（主攻）+ 台湾→大陆敏感货（补盲区）
Phase 2（渠道恢复后）：大陆→台湾敏感货
Phase 3（成熟期）：三线并进，双品牌矩阵
```

---

## 二、目录结构

```
sites/subaotw-cn/
├── index.html                    # 首页：大件设备+敏感货入口
├── equipment/                    # 【第一层】大件设备品类页
│   ├── index.html                # 设备运输总览
│   ├── cnc-export-taiwan.html    # CNC机床出口台湾
│   ├── injection-molding.html    # 注塑机运输
│   ├── press-machine.html        # 冲床/折弯机
│   ├── packaging-equipment.html  # 包装机械
│   ├── textile-machinery.html    # 纺织设备
│   ├── printing-equipment.html   # 印刷机械
│   ├── medical-instruments.html  # 医疗仪器
│   ├── lab-equipment.html        # 实验室设备
│   ├── electrical-equipment.html # 电力设备
│   ├── construction-machinery.html # 工程机械
│   ├── food-processing.html      # 食品加工设备
│   ├── plastic-machinery.html    # 塑料机械
│   ├── woodworking.html          # 木工机械
│   ├── metal-processing.html     # 金属加工设备
│   ├── mining-equipment.html     # 矿山设备
│   ├── generator.html            # 发电机/变压器
│   ├── pump-valve.html           # 泵阀设备
│   ├── mold-tooling.html         # 模具/工装
│   └── industrial-robot.html     # 工业机器人
├── tw-to-cn/                     # 【第二层】台湾→大陆 敏感货
│   ├── index.html                # 台湾寄大陆总览
│   ├── food-shipping.html        # 台湾食品寄大陆
│   ├── tea-shipping.html         # 台湾茶叶寄大陆
│   ├── health-products.html      # 台湾保健品寄大陆
│   ├── cosmetics-shipping.html   # 台湾化妆品寄大陆
│   ├── medicine-shipping.html    # 台湾药品寄大陆
│   ├── mooncake-shipping.html    # 台湾月饼寄大陆
│   ├── clothing-shipping.html    # 台湾服饰寄大陆
│   ├── books-shipping.html       # 台湾书籍寄大陆
│   └── baby-products.html        # 台湾母婴用品寄大陆
├── guide/                        # 【第三层】知识权威页
│   ├── equipment-export-process.html  # 大件设备出口全流程
│   ├── customs-documents.html    # 设备出口报关文件清单
│   ├── taiwan-import-tax.html    # 台湾进口关税计算
│   ├── packaging-standard.html   # 设备木箱包装标准
│   ├── oversize-permit.html      # 超限货物运输许可
│   ├── ecfa-tariff.html          # ECFA框架设备关税优惠
│   ├── shipping-methods.html     # 海运vs空运vs陆运对比
│   ├── insurance-guide.html      # 设备运输保险指南
│   ├── weight-calculation.html   # 体积重vs实重计算
│   └── tw-cn-logistics-terms.html # 两岸物流术语表
├── cases/                        # 【信任层】案例
│   ├── index.html                # 案例总览
│   ├── case-cnc-dongguan.html    # CNC设备→东莞工厂
│   ├── case-injection-shenzhen.html # 注塑机→深圳
│   ├── case-medical-shanghai.html # 医疗仪器→上海
│   └── case-textile-fujian.html  # 纺织设备→福建
├── pricing.html                  # 大件设备运费估算
├── faq.html                      # 常见问题
├── about.html                    # 关于我们
├── contact.html                  # 联系我们
├── article-list.html             # 全部文章
├── sitemap.xml
├── robots.txt
└── _redirects
```

**页面总数：60 页**

---

## 三、SEO 关键词矩阵

### 百度主关键词（按搜索意图分层）

| 层级 | 关键词类型 | 示例 | 页面数 | 竞争度 |
|------|-----------|------|--------|--------|
| 品类页 | 设备名+台湾/出口 | "CNC机床出口台湾" | 20 | 🟢 低 |
| 知识页 | 流程/文件/关税 | "设备出口报关文件" | 10 | 🟢 低 |
| 敏感货页 | 品名+寄大陆 | "台湾食品寄大陆" | 10 | 🟡 中 |
| 品牌页 | 速豹集运 | "速豹集运" | 5 | 🟢 低 |

### 全渠道内容矩阵

| 渠道 | 内容类型 | 频率 | 目标 |
|------|----------|------|------|
| **百度SEO** | 品类页+知识页 | 每周3篇 | 占领长尾搜索 |
| **小红书** | 设备运输案例图文 | 每周2篇 | 工厂客户种草 |
| **抖音** | 装柜/运输实拍 | 每周1条 | 品牌曝光 |
| **知乎** | 行业专业解答 | 每周1篇 | 信任建设 |
| **AI搜索** | 全站FAQ Schema | 标配 | 防守位 |

---

## 四、技术SEO

### Schema 结构化数据
- 品类页：Product + FAQPage
- 知识页：Article + FAQPage + HowTo
- 案例页：Article + Review
- 首页：Organization + WebSite + ItemList

### 百度专属
- 主动推送 API（参考 VideoTV 的推送脚本）
- 熊掌号/百家号（可选）
- 移动适配（百度移动优先）

### Core Web Vitals
- 全部静态 HTML，无框架，天然快
- 图片 WebP 格式，压缩 <100KB
- LCP < 2.5s / FID < 100ms / CLS < 0.1

---

## 五、执行路线图

| 阶段 | 时间 | 任务 | 产出 |
|------|------|------|------|
| **即刻** | 备案通过前 | 首页+设备品类页前5篇 | 5 页内容 |
| **第1周** | 备案通过 | 20个设备页+10个知识页 | 30 页上线 |
| **第2周** | 上线后 | 10个敏感货页+5个案例页 | 45 页 |
| **第3周** | 内容期 | 剩余15页+百度推送+小红书 | 60 页全量 |
| **第4周** | 优化期 | GSC/百度站长分析+调优 | 持续迭代 |

---

## 六、发布前检查清单

- [ ] 所有页面标题含「台湾」或「两岸」
- [ ] Schema 正确，百度 Rich Result 可用
- [ ] robots.txt 允许百度蜘蛛
- [ ] sitemap.xml 完整
- [ ] 移动端响应式正常
- [ ] 内链网络完整（设备页↔知识页↔案例页）
- [ ] 所有外链指向 subaotw.cn（非 subao.tw）
- [ ] 百度主动推送脚本就绪
