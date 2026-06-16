# -*- coding: utf-8 -*-
from _compare_lib import render

SLUG = "noark-vs-perplexity.html"
COMP = "Perplexity"

def rel(p):
    base = "/" + (p + "/" if p else "")
    return (base,
            base + "noark-vs-chatgpt.html",
            base + "noark-vs-character-ai.html",
            base + "noark-vs-gemini.html",
            base + "noark-vs-apple-intelligence.html",
            base + "#faq",
            base + "#data-privacy")

content = {}

# ---------------- English ----------------
hp, gp, cp, mp, ap, fp, pp = rel("")
content[""] = {
 "title": "NoArk vs Perplexity: Private News Analysis, Not Just Search Answers",
 "desc": "NoArk vs Perplexity compared: news analysis vs search answers, privacy, sign-in, and price. Perplexity is an answer engine; NoArk gives you live global headlines with one-tap interpretation, counsel from history's wisest minds, and a full Apple super app — with no account and every conversation on your own device. Free on iPhone, iPad, Mac & Apple Vision.",
 "keywords": "NoArk vs Perplexity, Perplexity alternative, private Perplexity, private AI search, AI news analysis, live headlines AI, AI without sign-in, on-device AI, Perplexity alternative iPhone, Claude Fable, DeepSeek, free Perplexity alternative",
 "ogdesc": "How NoArk differs from Perplexity: it interprets live headlines instead of just answering search queries, adds counsel from history's wisest minds and a full Apple super app, and keeps every conversation private on your own device with no account.",
 "twdesc": "It interprets live headlines instead of just answering search queries, adds counsel from history's wisest minds and a full Apple super app, and keeps everything private with no account.",
 "h1": "NoArk vs Perplexity",
 "subtitle": "Both turn questions into answers. Only one interprets the news for you, offers counsel from history's wisest minds, and keeps every search private with no account.",
 "intro": "Perplexity is a fast, useful answer engine: it searches the web and hands back a cited summary. <strong>NoArk — Infinity Memory</strong> goes a step further — it brings you <strong>live global headlines with one-tap analysis</strong> that interprets what the news <em>means</em>, adds <strong>counsel from history's wisest minds</strong>, and wraps it in a full Apple super app — all with <strong>no account</strong> and every conversation kept on your own device. Here's the honest comparison.",
 "glance": "At a glance",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("What it's built for", "<span class='yes'>Understanding</span> — live headlines, one-tap analysis, counsel, and 40+ workflows across your life and the markets", "Search — turning a query into a cited web answer"),
  ("News &amp; analysis", "<span class='yes'>Live global headlines</span> with one-tap analysis that interprets what a story means — not just a summary", "Summarized answers with source citations"),
  ("History's wisest minds", "<span class='yes'>Yes</span> — Fiat Lux: AI versions of Charlie Munger, Steve Jobs, Einstein, Marcus Aurelius &amp; 40+ more, grounded in how they actually reasoned", "A general answer engine"),
  ("Your conversations", "<span class='yes'>Stored only on your device</span> and in your own iCloud — never warehoused or used to train", "Sent to the company's servers"),
  ("Data collection", "<span class='yes'>None</span> — Apple's App Privacy label: “Data Not Collected”", "Collects account, usage, and search data"),
  ("Sign-in required", "<span class='yes'>No</span> — no account, email, or phone number", "Requires an account for full use"),
  ("Beyond search", "A full Apple super app — markets, productivity, travel, education &amp; 40+ workflows, on iPhone, iPad, Mac &amp; Vision", "Primarily an answer &amp; research engine"),
  ("Price", "<span class='yes'>Free</span> to download (optional in-app purchases)", "Free tier; paid Pro for more"),
 ],
 "note": "Comparison reflects publicly available information as of June 2026. Perplexity is a trademark of its respective owner; NoArk is an independent app and is not affiliated with or endorsed by it.",
 "sections": [
  ("Analysis, not just answers", [
   "Perplexity is excellent at one thing: you ask, it searches the web and returns a summarized answer with citations. NoArk is built for the next step — <strong>understanding</strong>. Its home surface is a stream of <strong>live global headlines</strong>, and a single tap gives you <strong>analysis that interprets what a story actually means</strong> for you and the markets, drawing on many frontier models — Claude's Fable, DeepSeek, Mistral, Kimi, and Gemini. You don't just get the news; you get a reading of it.",
  ]),
  ("Private by default — no account, nothing collected", [
   "To get the most out of Perplexity you sign in, and your searches are sent to the company's servers. NoArk takes the opposite path: there's <strong>no sign-in</strong> — no email, no phone number — and your conversations are <strong>stored only on your device and in your own iCloud</strong>, never warehoused on our servers and never used to train any model. Apple's official App Privacy label for NoArk reads <a href='" + pp + "'>“Data Not Collected”</a>, the strictest there is. What you search stays yours.",
  ]),
  ("More than an answer engine: counsel + a full super app", [
   "Beyond the headlines, NoArk's <strong>Fiat Lux</strong> tab lets you bring real questions to AI versions of history's wisest minds — Charlie Munger, Steve Jobs, Marcus Aurelius, and 40+ more — grounded in how they actually reasoned. And it's a <strong>full Apple super app</strong> for iPhone, iPad, Mac, and Apple Vision: 40+ ready-made workflows across markets, productivity, travel, education, and life admin, with an investing brain built by the team behind TradingTransformer, inspired by Claude Shannon's vision of AI stock-picking.",
  ]),
 ],
 "related_heading": "Keep reading",
 "related": [
  (hp, "NoArk — Infinity Memory: the intelligent AI OS & super app"),
  (gp, "NoArk vs ChatGPT"),
  (mp, "NoArk vs Google Gemini"),
  (cp, "NoArk vs Character.AI"),
  (ap, "NoArk vs Apple Intelligence"),
  (hp + "noark-vs-manus.html", "NoArk vs Manus"),
  (fp, "Frequently asked questions about NoArk"),
 ],
 "faq": [
  ("Is NoArk a Perplexity alternative?", "Yes, and a broader one. Where Perplexity answers search queries with citations, NoArk gives you live global headlines with one-tap analysis that interprets what the news means, plus counsel from history's wisest minds and 40+ workflows — all with no account and every conversation kept on your own device. Apple labels it “Data Not Collected.”"),
  ("Does NoArk do news analysis?", "Yes. NoArk's home is a stream of live global headlines, and a single tap gives you analysis that interprets what a story means for you and the markets — drawing on many frontier models — rather than just summarizing it."),
  ("Is my search private with NoArk?", "Yes. There's no sign-in and no data collection: your conversations and searches stay on your own device and in your own iCloud, never warehoused on our servers and never used to train models. Apple's App Privacy label reads “Data Not Collected.”"),
  ("Which AI models does NoArk use?", "NoArk routes each request to the best of many frontier models — Anthropic's Claude (Fable), DeepSeek, Mistral, Kimi, and Google's Gemini — instead of relying on a single one."),
  ("Is NoArk free?", "NoArk is free to download on iPhone, iPad, Mac, and Apple Vision, with optional in-app purchases. There's no account and no data collection required to start."),
 ],
}

