#!/usr/bin/env python3
"""
批量修复简版 header 页面：统一到站内标准模板
- 8 个简版：替换 header + 加 style.css + 删 header 内联样式
- 1 个特例(heavy-cargo-shipping.html)：从零插入 header + 加 style.css
"""
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))

STYLE_TAG = '<link rel="stylesheet" href="style.css">'

STD_HEADER = '''<header class="header">
    <div class="container">
      <a href="/" class="logo">速豹集运<span>大件物流专线</span></a>
      <button class="burger" aria-label="菜单" onclick="this.nextElementSibling.classList.toggle('open')">☰</button>
      <nav class="nav">
        <a href="/equipment/">大件物流</a>
        <a href="/pricing-calculator">运费估算</a>
        <a href="/volume-calculator">材积计算</a>
        <a href="/prohibited-items-checker">禁运查询</a>
        <a href="/article-list">文章攻略</a>
        <a href="/contact">询价报价</a>
        <a href="/tw-to-cn/">台湾寄大陆</a>
        <a href="/about">关于我们</a>
      </nav>
    </div>
  </header>'''

# ============================================================
# Part 1: 8 个简版页面（有 header 但缺 logo/burger/style.css）
# ============================================================
SIMPLE_FILES = [
    "about-company.html",
    "city-shipping-guide.html",
    "equipment-cases.html",
    "faq-collection.html",
    "fcl-container-shipping.html",
    "shipping-price-list.html",
    "shipping-time-calculator.html",
    "service-navigation.html",
]

# OLD header pattern (matches the stripped-down <header> block with nav links)
OLD_HEADER_RE = re.compile(
    r'<header>\s*<div class="container">\s*<nav class="nav">\s*'
    r'<a href="/equipment/">[^<]*</a>\s*'
    r'<a href="/pricing-calculator">[^<]*</a>\s*'
    r'<a href="/volume-calculator">[^<]*</a>\s*'
    r'<a href="/prohibited-items-checker">[^<]*</a>\s*'
    r'<a href="/article-list">[^<]*</a>\s*'
    r'<a href="/contact">[^<]*</a>\s*'
    r'<a href="/tw-to-cn/">[^<]*</a>\s*'
    r'<a href="/about">[^<]*</a>\s*'
    r'\s*</nav>\s*</div>\s*</header>',
    re.DOTALL,
)

# Inline header style to remove
INLINE_HEADER_RE = re.compile(r'header\{[^}]*\}')

fixed_count = 0

for fname in SIMPLE_FILES:
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        print(f"[SKIP] {fname} - not found")
        continue

    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    original = html
    did_something = False

    # 1. Add <link rel="stylesheet" href="style.css"> after canonical
    canon_pattern = r'(<link rel="canonical" href="[^"]+">)'
    if STYLE_TAG not in html and re.search(canon_pattern, html):
        html = re.sub(canon_pattern, r'\1\n  ' + STYLE_TAG, html)
        did_something = True

    # 2. Replace old header with standard one
    if OLD_HEADER_RE.search(html):
        html = OLD_HEADER_RE.sub(STD_HEADER, html)
        did_something = True

    # 3. Remove inline header{...} style rules
    if INLINE_HEADER_RE.search(html):
        html = INLINE_HEADER_RE.sub('', html)
        did_something = True

    if did_something and html != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"[OK] {fname}")
        fixed_count += 1
    else:
        print(f"[SKIP] {fname} - no changes needed")

# ============================================================
# Part 2: heavy-cargo-shipping.html（完全没有 header）
# ============================================================
fpath = os.path.join(BASE, "heavy-cargo-shipping.html")
if os.path.exists(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    original = html
    did_something = False

    # 1. Add style.css
    canon_pattern = r'(<link rel="canonical" href="https://www\.subaotw\.cn/heavy-cargo-shipping">)'
    if STYLE_TAG not in html and re.search(canon_pattern, html):
        html = re.sub(canon_pattern, r'\1\n  ' + STYLE_TAG, html)
        did_something = True

    # 2. Insert header between <body> and <main>
    if '<body>' in html and STD_HEADER not in html:
        html = html.replace('<body>\n\n\n<main>', '<body>\n\n' + STD_HEADER + '\n<main>')
        did_something = True

    if did_something and html != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"[OK] heavy-cargo-shipping.html (added header from scratch)")
        fixed_count += 1
    else:
        print(f"[SKIP] heavy-cargo-shipping.html - no changes needed")

print(f"\nDone. Fixed {fixed_count} files.")
