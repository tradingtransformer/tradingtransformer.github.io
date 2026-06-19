#!/usr/bin/env python3
# Generates localized NoArk App Store covers (privacy + guidance) at 1242x2688.
# Geometry matches the approved English SVGs; only text/sizes change per locale.

FONT = "-apple-system,'SF Pro Display','Helvetica Neue',Arial,sans-serif"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def headline_block(lines, y0, lh, ls, gap_split=None, gap=0):
    """lines: list of (text, color_hex, italic_bool). Returns svg text elements."""
    out = []
    for i, (t, c, it) in enumerate(lines):
        y = y0 + i * lh + (gap if (gap_split is not None and i >= gap_split) else 0)
        style = ' font-style="italic"' if it else ''
        out.append(
            f'<text x="110" y="{y}" font-family="{FONT}" font-weight="800" '
            f'font-size="{ls["fs"]}" fill="{c}" letter-spacing="{ls["sp"]}"{style}>{esc(t)}</text>'
        )
    return "\n".join(out)

PRIVACY_DEFS = '''<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#04060d"/><stop offset="0.45" stop-color="#070b18"/>
    <stop offset="0.78" stop-color="#0a1622"/><stop offset="1" stop-color="#06120f"/>
  </linearGradient>
  <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#7ff0d0" stop-opacity="0.42"/>
    <stop offset="0.32" stop-color="#39d6a8" stop-opacity="0.22"/>
    <stop offset="0.7" stop-color="#1f9e8c" stop-opacity="0.05"/>
    <stop offset="1" stop-color="#1f9e8c" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="shieldFill" cx="0.5" cy="0.35" r="0.75">
    <stop offset="0" stop-color="#103428"/><stop offset="0.6" stop-color="#0a1f1c"/>
    <stop offset="1" stop-color="#06130f"/>
  </radialGradient>
  <linearGradient id="shieldEdge" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#8df3d3"/><stop offset="1" stop-color="#2fae8e"/>
  </linearGradient>
  <linearGradient id="ring" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#9af5da" stop-opacity="0.9"/>
    <stop offset="1" stop-color="#2fae8e" stop-opacity="0.15"/>
  </linearGradient>
</defs>'''

STARS = '''<g fill="#ffffff">
  <circle cx="180" cy="300" r="2" opacity="0.5"/><circle cx="980" cy="240" r="2.5" opacity="0.6"/>
  <circle cx="1080" cy="520" r="1.6" opacity="0.4"/><circle cx="120" cy="700" r="1.8" opacity="0.45"/>
  <circle cx="1130" cy="980" r="2" opacity="0.5"/><circle cx="90" cy="1180" r="1.5" opacity="0.35"/>
  <circle cx="1150" cy="1500" r="2.2" opacity="0.5"/><circle cx="70" cy="1650" r="1.7" opacity="0.4"/>
  <circle cx="1100" cy="2050" r="1.8" opacity="0.45"/><circle cx="150" cy="2150" r="2" opacity="0.5"/>
  <circle cx="1000" cy="2380" r="1.5" opacity="0.35"/><circle cx="260" cy="2450" r="1.8" opacity="0.4"/>
</g>'''

def privacy_svg(d):
    hl = headline_block(d["hl"], d["y0"], d["lh"], d["ls"])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1242" height="2688" viewBox="0 0 1242 2688">
{PRIVACY_DEFS}
<rect width="1242" height="2688" fill="url(#bg)"/>
<ellipse cx="621" cy="1560" rx="880" ry="760" fill="url(#glow)"/>
{STARS}
{hl}
<g transform="translate(621,1560)">
  <circle cx="0" cy="0" r="430" fill="none" stroke="url(#ring)" stroke-width="2.5" opacity="0.5"/>
  <circle cx="0" cy="0" r="360" fill="none" stroke="url(#ring)" stroke-width="2" opacity="0.32"/>
  <path d="M0,-330 C140,-270 250,-250 300,-238 C300,-60 250,170 0,338 C-250,170 -300,-60 -300,-238 C-250,-250 -140,-270 0,-330 Z"
        fill="url(#shieldFill)" stroke="url(#shieldEdge)" stroke-width="10"/>
  <g transform="translate(0,-30)">
    <path d="M-92,-30 a92,110 0 0 1 184,0" fill="none" stroke="#bff6e4" stroke-width="26"/>
    <rect x="-130" y="-30" width="260" height="200" rx="34" fill="#0d2a22" stroke="#7ff0d0" stroke-width="11"/>
    <circle cx="0" cy="48" r="30" fill="#7ff0d0"/>
    <rect x="-14" y="62" width="28" height="62" rx="14" fill="#7ff0d0"/>
  </g>
  <text x="0" y="232" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="{d['cap_fs']}" fill="#9af5da" letter-spacing="2">{esc(d['cap'])}</text>