# ---------------- Spanish ----------------
hp, gp, cp, mp, ap, fp, pp = rel("es")
content["es"] = {
 "title": "NoArk vs Perplexity: análisis de noticias privado, no solo respuestas de búsqueda",
 "desc": "Comparativa NoArk vs Perplexity: análisis de noticias frente a respuestas de búsqueda, privacidad, registro y precio. Perplexity es un motor de respuestas; NoArk te da titulares globales en directo con interpretación de un toque, consejo de las mentes más sabias de la historia y una súper app de Apple — sin cuenta y con cada conversación en tu propio dispositivo. Gratis en iPhone, iPad, Mac y Apple Vision.",
 "keywords": "NoArk vs Perplexity, alternativa a Perplexity, Perplexity privado, búsqueda con IA privada, análisis de noticias con IA, titulares en directo IA, IA sin registro, IA en el dispositivo, alternativa a Perplexity iPhone, Claude Fable, DeepSeek, alternativa gratis a Perplexity",
 "ogdesc": "En qué se diferencia NoArk de Perplexity: interpreta titulares en directo en lugar de solo responder búsquedas, añade consejo de las mentes más sabias de la historia y una súper app de Apple, y mantiene cada conversación privada en tu propio dispositivo, sin cuenta.",
 "twdesc": "Interpreta titulares en directo en vez de solo responder búsquedas, añade consejo de las mentes más sabias y una súper app de Apple, y lo mantiene todo privado sin cuenta.",
 "h1": "NoArk vs Perplexity",
 "subtitle": "Ambos convierten preguntas en respuestas. Solo uno interpreta las noticias por ti, ofrece consejo de las mentes más sabias de la historia y mantiene cada búsqueda privada sin cuenta.",
 "intro": "Perplexity es un motor de respuestas rápido y útil: busca en la web y te devuelve un resumen con citas. <strong>NoArk — Infinity Memory</strong> va un paso más allá — te trae <strong>titulares globales en directo con análisis de un toque</strong> que interpreta lo que <em>significan</em> las noticias, añade <strong>consejo de las mentes más sabias de la historia</strong> y lo envuelve en una súper app de Apple completa — todo <strong>sin cuenta</strong> y con cada conversación en tu propio dispositivo. Esta es la comparación honesta.",
 "glance": "De un vistazo",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("Para qué está hecho", "<span class='yes'>Comprender</span> — titulares en directo, análisis de un toque, consejo y más de 40 flujos de trabajo de tu vida y los mercados", "Buscar — convertir una consulta en una respuesta web con citas"),
  ("Noticias y análisis", "<span class='yes'>Titulares globales en directo</span> con análisis de un toque que interpreta lo que significa una noticia — no solo un resumen", "Respuestas resumidas con citas de fuentes"),
  ("Las mentes más sabias de la historia", "<span class='yes'>Sí</span> — Fiat Lux: versiones de IA de Charlie Munger, Steve Jobs, Einstein, Marco Aurelio y más de 40, basadas en cómo razonaban de verdad", "Un motor de respuestas general"),
  ("Tus conversaciones", "<span class='yes'>Guardadas solo en tu dispositivo</span> y en tu propio iCloud — nunca almacenadas ni usadas para entrenar", "Enviadas a los servidores de la empresa"),
  ("Recopilación de datos", "<span class='yes'>Ninguna</span> — etiqueta de privacidad de Apple: «No se recopilan datos»", "Recopila datos de cuenta, uso y búsquedas"),
  ("Registro obligatorio", "<span class='yes'>No</span> — sin cuenta, correo ni número de teléfono", "Requiere una cuenta para el uso completo"),
  ("Más allá de la búsqueda", "Una súper app de Apple completa — mercados, productividad, viajes, educación y más de 40 flujos de trabajo, en iPhone, iPad, Mac y Vision", "Sobre todo un motor de respuestas e investigación"),
  ("Precio", "<span class='yes'>Gratis</span> (compras opcionales dentro de la app)", "Nivel gratuito; Pro de pago para más"),
 ],
 "note": "Comparativa basada en información pública a junio de 2026. Perplexity es una marca de su titular; NoArk es una app independiente, no afiliada ni respaldada por aquella.",
 "sections": [
  ("Análisis, no solo respuestas", [
   "Perplexity es excelente en una cosa: preguntas, busca en la web y devuelve una respuesta resumida con citas. NoArk está hecho para el paso siguiente — <strong>comprender</strong>. Su pantalla principal es un flujo de <strong>titulares globales en directo</strong>, y un solo toque te da <strong>análisis que interpreta lo que una noticia significa de verdad</strong> para ti y para los mercados, recurriendo a muchos modelos de frontera — Claude Fable, DeepSeek, Mistral, Kimi y Gemini. No solo recibes la noticia; recibes una lectura de ella.",
  ]),
  ("Privado por defecto — sin cuenta, sin recopilar nada", [
   "Para aprovechar Perplexity al máximo inicias sesión, y tus búsquedas se envían a los servidores de la empresa. NoArk hace lo contrario: <strong>no hay registro</strong> — ni correo ni número de teléfono — y tus conversaciones se <strong>guardan solo en tu dispositivo y en tu propio iCloud</strong>, nunca almacenadas en nuestros servidores ni usadas para entrenar ningún modelo. La etiqueta oficial de privacidad de Apple para NoArk dice <a href='" + pp + "'>«No se recopilan datos»</a>, la más estricta que existe. Lo que buscas sigue siendo tuyo.",
  ]),
  ("Más que un motor de respuestas: consejo + una súper app completa", [
   "Más allá de los titulares, la pestaña <strong>Fiat Lux</strong> de NoArk te deja llevar preguntas reales a versiones de IA de las mentes más sabias de la historia — Charlie Munger, Steve Jobs, Marco Aurelio y más de 40 — basadas en cómo razonaban de verdad. Y es una <strong>súper app de Apple completa</strong> para iPhone, iPad, Mac y Apple Vision: más de 40 flujos de trabajo listos que abarcan mercados, productividad, viajes, educación y gestión diaria, con un cerebro inversor creado por el equipo de TradingTransformer, inspirado en la visión de Claude Shannon sobre la IA que elige acciones.",
  ]),
 ],
 "related_heading": "Sigue leyendo",
 "related": [
  (hp, "NoArk — Infinity Memory: el SO inteligente y súper app de IA"),
  (gp, "NoArk vs ChatGPT"),
  (mp, "NoArk vs Google Gemini"),
  (cp, "NoArk vs Character.AI"),
  (ap, "NoArk vs Apple Intelligence"),
  (hp + "noark-vs-manus.html", "NoArk vs Manus"),
  (fp, "Preguntas frecuentes sobre NoArk"),
 ],
 "faq": [
  ("¿Es NoArk una alternativa a Perplexity?", "Sí, y más amplia. Donde Perplexity responde búsquedas con citas, NoArk te da titulares globales en directo con análisis de un toque que interpreta lo que significan las noticias, además de consejo de las mentes más sabias de la historia y más de 40 flujos de trabajo — todo sin cuenta y con cada conversación en tu propio dispositivo. Apple la etiqueta como «No se recopilan datos»."),
  ("¿NoArk hace análisis de noticias?", "Sí. La pantalla principal de NoArk es un flujo de titulares globales en directo, y un solo toque te da análisis que interpreta lo que una noticia significa para ti y para los mercados — recurriendo a muchos modelos de frontera — en lugar de solo resumirla."),
  ("¿Mi búsqueda es privada con NoArk?", "Sí. No hay registro ni recopilación de datos: tus conversaciones y búsquedas se quedan en tu propio dispositivo y en tu propio iCloud, nunca almacenadas en nuestros servidores ni usadas para entrenar modelos. La etiqueta de privacidad de Apple dice «No se recopilan datos»."),
  ("¿Qué modelos de IA usa NoArk?", "NoArk dirige cada petición al mejor de muchos modelos de frontera — Claude (Fable) de Anthropic, DeepSeek, Mistral, Kimi y Gemini de Google — en lugar de depender de uno solo."),
  ("¿Es NoArk gratis?", "NoArk es gratis en iPhone, iPad, Mac y Apple Vision, con compras opcionales dentro de la app. No hace falta cuenta ni recopilación de datos para empezar."),
 ],
}

