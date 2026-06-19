#!/usr/bin/env python3
# Generates localized NoArk Reddit covers (privacy + guidance + bespoke) at 1080x1350.
# Centerpiece geometry is identical to the App Store covers (same internal coords);
# only the canvas, headline layout and supporting-text positions change for the
# squarer Reddit format. Localized text is shared with _build_appstore_covers.py.

FONT = "-apple-system,'SF Pro Display','Helvetica Neue',Arial,sans-serif"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def is_cjk(ch):
    return ord(ch) >= 0x2E80

# ---- width estimation (advance widths relative to font size) ----
def text_units(s, latin_factor):
    u = 0.0
    for ch in s:
        if ch == " ":
            u += 0.30
        elif is_cjk(ch):
            u += 1.0
        else:
            u += latin_factor
    return u

def fit_fs(s, base_fs, max_w, latin_factor):
    u = text_units(s, latin_factor)
    if u <= 0:
        return base_fs
    return int(min(base_fs, max_w / u))

# ---- headline layout ----
HEAD_MAXW = 974  # left x=70, ~36 right margin

def headline_fs(lines, base_latin, base_cjk, cjk):
    base = base_cjk if cjk else base_latin
    factor = 0.56
    fs = base
    for (t, _c, _it) in lines:
        fs = min(fs, fit_fs(t, base, HEAD_MAXW, factor))
    return fs

def layout_no_gap(n, fs, bot):
    lh = round(fs * 1.2)
    if 150 + (n - 1) * lh > bot:
        lh = (bot - 150) // (n - 1)
    span = (n - 1) * lh
    y0 = round((150 + bot - span) / 2)
    return [y0 + i * lh for i in range(n)], lh

def layout_gap(fs, bot, gap=36):
    lh = round(fs * 1.16)
    if 150 + 3 * lh + gap > bot:
        lh = (bot - 150 - gap) // 3
    span = 3 * lh + gap
    y0 = round((150 + bot - span) / 2)
    return [y0, y0 + lh, y0 + 2 * lh + gap, y0 + 3 * lh + gap], lh

def headline_svg(lines, ys, fs, cjk):
    sp = -1 if cjk else -2
    out = []
    for (t, c, it), y in zip(lines, ys):
        style = ' font-style="italic"' if it else ''
        out.append(
            f'<text x="70" y="{y}" font-family="{FONT}" font-weight="800" '
            f'font-size="{fs}" fill="{c}" letter-spacing="{sp}"{style}>{esc(t)}</text>'
        )
    return "\n".join(out)

def support_svg(d):
    sup_fs = fit_fs(d["sup"], 38, 1000, 0.5)
    trust_fs = fit_fs(d["trust"], 40, 1000, 0.52)
    return (
        f'<text x="540" y="1115" text-anchor="middle" font-family="{FONT}" font-weight="500" '
        f'font-size="{sup_fs}" fill="#aeb6c4">{esc(d["sup"])}</text>\n'
        f'<text x="540" y="1190" text-anchor="middle" font-family="{FONT}" font-weight="600" '
        f'font-size="{trust_fs}" fill="#cfd5e0">{esc(d["trust"])}</text>\n'
        f'<text x="50" y="1305" font-family="{FONT}" font-weight="600" font-size="32" '
        f'fill="#ffffff">{esc(d["brand"])}</text>'
    )

STARS = '''<g fill="#ffffff">
  <circle cx="150" cy="180" r="2" opacity="0.5"/><circle cx="900" cy="140" r="2.4" opacity="0.6"/>
  <circle cx="1010" cy="360" r="1.6" opacity="0.4"/><circle cx="80" cy="500" r="1.8" opacity="0.45"/>
  <circle cx="1020" cy="700" r="2" opacity="0.5"/><circle cx="60" cy="900" r="1.5" opacity="0.35"/>
  <circle cx="1000" cy="1080" r="1.8" opacity="0.45"/><circle cx="120" cy="1180" r="2" opacity="0.5"/>
</g>'''

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

