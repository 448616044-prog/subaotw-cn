#!/usr/bin/env python3
"""
全站联系触发点注入脚本
1. 右侧悬浮联系栏（电话+微信）→ 全部74页
2. 内容页内嵌CTA咨询条 → 设备/指南/搬家/货运页
3. Footer微信强化 → 全部74页
"""
import os, re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ═════════════════════════════════════════════════════════
# 1. 注入 style.css — 悬浮联系栏 + 内嵌CTA样式
# ═════════════════════════════════════════════════════════

FLOATING_CSS = """
/* 右侧悬浮联系栏 */
.float-contact{position:fixed;right:12px;bottom:120px;z-index:9999;display:flex;flex-direction:column;gap:10px}
.float-contact a{display:flex;align-items:center;justify-content:center;width:52px;height:52px;border-radius:50%;color:#fff;text-decoration:none;font-size:22px;box-shadow:0 4px 12px rgba(0,0,0,.2);transition:all .25s;position:relative}
.float-contact a:hover{transform:scale(1.1);box-shadow:0 6px 20px rgba(0,0,0,.3)}
.float-contact .fc-tel{background:linear-gradient(135deg,#2563eb,#1d4ed8)}
.float-contact .fc-wechat{background:linear-gradient(135deg,#07c160,#06ad56)}
.float-contact .fc-wechat .fc-tooltip{position:absolute;right:62px;bottom:0;background:#fff;color:#333;border-radius:10px;padding:10px;font-size:13px;white-space:nowrap;box-shadow:0 4px 16px rgba(0,0,0,.15);opacity:0;pointer-events:none;transition:opacity .2s;text-align:center;line-height:1.5}
.float-contact .fc-wechat:hover .fc-tooltip{opacity:1}
.float-contact .fc-wechat .fc-tooltip strong{display:block;font-size:15px;color:#1a56db;margin-bottom:4px}
.float-contact .fc-wechat .fc-tooltip .fc-copy{cursor:pointer;color:#07c160;font-weight:700;font-size:12px;margin-top:4px;display:inline-block;padding:2px 8px;border:1px solid #07c160;border-radius:4px}
.fc-text{position:absolute;right:62px;background:rgba(0,0,0,.85);color:#fff;padding:6px 14px;border-radius:6px;font-size:13px;white-space:nowrap;opacity:0;pointer-events:none;transition:opacity .2s}
.float-contact a:hover .fc-text{opacity:1}

/* 内嵌咨询CTA条 */
.inline-cta{margin:32px 0;background:linear-gradient(135deg,#eff6ff,#dbeafe);border:1px solid #bfdbfe;border-radius:12px;padding:24px;text-align:center}
.inline-cta h3{font-size:18px;color:#1a56db;margin:0 0 8px}
.inline-cta p{font-size:14px;color:#475569;margin:0 0 16px}
.inline-cta .cta-btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.inline-cta .cta-btn{display:inline-flex;align-items:center;gap:6px;padding:10px 24px;border-radius:8px;font-size:15px;font-weight:600;text-decoration:none;transition:all .2s}
.inline-cta .cta-btn-primary{background:#1a56db;color:#fff}
.inline-cta .cta-btn-primary:hover{background:#1e40af;transform:translateY(-1px)}
.inline-cta .cta-btn-secondary{background:#fff;color:#1a56db;border:2px solid #1a56db}
.inline-cta .cta-btn-secondary:hover{background:#eff6ff;transform:translateY(-1px)}

/* 底部大CTA条 */
.bottom-cta{background:linear-gradient(135deg,#1a56db,#1e40af);color:#fff;padding:48px 0;text-align:center;margin-top:0}
.bottom-cta h2{font-size:24px;font-weight:700;margin:0 0 12px}
.bottom-cta p{font-size:16px;opacity:.9;margin:0 0 20px;line-height:1.6}
.bottom-cta .cta-row{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}
.bottom-cta .cta-btn-white{display:inline-flex;align-items:center;gap:8px;padding:14px 32px;border-radius:10px;font-size:16px;font-weight:600;text-decoration:none;transition:all .2s;background:#fff;color:#1a56db}
.bottom-cta .cta-btn-white:hover{transform:translateY(-2px);box-shadow:0 4px 16px rgba(255,255,255,.3)}
.bottom-cta .cta-btn-outline{display:inline-flex;align-items:center;gap:8px;padding:14px 32px;border-radius:10px;border:2px solid rgba(255,255,255,.6);color:#fff;font-size:16px;font-weight:600;text-decoration:none;transition:all .2s}
.bottom-cta .cta-btn-outline:hover{background:rgba(255,255,255,.1);transform:translateY(-2px)}
@media(max-width:768px){.float-contact{right:8px;bottom:80px;gap:8px}.float-contact a{width:44px;height:44px;font-size:18px}.bottom-cta{padding:32px 16px}.bottom-cta h2{font-size:20px}}
"""

# ═════════════════════════════════════════════════════════
# 2. 悬浮联系栏 HTML（全站所有页面）
# ═════════════════════════════════════════════════════════

FLOATING_HTML = """  <!-- 右侧悬浮联系 -->
  <div class="float-contact">
    <a href="tel:13026603164" class="fc-tel" title="电话咨询">
      <span class="fc-text">📞 13026603164</span>
      📞
    </a>
    <a href="javascript:void(0)" class="fc-wechat" title="添加微信" onclick="navigator.clipboard.writeText('13026603164');this.querySelector('.fc-tooltip').innerHTML='<strong>✅ 已复制</strong>微信：13026603164<br><span style=color:#07c160>打开微信添加好友</span>'">
      <div class="fc-tooltip">
        <strong>微信扫码或搜索</strong>
        微信号：13026603164<br>
        <span class="fc-copy" onclick="event.stopPropagation();navigator.clipboard.writeText('13026603164');this.textContent='✅ 已复制'">📋 复制微信号</span>
      </div>
      💬
    </a>
  </div>"""