</g>
<text x="621" y="2150" text-anchor="middle" font-family="{FONT}" font-weight="500" font-size="{d['sup_fs']}" fill="#aeb6c4">{esc(d['sup'])}</text>
<text x="621" y="2400" text-anchor="middle" font-family="{FONT}" font-weight="600" font-size="{d['trust_fs']}" fill="#cfd5e0">{esc(d['trust'])}</text>
<text x="110" y="2620" font-family="{FONT}" font-weight="600" font-size="34" fill="#7a8294">{esc(d['brand'])}</text>
</svg>'''

GUID_DEFS = '''<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#05070f"/><stop offset="0.42" stop-color="#0b1020"/>
    <stop offset="0.72" stop-color="#161430"/><stop offset="1" stop-color="#241a26"/>
  </linearGradient>
  <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#ffe6b0" stop-opacity="0.5"/>
    <stop offset="0.34" stop-color="#ffcf8a" stop-opacity="0.26"/>
    <stop offset="0.7" stop-color="#ffb877" stop-opacity="0.05"/>
    <stop offset="1" stop-color="#ffb877" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="dial" cx="0.5" cy="0.4" r="0.7">
    <stop offset="0" stop-color="#241d12"/><stop offset="0.7" stop-color="#15120c"/>
    <stop offset="1" stop-color="#0c0a07"/>
  </radialGradient>
  <linearGradient id="rim" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#ffe2a6"/><stop offset="1" stop-color="#c79544"/>
  </linearGradient>
  <radialGradient id="star" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#fff4d6"/><stop offset="1" stop-color="#ffce7a"/>
  </radialGradient>
</defs>'''

def guidance_svg(d):
    hl = headline_block(d["hl"], d["y0"], d["lh"], d["ls"], gap_split=2, gap=d.get("gap", 38))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1242" height="2688" viewBox="0 0 1242 2688">
{GUID_DEFS}
<rect width="1242" height="2688" fill="url(#bg)"/>
<ellipse cx="621" cy="1580" rx="880" ry="780" fill="url(#glow)"/>
{STARS}
{hl}
<g transform="translate(621,1560)">
  <circle cx="0" cy="0" r="430" fill="none" stroke="url(#rim)" stroke-width="2.5" opacity="0.4"/>
  <circle cx="0" cy="0" r="356" fill="url(#dial)" stroke="url(#rim)" stroke-width="10"/>
  <circle cx="0" cy="0" r="356" fill="none" stroke="#ffe2a6" stroke-width="2" opacity="0.25"/>
  <g stroke="#ffe2a6" stroke-width="4" opacity="0.55">
    <line x1="0" y1="-330" x2="0" y2="-300"/><line x1="0" y1="300" x2="0" y2="330"/>
    <line x1="-330" y1="0" x2="-300" y2="0"/><line x1="300" y1="0" x2="330" y2="0"/>
  </g>
  <g stroke="#ffe2a6" stroke-width="2.5" opacity="0.3">
    <line x1="233" y1="-233" x2="212" y2="-212"/><line x1="-233" y1="-233" x2="-212" y2="-212"/>
    <line x1="233" y1="233" x2="212" y2="212"/><line x1="-233" y1="233" x2="-212" y2="212"/>
  </g>
  <g transform="rotate(18)">
    <path d="M0,-250 L46,40 L0,8 Z" fill="url(#rim)"/>
    <path d="M0,250 L-46,-40 L0,-8 Z" fill="#5a4a2a"/>
    <path d="M0,-250 L-46,40 L0,8 Z" fill="#d9aa55"/>
    <path d="M0,250 L46,-40 L0,-8 Z" fill="#403014"/>
  </g>
  <circle cx="0" cy="0" r="26" fill="#1a160e" stroke="#ffe2a6" stroke-width="6"/>
  <g transform="translate(0,-356)">
    <path d="M0,-46 L12,-12 46,0 12,12 0,46 -12,12 -46,0 -12,-12 Z" fill="url(#star)"/>
  </g>
  <text x="0" y="270" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="{d['cap_fs']}" fill="#ffd98a" letter-spacing="2">{esc(d['cap'])}</text>
</g>
<text x="621" y="2150" text-anchor="middle" font-family="{FONT}" font-weight="500" font-size="{d['sup_fs']}" fill="#aeb6c4">{esc(d['sup'])}</text>
<text x="621" y="2400" text-anchor="middle" font-family="{FONT}" font-weight="600" font-size="{d['trust_fs']}" fill="#cfd5e0">{esc(d['trust'])}</text>
<text x="110" y="2620" font-family="{FONT}" font-weight="600" font-size="34" fill="#7a8294">{esc(d['brand'])}</text>
</svg>'''

