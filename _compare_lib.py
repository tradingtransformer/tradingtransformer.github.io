"""Generator for 'NoArk vs <competitor>' comparison pages.

Reuses each locale's existing noark-vs-apple-intelligence.html for all shared,
already-localized chrome (style, nav, gtag, favicon, CTA, footer, tracking scripts)
so new pages are byte-for-byte consistent. Only the SEO head, JSON-LD, and the
article body are authored per competitor.
"""
import re, json, os

BASE = "https://www.tradingtransformer.com/"

# prefix -> (html lang attr, JSON-LD inLanguage, breadcrumb home name)
LOC = {
    "":      ("en",    None,      "NoArk — Infinity Memory"),
    "es":    ("es",    "es",      "NoArk — Infinity Memory"),
    "fr":    ("fr",    "fr",      "NoArk — Infinity Memory"),
    "ja":    ("ja",    "ja",      "NoArk — Infinity Memory"),
    "zh-cn": ("zh-CN", "zh-CN",   "NoArk — 无限记忆"),
    "zh-tw": ("zh-TW", "zh-TW",   "NoArk — 無限記憶"),
}
HREFLANG = [("en",""),("es","es"),("zh-Hans","zh-cn"),("zh-Hant","zh-tw"),("fr","fr"),("ja","ja")]

# Localized "Keep reading" cross-link to the question-shaped GEO page, injected
# into every comparison page's related list (except that page itself).
WHATTODO_SLUG = "which-ai-tells-you-what-to-do.html"
WHATTODO_LINK = {
    "":      ("/which-ai-tells-you-what-to-do.html", "Which AI tells you what to do, not just how?"),
    "es":    ("/es/which-ai-tells-you-what-to-do.html", "¿Qué IA te dice qué hacer, no solo cómo?"),
    "fr":    ("/fr/which-ai-tells-you-what-to-do.html", "Quelle IA vous dit quoi faire, pas seulement comment ?"),
    "ja":    ("/ja/which-ai-tells-you-what-to-do.html", "「どうやるか」でなく「何をすべきか」を教えるAIは？"),
    "zh-cn": ("/zh-cn/which-ai-tells-you-what-to-do.html", "哪款 AI 告诉你该做什么，而不只是怎么做？"),
    "zh-tw": ("/zh-tw/which-ai-tells-you-what-to-do.html", "哪款 AI 告訴你該做什麼，而不只是怎麼做？"),
}

# Localized heading for the visible FAQ section (keyed by prefix)
FAQ_HEADING = {
    "":      "Frequently asked questions",
    "es":    "Preguntas frecuentes",
    "fr":    "Questions fréquentes",
    "ja":    "よくある質問",
    "zh-cn": "常见问题",
    "zh-tw": "常見問題",
}

# Self-contained styling for the visible FAQ accordions (uses page CSS vars).
FAQ_STYLE = '''<style>
.faq{max-width:760px;margin:8px auto 0}
.faq-item{border-bottom:1px solid var(--hairline)}
.faq-item summary{cursor:pointer;list-style:none;padding:18px 0;font-weight:600;font-size:1.05em;color:var(--text);display:flex;justify-content:space-between;align-items:center;gap:16px}
.faq-item summary::-webkit-details-marker{display:none}
.faq-item summary::after{content:"+";font-size:1.4em;color:var(--accent);font-weight:400;line-height:1}
.faq-item[open] summary::after{content:"\\2013"}
.faq-a{padding:0 0 18px;color:var(--text-secondary);line-height:1.65}
.faq-a p{margin:0 0 10px}
.faq-a p:last-child{margin-bottom:0}
</style>'''


def _extract(prefix):
    """Pull reusable blocks from the locale's Apple Intelligence page."""
    path = (prefix + "/" if prefix else "") + "noark-vs-apple-intelligence.html"
    s = open(path, encoding="utf-8").read()
    def grab(pat):
        m = re.search(pat, s, re.S)
        if not m:
            raise SystemExit(f"pattern not found in {path}: {pat[:40]}")
        return m.group(1)
    return {
        "style":  grab(r'(<style>.*?</style>)'),
        "nav":    grab(r'(<header class="site-nav">.*?</header>)'),
        "gtag":   grab(r'(<!-- Google tag \(gtag\.js\) -->.*?)\n\n    <!-- Structured Data: Article'),
        "favicon":grab(r'(<!-- Favicon -->.*?)\n\n    <!-- Multilingual switcher -->'),
        "cta":    grab(r'(<div class="cta">.*?</div>)'),
        "footer": grab(r'(<footer>.*?</footer>)'),
        "tail":   grab(r'(<!-- Reddit Pixel -->.*?)</body>'),
    }


def _abs(prefix, slug):
    return f"{BASE}{prefix + '/' if prefix else ''}{slug}"


def _hreflang_block(slug, prefixes=None):
    # Only emit hreflang alternates for locales that actually exist (prefixes),
    # so English-first pages don't point at not-yet-built localized URLs.
    out = [f'    <link rel="canonical" href="{{CANON}}">']
    for code, pfx in HREFLANG:
        if prefixes is not None and pfx not in prefixes:
            continue
        out.append(f'    <link rel="alternate" hreflang="{code}" href="{_abs(pfx, slug)}">')
    out.append(f'    <link rel="alternate" hreflang="x-default" href="{_abs("", slug)}">')
    return "\n".join(out)


def _jsonld(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2)


