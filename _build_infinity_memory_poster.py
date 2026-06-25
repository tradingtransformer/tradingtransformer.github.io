#!/usr/bin/env python3
# Apple-Music-style promo poster for NoArk, in two formats:
#   Reddit     1080x1350
#   App Store  1242x2688
# The wswai cloud "A.I." logo (real photo) sits as an app-icon tile dead-centre
# with the "NOARK" wordmark below it; promo slogan up top, price + guarantee at
# the foot. Same blue brand gradient + starfield as the other covers.
#
# qlmanage fills a SQUARE viewport and clips a portrait viewBox, so each poster
# is authored on a W==H square with the art in a centre column; the side bars
# are cropped off after rendering. Build:
#   python3 _build_infinity_memory_poster.py
#   for s in reddit-1080x1350 appstore-1242x2688; do ... render+crop ... done
# (see the render loop in the shell history, or re-run the documented commands)

import base64

FONT = "-apple-system,'SF Pro Display','Helvetica Neue',Arial,sans-serif"
LOGO_B64 = base64.b64encode(open("wswai.jpeg", "rb").read()).decode()

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

DEFS = '''<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#5a0a16"/><stop offset="0.4" stop-color="#8c0f24"/>
    <stop offset="0.72" stop-color="#b21133"/><stop offset="1" stop-color="#c8143c"/>
  </linearGradient>
  <radialGradient id="glow" cx="0.5" cy="0.42" r="0.58">
    <stop offset="0" stop-color="#ff9caa" stop-opacity="0.6"/>
    <stop offset="0.34" stop-color="#ff4f6e" stop-opacity="0.32"/>
    <stop offset="0.72" stop-color="#e01e44" stop-opacity="0.06"/>
    <stop offset="1" stop-color="#e01e44" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="gloss" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#ffffff"/><stop offset="0.5" stop-color="#fff2f4"/>
    <stop offset="1" stop-color="#ffccd5"/>
  </linearGradient>
  <clipPath id="iconClip"><rect x="-150" y="-150" width="300" height="300" rx="66"/></clipPath>
  <filter id="soft" x="-40%" y="-40%" width="180%" height="200%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="16"/>
    <feOffset dx="0" dy="22" result="sh"/>
    <feFlood flood-color="#020714" flood-opacity="0.55"/>
    <feComposite in2="sh" operator="in"/>
    <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="iconShadow" x="-50%" y="-50%" width="200%" height="220%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="26"/>
    <feOffset dx="0" dy="30" result="sh"/>
    <feFlood flood-color="#02050f" flood-opacity="0.6"/>
    <feComposite in2="sh" operator="in"/>
    <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>'''

def stars(ox):
    pts = [(150,180,2,.5),(900,140,2.4,.6),(1010,360,1.6,.4),(80,500,1.8,.45),
           (1020,700,2,.5),(60,900,1.5,.35),(1000,1080,1.8,.45),(120,1180,2,.5),
           (300,100,1.4,.4),(780,1240,1.6,.4)]
    body = "".join(f'<circle cx="{x+ox}" cy="{y}" r="{r}" opacity="{o}"/>' for x,y,r,o in pts)
    return f'<g fill="#ffffff">{body}</g>'

def icon_group(cx, cy, scale):
    return f'''<g transform="translate({cx},{cy}) scale({scale})" filter="url(#iconShadow)">
  <image x="-150" y="-150" width="300" height="300" clip-path="url(#iconClip)"
         xlink:href="data:image/jpeg;base64,{LOGO_B64}"/>
  <rect x="-150" y="-150" width="300" height="300" rx="66" fill="none" stroke="#ffffff" stroke-opacity="0.35" stroke-width="2"/>
</g>'''

# wordmark "NOARK" + "∞  MEMORY" identity line stay Latin across locales (logotype).
COPY = {
 "en": dict(slogan="Infinity Memory. Zero exposure.", eyebrow="PREMIUM AI",
            price="Starts at $49.99", cta="Download on the App Store",
            guarantee="7-day money-back guarantee if you're not satisfied.",
            philan="50% of app profits go to philanthropy."),
 "es": dict(slogan="Memoria infinita. Cero exposición.", eyebrow="IA PREMIUM",
            price="Desde $49.99", cta="Descárgalo en el App Store",
            guarantee="Garantía de reembolso de 7 días si no estás satisfecho.",
            philan="El 50% de las ganancias se destina a obras benéficas."),
 "fr": dict(slogan="Mémoire infinie. Zéro exposition.", eyebrow="IA PREMIUM",
            price="À partir de 49,99 $", cta="Télécharger dans l'App Store",
            guarantee="Remboursé sous 7 jours en cas d'insatisfaction.",
            philan="50 % des bénéfices sont reversés à des œuvres caritatives."),
 "ja": dict(slogan="無限の記憶。露出ゼロ。", eyebrow="プレミアムAI",
            price="$49.99から", cta="App Storeでダウンロード",
            guarantee="ご満足いただけない場合、7日間返金保証。",
            philan="アプリ収益の50%を慈善活動に寄付します。"),
 "zh-cn": dict(slogan="无限记忆。零曝光。", eyebrow="高级 AI",
            price="$49.99 起", cta="在 App Store 下载",
            guarantee="7 天内不满意，全额退款。",
            philan="应用利润的 50% 用于慈善公益。"),
 "zh-tw": dict(slogan="無限記憶。零曝光。", eyebrow="進階 AI",
            price="$49.99 起", cta="在 App Store 下載",
            guarantee="7 天內不滿意，全額退款。",
            philan="應用程式利潤的 50% 用於慈善公益。"),
}
WORDMARK = "NOARK"
BRAND = "∞  MEMORY"
CJK = {"ja", "zh-cn", "zh-tw"}

