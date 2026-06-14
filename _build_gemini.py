# -*- coding: utf-8 -*-
from _compare_lib import render

SLUG = "noark-vs-gemini.html"
COMP = "Google Gemini"

def rel(p):
    base = "/" + (p + "/" if p else "")
    return (base,
            base + "noark-vs-chatgpt.html",
            base + "noark-vs-character-ai.html",
            base + "noark-vs-apple-intelligence.html",
            base + "#faq",
            base + "#data-privacy")

content = {}

# ---------------- English ----------------
hp, gp, cp, ap, fp, pp = rel("")
content[""] = {
 "title": "NoArk vs Google Gemini: A Private AI That Serves You, Not an Ad Business",
 "desc": "NoArk vs Google Gemini compared: who the AI serves, privacy, AI models, and price. NoArk collects no data and keeps every conversation on your own device — no Google account, no ads. It routes to many frontier models (yes, Gemini is one of them) and adds AI versions of history's wisest minds. Free on iPhone, iPad, Mac & Apple Vision.",
 "keywords": "NoArk vs Gemini, Google Gemini alternative, private Gemini, AI without Google account, no-ads AI, on-device AI, multi-model AI app, Gemini alternative iPhone, Claude Fable, DeepSeek, Mistral, Kimi, free Gemini alternative",
 "ogdesc": "How NoArk differs from Google Gemini: it serves only you — no ads, no data collection, conversations on your own device — routes to many frontier models (Gemini among them), and is a full Apple super app.",
 "twdesc": "It serves only you — no ads, no data collection, conversations on your own device — many frontier models (Gemini among them), and a full Apple super app.",
 "h1": "NoArk vs Google Gemini",
 "subtitle": "Both are powerful AI assistants. Only one collects nothing, shows no ads, and answers to you alone — while still using Gemini as one of many models.",
 "intro": "Google Gemini is a capable assistant — built by a company whose core business is advertising, and woven into the Google account that already follows you across the web. <strong>NoArk — Infinity Memory</strong> answers to a different master: <strong>you</strong>. No ads, no data collection, every conversation on your own device — and it still draws on <strong>many frontier models, Gemini included</strong>. Here's the honest comparison.",
 "glance": "At a glance",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("Who the AI serves", "<span class='yes'>Only you</span> — never monetizes your attention or data; 50% of app profits pledged to education", "Built by Google, whose core business is advertising; part of the wider Google ecosystem"),
  ("Your conversations", "<span class='yes'>Stored only on your device</span> and in your own iCloud — never warehoused or used to train", "Tied to your Google account; activity can be reviewed and used to improve Google's services"),
  ("Data collection", "<span class='yes'>None</span> — Apple's App Privacy label: “Data Not Collected”", "Collects account, usage, and conversation data"),
  ("Sign-in required", "<span class='yes'>No</span> — no account, email, or phone number", "Requires a Google account"),
  ("AI models", "<span class='yes'>Many frontier models</span> — Claude's Fable, DeepSeek, Mistral, Kimi, and Gemini — the best picked per task", "Google's Gemini models only"),
  ("History's wisest minds", "<span class='yes'>Yes</span> — Fiat Lux: AI versions of Charlie Munger, Steve Jobs, Einstein, Marcus Aurelius &amp; 40+ more, grounded in how they actually reasoned", "A single general-purpose assistant"),
  ("Beyond chat", "A full Apple super app — live headlines with one-tap analysis, markets, productivity, travel, education &amp; 40+ workflows, on iPhone, iPad, Mac &amp; Vision", "An assistant across Google's apps and services"),
  ("Price", "<span class='yes'>Free</span> to download (optional in-app purchases)", "Free tier; paid plans for more"),
 ],
 "note": "Comparison reflects publicly available information as of June 2026. Google and Gemini are trademarks of Google LLC; NoArk is an independent app and is not affiliated with or endorsed by it.",
 "sections": [
  ("Who the AI works for", [
   "This is the difference that matters most. Google's core business is <strong>advertising</strong>, and Gemini lives inside the same account that already tracks your search, your email, and your browsing. NoArk has no ad business and nothing to sell: it <strong>serves only you</strong>, never monetizes your attention or your data, and pledges 50% of app profits to education.",
   "Concretely, that means <strong>no sign-in</strong> — no Google account, no email, no phone number — and your conversations <strong>stored only on your device and in your own iCloud</strong>. Apple's official App Privacy label for NoArk reads <a href='" + pp + "'>“Data Not Collected”</a>, the strictest there is.",
  ]),
  ("Yes, NoArk uses Gemini too — as one of many", [
   "You don't have to give up Gemini's strengths to get privacy. NoArk routes each request to the best of <strong>many frontier models</strong> — Anthropic's Claude (Fable), DeepSeek, Mistral, Kimi, and Google's Gemini among them — so you get Gemini-class capability when it's the right tool, without being locked to a single provider. The difference: your content runs through these models' APIs without being stored on our servers or tied to an ad profile.",
  ]),
  ("More than an assistant: a private Apple super app", [
   "Gemini is an assistant spread across Google's apps. NoArk is a <strong>full Apple super app</strong> built for iPhone, iPad, Mac, and Apple Vision: live global headlines with one-tap analysis, 40+ ready-made workflows across markets, productivity, travel, education, and life admin, and an investing brain built by the team behind TradingTransformer, inspired by Claude Shannon's vision of AI stock-picking. Its <strong>Fiat Lux</strong> tab lets you bring real questions to AI versions of history's wisest minds — Charlie Munger, Steve Jobs, Marcus Aurelius, and 40+ more — grounded in how they actually reasoned.",
  ]),
 ],
 "related_heading": "Keep reading",
 "related": [
  (hp, "NoArk — Infinity Memory: the intelligent AI OS & super app"),
  (gp, "NoArk vs ChatGPT"),
  (cp, "NoArk vs Character.AI"),
  (ap, "NoArk vs Apple Intelligence"),
  (fp, "Frequently asked questions about NoArk"),
 ],
 "faq": [
  ("Is NoArk a private Google Gemini alternative?", "Yes. NoArk gives you frontier-model AI without a Google account and without data collection: your conversations stay on your own device and in your own iCloud, never used to train any model. Apple labels it “Data Not Collected.” It also routes to many models — including Gemini — and is a full Apple super app."),
  ("Does NoArk use my data for ads?", "No. NoArk shows no ads and never monetizes your attention or your data. It has no advertising business and collects no data — Apple's App Privacy label reads “Data Not Collected.” It serves only you."),
  ("Does NoArk use Gemini too?", "Yes — Gemini is one of the several frontier models NoArk can route to, alongside Anthropic's Claude (Fable), DeepSeek, Mistral, and Kimi. You get Gemini-class capability when it's the best tool, but your content isn't stored on our servers or tied to a Google ad profile."),
  ("Does NoArk need a Google account or sign-in?", "No. There's no account of any kind — no Google sign-in, no email, no phone number. You download NoArk and start, and nothing ties what you ask to who you are."),
  ("Is NoArk free?", "NoArk is free to download on iPhone, iPad, Mac, and Apple Vision, with optional in-app purchases. There's no account and no data collection required to start."),
 ],
}

