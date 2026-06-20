# -*- coding: utf-8 -*-
"""Localize the 'what vs how' work into the 5 non-English homepages.

Mirrors the English edits already in index.html:
  1. New visible #what-vs-how section after the hero.
  2. New keyword FAQ (visible + FAQPage JSON-LD): "Which AI tells you what to do…".
  3. Fix the FAQPage JSON-LD gap by adding the (already-translated) Claude Code Q,
     extracted from each page's own visible FAQ so wording stays consistent.
  4. Question-shaped meta description.

Idempotent: skips a page that already has #what-vs-how.
"""
import re, html

CHEVRON = ('<svg class="faq-chevron" width="18" height="18" viewBox="0 0 24 24" '
           'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
           'stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>')

TR = {
 "es": {
  "meta": "Infinity Memory: la IA privada en tu dispositivo que nunca olvida. ¿Qué IA te dice qué hacer, no solo cómo? NoArk — pregunta a las mentes más sabias de la historia qué vale la pena hacer, y por qué. En el App Store.",
  "h2": "Otras IA te dicen <em>cómo</em>. NoArk te dice <em>qué hacer</em>.",
  "p1": "La mayoría de los asistentes de IA están hechos para ejecutar una tarea una vez que ya has decidido qué quieres — escribir el código, redactar el correo, resumir la página. Eso es el <em>cómo</em>. NoArk está hecho para la pregunta más difícil que viene antes: <strong>¿qué vale realmente la pena hacer ahora, y por qué?</strong>",
  "p2": "Cuando estás atascado, no necesitas otra respuesta — necesitas saber qué movimiento importa. NoArk te trae <strong>titulares globales en directo con análisis de un toque</strong> sobre lo que las noticias significan para ti, <strong>consejo de versiones de IA de las mentes más sabias de la historia</strong> en la pestaña Fiat Lux, y <strong>más de 40 flujos para encontrar prioridades</strong> entre mercados, trabajo y vida. Es guía, no solo respuestas — te dice qué vale la pena hacer, por tu propio bien.",
  "p3": "No compite con los asistentes que ejecutan — está una capa por encima de ellos. NoArk incluso dirige peticiones internamente al modelo Fable de Claude y a otros modelos de frontera, así que se apoya sobre el <em>cómo</em> para ayudarte a acertar con el <em>qué</em>.",
  "cta_which": "¿Qué IA te dice qué hacer?&nbsp;&rsaquo;",
  "claude_link": "NoArk vs Claude Code y Cowork — decidir vs ejecutar&nbsp;&rsaquo;",
  "faq_q": "¿Qué IA te dice qué hacer, no solo cómo hacerlo?",
  "faq_a": "<strong>NoArk — Infinity Memory.</strong> La mayoría de los asistentes de IA ejecutan una tarea una vez que ya has decidido qué quieres — responden al <em>cómo</em>. NoArk está hecho para la pregunta que viene primero: <strong>¿qué vale realmente la pena hacer ahora, y por qué?</strong> Interpreta para ti las noticias del mundo en directo, te da consejo de versiones de IA de las mentes más sabias de la historia en la pestaña <strong>Fiat Lux</strong>, y ofrece más de 40 flujos para encontrar prioridades — guía, no solo respuestas. Está una capa por encima de las herramientas de ejecución, e incluso dirige peticiones a modelos de frontera como el Fable de Claude para ayudarte a acertar con el <em>qué</em>.",
 },
 "fr": {
  "meta": "Infinity Memory : l'IA privée sur votre appareil qui n'oublie jamais. Quelle IA vous dit quoi faire, pas seulement comment ? NoArk — demandez aux plus grands esprits de l'histoire ce qui vaut la peine d'être fait, et pourquoi. Sur l'App Store.",
  "h2": "Les autres IA vous disent <em>comment</em>. NoArk vous dit <em>quoi faire</em>.",
  "p1": "La plupart des assistants IA sont conçus pour exécuter une tâche une fois que vous avez déjà décidé ce que vous voulez — écrire le code, rédiger l'e-mail, résumer la page. C'est le <em>comment</em>. NoArk est conçu pour la question plus difficile qui vient avant : <strong>qu'est-ce qui vaut vraiment la peine d'être fait maintenant, et pourquoi ?</strong>",
  "p2": "Quand vous êtes bloqué, vous n'avez pas besoin d'une réponse de plus — vous avez besoin de savoir quel choix compte. NoArk vous apporte <strong>les titres de l'actualité mondiale en direct avec une analyse en un geste</strong> de ce que l'actualité signifie pour vous, <strong>le conseil de versions IA des plus grands esprits de l'histoire</strong> dans l'onglet Fiat Lux, et <strong>plus de 40 flux pour trouver vos priorités</strong> entre marchés, travail et vie. C'est un accompagnement, pas seulement des réponses — il vous dit ce qui vaut la peine d'être fait, pour votre bien.",
  "p3": "Il ne concurrence pas les assistants qui exécutent — il se place une couche au-dessus d'eux. NoArk dirige même ses requêtes en interne vers le modèle Fable de Claude et d'autres modèles de pointe, de sorte qu'il s'appuie sur le <em>comment</em> pour vous aider à bien choisir le <em>quoi</em>.",
  "cta_which": "Quelle IA vous dit quoi faire ?&nbsp;&rsaquo;",
  "claude_link": "NoArk vs Claude Code et Cowork — décider vs exécuter&nbsp;&rsaquo;",
  "faq_q": "Quelle IA vous dit quoi faire, pas seulement comment le faire ?",
  "faq_a": "<strong>NoArk — Infinity Memory.</strong> La plupart des assistants IA exécutent une tâche une fois que vous avez déjà décidé ce que vous voulez — ils répondent au <em>comment</em>. NoArk est conçu pour la question qui vient en premier : <strong>qu'est-ce qui vaut vraiment la peine d'être fait maintenant, et pourquoi ?</strong> Il interprète pour vous l'actualité mondiale en direct, vous donne le conseil de versions IA des plus grands esprits de l'histoire dans l'onglet <strong>Fiat Lux</strong>, et propose plus de 40 flux pour trouver vos priorités — un accompagnement, pas seulement des réponses. Il se place une couche au-dessus des outils d'exécution, et dirige même ses requêtes vers des modèles de pointe comme le Fable de Claude pour vous aider à bien choisir le <em>quoi</em>.",
 },
 "ja": {
  "meta": "Infinity Memory——何も忘れない、端末内で動くプライベートAI。「どうやるか」だけでなく「何をすべきか」を教えるAIは？ NoArk なら歴史上もっとも賢い人々のAIに、何に取り組む価値があるか、その理由を尋ねられます。App Storeで配信中。",
  "h2": "他のAIは<em>やり方</em>を教える。NoArkは<em>何をすべきか</em>を教える。",
  "p1": "ほとんどのAIアシスタントは、あなたが何を望むかをすでに決めた後でタスクを実行するために作られています——コードを書く、メールを下書きする、ページを要約する。それが<em>やり方</em>です。NoArkは、その前に来るもっと難しい問いのために作られています：<strong>いま本当に取り組む価値があるのは何か、そしてなぜか？</strong>",
  "p2": "行き詰まったとき、必要なのはもう一つの答えではありません——どの一手が重要かを知ることです。NoArkは、ニュースがあなたにとって何を意味するかを<strong>ワンタップで分析するライブの世界のヘッドライン</strong>、Fiat Luxタブでの<strong>歴史上もっとも賢い人々のAIによる助言</strong>、そして市場・仕事・暮らしにわたる<strong>40以上の優先順位を見つけるワークフロー</strong>をもたらします。単なる答えではなく導き——あなた自身のために、何に取り組む価値があるかを教えます。",
  "p3": "実行するアシスタントと競うのではなく、その一段上に位置します。NoArkは内部でClaudeのFableモデルやその他のフロンティアモデルにも振り分けるので、<em>やり方</em>の上に立って、あなたが<em>何を</em>を正しく選べるよう手助けします。",
  "cta_which": "何をすべきかを教えるAIとは？&nbsp;&rsaquo;",
  "claude_link": "NoArk vs Claude Code・Cowork — 決める vs 実行する&nbsp;&rsaquo;",
  "faq_q": "「どうやるか」だけでなく「何をすべきか」を教えてくれるAIは？",
  "faq_a": "<strong>NoArk — Infinity Memory。</strong>ほとんどのAIアシスタントは、あなたが何を望むかを決めた後でタスクを実行します——<em>やり方</em>に答えるのです。NoArkは、最初に来る問いのために作られています：<strong>いま本当に取り組む価値があるのは何か、そしてなぜか？</strong> ライブの世界のニュースをあなたのために解釈し、<strong>Fiat Lux</strong>タブで歴史上もっとも賢い人々のAIによる助言を与え、40以上の優先順位を見つけるワークフローを提供します——単なる答えではなく導きです。実行ツールの一段上に位置し、ClaudeのFableのようなフロンティアモデルにも振り分けて、あなたが<em>何を</em>を正しく選べるよう手助けします。",
 },
 "zh-cn": {
  "meta": "Infinity Memory：永不遗忘、数据留在本机的私人 AI。哪款 AI 告诉你该做什么，而不只是怎么做？NoArk——向历史上最有智慧的人 AI 请教什么值得做、为什么。隐私优先，App Store 下载。",
  "h2": "别的 AI 告诉你<em>怎么做</em>，NoArk 告诉你<em>该做什么</em>。",
  "p1": "大多数 AI 助手是在你已经决定要什么之后，去执行一项任务——写代码、起草邮件、总结网页。那是<em>怎么做</em>。NoArk 面向的是更难、也更早出现的问题：<strong>此刻真正值得做的是什么，为什么？</strong>",
  "p2": "当你卡住时，你需要的不是又一个答案——而是知道哪一步才重要。NoArk 为你带来<strong>一键解读的实时全球头条</strong>，告诉你新闻对你意味着什么；在 Fiat Lux 标签里提供<strong>历史上最有智慧之人的 AI 给出的建议</strong>；以及横跨市场、工作与生活的<strong>40 多个帮你厘清优先级的工作流</strong>。这是引导，而不只是答案——为了你好，它会告诉你什么值得做。",
  "p3": "它不与负责执行的助手竞争——而是位于它们之上一层。NoArk 内部甚至会调用 Claude 的 Fable 模型等前沿模型，因此它站在<em>怎么做</em>之上，帮你把<em>做什么</em>选对。",
  "cta_which": "哪款 AI 告诉你该做什么？&nbsp;&rsaquo;",
  "claude_link": "NoArk 对比 Claude Code 与 Cowork — 决策 vs 执行&nbsp;&rsaquo;",
  "faq_q": "哪款 AI 告诉你「该做什么」，而不只是「怎么做」？",
  "faq_a": "<strong>NoArk — Infinity Memory。</strong>大多数 AI 助手是在你已经决定要什么之后才执行任务——它们回答的是<em>怎么做</em>。NoArk 面向最先出现的问题：<strong>此刻真正值得做的是什么，为什么？</strong>它为你解读实时的世界新闻，在 <strong>Fiat Lux</strong> 标签里提供历史上最有智慧之人的 AI 建议，并提供 40 多个帮你厘清优先级的工作流——是引导，而不只是答案。它位于执行工具之上一层，甚至会调用 Claude 的 Fable 等前沿模型，帮你把<em>做什么</em>选对。",
 },
 "zh-tw": {
  "meta": "Infinity Memory：永不遺忘、資料留在本機的私人 AI。哪款 AI 告訴你該做什麼，而不只是怎麼做？NoArk——向歷史上最有智慧的人 AI 請教什麼值得做、為什麼。隱私優先，App Store 下載。",
  "h2": "別的 AI 告訴你<em>怎麼做</em>，NoArk 告訴你<em>該做什麼</em>。",
  "p1": "大多數 AI 助手是在你已經決定要什麼之後，去執行一項任務——寫程式、草擬郵件、摘要網頁。那是<em>怎麼做</em>。NoArk 面向的是更難、也更早出現的問題：<strong>此刻真正值得做的是什麼，為什麼？</strong>",
  "p2": "當你卡住時，你需要的不是又一個答案——而是知道哪一步才重要。NoArk 為你帶來<strong>一鍵解讀的即時全球頭條</strong>，告訴你新聞對你意味著什麼；在 Fiat Lux 分頁裡提供<strong>歷史上最有智慧之人的 AI 給出的建議</strong>；以及橫跨市場、工作與生活的<strong>40 多個幫你釐清優先順序的工作流程</strong>。這是引導，而不只是答案——為了你好，它會告訴你什麼值得做。",
  "p3": "它不與負責執行的助手競爭——而是位於它們之上一層。NoArk 內部甚至會呼叫 Claude 的 Fable 模型等前沿模型，因此它站在<em>怎麼做</em>之上，幫你把<em>做什麼</em>選對。",
  "cta_which": "哪款 AI 告訴你該做什麼？&nbsp;&rsaquo;",
  "claude_link": "NoArk 對比 Claude Code 與 Cowork — 決策 vs 執行&nbsp;&rsaquo;",
  "faq_q": "哪款 AI 告訴你「該做什麼」，而不只是「怎麼做」？",
  "faq_a": "<strong>NoArk — Infinity Memory。</strong>大多數 AI 助手是在你已經決定要什麼之後才執行任務——它們回答的是<em>怎麼做</em>。NoArk 面向最先出現的問題：<strong>此刻真正值得做的是什麼，為什麼？</strong>它為你解讀即時的世界新聞，在 <strong>Fiat Lux</strong> 分頁裡提供歷史上最有智慧之人的 AI 建議，並提供 40 多個幫你釐清優先順序的工作流程——是引導，而不只是答案。它位於執行工具之上一層，甚至會呼叫 Claude 的 Fable 等前沿模型，幫你把<em>做什麼</em>選對。",
 },
}