def render(slug, competitor_display, content):
    """content: dict prefix -> field dict. Writes one file per locale."""
    present = set(content.keys())
    for prefix, c in content.items():
        lang, inlang, home_name = LOC[prefix]
        b = _extract(prefix)
        canon = _abs(prefix, slug)
        home_url = BASE + (prefix + "/" if prefix else "")

        # --- table rows ---
        rows = ""
        for feat, noark, comp in c["rows"]:
            rows += (f'                    <tr>\n'
                     f'                        <td>{feat}</td>\n'
                     f'                        <td>{noark}</td>\n'
                     f'                        <td>{comp}</td>\n'
                     f'                    </tr>\n')

        # --- sections ---
        secs = ""
        for h2, paras in c["sections"]:
            secs += f'            <h2>{h2}</h2>\n'
            for p in paras:
                # block-level HTML (lists, figures, style) is emitted raw, not wrapped in <p>
                if p.lstrip().startswith(("<ul", "<ol", "<div", "<figure", "<style", "<table")):
                    secs += f'            {p}\n'
                else:
                    secs += f'            <p>{p}</p>\n'

        # --- related (auto-inject the GEO cross-link, except on that page itself) ---
        related = list(c["related"])
        wt = WHATTODO_LINK.get(prefix)
        if wt and slug != WHATTODO_SLUG and wt[0] not in [r[0] for r in related]:
            related.insert(1, wt)
        rel = f'            <div class="related">\n                <h2>{c["related_heading"]}</h2>\n                <ul>\n'
        for href, label in related:
            rel += f'                    <li><a href="{href}">{label}</a></li>\n'
        rel += '                </ul>\n            </div>'

        # --- visible FAQ (mirrors the FAQPage JSON-LD) ---
        faq_heading = FAQ_HEADING.get(prefix, "Frequently asked questions")
        faq_html = (f'            {FAQ_STYLE}\n'
                    f'            <h2 id="faq">{faq_heading}</h2>\n'
                    f'            <div class="faq">\n')
        for q, a in c["faq"]:
            faq_html += (f'                <details class="faq-item">\n'
                         f'                    <summary>{q}</summary>\n'
                         f'                    <div class="faq-a"><p>{a}</p></div>\n'
                         f'                </details>\n')
        faq_html += '            </div>'

        # --- JSON-LD ---
        article = {
            "@context": "https://schema.org", "@type": "Article",
            "headline": c["title"], "description": c["ogdesc"],
            "image": BASE + "og-image.jpg",
            "author": {"@type": "Organization", "name": "TradingTransformer Technologies LLC", "url": BASE},
            "publisher": {"@type": "Organization", "name": "TradingTransformer Technologies LLC",
                          "logo": {"@type": "ImageObject", "url": BASE + "wswai.jpeg"}},
            "datePublished": "2026-06-14", "dateModified": "2026-06-14",
            "mainEntityOfPage": canon,
        }
        if inlang:
            article["inLanguage"] = inlang
        faqpage = {"@context": "https://schema.org", "@type": "FAQPage"}
        if inlang:
            faqpage["inLanguage"] = inlang
        faqpage["mainEntity"] = [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faq"]
        ]
        crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList",
                 "itemListElement": [
                     {"@type": "ListItem", "position": 1, "name": home_name, "item": home_url},
                     {"@type": "ListItem", "position": 2, "name": c["h1"], "item": canon},
                 ]}

        head_seo = f'''    <!-- SEO Meta Tags -->
    <title>{c["title"]}</title>
    <meta name="description" content="{c["desc"]}">
    <meta name="keywords" content="{c["keywords"]}">
    <meta name="author" content="TradingTransformer Technologies LLC">
    <meta name="robots" content="index, follow">
{_hreflang_block(slug, present).replace("{CANON}", canon)}

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="{canon}">
    <meta property="og:title" content="{c["title"]}">
    <meta property="og:description" content="{c["ogdesc"]}">
    <meta property="og:image" content="{BASE}og-image.jpg">
    <meta property="og:site_name" content="TradingTransformer Technologies LLC">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:site" content="@ws_ai_agents">
    <meta property="twitter:creator" content="@ws_ai_agents">
    <meta property="twitter:url" content="{canon}">
    <meta property="twitter:title" content="{c["title"]}">
    <meta property="twitter:description" content="{c["twdesc"]}">
    <meta property="twitter:image" content="{BASE}og-image.jpg">'''

        html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

{head_seo}

    {b["favicon"]}

    <!-- Multilingual switcher -->
    <script src="/lang-switcher.js" defer></script>
    <meta name="theme-color" content="#ffffff">

    {b["gtag"]}

    <!-- Structured Data: Article (JSON-LD) -->
    <script type="application/ld+json">
{_jsonld(article)}
    </script>

    <!-- Structured Data: FAQPage (JSON-LD) -->
    <script type="application/ld+json">
{_jsonld(faqpage)}
    </script>

    <!-- Structured Data: Breadcrumbs (JSON-LD) -->
    <script type="application/ld+json">
{_jsonld(crumb)}
    </script>

    {b["style"]}
</head>
<body>
    {b["nav"]}

    <article>
        <div class="container">
            <h1>{c["h1"]}</h1>
            <p class="subtitle">{c["subtitle"]}</p>

            <p>{c["intro"]}</p>

            <h2>{c["glance"]}</h2>
            <table class="compare">
                <thead>
                    <tr><th>&nbsp;</th><th>{c["col_noark"]}</th><th>{c.get("col_comp", competitor_display)}</th></tr>
                </thead>
                <tbody>
{rows}                </tbody>
            </table>
            <p class="table-note">{c["note"]}</p>

{secs}
{faq_html}

            {b["cta"]}

{rel}
        </div>
    </article>

    {b["footer"]}

    {b["tail"]}</body>
</html>
'''
        out = (prefix + "/" if prefix else "") + slug
        open(out, "w", encoding="utf-8").write(html)
        print("wrote", out)