# ---------------- Spanish ----------------
hp, gp, cp, ap, fp, pp = rel("es")
content["es"] = {
 "title": "NoArk vs Google Gemini: una IA privada que te sirve a ti, no a un negocio de anuncios",
 "desc": "Comparativa NoArk vs Google Gemini: a quién sirve la IA, privacidad, modelos de IA y precio. NoArk no recopila datos y mantiene cada conversación en tu propio dispositivo — sin cuenta de Google, sin anuncios. Recurre a muchos modelos de frontera (sí, Gemini es uno de ellos) y añade versiones de IA de las mentes más sabias de la historia. Gratis en iPhone, iPad, Mac y Apple Vision.",
 "keywords": "NoArk vs Gemini, alternativa a Google Gemini, Gemini privado, IA sin cuenta de Google, IA sin anuncios, IA en el dispositivo, app de IA multimodelo, alternativa a Gemini iPhone, Claude Fable, DeepSeek, Mistral, Kimi, alternativa gratis a Gemini",
 "ogdesc": "En qué se diferencia NoArk de Google Gemini: te sirve solo a ti — sin anuncios, sin recopilación de datos, conversaciones en tu propio dispositivo — recurre a muchos modelos de frontera (Gemini entre ellos) y es una súper app de Apple.",
 "twdesc": "Te sirve solo a ti — sin anuncios, sin recopilación de datos, conversaciones en tu propio dispositivo — muchos modelos de frontera (Gemini incluido) y una súper app de Apple.",
 "h1": "NoArk vs Google Gemini",
 "subtitle": "Ambos son asistentes de IA potentes. Solo uno no recopila nada, no muestra anuncios y responde solo ante ti — usando además Gemini como uno de muchos modelos.",
 "intro": "Google Gemini es un asistente capaz — creado por una empresa cuyo negocio principal es la publicidad, e integrado en la cuenta de Google que ya te sigue por la web. <strong>NoArk — Infinity Memory</strong> responde ante otro amo: <strong>tú</strong>. Sin anuncios, sin recopilación de datos, cada conversación en tu propio dispositivo — y aun así recurre a <strong>muchos modelos de frontera, Gemini incluido</strong>. Esta es la comparación honesta.",
 "glance": "De un vistazo",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("A quién sirve la IA", "<span class='yes'>Solo a ti</span> — nunca monetiza tu atención ni tus datos; el 50% de los beneficios se destina a educación", "Creada por Google, cuyo negocio principal es la publicidad; parte del ecosistema de Google"),
  ("Tus conversaciones", "<span class='yes'>Guardadas solo en tu dispositivo</span> y en tu propio iCloud — nunca almacenadas ni usadas para entrenar", "Vinculadas a tu cuenta de Google; la actividad puede revisarse y usarse para mejorar los servicios de Google"),
  ("Recopilación de datos", "<span class='yes'>Ninguna</span> — etiqueta de privacidad de Apple: «No se recopilan datos»", "Recopila datos de cuenta, uso y conversaciones"),
  ("Registro obligatorio", "<span class='yes'>No</span> — sin cuenta, correo ni número de teléfono", "Requiere una cuenta de Google"),
  ("Modelos de IA", "<span class='yes'>Muchos modelos de frontera</span> — Claude Fable, DeepSeek, Mistral, Kimi y Gemini — el mejor para cada tarea", "Solo los modelos Gemini de Google"),
  ("Las mentes más sabias de la historia", "<span class='yes'>Sí</span> — Fiat Lux: versiones de IA de Charlie Munger, Steve Jobs, Einstein, Marco Aurelio y más de 40, basadas en cómo razonaban de verdad", "Un único asistente de uso general"),
  ("Más allá del chat", "Una súper app de Apple completa — titulares en directo con análisis de un toque, mercados, productividad, viajes, educación y más de 40 flujos de trabajo, en iPhone, iPad, Mac y Vision", "Un asistente repartido por las apps y servicios de Google"),
  ("Precio", "<span class='yes'>Gratis</span> (compras opcionales dentro de la app)", "Nivel gratuito; planes de pago para más"),
 ],
 "note": "Comparativa basada en información pública a junio de 2026. Google y Gemini son marcas de Google LLC; NoArk es una app independiente, no afiliada ni respaldada por aquella.",
 "sections": [
  ("Para quién trabaja la IA", [
   "Esta es la diferencia que más importa. El negocio principal de Google es la <strong>publicidad</strong>, y Gemini vive dentro de la misma cuenta que ya registra tus búsquedas, tu correo y tu navegación. NoArk no tiene negocio publicitario ni nada que vender: <strong>te sirve solo a ti</strong>, nunca monetiza tu atención ni tus datos, y destina el 50% de los beneficios a educación.",
   "En concreto, eso significa <strong>sin registro</strong> — ni cuenta de Google, ni correo, ni número de teléfono — y tus conversaciones <strong>guardadas solo en tu dispositivo y en tu propio iCloud</strong>. La etiqueta oficial de privacidad de Apple para NoArk dice <a href='" + pp + "'>«No se recopilan datos»</a>, la más estricta que existe.",
  ]),
  ("Sí, NoArk también usa Gemini — como uno de muchos", [
   "No tienes que renunciar a las fortalezas de Gemini para tener privacidad. NoArk dirige cada petición al mejor de <strong>muchos modelos de frontera</strong> — Claude (Fable) de Anthropic, DeepSeek, Mistral, Kimi y Gemini de Google entre ellos — así que obtienes capacidad de nivel Gemini cuando es la herramienta adecuada, sin quedar atado a un único proveedor. La diferencia: tu contenido pasa por las API de estos modelos sin almacenarse en nuestros servidores ni vincularse a un perfil publicitario.",
  ]),
  ("Más que un asistente: una súper app de Apple privada", [
   "Gemini es un asistente repartido por las apps de Google. NoArk es una <strong>súper app de Apple completa</strong> para iPhone, iPad, Mac y Apple Vision: titulares globales en directo con análisis de un toque, más de 40 flujos de trabajo listos que abarcan mercados, productividad, viajes, educación y gestión diaria, y un cerebro inversor creado por el equipo de TradingTransformer, inspirado en la visión de Claude Shannon sobre la IA que elige acciones. Su pestaña <strong>Fiat Lux</strong> te deja llevar preguntas reales a versiones de IA de las mentes más sabias de la historia — Charlie Munger, Steve Jobs, Marco Aurelio y más de 40 — basadas en cómo razonaban de verdad.",
  ]),
 ],
 "related_heading": "Sigue leyendo",
 "related": [
  (hp, "NoArk — Infinity Memory: el SO inteligente y súper app de IA"),
  (gp, "NoArk vs ChatGPT"),
  (cp, "NoArk vs Character.AI"),
  (ap, "NoArk vs Apple Intelligence"),
  (fp, "Preguntas frecuentes sobre NoArk"),
 ],
 "faq": [
  ("¿Es NoArk una alternativa privada a Google Gemini?", "Sí. NoArk te da IA de modelos de frontera sin cuenta de Google y sin recopilación de datos: tus conversaciones se quedan en tu propio dispositivo y en tu propio iCloud, sin usarse nunca para entrenar ningún modelo. Apple la etiqueta como «No se recopilan datos». Además recurre a muchos modelos — incluido Gemini — y es una súper app de Apple completa."),
  ("¿NoArk usa mis datos para anuncios?", "No. NoArk no muestra anuncios y nunca monetiza tu atención ni tus datos. No tiene negocio publicitario y no recopila datos — la etiqueta de privacidad de Apple dice «No se recopilan datos». Te sirve solo a ti."),
  ("¿NoArk también usa Gemini?", "Sí — Gemini es uno de los varios modelos de frontera a los que NoArk puede recurrir, junto a Claude (Fable) de Anthropic, DeepSeek, Mistral y Kimi. Obtienes capacidad de nivel Gemini cuando es la mejor herramienta, pero tu contenido no se almacena en nuestros servidores ni se vincula a un perfil publicitario de Google."),
  ("¿NoArk necesita una cuenta de Google o registro?", "No. No hay cuenta de ningún tipo — ni inicio de sesión de Google, ni correo, ni número de teléfono. Descargas NoArk y empiezas, y nada vincula lo que preguntas con quién eres."),
  ("¿Es NoArk gratis?", "NoArk es gratis en iPhone, iPad, Mac y Apple Vision, con compras opcionales dentro de la app. No hace falta cuenta ni recopilación de datos para empezar."),
 ],
}