def text_units(s, latin):
    u = 0.0
    for ch in s:
        if ch == " ": u += 0.30
        elif ord(ch) >= 0x2E80: u += 1.0
        else: u += latin
    return u

def fit(s, base, max_w, latin=0.55):
    u = text_units(s, latin)
    return base if u <= 0 else int(min(base, max_w / u))

# per-format geometry. SQ = square canvas side; OX = left pad of the W column.
LAYOUTS = {
    "reddit-1080x1350": dict(
        W=1080, H=1350, glowy=600,
        slogan=(156,46), icon=(430,1.0), word=(790,176), brand=(864,44,14),
        eyebrow=(972,30,6), price=(1036,50), btn=(1148,512,92,46,13,36),
        guar=(1262,28), phil=(1304,27),
    ),
    "appstore-1242x2688": dict(
        W=1242, H=2688, glowy=1040,
        slogan=(340,62), icon=(1020,1.78), word=(1650,300), brand=(1772,68,22),
        eyebrow=(2020,42,9), price=(2128,86), btn=(2360,820,150,75,20,58),
        guar=(2512,40), phil=(2574,38),
    ),
}

def poster(L, C, cjk):
    SQ = L["H"]
    OX = (SQ - L["W"]) // 2
    XC = OX + L["W"] // 2
    sl_y, sl_fs = L["slogan"]
    ic_y, ic_sc = L["icon"]
    w_y, w_fs = L["word"]
    b_y, b_fs, b_ls = L["brand"]
    e_y, e_fs, e_ls = L["eyebrow"]
    p_y, p_fs = L["price"]
    bt_y, bt_w, bt_h, bt_r, bt_dy, bt_fs = L["btn"]
    g_y, g_fs = L["guar"]
    ph_y, ph_fs = L["phil"]
    wls = -4 if w_fs < 200 else -7
    lat = 0.55
    # shrink variable-length strings to the column so nothing clips
    sl_fs = fit(C["slogan"], sl_fs, L["W"] - 90, lat)
    e_fs  = fit(C["eyebrow"], e_fs, L["W"] - 120, lat)
    p_fs  = fit(C["price"], p_fs, L["W"] * 0.6, lat)
    bt_fs = fit(C["cta"], bt_fs, bt_w - 70, lat)
    g_fs  = fit(C["guarantee"], g_fs, L["W"] - 70, lat)
    ph_fs = fit(C["philan"], ph_fs, L["W"] - 70, lat)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{SQ}" height="{SQ}" viewBox="0 0 {SQ} {SQ}">
{DEFS}
<rect width="{SQ}" height="{SQ}" fill="url(#bg)"/>
<ellipse cx="{XC}" cy="{L["glowy"]}" rx="{int(L["W"]*0.70)}" ry="{int(L["H"]*0.44)}" fill="url(#glow)"/>
<g transform="translate({OX},0)">{stars(0)}</g>

<text x="{XC}" y="{sl_y}" text-anchor="middle" font-family="{FONT}" font-weight="600" font-size="{sl_fs}" fill="#ffd9df" letter-spacing="0.5">{esc(C["slogan"])}</text>

{icon_group(XC, ic_y, ic_sc)}

<text x="{XC}" y="{w_y}" text-anchor="middle" font-family="{FONT}" font-weight="800" font-size="{w_fs}" letter-spacing="{wls}" fill="url(#gloss)" filter="url(#soft)">{esc(WORDMARK)}</text>
<text x="{XC}" y="{b_y}" text-anchor="middle" font-family="{FONT}" font-weight="600" font-size="{b_fs}" letter-spacing="{b_ls}" fill="#ffb3bf">{esc(BRAND)}</text>

<text x="{XC}" y="{e_y}" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="{e_fs}" letter-spacing="{e_ls}" fill="#ffc0cb">{esc(C["eyebrow"])}</text>
<text x="{XC}" y="{p_y}" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="{p_fs}" fill="#ffffff">{esc(C["price"])}</text>

<g transform="translate({XC},{bt_y})">
  <rect x="{-bt_w//2}" y="{-bt_h//2}" width="{bt_w}" height="{bt_h}" rx="{bt_r}" fill="#ffffff"/>
  <text x="0" y="{bt_dy}" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="{bt_fs}" fill="#0a1424">{esc(C["cta"])}</text>
</g>
<text x="{XC}" y="{g_y}" text-anchor="middle" font-family="{FONT}" font-weight="500" font-size="{g_fs}" fill="#f3c2cb">{esc(C["guarantee"])}</text>
<text x="{XC}" y="{ph_y}" text-anchor="middle" font-family="{FONT}" font-weight="600" font-size="{ph_fs}" fill="#ffd9df">{esc(C["philan"])}</text>
</svg>'''

# Reddit: English only. App Store: all locales.
n = 0
open("noark-reddit-infinity-memory-1080x1350-en.svg", "w", encoding="utf-8").write(
    poster(LAYOUTS["reddit-1080x1350"], COPY["en"], False)); n += 1
print("wrote noark-reddit-infinity-memory-1080x1350-en.svg")
for loc, C in COPY.items():
    fn = f"noark-appstore-infinity-memory-1242x2688-{loc}.svg"
    open(fn, "w", encoding="utf-8").write(poster(LAYOUTS["appstore-1242x2688"], C, loc in CJK))
    print("wrote", fn); n += 1
print(n, "svgs")