# ---------------- French ----------------
hp, gp, cp, mp, ap, fp, pp = rel("fr")
content["fr"] = {
 "title": "NoArk vs Perplexity : analyse privée de l'actualité, pas seulement des réponses de recherche",
 "desc": "Comparatif NoArk vs Perplexity : analyse de l'actualité contre réponses de recherche, confidentialité, inscription et prix. Perplexity est un moteur de réponses ; NoArk vous donne l'actualité mondiale en direct avec une interprétation en un geste, le conseil des plus grands esprits de l'histoire et une super app Apple — sans compte et avec chaque conversation sur votre propre appareil. Gratuit sur iPhone, iPad, Mac et Apple Vision.",
 "keywords": "NoArk vs Perplexity, alternative à Perplexity, Perplexity privé, recherche IA privée, analyse d'actualité IA, actualité en direct IA, IA sans inscription, IA sur l'appareil, alternative à Perplexity iPhone, Claude Fable, DeepSeek, alternative gratuite à Perplexity",
 "ogdesc": "En quoi NoArk diffère de Perplexity : elle interprète l'actualité en direct au lieu de simplement répondre aux recherches, ajoute le conseil des plus grands esprits de l'histoire et une super app Apple, et garde chaque conversation privée sur votre propre appareil, sans compte.",
 "twdesc": "Elle interprète l'actualité en direct au lieu de simplement répondre aux recherches, ajoute le conseil des plus grands esprits et une super app Apple, et garde tout privé sans compte.",
 "h1": "NoArk vs Perplexity",
 "subtitle": "Les deux transforment les questions en réponses. Une seule interprète l'actualité pour vous, offre le conseil des plus grands esprits de l'histoire et garde chaque recherche privée, sans compte.",
 "intro": "Perplexity est un moteur de réponses rapide et utile : il cherche sur le web et vous renvoie un résumé sourcé. <strong>NoArk — Infinity Memory</strong> va un cran plus loin — il vous apporte <strong>l'actualité mondiale en direct avec une analyse en un geste</strong> qui interprète ce que l'actualité <em>signifie</em>, ajoute le <strong>conseil des plus grands esprits de l'histoire</strong> et enveloppe le tout dans une super app Apple complète — le tout <strong>sans compte</strong> et avec chaque conversation gardée sur votre propre appareil. Voici la comparaison honnête.",
 "glance": "En un coup d'œil",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("Conçu pour", "<span class='yes'>Comprendre</span> — actualité en direct, analyse en un geste, conseil et plus de 40 flux de travail de votre vie et des marchés", "Chercher — transformer une requête en réponse web sourcée"),
  ("Actualité et analyse", "<span class='yes'>Actualité mondiale en direct</span> avec une analyse en un geste qui interprète ce que signifie une nouvelle — pas qu'un résumé", "Réponses résumées avec citations de sources"),
  ("Les plus grands esprits de l'histoire", "<span class='yes'>Oui</span> — Fiat Lux : des versions IA de Charlie Munger, Steve Jobs, Einstein, Marc Aurèle et plus de 40 autres, ancrées dans leur vraie façon de raisonner", "Un moteur de réponses généraliste"),
  ("Vos conversations", "<span class='yes'>Stockées uniquement sur votre appareil</span> et dans votre propre iCloud — jamais entreposées ni utilisées pour entraîner", "Envoyées aux serveurs de l'entreprise"),
  ("Collecte de données", "<span class='yes'>Aucune</span> — étiquette de confidentialité d'Apple : « Données non collectées »", "Collecte des données de compte, d'usage et de recherche"),
  ("Inscription requise", "<span class='yes'>Non</span> — pas de compte, d'e-mail ni de numéro de téléphone", "Nécessite un compte pour un usage complet"),
  ("Au-delà de la recherche", "Une super app Apple complète — marchés, productivité, voyage, éducation et plus de 40 flux de travail, sur iPhone, iPad, Mac et Vision", "Surtout un moteur de réponses et de recherche"),
  ("Prix", "<span class='yes'>Gratuit</span> (achats intégrés optionnels)", "Offre gratuite ; Pro payant pour plus"),
 ],
 "note": "Comparaison fondée sur des informations publiques en juin 2026. Perplexity est une marque de son détenteur respectif ; NoArk est une app indépendante, ni affiliée ni approuvée par celle-ci.",
 "sections": [
  ("De l'analyse, pas seulement des réponses", [
   "Perplexity excelle dans une chose : vous demandez, il cherche sur le web et renvoie une réponse résumée avec citations. NoArk est conçu pour l'étape suivante — <strong>comprendre</strong>. Son écran principal est un flux d'<strong>actualité mondiale en direct</strong>, et un seul geste vous donne une <strong>analyse qui interprète ce qu'une nouvelle signifie vraiment</strong> pour vous et les marchés, en faisant appel à de nombreux modèles de pointe — Claude Fable, DeepSeek, Mistral, Kimi et Gemini. Vous ne recevez pas seulement l'actualité ; vous en recevez une lecture.",
  ]),
  ("Privé par défaut — sans compte, rien de collecté", [
   "Pour tirer le meilleur de Perplexity, vous vous connectez, et vos recherches sont envoyées aux serveurs de l'entreprise. NoArk fait l'inverse : il n'y a <strong>aucune inscription</strong> — pas d'e-mail, pas de numéro de téléphone — et vos conversations sont <strong>stockées uniquement sur votre appareil et dans votre propre iCloud</strong>, jamais entreposées sur nos serveurs ni utilisées pour entraîner un modèle. L'étiquette officielle de confidentialité d'Apple pour NoArk indique <a href='" + pp + "'>« Données non collectées »</a>, la plus stricte qui soit. Ce que vous cherchez reste à vous.",
  ]),
  ("Plus qu'un moteur de réponses : du conseil + une super app complète", [
   "Au-delà de l'actualité, l'onglet <strong>Fiat Lux</strong> de NoArk vous laisse apporter de vraies questions à des versions IA des plus grands esprits de l'histoire — Charlie Munger, Steve Jobs, Marc Aurèle et plus de 40 autres — ancrées dans leur vraie façon de raisonner. Et c'est une <strong>super app Apple complète</strong> pour iPhone, iPad, Mac et Apple Vision : plus de 40 flux de travail prêts à l'emploi couvrant marchés, productivité, voyage, éducation et gestion du quotidien, avec un cerveau d'investisseur créé par l'équipe de TradingTransformer, inspiré par la vision de Claude Shannon d'une IA qui choisit les actions.",
  ]),
 ],
 "related_heading": "À lire ensuite",
 "related": [
  (hp, "NoArk — Infinity Memory : l'OS intelligent et la super app IA"),
  (gp, "NoArk vs ChatGPT"),
  (mp, "NoArk vs Google Gemini"),
  (cp, "NoArk vs Character.AI"),
  (ap, "NoArk vs Apple Intelligence"),
  (hp + "noark-vs-manus.html", "NoArk vs Manus"),
  (fp, "Questions fréquentes sur NoArk"),
 ],
 "faq": [
  ("NoArk est-elle une alternative à Perplexity ?", "Oui, et plus large. Là où Perplexity répond aux recherches avec des citations, NoArk vous donne l'actualité mondiale en direct avec une analyse en un geste qui interprète ce que signifie l'actualité, plus le conseil des plus grands esprits de l'histoire et plus de 40 flux de travail — le tout sans compte et avec chaque conversation gardée sur votre propre appareil. Apple l'étiquette « Données non collectées »."),
  ("NoArk fait-elle de l'analyse d'actualité ?", "Oui. L'écran principal de NoArk est un flux d'actualité mondiale en direct, et un seul geste vous donne une analyse qui interprète ce qu'une nouvelle signifie pour vous et les marchés — en faisant appel à de nombreux modèles de pointe — plutôt que de simplement la résumer."),
  ("Ma recherche est-elle privée avec NoArk ?", "Oui. Il n'y a aucune inscription ni collecte de données : vos conversations et recherches restent sur votre propre appareil et dans votre propre iCloud, jamais entreposées sur nos serveurs ni utilisées pour entraîner des modèles. L'étiquette de confidentialité d'Apple indique « Données non collectées »."),
  ("Quels modèles d'IA NoArk utilise-t-elle ?", "NoArk route chaque requête vers le meilleur de nombreux modèles de pointe — Claude (Fable) d'Anthropic, DeepSeek, Mistral, Kimi et Gemini de Google — au lieu de dépendre d'un seul."),
  ("NoArk est-elle gratuite ?", "NoArk est gratuite sur iPhone, iPad, Mac et Apple Vision, avec des achats intégrés optionnels. Aucun compte ni aucune collecte de données n'est nécessaire pour commencer."),
 ],
}

