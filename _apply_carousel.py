#!/usr/bin/env python3
# Replaces the single wisest-minds screenshot in the #wisest-minds section with a
# thumb-swipeable carousel of the 4 Reddit covers, on all 6 localized homepages.

APPSTORE = "https://apps.apple.com/us/app/noark-infinity-memory/id6747843100"

FILES = {
 "en":    "index.html",
 "es":    "es/index.html",
 "fr":    "fr/index.html",
 "ja":    "ja/index.html",
 "zh-cn": "zh-cn/index.html",
 "zh-tw": "zh-tw/index.html",
}

ARIA = {
 "en": "View NoArk — Infinity Memory on the App Store",
 "es": "Ver NoArk — Infinity Memory en el App Store",
 "fr": "Voir NoArk — Infinity Memory sur l'App Store",
 "ja": "App Store で NoArk — Infinity Memory を見る",
 "zh-cn": "在 App Store 查看 NoArk — 无限记忆",
 "zh-tw": "在 App Store 查看 NoArk — 無限記憶",
}

HINT = {
 "en": "Swipe to explore &rarr;",
 "es": "Desliza para explorar &rarr;",
 "fr": "Faites glisser pour explorer &rarr;",
 "ja": "スワイプして見る &rarr;",
 "zh-cn": "滑动查看更多 &rarr;",
 "zh-tw": "滑動查看更多 &rarr;",
}

# alt text per theme per locale
ALT = {
 "wisest-minds": {
  "en": "When life feels confusing, don't figure it out alone. Ask the wisest minds in history — Munger, Jobs, Einstein, da Vinci, Aurelius and 30+ more — in the NoArk app.",
  "es": "Cuando la vida se vuelve confusa, no lo afrontes a solas. Pregunta a las mentes más sabias de la historia — Munger, Jobs, Einstein, da Vinci, Aurelio y 30+ más — en la app NoArk.",
  "fr": "Quand la vie devient confuse, ne restez pas seul face à ça. Demandez aux plus grands esprits de l'histoire — Munger, Jobs, Einstein, de Vinci, Aurèle et 30+ autres — dans l'app NoArk.",
  "ja": "人生に迷ったとき、ひとりで抱え込まないで。歴史上の賢人たち（マンガー、ジョブズ、アインシュタイン、他30名以上）に、NoArkアプリで聞いてみよう。",
  "zh-cn": "当生活陷入迷茫，别一个人去面对。在 NoArk 应用中请教历史上最智慧的人——芒格、乔布斯、爱因斯坦、达·芬奇等 30+ 位。",
  "zh-tw": "當生活陷入迷惘，別獨自面對。在 NoArk 應用程式中請教歷史上最有智慧的人——蒙格、賈伯斯、愛因斯坦、達文西、奧理略等 30+ 位。",
 },
 "privacy": {
  "en": "The only AI that never stores or sells your data. End-to-end encrypted. No tracking, no ads, no selling. Ever.",
  "es": "La única IA que nunca guarda ni vende tus datos. Cifrado de extremo a extremo. Sin rastreo, sin anuncios, sin venta. Nunca.",
  "fr": "La seule IA qui ne stocke ni ne vend vos données. Chiffré de bout en bout. Aucun pistage, aucune pub, aucune vente. Jamais.",
  "ja": "あなたのデータを保存も販売もしない唯一のAI。エンドツーエンド暗号化。追跡なし、広告なし、販売なし。",
  "zh-cn": "唯一不存储也不出售你数据的 AI。端到端加密。不追踪、无广告、绝不出售。",
  "zh-tw": "唯一不儲存也不出售你資料的 AI。端到端加密。不追蹤、無廣告、絕不出售。",
 },
 "guidance": {
  "en": "Other AIs tell you how. NoArk tells you what to do — guidance, not just answers. It tells you what's worth doing, for your own good.",
  "es": "Otras IA te dicen cómo. NoArk te dice qué hacer — orientación, no solo respuestas. Te dice qué vale la pena hacer, por tu propio bien.",
  "fr": "Les autres IA disent comment. NoArk vous dit quoi faire — des conseils, pas que des réponses. Il vous dit ce qui compte, pour votre bien.",
  "ja": "他のAIはやり方を教える。NoArkは進む道を教える——答えだけでなく、導きを。本当にすべきことを、あなたのために。",
  "zh-cn": "别的 AI 只教你怎么做。NoArk 告诉你该做什么——不止给答案，更给方向。告诉你什么值得做，为你好。",
  "zh-tw": "別的 AI 只教你怎麼做。NoArk 告訴你該做什麼——不只給答案，更給方向。告訴你什麼值得做，為你好。",
 },
 "bespoke": {
  "en": "The only AI that builds features for every diamond customer — bespoke, built for you. Tell us what you want most, we build it for you.",
  "es": "La única IA que crea funciones para cada cliente diamante — hecho a medida para ti. Dinos qué quieres más y lo creamos para ti.",
  "fr": "La seule IA qui crée des fonctions pour chaque client diamant — sur mesure, rien que pour vous. Dites-nous ce que vous voulez, on le crée pour vous.",
  "ja": "ダイヤモンド顧客一人ひとりに機能を作る唯一のAI——あなただけのために。欲しい機能を、私たちが形にします。",
  "zh-cn": "唯一为每位钻石客户定制功能的 AI——为你量身打造。告诉我们你最想要的，我们为你打造。",
  "zh-tw": "唯一為每位鑽石客戶訂製功能的 AI——為你量身打造。告訴我們你最想要的，我們為你打造。",
 },
}