# ---------------- French ----------------
hp, gp, cp, ap, fp, pp = rel("fr")
content["fr"] = {
 "title": "NoArk vs Google Gemini : une IA privée qui vous sert, vous, pas un business publicitaire",
 "desc": "Comparatif NoArk vs Google Gemini : à qui sert l'IA, confidentialité, modèles d'IA et prix. NoArk ne collecte aucune donnée et garde chaque conversation sur votre propre appareil — sans compte Google, sans publicité. Elle fait appel à de nombreux modèles de pointe (oui, Gemini en fait partie) et ajoute des versions IA des plus grands esprits de l'histoire. Gratuit sur iPhone, iPad, Mac et Apple Vision.",
 "keywords": "NoArk vs Gemini, alternative à Google Gemini, Gemini privé, IA sans compte Google, IA sans publicité, IA sur l'appareil, app IA multi-modèles, alternative à Gemini iPhone, Claude Fable, DeepSeek, Mistral, Kimi, alternative gratuite à Gemini",
 "ogdesc": "En quoi NoArk diffère de Google Gemini : elle ne sert que vous — sans publicité, sans collecte de données, conversations sur votre appareil — fait appel à de nombreux modèles de pointe (Gemini compris) et c'est une super app Apple.",
 "twdesc": "Elle ne sert que vous — sans publicité, sans collecte de données, conversations sur votre appareil — de nombreux modèles de pointe (Gemini compris) et une super app Apple.",
 "h1": "NoArk vs Google Gemini",
 "subtitle": "Les deux sont de puissants assistants IA. Une seule ne collecte rien, n'affiche aucune publicité et ne répond qu'à vous — tout en utilisant Gemini comme l'un de ses nombreux modèles.",
 "intro": "Google Gemini est un assistant capable — conçu par une entreprise dont le cœur de métier est la publicité, et intégré au compte Google qui vous suit déjà sur le web. <strong>NoArk — Infinity Memory</strong> répond à un autre maître : <strong>vous</strong>. Sans publicité, sans collecte de données, chaque conversation sur votre propre appareil — et elle fait tout de même appel à <strong>de nombreux modèles de pointe, Gemini compris</strong>. Voici la comparaison honnête.",
 "glance": "En un coup d'œil",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("À qui sert l'IA", "<span class='yes'>À vous seul</span> — ne monétise jamais votre attention ni vos données ; 50 % des profits promis à l'éducation", "Conçue par Google, dont le cœur de métier est la publicité ; intégrée au plus large écosystème Google"),
  ("Vos conversations", "<span class='yes'>Stockées uniquement sur votre appareil</span> et dans votre propre iCloud — jamais entreposées ni utilisées pour entraîner", "Liées à votre compte Google ; l'activité peut être examinée et servir à améliorer les services de Google"),
  ("Collecte de données", "<span class='yes'>Aucune</span> — étiquette de confidentialité d'Apple : « Données non collectées »", "Collecte des données de compte, d'usage et de conversation"),
  ("Inscription requise", "<span class='yes'>Non</span> — pas de compte, d'e-mail ni de numéro de téléphone", "Nécessite un compte Google"),
  ("Modèles d'IA", "<span class='yes'>De nombreux modèles de pointe</span> — Claude Fable, DeepSeek, Mistral, Kimi et Gemini — le meilleur pour chaque tâche", "Uniquement les modèles Gemini de Google"),
  ("Les plus grands esprits de l'histoire", "<span class='yes'>Oui</span> — Fiat Lux : des versions IA de Charlie Munger, Steve Jobs, Einstein, Marc Aurèle et plus de 40 autres, ancrées dans leur vraie façon de raisonner", "Un unique assistant généraliste"),
  ("Au-delà du chat", "Une super app Apple complète — actualité en direct avec analyse en un geste, marchés, productivité, voyage, éducation et plus de 40 flux de travail, sur iPhone, iPad, Mac et Vision", "Un assistant réparti dans les apps et services de Google"),
  ("Prix", "<span class='yes'>Gratuit</span> (achats intégrés optionnels)", "Offre gratuite ; forfaits payants pour plus"),
 ],
 "note": "Comparaison fondée sur des informations publiques en juin 2026. Google et Gemini sont des marques de Google LLC ; NoArk est une app indépendante, ni affiliée ni approuvée par celle-ci.",
 "sections": [
  ("Pour qui l'IA travaille", [
   "C'est la différence qui compte le plus. Le cœur de métier de Google est la <strong>publicité</strong>, et Gemini vit dans le même compte qui enregistre déjà vos recherches, vos e-mails et votre navigation. NoArk n'a aucun business publicitaire et rien à vendre : elle <strong>ne sert que vous</strong>, ne monétise jamais votre attention ni vos données, et promet 50 % de ses profits à l'éducation.",
   "Concrètement, cela signifie <strong>aucune inscription</strong> — pas de compte Google, pas d'e-mail, pas de numéro de téléphone — et vos conversations <strong>stockées uniquement sur votre appareil et dans votre propre iCloud</strong>. L'étiquette officielle de confidentialité d'Apple pour NoArk indique <a href='" + pp + "'>« Données non collectées »</a>, la plus stricte qui soit.",
  ]),
  ("Oui, NoArk utilise aussi Gemini — comme l'un de ses nombreux modèles", [
   "Vous n'avez pas à renoncer aux forces de Gemini pour avoir la confidentialité. NoArk route chaque requête vers le meilleur de <strong>nombreux modèles de pointe</strong> — Claude (Fable) d'Anthropic, DeepSeek, Mistral, Kimi et Gemini de Google notamment — vous obtenez donc une capacité de niveau Gemini quand c'est le bon outil, sans être lié à un seul fournisseur. La différence : votre contenu passe par les API de ces modèles sans être stocké sur nos serveurs ni rattaché à un profil publicitaire.",
  ]),
  ("Plus qu'un assistant : une super app Apple privée", [
   "Gemini est un assistant réparti dans les apps de Google. NoArk est une <strong>super app Apple complète</strong> pour iPhone, iPad, Mac et Apple Vision : actualité mondiale en direct avec analyse en un geste, plus de 40 flux de travail prêts à l'emploi couvrant marchés, productivité, voyage, éducation et gestion du quotidien, et un cerveau d'investisseur créé par l'équipe de TradingTransformer, inspiré par la vision de Claude Shannon d'une IA qui choisit les actions. Son onglet <strong>Fiat Lux</strong> vous laisse apporter de vraies questions à des versions IA des plus grands esprits de l'histoire — Charlie Munger, Steve Jobs, Marc Aurèle et plus de 40 autres — ancrées dans leur vraie façon de raisonner.",
  ]),
 ],
 "related_heading": "À lire ensuite",
 "related": [
  (hp, "NoArk — Infinity Memory : l'OS intelligent et la super app IA"),
  (gp, "NoArk vs ChatGPT"),
  (cp, "NoArk vs Character.AI"),
  (ap, "NoArk vs Apple Intelligence"),
  (fp, "Questions fréquentes sur NoArk"),
 ],
 "faq": [
  ("NoArk est-elle une alternative privée à Google Gemini ?", "Oui. NoArk vous offre une IA de modèles de pointe sans compte Google et sans collecte de données : vos conversations restent sur votre propre appareil et dans votre propre iCloud, jamais utilisées pour entraîner un modèle. Apple l'étiquette « Données non collectées ». Elle fait aussi appel à de nombreux modèles — Gemini compris — et c'est une super app Apple complète."),
  ("NoArk utilise-t-elle mes données pour la publicité ?", "Non. NoArk n'affiche aucune publicité et ne monétise jamais votre attention ni vos données. Elle n'a aucun business publicitaire et ne collecte aucune donnée — l'étiquette de confidentialité d'Apple indique « Données non collectées ». Elle ne sert que vous."),
  ("NoArk utilise-t-elle aussi Gemini ?", "Oui — Gemini est l'un des nombreux modèles de pointe que NoArk peut solliciter, aux côtés de Claude (Fable) d'Anthropic, DeepSeek, Mistral et Kimi. Vous obtenez une capacité de niveau Gemini quand c'est le meilleur outil, mais votre contenu n'est pas stocké sur nos serveurs ni rattaché à un profil publicitaire Google."),
  ("NoArk nécessite-t-elle un compte Google ou une inscription ?", "Non. Il n'y a aucun compte — pas de connexion Google, pas d'e-mail, pas de numéro de téléphone. Vous téléchargez NoArk et commencez, et rien ne relie ce que vous demandez à qui vous êtes."),
  ("NoArk est-elle gratuite ?", "NoArk est gratuite sur iPhone, iPad, Mac et Apple Vision, avec des achats intégrés optionnels. Aucun compte ni aucune collecte de données n'est nécessaire pour commencer."),
 ],
}