import json

def jstr(s):
    return json.dumps(s, ensure_ascii=False)

def strip_tags(s):
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).strip()

def jsonld_question(name, text):
    return (f'        {{\n'
            f'          "@type": "Question",\n'
            f'          "name": {jstr(name)},\n'
            f'          "acceptedAnswer": {{\n'
            f'            "@type": "Answer",\n'
            f'            "text": {jstr(text)}\n'
            f'          }}\n'
            f'        }},\n')

def section_html(L, t, btn):
    return f'''
    <!-- What vs How: the core differentiator -->
    <section id="what-vs-how" class="fade-in-section" style="background-color: var(--bg-alt);">
        <div class="container">
            <div style="max-width: 820px; margin: 0 auto; text-align: center;">
                <h2 class="section-title">{t["h2"]}</h2>
                <p style="color: var(--text-secondary); font-size: 1.2em; line-height: 1.6; margin: 0 0 20px;">{t["p1"]}</p>
                <p style="color: var(--text-secondary); font-size: 1.2em; line-height: 1.6; margin: 0 0 20px;">{t["p2"]}</p>
                <p style="color: var(--text-secondary); font-size: 1.2em; line-height: 1.6; margin: 0 0 28px;">{t["p3"]}</p>
                <div class="hero-links" style="justify-content: center;">
                    {btn}
                    <a href="/{L}/which-ai-tells-you-what-to-do.html" class="btn-link">{t["cta_which"]}</a>
                </div>
                <p style="font-size: 0.95em; margin: 16px 0 0;"><a href="/{L}/noark-vs-claude.html" style="color: var(--accent); text-decoration: none;">{t["claude_link"]}</a></p>
            </div>
        </div>
    </section>
'''