# ---------------- Japanese ----------------
hp, gp, cp, mp, ap, fp, pp = rel("ja")
content["ja"] = {
 "title": "NoArk vs Perplexity：検索の回答だけでなく、プライベートなニュース分析",
 "desc": "NoArk と Perplexity を比較：ニュース分析か検索回答か、プライバシー、サインイン、価格。Perplexity は回答エンジン。NoArk はワンタップ解釈つきのライブ世界ニュース、歴史上の賢人の助言、フル機能の Apple スーパーアプリを提供し、アカウント不要で、すべての会話をあなたのデバイスに保ちます。iPhone・iPad・Mac・Apple Vision で無料。",
 "keywords": "NoArk vs Perplexity, Perplexity 代替, プライベート Perplexity, プライベート AI 検索, AI ニュース分析, ライブニュース AI, サインイン不要 AI, オンデバイス AI, Perplexity 代替 iPhone, Claude Fable, DeepSeek, 無料 Perplexity 代替",
 "ogdesc": "NoArk が Perplexity と違う点：検索に答えるだけでなくライブニュースを解釈し、歴史上の賢人の助言とフル機能の Apple スーパーアプリを加え、アカウント不要で会話をあなたのデバイスに保ちます。",
 "twdesc": "検索に答えるだけでなくライブニュースを解釈し、歴史上の賢人の助言とフル機能の Apple スーパーアプリを加え、アカウント不要ですべてを非公開に。",
 "h1": "NoArk vs Perplexity",
 "subtitle": "どちらも問いを回答に変えます。しかし、ニュースをあなたのために解釈し、歴史上の賢人の助言を提供し、すべての検索をアカウント不要で非公開に保つのは一方だけです。",
 "intro": "Perplexity は速くて便利な回答エンジンです。ウェブを検索し、出典つきの要約を返します。<strong>NoArk — Infinity Memory</strong> はもう一歩進みます。<strong>ワンタップ分析つきのライブ世界ニュース</strong>で、その出来事が何を<em>意味するか</em>を解釈し、<strong>歴史上の賢人の助言</strong>を加え、フル機能の Apple スーパーアプリに包みます — すべて<strong>アカウント不要</strong>で、会話はあなた自身のデバイスに保たれます。これが率直な比較です。",
 "glance": "ひと目でわかる比較",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("何のためのものか", "<span class='yes'>理解</span> — ライブニュース、ワンタップ分析、助言、暮らしと市場にわたる40以上のワークフロー", "検索 — 問い合わせを出典つきのウェブ回答に変える"),
  ("ニュースと分析", "<span class='yes'>ライブ世界ニュース</span>＋ワンタップ分析。記事が何を意味するかを解釈 — 単なる要約ではありません", "出典を引いた要約回答"),
  ("歴史上の賢人", "<span class='yes'>あり</span> — Fiat Lux：チャーリー・マンガー、スティーブ・ジョブズ、アインシュタイン、マルクス・アウレリウスほか40名以上のAI版。実際の考え方に基づく", "汎用の回答エンジン"),
  ("あなたの会話", "<span class='yes'>あなたのデバイス</span>とあなた自身の iCloud だけに保存 — 蓄積も学習利用もされません", "企業のサーバーに送信"),
  ("データ収集", "<span class='yes'>なし</span> — Apple のプライバシーラベル：「データは収集されません」", "アカウント・利用状況・検索のデータを収集"),
  ("サインイン", "<span class='yes'>不要</span> — アカウントもメールも電話番号も不要", "本格利用にアカウントが必要"),
  ("検索の先", "フル機能の Apple スーパーアプリ — 市場、生産性、旅行、教育、40以上のワークフロー。iPhone・iPad・Mac・Vision 対応", "主に回答・リサーチエンジン"),
  ("価格", "<span class='yes'>無料</span>（オプションのアプリ内課金あり）", "無料プラン。さらに使うには有料 Pro"),
 ],
 "note": "本比較は2026年6月時点の公開情報に基づきます。Perplexity は各権利者の商標です。NoArk は独立したアプリであり、提携や承認はありません。",
 "sections": [
  ("回答だけでなく、分析を", [
   "Perplexity はひとつのことに優れています。尋ねれば、ウェブを検索し、出典つきの要約回答を返します。NoArk はその次の一歩 — <strong>理解</strong> のために作られています。ホーム画面は<strong>ライブ世界ニュース</strong>の流れで、ワンタップで、その出来事があなたと市場にとって<strong>本当は何を意味するかを解釈する分析</strong>が得られます。多数のフロンティアモデル — Claude Fable、DeepSeek、Mistral、Kimi、Gemini — を活用します。ニュースを受け取るだけでなく、その読み解きが得られます。",
  ]),
  ("既定でプライベート — アカウントなし、何も収集しない", [
   "Perplexity を最大限使うにはサインインし、検索は企業のサーバーに送られます。NoArk は逆です。<strong>サインインは不要</strong> — メールも電話番号もなく — あなたの会話は<strong>あなたのデバイスとあなた自身の iCloud だけに保存</strong>され、私たちのサーバーに蓄積されることも、どのモデルの学習に使われることもありません。Apple 公式の NoArk のプライバシーラベルは <a href='" + pp + "'>「データは収集されません」</a> — 最も厳格なラベルです。あなたが検索したものは、あなたのものです。",
  ]),
  ("回答エンジン以上：助言＋フル機能のスーパーアプリ", [
   "ニュースの先で、NoArk の <strong>Fiat Lux</strong> タブでは、本当の問いを歴史上の賢人のAI版 — チャーリー・マンガー、スティーブ・ジョブズ、マルクス・アウレリウスほか40名以上 — に持ち込めます。いずれも実際の考え方に基づいています。そして iPhone・iPad・Mac・Apple Vision のための<strong>フル機能の Apple スーパーアプリ</strong>です。市場・生産性・旅行・教育・生活の雑務にわたる40以上の即戦力ワークフローと、TradingTransformer チームが作り、クロード・シャノンのAI株式選択のビジョンに着想を得た投資する頭脳を備えます。",
  ]),
 ],
 "related_heading": "あわせて読む",
 "related": [
  (hp, "NoArk — Infinity Memory：インテリジェントAI OS・スーパーアプリ"),
  (gp, "NoArk vs ChatGPT"),
  (mp, "NoArk vs Google Gemini"),
  (cp, "NoArk vs Character.AI"),
  (ap, "NoArk vs Apple Intelligence"),
  (hp + "noark-vs-manus.html", "NoArk vs Manus"),
  (fp, "NoArk についてのよくある質問"),
 ],
 "faq": [
  ("NoArk は Perplexity の代替になりますか？", "はい、しかもより広範です。Perplexity が出典つきで検索に答えるのに対し、NoArk はワンタップ分析つきのライブ世界ニュースで、その意味を解釈し、さらに歴史上の賢人の助言と40以上のワークフローを提供します — すべてアカウント不要で、会話はあなた自身のデバイスに保たれます。Apple のラベルは「データは収集されません」です。"),
  ("NoArk はニュース分析をしますか？", "はい。NoArk のホームはライブ世界ニュースの流れで、ワンタップで、その出来事があなたと市場にとって何を意味するかを解釈する分析が得られます — 多数のフロンティアモデルを活用し — 単に要約するだけではありません。"),
  ("NoArk では私の検索はプライベートですか？", "はい。サインインもデータ収集もありません。あなたの会話と検索はあなた自身のデバイスとあなた自身の iCloud に残り、私たちのサーバーに蓄積されることも、モデルの学習に使われることもありません。Apple のプライバシーラベルは「データは収集されません」です。"),
  ("NoArk はどのAIモデルを使いますか？", "NoArk はリクエストごとに、Anthropic の Claude（Fable）、DeepSeek、Mistral、Kimi、Google の Gemini など多数のフロンティアモデルから最適なものを選びます。単一のモデルに頼りません。"),
  ("NoArk は無料ですか？", "NoArk は iPhone・iPad・Mac・Apple Vision で無料で、オプションのアプリ内課金があります。始めるのにアカウントもデータ収集も不要です。"),
 ],
}