ORDER = ["wisest-minds", "privacy", "guidance", "bespoke"]

OLD_OPEN = '<div style="display: flex; justify-content: center; margin: 0 auto 48px;">'

def esc_attr(s):
    return s.replace("&", "&amp;").replace('"', "&quot;")

def slide(theme, loc):
    alt = esc_attr(ALT[theme][loc])
    aria = esc_attr(ARIA[loc])
    src = f"/noark-reddit-{theme}-1080x1350-{loc}.png"
    return (
        f'                    <a href="{APPSTORE}" target="_blank" rel="noopener noreferrer" aria-label="{aria}" style="flex: 0 0 auto; scroll-snap-align: center;">\n'
        f'                        <img src="{src}" alt="{alt}" width="1080" height="1350" loading="lazy" style="display: block; width: 270px; max-width: 72vw; height: auto; border-radius: 24px; border: 1px solid var(--hairline); box-shadow: 0 18px 50px rgba(0,0,0,0.28);">\n'
        f'                    </a>'
    )

def block(loc):
    slides = "\n".join(slide(t, loc) for t in ORDER)
    return (
        '            <style>.reddit-carousel{scrollbar-width:none}.reddit-carousel::-webkit-scrollbar{display:none}</style>\n'
        '            <div style="max-width: 980px; margin: 0 auto 14px;">\n'
        '                <div class="reddit-carousel" style="display: flex; gap: 18px; overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; padding: 6px 4px 16px;">\n'
        f'{slides}\n'
        '                </div>\n'
        '            </div>\n'
        f'            <p style="text-align: center; margin: 0 auto 48px; color: var(--text-secondary); font-size: 0.95em;">{HINT[loc]}</p>'
    )

for loc, path in FILES.items():
    lines = open(path, encoding="utf-8").read().split("\n")
    start = None
    for i, ln in enumerate(lines):
        if ln.strip() == OLD_OPEN:
            start = i
            break
    if start is None:
        raise SystemExit(f"open div not found in {path}")
    # block is exactly 5 lines: div, a, img, /a, /div
    if lines[start + 4].strip() != "</div>":
        raise SystemExit(f"unexpected block shape in {path}: {lines[start+4]!r}")
    indent = lines[start][: len(lines[start]) - len(lines[start].lstrip())]
    new_lines = lines[:start] + block(loc).split("\n") + lines[start + 5:]
    open(path, "w", encoding="utf-8").write("\n".join(new_lines))
    print("updated", path)