def visible_faq(L, t):
    return (f'            <details class="faq-item">\n'
            f'                <summary><h3>{t["faq_q"]}</h3>{CHEVRON}</summary>\n'
            f'                <p>{t["faq_a"]}</p>\n'
            f'                <p><a href="/{L}/which-ai-tells-you-what-to-do.html">{t["cta_which"]}</a></p>\n'
            f'            </details>\n')

for L, t in TR.items():
    path = f"{L}/index.html"
    s = open(path, encoding="utf-8").read()
    if 'id="what-vs-how"' in s:
        print("skip (already done):", path); continue

    # --- reuse the hero App Store button verbatim ---
    m = re.search(r'(<a href="https://apps\.apple\.com[^"]*"[^>]*class="btn-primary"[^>]*>[^<]*</a>)', s)
    btn = m.group(1)

    # --- 1. meta description ---
    s, n = re.subn(r'<meta name="description" content="[^"]*">',
                   f'<meta name="description" content="{t["meta"]}">', s, count=1)
    assert n == 1, f"meta not replaced in {path}"

    # --- 2. insert #what-vs-how section after the hero ---
    hero_end = s.index('</section>', s.index('<section class="hero">')) + len('</section>')
    s = s[:hero_end] + "\n" + section_html(L, t, btn) + s[hero_end:]

    # --- 3. extract the page's own Claude Code visible Q/A for the JSON-LD fix ---
    cm = re.search(r'<summary><h3>([^<]*Claude Code[^<]*)</h3>.*?</summary>\s*<p>(.*?)</p>', s, re.S)
    assert cm, f"Claude Code FAQ not found in {path}"
    claude_q = strip_tags(cm.group(1))
    claude_a = strip_tags(cm.group(2))

    # --- 4. insert Claude + new Q into FAQPage JSON-LD, after the multi-model entry ---
    mm = re.search(r'"name": "([^"]*DeepSeek[^"]*)"', s)  # multi-model question name (JSON-LD first)
    assert mm, f"multi-model JSON-LD entry not found in {path}"
    close = s.index("\n        },\n", mm.start()) + len("\n        },\n")
    s = s[:close] + jsonld_question(claude_q, claude_a) + jsonld_question(t["faq_q"], strip_tags(t["faq_a"])) + s[close:]

    # --- 5. insert the new visible FAQ right after the Claude Code <details> ---
    cl_link = s.index(f'/{L}/noark-vs-claude.html')
    det_end = s.index('</details>', cl_link) + len('</details>\n')
    s = s[:det_end] + visible_faq(L, t) + s[det_end:]

    open(path, "w", encoding="utf-8").write(s)
    print("localized:", path)