# ---------------- Simplified Chinese ----------------
hp, gp, cp, mp, ap, fp, pp = rel("zh-cn")
content["zh-cn"] = {
 "title": "NoArk 对比 Perplexity：私密的新闻分析，而不只是搜索答案",
 "desc": "NoArk 与 Perplexity 全面对比：新闻分析还是搜索答案、隐私、登录与价格。Perplexity 是答案引擎；NoArk 给你带一键解读的实时全球头条、历史智者的建议，以及一款完整的 Apple 超级应用——无需账户，每段对话都留在你自己的设备上。iPhone、iPad、Mac 和 Apple Vision 免费下载。",
 "keywords": "NoArk 对比 Perplexity, Perplexity 替代品, 私密 Perplexity, 私密 AI 搜索, AI 新闻分析, 实时头条 AI, 无需登录的 AI, 端侧 AI, Perplexity 替代 iPhone, Claude Fable, DeepSeek, 免费 Perplexity 替代品",
 "ogdesc": "NoArk 与 Perplexity 的不同：它解读实时头条，而不只是回答搜索；加入历史智者的建议和一款完整的 Apple 超级应用；并让每段对话都私密地留在你自己的设备上，无需账户。",
 "twdesc": "它解读实时头条，而不只是回答搜索；加入历史智者的建议和一款完整的 Apple 超级应用；并让一切私密、无需账户。",
 "h1": "NoArk 对比 Perplexity",
 "subtitle": "两者都把问题变成答案。但只有一个为你解读新闻、提供历史智者的建议，并让每次搜索都保持私密、无需账户。",
 "intro": "Perplexity 是一个快速好用的答案引擎：它搜索网络，返回一段带引用的摘要。<strong>NoArk — 无限记忆</strong>更进一步——它为你带来<strong>带一键分析的实时全球头条</strong>，解读新闻<em>意味着什么</em>，加入<strong>历史智者的建议</strong>，并把这一切包进一款完整的 Apple 超级应用——全部<strong>无需账户</strong>，每段对话都留在你自己的设备上。下面是坦诚的对比。",
 "glance": "一览对比",
 "col_noark": "NoArk — 无限记忆",
 "rows": [
  ("为何而生", "<span class='yes'>理解</span>——实时头条、一键分析、建议，以及覆盖你生活与市场的 40 多个工作流", "搜索——把一个查询变成带引用的网络答案"),
  ("新闻与分析", "<span class='yes'>实时全球头条</span>＋一键分析，解读一条新闻意味着什么——不只是摘要", "带来源引用的摘要式回答"),
  ("历史上的智者", "<span class='yes'>有</span>——Fiat Lux：查理·芒格、史蒂夫·乔布斯、爱因斯坦、马可·奥勒留等 40 多位的 AI 版本，立足于他们真实的思考方式", "一个通用的答案引擎"),
  ("你的对话", "<span class='yes'>只保存在你的设备</span>和你自己的 iCloud 中——绝不堆放或用于训练", "发送到公司服务器"),
  ("数据收集", "<span class='yes'>无</span>——Apple 隐私标签：“不收集数据”", "收集账户、使用和搜索数据"),
  ("是否需要登录", "<span class='yes'>不需要</span>——无账户、邮箱或手机号", "完整使用需要账户"),
  ("搜索之外", "一款完整的 Apple 超级应用——市场、生产力、旅行、教育和 40 多个工作流，支持 iPhone、iPad、Mac 和 Vision", "主要是答案与研究引擎"),
  ("价格", "<span class='yes'>免费</span>下载（含可选的应用内购买）", "免费档；付费 Pro 解锁更多"),
 ],
 "note": "对比基于截至 2026 年 6 月的公开信息。Perplexity 是其各自所有者的商标；NoArk 是独立应用，与其无关联，也未获其背书。",
 "sections": [
  ("分析，而不只是答案", [
   "Perplexity 把一件事做得很好：你问，它搜索网络，返回一段带引用的摘要式回答。NoArk 为下一步而生——<strong>理解</strong>。它的主界面是一条<strong>实时全球头条</strong>的信息流，轻轻一点，就能得到<strong>解读一条新闻对你和市场究竟意味着什么的分析</strong>，调用多个前沿模型——Claude Fable、DeepSeek、Mistral、Kimi 和 Gemini。你得到的不只是新闻，而是对它的一种解读。",
  ]),
  ("默认私密——无需账户，什么都不收集", [
   "要充分用好 Perplexity，你需要登录，而你的搜索会被发送到公司服务器。NoArk 恰恰相反：<strong>无需登录</strong>——没有邮箱、没有手机号——你的对话<strong>只保存在你的设备和你自己的 iCloud 中</strong>，绝不堆放在我们的服务器上，也绝不用于训练任何模型。Apple 官方为 NoArk 出具的隐私标签写着 <a href='" + pp + "'>“不收集数据”</a>——最严格的一档。你搜索的内容，依然属于你。",
  ]),
  ("不只是答案引擎：建议＋一款完整的超级应用", [
   "在头条之外，NoArk 的 <strong>Fiat Lux</strong> 标签让你把真实的问题带给历史上最有智慧的人的 AI 版本——查理·芒格、史蒂夫·乔布斯、马可·奥勒留等 40 多位——每一位都立足于他们真实的思考方式。它还是一款面向 iPhone、iPad、Mac 和 Apple Vision 的<strong>完整 Apple 超级应用</strong>：涵盖市场、生产力、旅行、教育和生活事务的 40 多个开箱即用工作流，以及由 TradingTransformer 团队打造、灵感来自克劳德·香农 AI 选股愿景的投资大脑。",
  ]),
 ],
 "related_heading": "继续阅读",
 "related": [
  (hp, "NoArk — 无限记忆：智能 AI 操作系统与超级应用"),
  (gp, "NoArk 对比 ChatGPT"),
  (mp, "NoArk 对比 Google Gemini"),
  (cp, "NoArk 对比 Character.AI"),
  (ap, "NoArk 对比 Apple Intelligence"),
  (hp + "noark-vs-manus.html", "NoArk 对比 Manus"),
  (fp, "关于 NoArk 的常见问题"),
 ],
 "faq": [
  ("NoArk 是 Perplexity 的替代品吗？", "是的，而且更宽广。Perplexity 用引用回答搜索，而 NoArk 给你带一键分析的实时全球头条，解读新闻意味着什么，还有历史智者的建议和 40 多个工作流——全部无需账户，每段对话都留在你自己的设备上。Apple 的标签是“不收集数据”。"),
  ("NoArk 会做新闻分析吗？", "会。NoArk 的主界面是实时全球头条的信息流，轻轻一点，就能得到解读一条新闻对你和市场意味着什么的分析——调用多个前沿模型——而不只是把它摘要一下。"),
  ("用 NoArk 我的搜索私密吗？", "私密。没有登录、也不收集数据：你的对话和搜索都留在你自己的设备和你自己的 iCloud 中，绝不堆放在我们的服务器上，也绝不用于训练模型。Apple 的隐私标签写着“不收集数据”。"),
  ("NoArk 用哪些 AI 模型？", "NoArk 将每个请求路由到众多前沿模型中最合适的一个——Anthropic 的 Claude（Fable）、DeepSeek、Mistral、Kimi 和谷歌的 Gemini——而不是依赖单一一个。"),
  ("NoArk 免费吗？", "NoArk 在 iPhone、iPad、Mac 和 Apple Vision 上免费下载，含可选的应用内购买。开始使用无需账户，也不收集数据。"),
 ],
}