# ---------------- Japanese ----------------
hp, gp, cp, ap, fp, pp = rel("ja")
content["ja"] = {
 "title": "NoArk vs Google Gemini：広告ビジネスではなく、あなたに仕えるプライベートAI",
 "desc": "NoArk と Google Gemini を比較：AIが誰に仕えるか、プライバシー、AIモデル、価格。NoArk はデータを収集せず、すべての会話をあなたのデバイスに保ちます — Google アカウント不要、広告なし。多数のフロンティアモデル（はい、Gemini もそのひとつ）を使い分け、歴史上の賢人のAI版も備えます。iPhone・iPad・Mac・Apple Vision で無料。",
 "keywords": "NoArk vs Gemini, Google Gemini 代替, プライベート Gemini, Google アカウント不要 AI, 広告なし AI, オンデバイス AI, マルチモデルAIアプリ, Gemini 代替 iPhone, Claude Fable, DeepSeek, Mistral, Kimi, 無料 Gemini 代替",
 "ogdesc": "NoArk が Google Gemini と違う点：あなただけに仕える — 広告なし、データ収集なし、会話はあなたのデバイスに — 多数のフロンティアモデル（Gemini を含む）を使い分け、しかも Apple スーパーアプリ。",
 "twdesc": "あなただけに仕える — 広告なし、データ収集なし、会話はあなたのデバイスに — 多数のフロンティアモデル（Gemini を含む）、しかも Apple スーパーアプリ。",
 "h1": "NoArk vs Google Gemini",
 "subtitle": "どちらも強力なAIアシスタントです。しかし、何も収集せず、広告を出さず、あなただけに応えるのは一方だけ — しかも Gemini を多数のモデルのひとつとして使います。",
 "intro": "Google Gemini は有能なアシスタントです — ただし、中核事業が広告である企業が作り、すでにウェブ上であなたを追う Google アカウントに組み込まれています。<strong>NoArk — Infinity Memory</strong> が仕える相手は違います。<strong>あなた</strong>です。広告なし、データ収集なし、すべての会話はあなた自身のデバイスに — それでいて<strong>多数のフロンティアモデル（Gemini を含む）</strong>を活用します。これが率直な比較です。",
 "glance": "ひと目でわかる比較",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("AIが誰に仕えるか", "<span class='yes'>あなただけ</span> — 注意もデータも収益化しません。利益の50%を教育に寄付", "中核事業が広告である Google が開発。広範な Google エコシステムの一部"),
  ("あなたの会話", "<span class='yes'>あなたのデバイス</span>とあなた自身の iCloud だけに保存 — 蓄積も学習利用もされません", "あなたの Google アカウントに紐づき、活動が確認され Google のサービス改善に使われることがあります"),
  ("データ収集", "<span class='yes'>なし</span> — Apple のプライバシーラベル：「データは収集されません」", "アカウント・利用状況・会話のデータを収集"),
  ("サインイン", "<span class='yes'>不要</span> — アカウントもメールも電話番号も不要", "Google アカウントが必要"),
  ("AIモデル", "<span class='yes'>多数のフロンティアモデル</span> — Claude Fable、DeepSeek、Mistral、Kimi、Gemini — タスクごとに最適なものを選択", "Google の Gemini モデルのみ"),
  ("歴史上の賢人", "<span class='yes'>あり</span> — Fiat Lux：チャーリー・マンガー、スティーブ・ジョブズ、アインシュタイン、マルクス・アウレリウスほか40名以上のAI版。実際の考え方に基づく", "単一の汎用アシスタント"),
  ("チャットの先", "フル機能の Apple スーパーアプリ — ワンタップ分析つきライブニュース、市場、生産性、旅行、教育、40以上のワークフロー。iPhone・iPad・Mac・Vision 対応", "Google のアプリやサービスにまたがるアシスタント"),
  ("価格", "<span class='yes'>無料</span>（オプションのアプリ内課金あり）", "無料プラン。さらに使うには有料プラン"),
 ],
 "note": "本比較は2026年6月時点の公開情報に基づきます。Google と Gemini は Google LLC の商標です。NoArk は独立したアプリであり、提携や承認はありません。",
 "sections": [
  ("AIは誰のために働くか", [
   "これが最も重要な違いです。Google の中核事業は<strong>広告</strong>であり、Gemini は、あなたの検索・メール・閲覧をすでに記録している同じアカウントの中にあります。NoArk には広告事業も、売るものもありません。<strong>あなただけに仕え</strong>、注意もデータも決して収益化せず、利益の50%を教育に寄付します。",
   "具体的には、<strong>サインインなし</strong> — Google アカウントもメールも電話番号もなく — あなたの会話は<strong>あなたのデバイスとあなた自身の iCloud だけに保存</strong>されます。Apple 公式の NoArk のプライバシーラベルは <a href='" + pp + "'>「データは収集されません」</a> — 最も厳格なラベルです。",
  ]),
  ("はい、NoArk も Gemini を使います — 多数のうちのひとつとして", [
   "プライバシーのために Gemini の強みを手放す必要はありません。NoArk は各リクエストを<strong>多数のフロンティアモデル</strong> — Anthropic の Claude（Fable）、DeepSeek、Mistral、Kimi、Google の Gemini など — の中で最適なものへ振り分けます。だから適切な場面では Gemini 級の能力が得られ、単一のプロバイダーに縛られません。違いはこうです。あなたのコンテンツはこれらのモデルの API を通りますが、私たちのサーバーに保存されることも、広告プロファイルに紐づけられることもありません。",
  ]),
  ("アシスタント以上：プライベートな Apple スーパーアプリ", [
   "Gemini は Google のアプリにまたがるアシスタントです。NoArk は iPhone・iPad・Mac・Apple Vision のための<strong>フル機能の Apple スーパーアプリ</strong>です。ワンタップ分析つきのライブ世界ニュース、市場・生産性・旅行・教育・生活の雑務にわたる40以上の即戦力ワークフロー、そして TradingTransformer チームが作り、クロード・シャノンのAI株式選択のビジョンに着想を得た投資する頭脳。<strong>Fiat Lux</strong> タブでは、本当の問いを歴史上の賢人のAI版 — チャーリー・マンガー、スティーブ・ジョブズ、マルクス・アウレリウスほか40名以上 — に持ち込めます。いずれも実際の考え方に基づいています。",
  ]),
 ],
 "related_heading": "あわせて読む",
 "related": [
  (hp, "NoArk — Infinity Memory：インテリジェントAI OS・スーパーアプリ"),
  (gp, "NoArk vs ChatGPT"),
  (cp, "NoArk vs Character.AI"),
  (ap, "NoArk vs Apple Intelligence"),
  (fp, "NoArk についてのよくある質問"),
 ],
 "faq": [
  ("NoArk はプライベートな Google Gemini の代替になりますか？", "はい。NoArk は Google アカウントなし・データ収集なしでフロンティアモデルのAIを提供します。会話はあなた自身のデバイスとあなた自身の iCloud に残り、どのモデルの学習にも使われません。Apple のラベルは「データは収集されません」です。さらに多数のモデル（Gemini を含む）を使い分け、フル機能の Apple スーパーアプリでもあります。"),
  ("NoArk は私のデータを広告に使いますか？", "いいえ。NoArk は広告を出さず、あなたの注意もデータも決して収益化しません。広告事業はなく、データも収集しません — Apple のプライバシーラベルは「データは収集されません」です。あなただけに仕えます。"),
  ("NoArk も Gemini を使いますか？", "はい — Gemini は、NoArk が振り分けられる複数のフロンティアモデルのひとつで、Anthropic の Claude（Fable）、DeepSeek、Mistral、Kimi と並びます。最適な場面では Gemini 級の能力が得られますが、あなたのコンテンツは私たちのサーバーに保存されることも、Google の広告プロファイルに紐づけられることもありません。"),
  ("NoArk は Google アカウントやサインインが必要ですか？", "いいえ。いかなるアカウントも不要です — Google サインインもメールも電話番号も不要。NoArk をダウンロードしてすぐに始められ、あなたの尋ねることとあなたの身元を結び付けるものは何もありません。"),
  ("NoArk は無料ですか？", "NoArk は iPhone・iPad・Mac・Apple Vision で無料で、オプションのアプリ内課金があります。始めるのにアカウントもデータ収集も不要です。"),
 ],
}