BESPOKE_DEFS = '''<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#04060f"/><stop offset="0.45" stop-color="#070d1c"/>
    <stop offset="0.78" stop-color="#0b1630"/><stop offset="1" stop-color="#10162e"/>
  </linearGradient>
  <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#9ccbff" stop-opacity="0.45"/>
    <stop offset="0.32" stop-color="#5b9bf0" stop-opacity="0.24"/>
    <stop offset="0.7" stop-color="#2f6ad6" stop-opacity="0.05"/>
    <stop offset="1" stop-color="#2f6ad6" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="diaFill" cx="0.5" cy="0.28" r="0.85">
    <stop offset="0" stop-color="#e4f1ff"/><stop offset="0.45" stop-color="#8cc2ff"/>
    <stop offset="1" stop-color="#2f6ad6"/>
  </radialGradient>
  <linearGradient id="diaEdge" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#eaf6ff"/><stop offset="1" stop-color="#4f97e8"/>
  </linearGradient>
  <linearGradient id="ring" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#bfe0ff" stop-opacity="0.9"/>
    <stop offset="1" stop-color="#3f7fd6" stop-opacity="0.15"/>
  </linearGradient>
</defs>'''

def bespoke_svg(d):
    hl = headline_block(d["hl"], d["y0"], d["lh"], d["ls"])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1242" height="2688" viewBox="0 0 1242 2688">
{BESPOKE_DEFS}
<rect width="1242" height="2688" fill="url(#bg)"/>
<ellipse cx="621" cy="1560" rx="880" ry="760" fill="url(#glow)"/>
{STARS}
{hl}
<g transform="translate(621,1560)">
  <circle cx="0" cy="0" r="430" fill="none" stroke="url(#ring)" stroke-width="2.5" opacity="0.5"/>
  <circle cx="0" cy="0" r="360" fill="none" stroke="url(#ring)" stroke-width="2" opacity="0.32"/>
  <path d="M-150,-180 L150,-180 L260,-90 L0,300 L-260,-90 Z" fill="url(#diaFill)" stroke="url(#diaEdge)" stroke-width="9" stroke-linejoin="round"/>
  <line x1="-260" y1="-90" x2="260" y2="-90" stroke="#eaf6ff" stroke-width="5" opacity="0.85"/>
  <g stroke="#eaf6ff" stroke-width="3" opacity="0.55" fill="none">
    <line x1="-150" y1="-180" x2="-260" y2="-90"/><line x1="150" y1="-180" x2="260" y2="-90"/>
    <line x1="-150" y1="-180" x2="0" y2="-90"/><line x1="150" y1="-180" x2="0" y2="-90"/>
    <line x1="-150" y1="-180" x2="-120" y2="-90"/><line x1="150" y1="-180" x2="120" y2="-90"/>
  </g>
  <g stroke="#dbeeff" stroke-width="3" opacity="0.5" fill="none">
    <line x1="-260" y1="-90" x2="0" y2="300"/><line x1="260" y1="-90" x2="0" y2="300"/>
    <line x1="-120" y1="-90" x2="0" y2="300"/><line x1="120" y1="-90" x2="0" y2="300"/>
    <line x1="0" y1="-90" x2="0" y2="300"/>
  </g>
  <g transform="translate(300,-250)" fill="#ffffff">
    <path d="M0,-34 L8,-8 34,0 8,8 0,34 -8,8 -34,0 -8,-8 Z"/>
  </g>
  <circle cx="-230" cy="-150" r="6" fill="#ffffff" opacity="0.8"/>
  <text x="0" y="392" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="{d['cap_fs']}" fill="#bfe0ff" letter-spacing="2">{esc(d['cap'])}</text>
