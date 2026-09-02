# subaotw.cn 上线清单

> 更新时间：2026-06-01
> 状态：备案已通过 ✅

---

## 一、页面完成度

| 页面 | URL | 状态 |
|------|-----|------|
| 首页 | / | ✅ 双线入口 |
| 设备总览 | /equipment/ | ✅ 19品类卡片（2026-06-01更新） |
| CNC机床 | /equipment/cnc-export-taiwan | ✅ |
| 注塑机 | /equipment/injection-molding | ✅ |
| 冲床/折弯机 | /equipment/press-machine | ✅ |
| 包装机械 | /equipment/packaging-equipment | ✅ |
| 医疗仪器 | /equipment/medical-instruments | ✅ |
| 工业机器人 | /equipment/industrial-robot | ✅ |
| 纺织设备 | /equipment/textile-machinery | ✅ 2026-06-01新增 |
| 印刷机械 | /equipment/printing-equipment | ✅ 2026-06-01新增 |
| 电力设备 | /equipment/electrical-equipment | ✅ 2026-06-01新增 |
| 工程机械 | /equipment/construction-machinery | ✅ 2026-06-01新增 |
| 食品加工 | /equipment/food-processing | ✅ 2026-06-01新增 |
| 塑料机械 | /equipment/plastic-machinery | ✅ 2026-06-01新增 |
| 木工机械 | /equipment/woodworking | ✅ 2026-06-01新增 |
| 金属加工 | /equipment/metal-processing | ✅ 2026-06-01新增 |
| 矿山设备 | /equipment/mining-equipment | ✅ 2026-06-01新增 |
| 发电机 | /equipment/generator | ✅ 2026-06-01新增 |
| 泵阀设备 | /equipment/pump-valve | ✅ 2026-06-01新增 |
| 模具工装 | /equipment/mold-tooling | ✅ 2026-06-01新增 |
| 实验室设备 | /equipment/lab-equipment | ✅ 2026-06-01新增 |
| 设备出口流程 | /guide/equipment-export-process | ✅ |
| 台湾食品寄大陆 | /tw-to-cn/food-shipping | ✅ |
| 关于我们 | /about | ✅ |
| 常见问题 | /faq | ✅ |
| 联系我们 | /contact | ✅ |
| 运费估算 | /pricing | ⚠️ 需更新为大件定价 |
| 台湾寄大陆总览 | /tw-to-cn | ⚠️ 需更新内容 |

**已完成：27/29 页** 🔺

---

## 二、技术配置

| 项目 | 状态 | 说明 |
|------|------|------|
| sitemap.xml | ✅ | 29个URL（2026-06-01更新） |
| robots.txt | ✅ | 允许百度蜘蛛 |
| 百度推送脚本 | ✅ | baidu-push-subaotw-cn.py（待获取百度token） |
| 部署脚本 | ✅ | deploy-subaotw-cn.sh |
| Schema结构化数据 | ✅ | equipment/index ItemList(19项) |

---

## 三、上线步骤

### 第1步：DNS 解析
```
在域名管理后台添加 A 记录：
  subaotw.cn  →  175.178.184.141
  www.subaotw.cn  →  175.178.184.141
```

### 第2步：部署到服务器
```bash
bash /Users/mac/WorkBuddy/Claw/物流項目/deploy-subaotw-cn.sh
```

### 第3步：验证上线
```bash
curl -H 'Host: subaotw.cn' http://175.178.184.141/
```

### 第4步：百度站长平台
1. 登录 zhanzhang.baidu.com
2. 添加站点 subaotw.cn
3. 验证所有权（HTML文件/HTML标签）
4. 获取推送 token，填入 baidu-push-subaotw-cn.py
5. 提交 sitemap

### 第5步：首次推送
```bash
python3 baidu-push-subaotw-cn.py
```

---

## 四、待补充内容（上线后第1周）

| 优先级 | 页面 | 说明 |
|--------|------|------|
| P0 | /equipment/ 剩余13个品类页 | ✅ 2026-06-01已全部完成 |
| P0 | /tw-to-cn/ 9个敏感货页 | ✅ 2026-06-02 全部完成 |
| P1 | /guide/ 9个知识页 | 报关文件/关税/包装标准/ECFA等 |
| P1 | /cases/ 6个案例页 | CNC→东莞/注塑机→深圳等 |
| P2 | 百度站长验证 | 🔴 需要登录 zhanzhang.baidu.com 添加站点 |
| P2 | 百度推送token获取 | 验证通过后在站长平台获取 |