# ---------------- Simplified Chinese ----------------
hp, gp, cp, ap, fp, pp = rel("zh-cn")
content["zh-cn"] = {
 "title": "NoArk 对比 Google Gemini：为你服务、而非为广告生意服务的私密 AI",
 "desc": "NoArk 与 Google Gemini 全面对比：AI 为谁服务、隐私、AI 模型与价格。NoArk 不收集数据，把每段对话都留在你自己的设备上——无需 Google 账户、没有广告。它调用多个前沿模型（没错，Gemini 就是其中之一），并加入历史智者的 AI 版本。iPhone、iPad、Mac 和 Apple Vision 免费下载。",
 "keywords": "NoArk 对比 Gemini, Google Gemini 替代品, 私密 Gemini, 无需 Google 账户的 AI, 无广告 AI, 端侧 AI, 多模型 AI 应用, Gemini 替代 iPhone, Claude Fable, DeepSeek, Mistral, Kimi, 免费 Gemini 替代品",
 "ogdesc": "NoArk 与 Google Gemini 的不同：只为你服务——没有广告、不收集数据、对话留在你自己的设备上——调用多个前沿模型（含 Gemini），而且是一款 Apple 超级应用。",
 "twdesc": "只为你服务——没有广告、不收集数据、对话留在你自己的设备上——多个前沿模型（含 Gemini），而且是一款 Apple 超级应用。",
 "h1": "NoArk 对比 Google Gemini",
 "subtitle": "两者都是强大的 AI 助手。但只有一个什么都不收集、不展示广告、只对你负责——同时仍把 Gemini 作为多个模型之一来使用。",
 "intro": "Google Gemini 是个能干的助手——但它由一家核心业务是广告的公司打造，并嵌入那个早已在全网跟随你的 Google 账户。<strong>NoArk — 无限记忆</strong>效忠的是另一个主人：<strong>你</strong>。没有广告、不收集数据、每段对话都留在你自己的设备上——而且它依然调用<strong>多个前沿模型，包括 Gemini</strong>。下面是坦诚的对比。",
 "glance": "一览对比",
 "col_noark": "NoArk — 无限记忆",
 "rows": [
  ("AI 为谁服务", "<span class='yes'>只为你</span>——绝不把你的注意力或数据变现；将利润的 50% 捐给教育", "由核心业务是广告的 Google 打造；是更广阔 Google 生态的一部分"),
  ("你的对话", "<span class='yes'>只保存在你的设备</span>和你自己的 iCloud 中——绝不堆放或用于训练", "与你的 Google 账户绑定；活动可能被审阅并用于改进 Google 的服务"),
  ("数据收集", "<span class='yes'>无</span>——Apple 隐私标签：“不收集数据”", "收集账户、使用和对话数据"),
  ("是否需要登录", "<span class='yes'>不需要</span>——无账户、邮箱或手机号", "需要 Google 账户"),
  ("AI 模型", "<span class='yes'>多个前沿模型</span>——Claude Fable、DeepSeek、Mistral、Kimi 和 Gemini——为每个任务挑选最合适的", "仅 Google 的 Gemini 模型"),
  ("历史上的智者", "<span class='yes'>有</span>——Fiat Lux：查理·芒格、史蒂夫·乔布斯、爱因斯坦、马可·奥勒留等 40 多位的 AI 版本，立足于他们真实的思考方式", "单一的通用助手"),
  ("聊天之外", "一款完整的 Apple 超级应用——带一键分析的实时头条、市场、生产力、旅行、教育和 40 多个工作流，支持 iPhone、iPad、Mac 和 Vision", "一个遍布 Google 应用与服务的助手"),
  ("价格", "<span class='yes'>免费</span>下载（含可选的应用内购买）", "免费档；更多功能需付费"),
 ],
 "note": "对比基于截至 2026 年 6 月的公开信息。Google 和 Gemini 是 Google LLC 的商标；NoArk 是独立应用，与其无关联，也未获其背书。",
 "sections": [
  ("AI 为谁工作", [
   "这是最重要的区别。Google 的核心业务是<strong>广告</strong>，而 Gemini 就在那个早已记录你的搜索、邮件和浏览的同一账户里。NoArk 没有广告生意，也没有什么要卖给你：它<strong>只为你服务</strong>，绝不把你的注意力或数据变现，并将利润的 50% 捐给教育。",
   "具体来说，这意味着<strong>无需登录</strong>——没有 Google 账户、没有邮箱、没有手机号——你的对话<strong>只保存在你的设备和你自己的 iCloud 中</strong>。Apple 官方为 NoArk 出具的隐私标签写着 <a href='" + pp + "'>“不收集数据”</a>——最严格的一档。",
  ]),
  ("没错，NoArk 也用 Gemini——作为多个模型之一", [
   "你不必为了隐私而放弃 Gemini 的强项。NoArk 把每个请求路由到<strong>多个前沿模型</strong>中最合适的一个——包括 Anthropic 的 Claude（Fable）、DeepSeek、Mistral、Kimi 和谷歌的 Gemini——所以在合适的场景你能获得 Gemini 级别的能力，又不被单一供应商绑定。区别在于：你的内容会经过这些模型的 API，但不会存放在我们的服务器上，也不会与广告画像绑定。",
  ]),
  ("不只是助手：一款私密的 Apple 超级应用", [
   "Gemini 是一个遍布 Google 应用的助手。NoArk 则是一款面向 iPhone、iPad、Mac 和 Apple Vision 的<strong>完整 Apple 超级应用</strong>：带一键分析的实时全球头条，涵盖市场、生产力、旅行、教育和生活事务的 40 多个开箱即用工作流，以及由 TradingTransformer 团队打造、灵感来自克劳德·香农 AI 选股愿景的投资大脑。它的 <strong>Fiat Lux</strong> 标签让你把真实的问题带给历史上最有智慧的人的 AI 版本——查理·芒格、史蒂夫·乔布斯、马可·奥勒留等 40 多位——每一位都立足于他们真实的思考方式。",
  ]),
 ],
 "related_heading": "继续阅读",
 "related": [
  (hp, "NoArk — 无限记忆：智能 AI 操作系统与超级应用"),
  (gp, "NoArk 对比 ChatGPT"),
  (cp, "NoArk 对比 Character.AI"),
  (ap, "NoArk 对比 Apple Intelligence"),
  (fp, "关于 NoArk 的常见问题"),
 ],
 "faq": [
  ("NoArk 是私密的 Google Gemini 替代品吗？", "是的。NoArk 在没有 Google 账户、不收集数据的前提下为你提供前沿模型 AI：你的对话留在你自己的设备和你自己的 iCloud 中，绝不用于训练任何模型。Apple 的标签是“不收集数据”。它还调用多个模型——包括 Gemini——并且是一款完整的 Apple 超级应用。"),
  ("NoArk 会用我的数据做广告吗？", "不会。NoArk 不展示广告，也绝不把你的注意力或数据变现。它没有广告生意，也不收集数据——Apple 的隐私标签写着“不收集数据”。它只为你服务。"),
  ("NoArk 也用 Gemini 吗？", "是的——Gemini 是 NoArk 可以路由到的多个前沿模型之一，与 Anthropic 的 Claude（Fable）、DeepSeek、Mistral 和 Kimi 并列。在最合适的场景你能获得 Gemini 级别的能力，但你的内容不会存放在我们的服务器上，也不会与 Google 的广告画像绑定。"),
  ("NoArk 需要 Google 账户或登录吗？", "不需要。没有任何账户——没有 Google 登录、没有邮箱、没有手机号。你下载 NoArk 即可开始，没有任何东西把你提的问题和你的身份绑定。"),
  ("NoArk 免费吗？", "NoArk 在 iPhone、iPad、Mac 和 Apple Vision 上免费下载，含可选的应用内购买。开始使用无需账户，也不收集数据。"),
 ],
}