</g>
<text x="621" y="2150" text-anchor="middle" font-family="{FONT}" font-weight="500" font-size="{d['sup_fs']}" fill="#aeb6c4">{esc(d['sup'])}</text>
<text x="621" y="2400" text-anchor="middle" font-family="{FONT}" font-weight="600" font-size="{d['trust_fs']}" fill="#cfd5e0">{esc(d['trust'])}</text>
<text x="110" y="2620" font-family="{FONT}" font-weight="600" font-size="34" fill="#7a8294">{esc(d['brand'])}</text>
</svg>'''

W = "#ffffff"; ACC_P = "#5ee8c0"; ACC_B = "#8ec6ff"
MUTE = "#9aa1b2"; MUTE2 = "#c7cdda"; ACC_G = "#ffd98a"
LAT = {"fs": 112, "sp": -3}; LATg = {"fs": 106, "sp": -3}
CJK = {"fs": 116, "sp": -1}; CJKg = {"fs": 102, "sp": -1}

# ---- PRIVACY data per locale ----
PRIV = {
 "es": dict(hl=[("La única IA",W,0),("que nunca guarda",W,0),("ni vende",W,0),("tus datos.",ACC_P,0)],
            y0=455, lh=128, ls=LAT, cap="CIFRADO DE EXTREMO A EXTREMO", cap_fs=30,
            sup="Sin rastreo. Sin anuncios. Sin venta. Nunca.", sup_fs=42,
            trust="La eligen usuarios de iOS en 20+ países", trust_fs=44),
 "fr": dict(hl=[("La seule IA",W,0),("qui ne stocke",W,0),("ni ne vend",W,0),("vos données.",ACC_P,0)],
            y0=455, lh=128, ls=LAT, cap="CHIFFRÉ DE BOUT EN BOUT", cap_fs=36,
            sup="Aucun pistage. Aucune pub. Aucune vente. Jamais.", sup_fs=38,
            trust="Adoptée par des utilisateurs iOS dans 20+ pays", trust_fs=38),
 "ja": dict(hl=[("あなたのデータを",W,0),("保存も販売も",W,0),("しない",W,0),("唯一のAI。",ACC_P,0)],
            y0=470, lh=146, ls=CJK, cap="エンドツーエンド暗号化", cap_fs=40,
            sup="追跡なし。広告なし。販売なし。", sup_fs=44,
            trust="20か国以上のiOSユーザーに信頼されています", trust_fs=38),
 "zh-cn": dict(hl=[("唯一不存储",W,0),("也不出售你",W,0),("数据的 AI。",ACC_P,0)],
            y0=500, lh=146, ls=CJK, cap="端到端加密", cap_fs=44,
            sup="不追踪。无广告。绝不出售。", sup_fs=46,
            trust="20+ 国家的 iOS 用户信赖之选", trust_fs=44),
 "zh-tw": dict(hl=[("唯一不儲存",W,0),("也不出售你",W,0),("資料的 AI。",ACC_P,0)],
            y0=500, lh=146, ls=CJK, cap="端到端加密", cap_fs=44,
            sup="不追蹤。無廣告。絕不出售。", sup_fs=46,
            trust="20+ 國家的 iOS 使用者信賴之選", trust_fs=44),
}

# ---- GUIDANCE data per locale ----
GUID = {
 "es": dict(hl=[("Otras IA te dicen",MUTE,0),("cómo.",MUTE2,1),("NoArk te dice",W,0),("qué hacer.",ACC_G,1)],
            y0=450, lh=126, ls=LATg, gap=38, cap="ORIENTACIÓN, NO SOLO RESPUESTAS", cap_fs=36,
            sup="Te dice qué vale la pena hacer — por tu propio bien.", sup_fs=40,
            trust="La eligen usuarios de iOS en 20+ países", trust_fs=44),
 "fr": dict(hl=[("Les autres IA",MUTE,0),("disent comment.",MUTE2,1),("NoArk vous dit",W,0),("quoi faire.",ACC_G,1)],
            y0=450, lh=126, ls=LATg, gap=38, cap="DES CONSEILS, PAS QUE DES RÉPONSES", cap_fs=33,
            sup="Il vous dit ce qui compte — pour votre bien.", sup_fs=42,
            trust="Adoptée par des utilisateurs iOS dans 20+ pays", trust_fs=38),
 "ja": dict(hl=[("他のAIは",MUTE,0),("やり方を教える。",MUTE2,1),("NoArkは",W,0),("進む道を教える。",ACC_G,1)],
            y0=460, lh=140, ls=CJKg, gap=36, cap="答えだけでなく、導きを", cap_fs=40,
            sup="本当にすべきことを、あなたのために。", sup_fs=44,
            trust="20か国以上のiOSユーザーに信頼されています", trust_fs=38),
 "zh-cn": dict(hl=[("别的 AI 只教你",MUTE,0),("怎么做。",MUTE2,1),("NoArk 告诉你",W,0),("该做什么。",ACC_G,1)],
            y0=460, lh=140, ls=CJKg, gap=36, cap="不止给答案，更给方向", cap_fs=42,
            sup="告诉你什么值得做——为你好。", sup_fs=46,
            trust="20+ 国家的 iOS 用户信赖之选", trust_fs=44),
 "zh-tw": dict(hl=[("別的 AI 只教你",MUTE,0),("怎麼做。",MUTE2,1),("NoArk 告訴你",W,0),("該做什麼。",ACC_G,1)],
            y0=460, lh=140, ls=CJKg, gap=36, cap="不只給答案，更給方向", cap_fs=42,
            sup="告訴你什麼值得做——為你好。", sup_fs=46,
            trust="20+ 國家的 iOS 使用者信賴之選", trust_fs=44),
}

# ---- BESPOKE data per locale ----
BESP = {
 "es": dict(hl=[("La única IA que",W,0),("crea funciones",W,0),("para cada",W,0),("cliente diamante.",ACC_B,0)],
            y0=455, lh=128, ls={"fs":106,"sp":-3}, cap="HECHO A MEDIDA PARA TI", cap_fs=44,
            sup="Dinos qué quieres más y lo creamos para ti.", sup_fs=44,
            trust="La eligen usuarios de iOS en 20+ países", trust_fs=44),
 "fr": dict(hl=[("La seule IA qui",W,0),("crée des fonctions",W,0),("pour chaque",W,0),("client diamant.",ACC_B,0)],
            y0=455, lh=128, ls={"fs":98,"sp":-3}, cap="SUR MESURE, RIEN QUE POUR VOUS", cap_fs=38,
            sup="Dites-nous ce que vous voulez — on le crée pour vous.", sup_fs=38,
            trust="Adoptée par des utilisateurs iOS dans 20+ pays", trust_fs=38),
 "ja": dict(hl=[("ダイヤモンド",W,0),("顧客一人ひとりに",W,0),("機能を作る",W,0),("唯一のAI。",ACC_B,0)],
            y0=470, lh=146, ls=CJK, cap="あなただけのために", cap_fs=44,
            sup="欲しい機能を、私たちが形にします。", sup_fs=42,
            trust="20か国以上のiOSユーザーに信頼されています", trust_fs=38),
 "zh-cn": dict(hl=[("唯一为每位",W,0),("钻石客户定制",W,0),("功能的 AI。",ACC_B,0)],
            y0=500, lh=146, ls=CJK, cap="为你量身打造", cap_fs=44,
            sup="告诉我们你最想要的，我们为你打造。", sup_fs=46,
            trust="20+ 国家的 iOS 用户信赖之选", trust_fs=44),
 "zh-tw": dict(hl=[("唯一為每位",W,0),("鑽石客戶訂製",W,0),("功能的 AI。",ACC_B,0)],
            y0=500, lh=146, ls=CJK, cap="為你量身打造", cap_fs=44,
            sup="告訴我們你最想要的，我們為你打造。", sup_fs=46,
            trust="20+ 國家的 iOS 使用者信賴之選", trust_fs=44),
}

BRAND = {"es": "NoArk — Memoria Infinita", "fr": "NoArk — Mémoire Infinie",
         "ja": "NoArk — 無限の記憶", "zh-cn": "NoArk — 无限记忆",
         "zh-tw": "NoArk — 無限記憶"}

for loc, d in PRIV.items():
    d["brand"] = BRAND[loc]
    open(f"noark-appstore-privacy-1242x2688-{loc}.svg", "w", encoding="utf-8").write(privacy_svg(d))
for loc, d in GUID.items():
    d["brand"] = BRAND[loc]
    open(f"noark-appstore-guidance-1242x2688-{loc}.svg", "w", encoding="utf-8").write(guidance_svg(d))
for loc, d in BESP.items():
    d["brand"] = BRAND[loc]
    open(f"noark-appstore-bespoke-1242x2688-{loc}.svg", "w", encoding="utf-8").write(bespoke_svg(d))
print("wrote", len(PRIV) + len(GUID) + len(BESP), "svgs")