# ═════════════════════════════════════════════════════════
# 3. 内嵌咨询CTA条（内容页中段）
# ═════════════════════════════════════════════════════════

INLINE_CTA = """  <div class="inline-cta">
    <h3>📦 有货物要发？30分钟出报价</h3>
    <p>微信/电话直连客服，发送货物信息（品类+尺寸+目的地），立即获取含全部费用的精准报价。</p>
    <div class="cta-btns">
      <a href="tel:13026603164" class="cta-btn cta-btn-primary">📞 立即致电 13026603164</a>
      <a href="javascript:void(0)" class="cta-btn cta-btn-secondary" onclick="navigator.clipboard.writeText('13026603164');this.textContent='✅ 已复制微信号，打开微信添加'">💬 复制微信号</a>
    </div>
  </div>"""

# ═════════════════════════════════════════════════════════
# 4. 底部大CTA（替换原有的简单CTA）
# ═════════════════════════════════════════════════════════

BOTTOM_CTA = """  <section class="bottom-cta">
    <div class="container">
      <h2>🚛 大件物流 · 微信直连 · 30分钟报价</h2>
      <p>搬家/家具/设备/建材/大货 — 大陆⇄台湾双向专线<br>添加微信：<strong>13026603164</strong>，发送货物信息立即出方案</p>
      <div class="cta-row">
        <a href="tel:13026603164" class="cta-btn-white">📞 一键拨号</a>
        <a href="javascript:void(0)" class="cta-btn-outline" onclick="navigator.clipboard.writeText('13026603164');this.textContent='✅ 已复制，打开微信添加好友'">💬 复制微信号</a>
        <a href="/contact" class="cta-btn-outline">📋 在线询价</a>
      </div>
    </div>
  </section>"""

# ═════════════════════════════════════════════════════════
# 主流程
# ═════════════════════════════════════════════════════════

def main():
    # Step 1: 注入 CSS
    css_path = os.path.join(BASE_DIR, 'style.css')
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    
    if 'float-contact' not in css:
        css += FLOATING_CSS
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(css)
        print("✅ style.css 已注入悬浮栏+CTA样式")
    else:
        print("⏭️  style.css 已包含样式，跳过")
    
    # Step 2: 所有页面注入悬浮联系栏
    html_files = []
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in ('.git',)]
        for f in files:
            if f.endswith('.html') and f != 'nav-preview.html':
                html_files.append(os.path.join(root, f))
    
    float_added = 0
    footer_updated = 0
    cta_added = 0
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        relpath = os.path.relpath(filepath, BASE_DIR)
        
        # 2a. 注入悬浮联系栏（放在 <body> 之后第一个位置）
        if 'float-contact' not in content:
            # 找到 </header> 之后的位置注入
            if '</header>' in content:
                content = content.replace('</header>', '</header>\n' + FLOATING_HTML)
                float_added += 1
            elif '<body>' in content:
                content = content.replace('<body>', '<body>\n' + FLOATING_HTML)
                float_added += 1
        
        # 2b. 内容页（equipment/guide/tw-to-cn/moving等）在中段加内嵌CTA
        is_content = any(d in relpath for d in ['equipment/', 'guide/', 'tw-to-cn/', 'cases/']) \
                     and 'index.html' not in os.path.basename(relpath)
        # 也包含根目录的新增页面
        is_content = is_content or any(p in relpath for p in [
            'moving-taiwan.html', 'moving-from-taiwan.html', 'furniture-shipping.html',
            'luggage-shipping.html', 'appliance-shipping.html', 'moving-cost.html',
            'bulk-cargo-taiwan.html', 'building-materials-taiwan.html', 'commercial-cargo.html'
        ])
        
        if is_content and 'inline-cta' not in content:
            # 在最后一个 </section> 或文章内容结尾前加CTA
            # 策略：在第二个 <h2> 之后插入
            h2_matches = list(re.finditer(r'<h2[^>]*>', content))
            if len(h2_matches) >= 2:
                pos = h2_matches[1].start()
                content = content[:pos] + INLINE_CTA + '\n' + content[pos:]
                cta_added += 1
        
        # 2c. 替换旧CTA为新的底部大CTA
        # 旧的CTA模式
        old_cta_patterns = [
            r'<section class="cta">\s*<div class="container">\s*<h2>[^<]*</h2>\s*<p>[^<]*</p>\s*<a[^>]*>立即咨询</a>\s*<a[^>]*>📞 拨打电话</a>\s*</div>\s*</section>',
        ]
        if 'bottom-cta' not in content:
            # 替换标准CTA块
            old_cta = re.search(r'<section class="cta">.*?</section>', content, re.DOTALL)
            if old_cta and '询价报价' not in content[old_cta.start():old_cta.end()]:
                content = content[:old_cta.start()] + BOTTOM_CTA + content[old_cta.end():]
                footer_updated += 1
        
        # 写回
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
    
    print(f"\n📊 注入统计：")
    print(f"  悬浮联系栏：{float_added} 页")
    print(f"  内嵌CTA条：{cta_added} 页")
    print(f"  底部大CTA：{footer_updated} 页")
    print(f"  总页面数：{len(html_files)}")

if __name__ == "__main__":
    main()