# ---------------- Traditional Chinese ----------------
hp, gp, cp, ap, fp, pp = rel("zh-tw")
content["zh-tw"] = {
 "title": "NoArk 對比 Google Gemini：為你服務、而非為廣告生意服務的私密 AI",
 "desc": "NoArk 與 Google Gemini 全面對比：AI 為誰服務、隱私、AI 模型與價格。NoArk 不收集資料，把每段對話都留在你自己的裝置上——無需 Google 帳號、沒有廣告。它調用多個前沿模型（沒錯，Gemini 就是其中之一），並加入歷史智者的 AI 版本。iPhone、iPad、Mac 和 Apple Vision 免費下載。",
 "keywords": "NoArk 對比 Gemini, Google Gemini 替代品, 私密 Gemini, 無需 Google 帳號的 AI, 無廣告 AI, 端側 AI, 多模型 AI 應用程式, Gemini 替代 iPhone, Claude Fable, DeepSeek, Mistral, Kimi, 免費 Gemini 替代品",
 "ogdesc": "NoArk 與 Google Gemini 的不同：只為你服務——沒有廣告、不收集資料、對話留在你自己的裝置上——調用多個前沿模型（含 Gemini），而且是一款 Apple 超級應用程式。",
 "twdesc": "只為你服務——沒有廣告、不收集資料、對話留在你自己的裝置上——多個前沿模型（含 Gemini），而且是一款 Apple 超級應用程式。",
 "h1": "NoArk 對比 Google Gemini",
 "subtitle": "兩者都是強大的 AI 助手。但只有一個什麼都不收集、不展示廣告、只對你負責——同時仍把 Gemini 作為多個模型之一來使用。",
 "intro": "Google Gemini 是個能幹的助手——但它由一家核心業務是廣告的公司打造，並嵌入那個早已在全網跟隨你的 Google 帳號。<strong>NoArk — 無限記憶</strong>效忠的是另一個主人：<strong>你</strong>。沒有廣告、不收集資料、每段對話都留在你自己的裝置上——而且它依然調用<strong>多個前沿模型，包括 Gemini</strong>。以下是坦誠的對比。",
 "glance": "一覽對比",
 "col_noark": "NoArk — 無限記憶",
 "rows": [
  ("AI 為誰服務", "<span class='yes'>只為你</span>——絕不把你的注意力或資料變現；將利潤的 50% 捐給教育", "由核心業務是廣告的 Google 打造；是更廣闊 Google 生態的一部分"),
  ("你的對話", "<span class='yes'>只保存在你的裝置</span>和你自己的 iCloud 中——絕不堆放或用於訓練", "與你的 Google 帳號綁定；活動可能被審閱並用於改進 Google 的服務"),
  ("資料收集", "<span class='yes'>無</span>——Apple 隱私標籤：「不收集資料」", "收集帳號、使用和對話資料"),
  ("是否需要登入", "<span class='yes'>不需要</span>——無帳號、電子郵件或手機號碼", "需要 Google 帳號"),
  ("AI 模型", "<span class='yes'>多個前沿模型</span>——Claude Fable、DeepSeek、Mistral、Kimi 和 Gemini——為每個任務挑選最合適的", "僅 Google 的 Gemini 模型"),
  ("歷史上的智者", "<span class='yes'>有</span>——Fiat Lux：查理·蒙格、史蒂夫·賈伯斯、愛因斯坦、馬可·奧理略等 40 多位的 AI 版本，立足於他們真實的思考方式", "單一的通用助手"),
  ("聊天之外", "一款完整的 Apple 超級應用程式——帶一鍵分析的即時頭條、市場、生產力、旅行、教育和 40 多個工作流程，支援 iPhone、iPad、Mac 和 Vision", "一個遍布 Google 應用與服務的助手"),
  ("價格", "<span class='yes'>免費</span>下載（含可選的應用程式內購買）", "免費檔；更多功能需付費"),
 ],
 "note": "對比基於截至 2026 年 6 月的公開資訊。Google 和 Gemini 是 Google LLC 的商標；NoArk 是獨立應用程式，與其無關聯，也未獲其背書。",
 "sections": [
  ("AI 為誰工作", [
   "這是最重要的區別。Google 的核心業務是<strong>廣告</strong>，而 Gemini 就在那個早已記錄你的搜尋、郵件和瀏覽的同一帳號裡。NoArk 沒有廣告生意，也沒有什麼要賣給你：它<strong>只為你服務</strong>，絕不把你的注意力或資料變現，並將利潤的 50% 捐給教育。",
   "具體來說，這意味著<strong>無需登入</strong>——沒有 Google 帳號、沒有電子郵件、沒有手機號碼——你的對話<strong>只保存在你的裝置和你自己的 iCloud 中</strong>。Apple 官方為 NoArk 出具的隱私標籤寫著 <a href='" + pp + "'>「不收集資料」</a>——最嚴格的一檔。",
  ]),
  ("沒錯，NoArk 也用 Gemini——作為多個模型之一", [
   "你不必為了隱私而放棄 Gemini 的強項。NoArk 把每個請求路由到<strong>多個前沿模型</strong>中最合適的一個——包括 Anthropic 的 Claude（Fable）、DeepSeek、Mistral、Kimi 和 Google 的 Gemini——所以在合適的場景你能獲得 Gemini 級別的能力，又不被單一供應商綁定。區別在於：你的內容會經過這些模型的 API，但不會存放在我們的伺服器上，也不會與廣告畫像綁定。",
  ]),
  ("不只是助手：一款私密的 Apple 超級應用程式", [
   "Gemini 是一個遍布 Google 應用的助手。NoArk 則是一款面向 iPhone、iPad、Mac 和 Apple Vision 的<strong>完整 Apple 超級應用程式</strong>：帶一鍵分析的即時全球頭條，涵蓋市場、生產力、旅行、教育和生活事務的 40 多個開箱即用工作流程，以及由 TradingTransformer 團隊打造、靈感來自克勞德·夏農 AI 選股願景的投資大腦。它的 <strong>Fiat Lux</strong> 分頁讓你把真實的問題帶給歷史上最有智慧的人的 AI 版本——查理·蒙格、史蒂夫·賈伯斯、馬可·奧理略等 40 多位——每一位都立足於他們真實的思考方式。",
  ]),
 ],
 "related_heading": "繼續閱讀",
 "related": [
  (hp, "NoArk — 無限記憶：智慧型 AI 作業系統與超級應用程式"),
  (gp, "NoArk 對比 ChatGPT"),
  (cp, "NoArk 對比 Character.AI"),
  (ap, "NoArk 對比 Apple Intelligence"),
  (fp, "關於 NoArk 的常見問題"),
 ],
 "faq": [
  ("NoArk 是私密的 Google Gemini 替代品嗎？", "是的。NoArk 在沒有 Google 帳號、不收集資料的前提下為你提供前沿模型 AI：你的對話留在你自己的裝置和你自己的 iCloud 中，絕不用於訓練任何模型。Apple 的標籤是「不收集資料」。它還調用多個模型——包括 Gemini——並且是一款完整的 Apple 超級應用程式。"),
  ("NoArk 會用我的資料做廣告嗎？", "不會。NoArk 不展示廣告，也絕不把你的注意力或資料變現。它沒有廣告生意，也不收集資料——Apple 的隱私標籤寫著「不收集資料」。它只為你服務。"),
  ("NoArk 也用 Gemini 嗎？", "是的——Gemini 是 NoArk 可以路由到的多個前沿模型之一，與 Anthropic 的 Claude（Fable）、DeepSeek、Mistral 和 Kimi 並列。在最合適的場景你能獲得 Gemini 級別的能力，但你的內容不會存放在我們的伺服器上，也不會與 Google 的廣告畫像綁定。"),
  ("NoArk 需要 Google 帳號或登入嗎？", "不需要。沒有任何帳號——沒有 Google 登入、沒有電子郵件、沒有手機號碼。你下載 NoArk 即可開始，沒有任何東西把你提的問題和你的身分綁定。"),
  ("NoArk 免費嗎？", "NoArk 在 iPhone、iPad、Mac 和 Apple Vision 上免費下載，含可選的應用程式內購買。開始使用無需帳號，也不收集資料。"),
 ],
}

render(SLUG, COMP, content)