# ---------------- Traditional Chinese ----------------
hp, gp, cp, mp, ap, fp, pp = rel("zh-tw")
content["zh-tw"] = {
 "title": "NoArk 對比 Perplexity：私密的新聞分析，而不只是搜尋答案",
 "desc": "NoArk 與 Perplexity 全面對比：新聞分析還是搜尋答案、隱私、登入與價格。Perplexity 是答案引擎；NoArk 給你帶一鍵解讀的即時全球頭條、歷史智者的建議，以及一款完整的 Apple 超級應用程式——無需帳號，每段對話都留在你自己的裝置上。iPhone、iPad、Mac 和 Apple Vision 免費下載。",
 "keywords": "NoArk 對比 Perplexity, Perplexity 替代品, 私密 Perplexity, 私密 AI 搜尋, AI 新聞分析, 即時頭條 AI, 無需登入的 AI, 端側 AI, Perplexity 替代 iPhone, Claude Fable, DeepSeek, 免費 Perplexity 替代品",
 "ogdesc": "NoArk 與 Perplexity 的不同：它解讀即時頭條，而不只是回答搜尋；加入歷史智者的建議和一款完整的 Apple 超級應用程式；並讓每段對話都私密地留在你自己的裝置上，無需帳號。",
 "twdesc": "它解讀即時頭條，而不只是回答搜尋；加入歷史智者的建議和一款完整的 Apple 超級應用程式；並讓一切私密、無需帳號。",
 "h1": "NoArk 對比 Perplexity",
 "subtitle": "兩者都把問題變成答案。但只有一個為你解讀新聞、提供歷史智者的建議，並讓每次搜尋都保持私密、無需帳號。",
 "intro": "Perplexity 是一個快速好用的答案引擎：它搜尋網路，返回一段帶引用的摘要。<strong>NoArk — 無限記憶</strong>更進一步——它為你帶來<strong>帶一鍵分析的即時全球頭條</strong>，解讀新聞<em>意味著什麼</em>，加入<strong>歷史智者的建議</strong>，並把這一切包進一款完整的 Apple 超級應用程式——全部<strong>無需帳號</strong>，每段對話都留在你自己的裝置上。以下是坦誠的對比。",
 "glance": "一覽對比",
 "col_noark": "NoArk — 無限記憶",
 "rows": [
  ("為何而生", "<span class='yes'>理解</span>——即時頭條、一鍵分析、建議，以及涵蓋你生活與市場的 40 多個工作流程", "搜尋——把一個查詢變成帶引用的網路答案"),
  ("新聞與分析", "<span class='yes'>即時全球頭條</span>＋一鍵分析，解讀一條新聞意味著什麼——不只是摘要", "帶來源引用的摘要式回答"),
  ("歷史上的智者", "<span class='yes'>有</span>——Fiat Lux：查理·蒙格、史蒂夫·賈伯斯、愛因斯坦、馬可·奧理略等 40 多位的 AI 版本，立足於他們真實的思考方式", "一個通用的答案引擎"),
  ("你的對話", "<span class='yes'>只保存在你的裝置</span>和你自己的 iCloud 中——絕不堆放或用於訓練", "傳送到公司伺服器"),
  ("資料收集", "<span class='yes'>無</span>——Apple 隱私標籤：「不收集資料」", "收集帳號、使用和搜尋資料"),
  ("是否需要登入", "<span class='yes'>不需要</span>——無帳號、電子郵件或手機號碼", "完整使用需要帳號"),
  ("搜尋之外", "一款完整的 Apple 超級應用程式——市場、生產力、旅行、教育和 40 多個工作流程，支援 iPhone、iPad、Mac 和 Vision", "主要是答案與研究引擎"),
  ("價格", "<span class='yes'>免費</span>下載（含可選的應用程式內購買）", "免費檔；付費 Pro 解鎖更多"),
 ],
 "note": "對比基於截至 2026 年 6 月的公開資訊。Perplexity 是其各自所有者的商標；NoArk 是獨立應用程式，與其無關聯，也未獲其背書。",
 "sections": [
  ("分析，而不只是答案", [
   "Perplexity 把一件事做得很好：你問，它搜尋網路，返回一段帶引用的摘要式回答。NoArk 為下一步而生——<strong>理解</strong>。它的主介面是一條<strong>即時全球頭條</strong>的資訊流，輕輕一點，就能得到<strong>解讀一條新聞對你和市場究竟意味著什麼的分析</strong>，調用多個前沿模型——Claude Fable、DeepSeek、Mistral、Kimi 和 Gemini。你得到的不只是新聞，而是對它的一種解讀。",
  ]),
  ("預設私密——無需帳號，什麼都不收集", [
   "要充分用好 Perplexity，你需要登入，而你的搜尋會被傳送到公司伺服器。NoArk 恰恰相反：<strong>無需登入</strong>——沒有電子郵件、沒有手機號碼——你的對話<strong>只保存在你的裝置和你自己的 iCloud 中</strong>，絕不堆放在我們的伺服器上，也絕不用於訓練任何模型。Apple 官方為 NoArk 出具的隱私標籤寫著 <a href='" + pp + "'>「不收集資料」</a>——最嚴格的一檔。你搜尋的內容，依然屬於你。",
  ]),
  ("不只是答案引擎：建議＋一款完整的超級應用程式", [
   "在頭條之外，NoArk 的 <strong>Fiat Lux</strong> 分頁讓你把真實的問題帶給歷史上最有智慧的人的 AI 版本——查理·蒙格、史蒂夫·賈伯斯、馬可·奧理略等 40 多位——每一位都立足於他們真實的思考方式。它還是一款面向 iPhone、iPad、Mac 和 Apple Vision 的<strong>完整 Apple 超級應用程式</strong>：涵蓋市場、生產力、旅行、教育和生活事務的 40 多個開箱即用工作流程，以及由 TradingTransformer 團隊打造、靈感來自克勞德·夏農 AI 選股願景的投資大腦。",
  ]),
 ],
 "related_heading": "繼續閱讀",
 "related": [
  (hp, "NoArk — 無限記憶：智慧型 AI 作業系統與超級應用程式"),
  (gp, "NoArk 對比 ChatGPT"),
  (mp, "NoArk 對比 Google Gemini"),
  (cp, "NoArk 對比 Character.AI"),
  (ap, "NoArk 對比 Apple Intelligence"),
  (hp + "noark-vs-manus.html", "NoArk 對比 Manus"),
  (fp, "關於 NoArk 的常見問題"),
 ],
 "faq": [
  ("NoArk 是 Perplexity 的替代品嗎？", "是的，而且更寬廣。Perplexity 用引用回答搜尋，而 NoArk 給你帶一鍵分析的即時全球頭條，解讀新聞意味著什麼，還有歷史智者的建議和 40 多個工作流程——全部無需帳號，每段對話都留在你自己的裝置上。Apple 的標籤是「不收集資料」。"),
  ("NoArk 會做新聞分析嗎？", "會。NoArk 的主介面是即時全球頭條的資訊流，輕輕一點，就能得到解讀一條新聞對你和市場意味著什麼的分析——調用多個前沿模型——而不只是把它摘要一下。"),
  ("用 NoArk 我的搜尋私密嗎？", "私密。沒有登入、也不收集資料：你的對話和搜尋都留在你自己的裝置和你自己的 iCloud 中，絕不堆放在我們的伺服器上，也絕不用於訓練模型。Apple 的隱私標籤寫著「不收集資料」。"),
  ("NoArk 用哪些 AI 模型？", "NoArk 將每個請求路由到眾多前沿模型中最合適的一個——Anthropic 的 Claude（Fable）、DeepSeek、Mistral、Kimi 和 Google 的 Gemini——而不是依賴單一一個。"),
  ("NoArk 免費嗎？", "NoArk 在 iPhone、iPad、Mac 和 Apple Vision 上免費下載，含可選的應用程式內購買。開始使用無需帳號，也不收集資料。"),
 ],
}

render(SLUG, COMP, content)