def privacy_svg(d, cjk):
    fs = headline_fs(d["hl"], 80, 100, cjk)
    ys, _ = layout_no_gap(len(d["hl"]), fs, 470)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350">
{PRIVACY_DEFS}
<rect width="1080" height="1350" fill="url(#bg)"/>
<ellipse cx="540" cy="760" rx="720" ry="560" fill="url(#glow)"/>
{STARS}
{headline_svg(d["hl"], ys, fs, cjk)}
<g transform="translate(540,765) scale(0.64)">
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
{support_svg(d)}
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

def guidance_svg(d, cjk):
    fs = headline_fs(d["hl"], 74, 92, cjk)
    ys, _ = layout_gap(fs, 475)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350">
{GUID_DEFS}
<rect width="1080" height="1350" fill="url(#bg)"/>
<ellipse cx="540" cy="770" rx="720" ry="570" fill="url(#glow)"/>
{STARS}
{headline_svg(d["hl"], ys, fs, cjk)}
<g transform="translate(540,770) scale(0.64)">
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
{support_svg(d)}
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

def bespoke_svg(d, cjk):
    fs = headline_fs(d["hl"], 78, 98, cjk)
    ys, _ = layout_no_gap(len(d["hl"]), fs, 480)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350">
{BESPOKE_DEFS}
<rect width="1080" height="1350" fill="url(#bg)"/>
<ellipse cx="540" cy="760" rx="720" ry="560" fill="url(#glow)"/>
{STARS}
{headline_svg(d["hl"], ys, fs, cjk)}
<g transform="translate(540,770) scale(0.62)">
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
{support_svg(d)}
</svg>'''

W = "#ffffff"; ACC_P = "#5ee8c0"; ACC_B = "#8ec6ff"
MUTE = "#9aa1b2"; MUTE2 = "#c7cdda"; ACC_G = "#ffd98a"

# ---- PRIVACY data per locale (shared with App Store covers) ----
PRIV = {
 "es": dict(hl=[("La única IA",W,0),("que nunca guarda",W,0),("ni vende",W,0),("tus datos.",ACC_P,0)],
            cap="CIFRADO DE EXTREMO A EXTREMO", cap_fs=30,
            sup="Sin rastreo. Sin anuncios. Sin venta. Nunca.",
            trust="La eligen usuarios de iOS en 20+ países"),
 "fr": dict(hl=[("La seule IA",W,0),("qui ne stocke",W,0),("ni ne vend",W,0),("vos données.",ACC_P,0)],
            cap="CHIFFRÉ DE BOUT EN BOUT", cap_fs=36,
            sup="Aucun pistage. Aucune pub. Aucune vente. Jamais.",
            trust="Adoptée par des utilisateurs iOS dans 20+ pays"),
 "ja": dict(hl=[("あなたのデータを",W,0),("保存も販売も",W,0),("しない",W,0),("唯一のAI。",ACC_P,0)],
            cap="エンドツーエンド暗号化", cap_fs=40,
            sup="追跡なし。広告なし。販売なし。",
            trust="20か国以上のiOSユーザーに信頼されています"),
 "zh-cn": dict(hl=[("唯一不存储",W,0),("也不出售你",W,0),("数据的 AI。",ACC_P,0)],
            cap="端到端加密", cap_fs=44,
            sup="不追踪。无广告。绝不出售。",
            trust="20+ 国家的 iOS 用户信赖之选"),
 "zh-tw": dict(hl=[("唯一不儲存",W,0),("也不出售你",W,0),("資料的 AI。",ACC_P,0)],
            cap="端到端加密", cap_fs=44,
            sup="不追蹤。無廣告。絕不出售。",
            trust="20+ 國家的 iOS 使用者信賴之選"),
}

# ---- GUIDANCE data per locale ----
GUID = {
 "es": dict(hl=[("Otras IA te dicen",MUTE,0),("cómo.",MUTE2,1),("NoArk te dice",W,0),("qué hacer.",ACC_G,1)],
            cap="ORIENTACIÓN, NO SOLO RESPUESTAS", cap_fs=36,
            sup="Te dice qué vale la pena hacer — por tu propio bien.",
            trust="La eligen usuarios de iOS en 20+ países"),
 "fr": dict(hl=[("Les autres IA",MUTE,0),("disent comment.",MUTE2,1),("NoArk vous dit",W,0),("quoi faire.",ACC_G,1)],
            cap="DES CONSEILS, PAS QUE DES RÉPONSES", cap_fs=33,
            sup="Il vous dit ce qui compte — pour votre bien.",
            trust="Adoptée par des utilisateurs iOS dans 20+ pays"),
 "ja": dict(hl=[("他のAIは",MUTE,0),("やり方を教える。",MUTE2,1),("NoArkは",W,0),("進む道を教える。",ACC_G,1)],
            cap="答えだけでなく、導きを", cap_fs=40,
            sup="本当にすべきことを、あなたのために。",
            trust="20か国以上のiOSユーザーに信頼されています"),
 "zh-cn": dict(hl=[("别的 AI 只教你",MUTE,0),("怎么做。",MUTE2,1),("NoArk 告诉你",W,0),("该做什么。",ACC_G,1)],
            cap="不止给答案，更给方向", cap_fs=42,
            sup="告诉你什么值得做——为你好。",
            trust="20+ 国家的 iOS 用户信赖之选"),
 "zh-tw": dict(hl=[("別的 AI 只教你",MUTE,0),("怎麼做。",MUTE2,1),("NoArk 告訴你",W,0),("該做什麼。",ACC_G,1)],
            cap="不只給答案，更給方向", cap_fs=42,
            sup="告訴你什麼值得做——為你好。",
            trust="20+ 國家的 iOS 使用者信賴之選"),
}

# ---- BESPOKE data per locale ----
BESP = {
 "es": dict(hl=[("La única IA que",W,0),("crea funciones",W,0),("para cada",W,0),("cliente diamante.",ACC_B,0)],
            cap="HECHO A MEDIDA PARA TI", cap_fs=44,
            sup="Dinos qué quieres más y lo creamos para ti.",
            trust="La eligen usuarios de iOS en 20+ países"),
 "fr": dict(hl=[("La seule IA qui",W,0),("crée des fonctions",W,0),("pour chaque",W,0),("client diamant.",ACC_B,0)],
            cap="SUR MESURE, RIEN QUE POUR VOUS", cap_fs=38,
            sup="Dites-nous ce que vous voulez — on le crée pour vous.",
            trust="Adoptée par des utilisateurs iOS dans 20+ pays"),
 "ja": dict(hl=[("ダイヤモンド",W,0),("顧客一人ひとりに",W,0),("機能を作る",W,0),("唯一のAI。",ACC_B,0)],
            cap="あなただけのために", cap_fs=44,
            sup="欲しい機能を、私たちが形にします。",
            trust="20か国以上のiOSユーザーに信頼されています"),
 "zh-cn": dict(hl=[("唯一为每位",W,0),("钻石客户定制",W,0),("功能的 AI。",ACC_B,0)],
            cap="为你量身打造", cap_fs=44,
            sup="告诉我们你最想要的，我们为你打造。",
            trust="20+ 国家的 iOS 用户信赖之选"),
 "zh-tw": dict(hl=[("唯一為每位",W,0),("鑽石客戶訂製",W,0),("功能的 AI。",ACC_B,0)],
            cap="為你量身打造", cap_fs=44,
            sup="告訴我們你最想要的，我們為你打造。",
            trust="20+ 國家的 iOS 使用者信賴之選"),
}

BRAND = {"es": "NoArk — Memoria Infinita", "fr": "NoArk — Mémoire Infinie",
         "ja": "NoArk — 無限の記憶", "zh-cn": "NoArk — 无限记忆",
         "zh-tw": "NoArk — 無限記憶"}

CJK_LOCALES = {"ja", "zh-cn", "zh-tw"}
n = 0
for loc, d in PRIV.items():
    d["brand"] = BRAND[loc]
    open(f"noark-reddit-privacy-1080x1350-{loc}.svg", "w", encoding="utf-8").write(privacy_svg(d, loc in CJK_LOCALES)); n += 1
for loc, d in GUID.items():
    d["brand"] = BRAND[loc]
    open(f"noark-reddit-guidance-1080x1350-{loc}.svg", "w", encoding="utf-8").write(guidance_svg(d, loc in CJK_LOCALES)); n += 1
for loc, d in BESP.items():
    d["brand"] = BRAND[loc]
    open(f"noark-reddit-bespoke-1080x1350-{loc}.svg", "w", encoding="utf-8").write(bespoke_svg(d, loc in CJK_LOCALES)); n += 1
print("wrote", n, "svgs")
