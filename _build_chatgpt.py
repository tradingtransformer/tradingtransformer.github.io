# -*- coding: utf-8 -*-
from _compare_lib import render

SLUG = "noark-vs-chatgpt.html"
COMP = "ChatGPT"

def rel(p):
    base = "/" + (p + "/" if p else "")
    return (base,                                   # hp home
            base + "noark-vs-character-ai.html",     # cp character.ai
            base + "noark-vs-apple-intelligence.html",  # ap apple
            base + "#faq",                           # fp faq
            base + "#data-privacy")                  # pp privacy

content = {}

# ---------------- English ----------------
hp, cp, ap, fp, pp = rel("")
content[""] = {
 "title": "NoArk vs ChatGPT: A Private, Multi-Model AI App With No Sign-In",
 "desc": "NoArk vs ChatGPT compared: sign-in, who your data serves, which AI models, and price. NoArk needs no account, keeps every conversation on your own device, routes to many frontier models — Claude's Fable, DeepSeek, Mistral, Kimi, Gemini — and is a full Apple super app with AI versions of history's wisest minds. Free on iPhone, iPad, Mac & Apple Vision.",
 "keywords": "NoArk vs ChatGPT, ChatGPT alternative, private ChatGPT, AI without sign-in, AI without account, on-device AI, multi-model AI app, ChatGPT alternative iPhone, Claude Fable, DeepSeek, Mistral, Kimi, Gemini, free ChatGPT alternative",
 "ogdesc": "How NoArk differs from ChatGPT: no account or sign-in, your chats stay on your own device, it routes to many frontier models instead of one, and it's a full Apple super app — not just a chatbox.",
 "twdesc": "No account, your chats stay on your own device, many frontier models instead of one, and a full Apple super app — not just a chatbox.",
 "h1": "NoArk vs ChatGPT",
 "subtitle": "Both answer almost anything. Only one asks for no account, keeps every conversation on your device, and picks the best of many AI models for each task.",
 "intro": "ChatGPT made conversational AI mainstream. <strong>NoArk — Infinity Memory</strong> keeps what's great about it and removes the trade-offs people quietly accept: <strong>no account, nothing collected, your conversations on your own device</strong>, and the freedom of <strong>many frontier models</strong> instead of one. It's also a full Apple super app, with AI versions of history's wisest minds. Here's the honest comparison.",
 "glance": "At a glance",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("Sign-in required", "<span class='yes'>No</span> — no account, email, or phone number", "Requires an account to use"),
  ("Your conversations", "<span class='yes'>Stored only on your device</span> and in your own iCloud — never warehoused or used to train", "Sent to the company's servers; by default may be used to improve its models (opt-out available)"),
  ("Data collection", "<span class='yes'>None</span> — Apple's App Privacy label: “Data Not Collected”", "Collects account, usage, and conversation data"),
  ("AI models", "<span class='yes'>Many frontier models</span> — Claude's Fable, DeepSeek, Mistral, Kimi, Gemini — the best picked per task", "OpenAI's own GPT models only"),
  ("History's wisest minds", "<span class='yes'>Yes</span> — Fiat Lux: AI versions of Charlie Munger, Steve Jobs, Einstein, Marcus Aurelius &amp; 40+ more, grounded in how they actually reasoned", "A single general-purpose assistant"),
  ("Beyond chat", "A full Apple super app — live headlines with one-tap analysis, markets, productivity, travel, education &amp; 40+ workflows, on iPhone, iPad, Mac &amp; Vision", "Chat plus built-in tools"),
  ("Business model", "Serves only you — never monetizes your attention or data; 50% of app profits pledged to education", "Subscription and a free tier, plus a growing agent &amp; enterprise business"),
  ("Price", "<span class='yes'>Free</span> to download (optional in-app purchases)", "Free tier; paid plans for more"),
 ],
 "note": "Comparison reflects publicly available information as of June 2026. ChatGPT is a trademark of OpenAI; NoArk is an independent app and is not affiliated with or endorsed by it.",
 "sections": [
  ("No account, nothing collected", [
   "To use ChatGPT you create an account, and your conversations are sent to the company's servers — by default they can be used to improve its models. NoArk takes the opposite path: there's <strong>no sign-in at all</strong> — no email, no phone number — and your chats are <strong>stored only on your device and in your own iCloud</strong>, never warehoused on our servers and never used to train anyone's model.",
   "Apple's official App Privacy label for NoArk reads <a href='" + pp + "'>“Data Not Collected”</a>, the strictest there is. The most personal questions you ask an AI never become someone else's training data.",
  ]),
  ("Many frontier models, not locked to one", [
   "ChatGPT can only ever be as good as OpenAI's own GPT models. NoArk isn't tied to a single provider: it routes each request to the best of <strong>many frontier models</strong> — Anthropic's Claude (Fable), DeepSeek, Mistral, Kimi, and Google's Gemini among them — so the thinking behind each answer is the strongest available for that task, not whatever one lab shipped last.",
  ]),
  ("More than a chatbox: a native Apple super app", [
   "ChatGPT is, at heart, a chat window. NoArk is a <strong>full Apple super app</strong> built for iPhone, iPad, Mac, and Apple Vision: live global headlines with one-tap analysis, 40+ ready-made workflows across markets, productivity, travel, education, and life admin, and an investing brain built by the team behind TradingTransformer, inspired by Claude Shannon's vision of AI stock-picking. Its <strong>Fiat Lux</strong> tab lets you bring real questions to AI versions of history's wisest minds — Charlie Munger, Steve Jobs, Marcus Aurelius, and 40+ more — grounded in how they actually reasoned.",
   "It's part of the same shift toward proactive, autonomous AI agents that products like Manus point to — but kept private, on your own device, and woven into the apps you already use.",
  ]),
 ],
 "related_heading": "Keep reading",
 "related": [
  (hp, "NoArk — Infinity Memory: the intelligent AI OS & super app"),
  (cp, "NoArk vs Character.AI"),
  (hp + "noark-vs-gemini.html", "NoArk vs Gemini"),
  (ap, "NoArk vs Apple Intelligence"),
  (fp, "Frequently asked questions about NoArk"),
 ],
 "faq": [
  ("Is NoArk a private ChatGPT alternative?", "Yes. NoArk answers almost anything ChatGPT can, but with no account and no data collection: your conversations stay on your own device and in your own iCloud, never used to train any model. Apple labels it “Data Not Collected.” It also routes to many frontier models and is a full Apple super app."),
  ("Does NoArk need a login like ChatGPT?", "No. There's no sign-in — no email, no phone number, no account at all. You can download NoArk and start immediately, and nothing ties what you ask to who you are."),
  ("Which AI models does NoArk use vs ChatGPT?", "ChatGPT uses OpenAI's own GPT models. NoArk isn't locked to one provider — it routes each request to the best of many frontier models, including Anthropic's Claude (Fable), DeepSeek, Mistral, Kimi, and Google's Gemini."),
  ("Does NoArk train on my conversations?", "No. Your conversations are stored only on your device and in your own iCloud — never warehoused on our servers and never used to train models. When NoArk calls frontier models through their APIs, your content isn't stored or used to train them either."),
  ("Is NoArk free?", "NoArk is free to download on iPhone, iPad, Mac, and Apple Vision, with optional in-app purchases. There's no account and no data collection required to start."),
 ],
}

# ---------------- Spanish ----------------
hp, cp, ap, fp, pp = rel("es")
content["es"] = {
 "title": "NoArk vs ChatGPT: una IA privada y multimodelo, sin registro",
 "desc": "Comparativa NoArk vs ChatGPT: registro, a quién sirven tus datos, qué modelos de IA y precio. NoArk no necesita cuenta, mantiene cada conversación en tu propio dispositivo, recurre a muchos modelos de frontera — Claude Fable, DeepSeek, Mistral, Kimi, Gemini — y es una súper app de Apple con versiones de IA de las mentes más sabias de la historia. Gratis en iPhone, iPad, Mac y Apple Vision.",
 "keywords": "NoArk vs ChatGPT, alternativa a ChatGPT, ChatGPT privado, IA sin registro, IA sin cuenta, IA en el dispositivo, app de IA multimodelo, alternativa a ChatGPT iPhone, Claude Fable, DeepSeek, Mistral, Kimi, Gemini, alternativa gratis a ChatGPT",
 "ogdesc": "En qué se diferencia NoArk de ChatGPT: sin cuenta ni registro, tus chats se quedan en tu propio dispositivo, recurre a muchos modelos de frontera en lugar de uno, y es una súper app de Apple — no solo un chat.",
 "twdesc": "Sin cuenta, tus chats se quedan en tu dispositivo, muchos modelos de frontera en lugar de uno, y una súper app de Apple — no solo un chat.",
 "h1": "NoArk vs ChatGPT",
 "subtitle": "Ambas responden casi cualquier cosa. Solo una no pide cuenta, mantiene cada conversación en tu dispositivo y elige el mejor de muchos modelos de IA para cada tarea.",
 "intro": "ChatGPT popularizó la IA conversacional. <strong>NoArk — Infinity Memory</strong> conserva lo bueno y elimina las concesiones que la gente acepta en silencio: <strong>sin cuenta, sin recopilación, tus conversaciones en tu propio dispositivo</strong>, y la libertad de <strong>muchos modelos de frontera</strong> en lugar de uno. Además es una súper app de Apple, con versiones de IA de las mentes más sabias de la historia. Esta es la comparación honesta.",
 "glance": "De un vistazo",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("Registro obligatorio", "<span class='yes'>No</span> — sin cuenta, correo ni número de teléfono", "Requiere una cuenta para usarlo"),
  ("Tus conversaciones", "<span class='yes'>Guardadas solo en tu dispositivo</span> y en tu propio iCloud — nunca almacenadas ni usadas para entrenar", "Enviadas a los servidores de la empresa; por defecto pueden usarse para mejorar sus modelos (con opción de exclusión)"),
  ("Recopilación de datos", "<span class='yes'>Ninguna</span> — etiqueta de privacidad de Apple: «No se recopilan datos»", "Recopila datos de cuenta, uso y conversaciones"),
  ("Modelos de IA", "<span class='yes'>Muchos modelos de frontera</span> — Claude Fable, DeepSeek, Mistral, Kimi, Gemini — el mejor para cada tarea", "Solo los modelos GPT propios de OpenAI"),
  ("Las mentes más sabias de la historia", "<span class='yes'>Sí</span> — Fiat Lux: versiones de IA de Charlie Munger, Steve Jobs, Einstein, Marco Aurelio y más de 40, basadas en cómo razonaban de verdad", "Un único asistente de uso general"),
  ("Más allá del chat", "Una súper app de Apple completa — titulares en directo con análisis de un toque, mercados, productividad, viajes, educación y más de 40 flujos de trabajo, en iPhone, iPad, Mac y Vision", "Chat más herramientas integradas"),
  ("Modelo de negocio", "Te sirve solo a ti — nunca monetiza tu atención ni tus datos; el 50% de los beneficios se destina a educación", "Suscripción y un nivel gratuito, además de un creciente negocio de agentes y empresas"),
  ("Precio", "<span class='yes'>Gratis</span> (compras opcionales dentro de la app)", "Nivel gratuito; planes de pago para más"),
 ],
 "note": "Comparativa basada en información pública a junio de 2026. ChatGPT es una marca de OpenAI; NoArk es una app independiente, no afiliada ni respaldada por aquella.",
 "sections": [
  ("Sin cuenta, sin recopilar nada", [
   "Para usar ChatGPT creas una cuenta, y tus conversaciones se envían a los servidores de la empresa — por defecto pueden usarse para mejorar sus modelos. NoArk hace lo contrario: <strong>no hay registro alguno</strong> — ni correo ni número de teléfono — y tus chats se <strong>guardan solo en tu dispositivo y en tu propio iCloud</strong>, nunca almacenados en nuestros servidores ni usados para entrenar el modelo de nadie.",
   "La etiqueta oficial de privacidad de Apple para NoArk dice <a href='" + pp + "'>«No se recopilan datos»</a>, la más estricta que existe. Las preguntas más personales que le haces a una IA nunca se convierten en datos de entrenamiento de otro.",
  ]),
  ("Muchos modelos de frontera, no atado a uno", [
   "ChatGPT solo puede ser tan bueno como los propios modelos GPT de OpenAI. NoArk no está atado a un único proveedor: dirige cada petición al mejor de <strong>muchos modelos de frontera</strong> — Claude (Fable) de Anthropic, DeepSeek, Mistral, Kimi y Gemini de Google entre ellos — para que el razonamiento detrás de cada respuesta sea el más fuerte disponible para esa tarea, no lo último que lanzó un solo laboratorio.",
  ]),
  ("Más que un chat: una súper app nativa de Apple", [
   "ChatGPT es, en esencia, una ventana de chat. NoArk es una <strong>súper app de Apple completa</strong> para iPhone, iPad, Mac y Apple Vision: titulares globales en directo con análisis de un toque, más de 40 flujos de trabajo listos que abarcan mercados, productividad, viajes, educación y gestión diaria, y un cerebro inversor creado por el equipo de TradingTransformer, inspirado en la visión de Claude Shannon sobre la IA que elige acciones. Su pestaña <strong>Fiat Lux</strong> te deja llevar preguntas reales a versiones de IA de las mentes más sabias de la historia — Charlie Munger, Steve Jobs, Marco Aurelio y más de 40 — basadas en cómo razonaban de verdad.",
   "Forma parte del mismo giro hacia agentes de IA proactivos y autónomos que apuntan productos como Manus — pero mantenido en privado, en tu propio dispositivo, e integrado en las apps que ya usas.",
  ]),
 ],
 "related_heading": "Sigue leyendo",
 "related": [
  (hp, "NoArk — Infinity Memory: el SO inteligente y súper app de IA"),
  (cp, "NoArk vs Character.AI"),
  (hp + "noark-vs-gemini.html", "NoArk vs Gemini"),
  (ap, "NoArk vs Apple Intelligence"),
  (fp, "Preguntas frecuentes sobre NoArk"),
 ],
 "faq": [
  ("¿Es NoArk una alternativa privada a ChatGPT?", "Sí. NoArk responde casi todo lo que responde ChatGPT, pero sin cuenta y sin recopilación de datos: tus conversaciones se quedan en tu propio dispositivo y en tu propio iCloud, sin usarse nunca para entrenar ningún modelo. Apple la etiqueta como «No se recopilan datos». Además recurre a muchos modelos de frontera y es una súper app de Apple completa."),
  ("¿NoArk necesita iniciar sesión como ChatGPT?", "No. No hay registro — ni correo, ni número de teléfono, ni cuenta alguna. Puedes descargar NoArk y empezar de inmediato, y nada vincula lo que preguntas con quién eres."),
  ("¿Qué modelos de IA usa NoArk frente a ChatGPT?", "ChatGPT usa los propios modelos GPT de OpenAI. NoArk no está atado a un único proveedor — dirige cada petición al mejor de muchos modelos de frontera, incluidos Claude (Fable) de Anthropic, DeepSeek, Mistral, Kimi y Gemini de Google."),
  ("¿NoArk entrena con mis conversaciones?", "No. Tus conversaciones se guardan solo en tu dispositivo y en tu propio iCloud — nunca almacenadas en nuestros servidores ni usadas para entrenar modelos. Cuando NoArk llama a modelos de frontera por sus API, tu contenido tampoco se almacena ni se usa para entrenarlos."),
  ("¿Es NoArk gratis?", "NoArk es gratis en iPhone, iPad, Mac y Apple Vision, con compras opcionales dentro de la app. No hace falta cuenta ni recopilación de datos para empezar."),
 ],
}

# ---------------- French ----------------
hp, cp, ap, fp, pp = rel("fr")
content["fr"] = {
 "title": "NoArk vs ChatGPT : une IA privée et multi-modèles, sans inscription",
 "desc": "Comparatif NoArk vs ChatGPT : inscription, à qui servent vos données, quels modèles d'IA et prix. NoArk ne demande aucun compte, garde chaque conversation sur votre propre appareil, fait appel à de nombreux modèles de pointe — Claude Fable, DeepSeek, Mistral, Kimi, Gemini — et c'est une super app Apple avec des versions IA des plus grands esprits de l'histoire. Gratuit sur iPhone, iPad, Mac et Apple Vision.",
 "keywords": "NoArk vs ChatGPT, alternative à ChatGPT, ChatGPT privé, IA sans inscription, IA sans compte, IA sur l'appareil, app IA multi-modèles, alternative à ChatGPT iPhone, Claude Fable, DeepSeek, Mistral, Kimi, Gemini, alternative gratuite à ChatGPT",
 "ogdesc": "En quoi NoArk diffère de ChatGPT : aucun compte ni inscription, vos conversations restent sur votre appareil, elle fait appel à de nombreux modèles de pointe plutôt qu'à un seul, et c'est une super app Apple — pas seulement une fenêtre de chat.",
 "twdesc": "Aucun compte, vos conversations restent sur votre appareil, de nombreux modèles de pointe plutôt qu'un seul, et une super app Apple — pas seulement un chat.",
 "h1": "NoArk vs ChatGPT",
 "subtitle": "Les deux répondent à presque tout. Une seule ne demande aucun compte, garde chaque conversation sur votre appareil et choisit le meilleur de nombreux modèles d'IA pour chaque tâche.",
 "intro": "ChatGPT a popularisé l'IA conversationnelle. <strong>NoArk — Infinity Memory</strong> en garde le meilleur et supprime les compromis que l'on accepte en silence : <strong>aucun compte, rien de collecté, vos conversations sur votre propre appareil</strong>, et la liberté de <strong>nombreux modèles de pointe</strong> plutôt qu'un seul. C'est aussi une super app Apple, avec des versions IA des plus grands esprits de l'histoire. Voici la comparaison honnête.",
 "glance": "En un coup d'œil",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("Inscription requise", "<span class='yes'>Non</span> — pas de compte, d'e-mail ni de numéro de téléphone", "Nécessite un compte pour l'utiliser"),
  ("Vos conversations", "<span class='yes'>Stockées uniquement sur votre appareil</span> et dans votre propre iCloud — jamais entreposées ni utilisées pour entraîner", "Envoyées aux serveurs de l'entreprise ; par défaut, peuvent servir à améliorer ses modèles (option de retrait)"),
  ("Collecte de données", "<span class='yes'>Aucune</span> — étiquette de confidentialité d'Apple : « Données non collectées »", "Collecte des données de compte, d'usage et de conversation"),
  ("Modèles d'IA", "<span class='yes'>De nombreux modèles de pointe</span> — Claude Fable, DeepSeek, Mistral, Kimi, Gemini — le meilleur pour chaque tâche", "Uniquement les modèles GPT maison d'OpenAI"),
  ("Les plus grands esprits de l'histoire", "<span class='yes'>Oui</span> — Fiat Lux : des versions IA de Charlie Munger, Steve Jobs, Einstein, Marc Aurèle et plus de 40 autres, ancrées dans leur vraie façon de raisonner", "Un unique assistant généraliste"),
  ("Au-delà du chat", "Une super app Apple complète — actualité en direct avec analyse en un geste, marchés, productivité, voyage, éducation et plus de 40 flux de travail, sur iPhone, iPad, Mac et Vision", "Chat et outils intégrés"),
  ("Modèle économique", "Ne sert que vous — ne monétise jamais votre attention ni vos données ; 50 % des profits promis à l'éducation", "Abonnement et offre gratuite, plus un business croissant d'agents et d'entreprises"),
  ("Prix", "<span class='yes'>Gratuit</span> (achats intégrés optionnels)", "Offre gratuite ; forfaits payants pour plus"),
 ],
 "note": "Comparaison fondée sur des informations publiques en juin 2026. ChatGPT est une marque d'OpenAI ; NoArk est une app indépendante, ni affiliée ni approuvée par celle-ci.",
 "sections": [
  ("Aucun compte, rien de collecté", [
   "Pour utiliser ChatGPT, vous créez un compte, et vos conversations sont envoyées aux serveurs de l'entreprise — par défaut, elles peuvent servir à améliorer ses modèles. NoArk fait l'inverse : il n'y a <strong>aucune inscription</strong> — pas d'e-mail, pas de numéro de téléphone — et vos conversations sont <strong>stockées uniquement sur votre appareil et dans votre propre iCloud</strong>, jamais entreposées sur nos serveurs ni utilisées pour entraîner le modèle de qui que ce soit.",
   "L'étiquette officielle de confidentialité d'Apple pour NoArk indique <a href='" + pp + "'>« Données non collectées »</a>, la plus stricte qui soit. Les questions les plus personnelles que vous posez à une IA ne deviennent jamais les données d'entraînement d'un autre.",
  ]),
  ("De nombreux modèles de pointe, sans en dépendre d'un seul", [
   "ChatGPT ne peut jamais être meilleur que les propres modèles GPT d'OpenAI. NoArk n'est pas lié à un seul fournisseur : il route chaque requête vers le meilleur de <strong>nombreux modèles de pointe</strong> — Claude (Fable) d'Anthropic, DeepSeek, Mistral, Kimi et Gemini de Google notamment — pour que le raisonnement derrière chaque réponse soit le plus solide disponible pour cette tâche, et non ce qu'un seul laboratoire a livré en dernier.",
  ]),
  ("Plus qu'un chat : une super app Apple native", [
   "ChatGPT est, au fond, une fenêtre de chat. NoArk est une <strong>super app Apple complète</strong> pour iPhone, iPad, Mac et Apple Vision : actualité mondiale en direct avec analyse en un geste, plus de 40 flux de travail prêts à l'emploi couvrant marchés, productivité, voyage, éducation et gestion du quotidien, et un cerveau d'investisseur créé par l'équipe de TradingTransformer, inspiré par la vision de Claude Shannon d'une IA qui choisit les actions. Son onglet <strong>Fiat Lux</strong> vous laisse apporter de vraies questions à des versions IA des plus grands esprits de l'histoire — Charlie Munger, Steve Jobs, Marc Aurèle et plus de 40 autres — ancrées dans leur vraie façon de raisonner.",
   "Cela s'inscrit dans le même tournant vers des agents IA proactifs et autonomes que pointent des produits comme Manus — mais en restant privé, sur votre propre appareil, et intégré aux apps que vous utilisez déjà.",
  ]),
 ],
 "related_heading": "À lire ensuite",
 "related": [
  (hp, "NoArk — Infinity Memory : l'OS intelligent et la super app IA"),
  (cp, "NoArk vs Character.AI"),
  (hp + "noark-vs-gemini.html", "NoArk vs Gemini"),
  (ap, "NoArk vs Apple Intelligence"),
  (fp, "Questions fréquentes sur NoArk"),
 ],
 "faq": [
  ("NoArk est-elle une alternative privée à ChatGPT ?", "Oui. NoArk répond à presque tout ce que ChatGPT sait faire, mais sans compte ni collecte de données : vos conversations restent sur votre propre appareil et dans votre propre iCloud, jamais utilisées pour entraîner un modèle. Apple l'étiquette « Données non collectées ». Elle fait aussi appel à de nombreux modèles de pointe et c'est une super app Apple complète."),
  ("NoArk nécessite-t-elle une connexion comme ChatGPT ?", "Non. Il n'y a aucune inscription — pas d'e-mail, pas de numéro de téléphone, aucun compte. Vous pouvez télécharger NoArk et commencer immédiatement, et rien ne relie ce que vous demandez à qui vous êtes."),
  ("Quels modèles d'IA NoArk utilise-t-elle face à ChatGPT ?", "ChatGPT utilise les propres modèles GPT d'OpenAI. NoArk n'est pas lié à un seul fournisseur — il route chaque requête vers le meilleur de nombreux modèles de pointe, dont Claude (Fable) d'Anthropic, DeepSeek, Mistral, Kimi et Gemini de Google."),
  ("NoArk s'entraîne-t-elle sur mes conversations ?", "Non. Vos conversations sont stockées uniquement sur votre appareil et dans votre propre iCloud — jamais entreposées sur nos serveurs ni utilisées pour entraîner des modèles. Quand NoArk appelle des modèles de pointe via leurs API, votre contenu n'est pas non plus stocké ni utilisé pour les entraîner."),
  ("NoArk est-elle gratuite ?", "NoArk est gratuite sur iPhone, iPad, Mac et Apple Vision, avec des achats intégrés optionnels. Aucun compte ni aucune collecte de données n'est nécessaire pour commencer."),
 ],
}

# ---------------- Japanese ----------------
hp, cp, ap, fp, pp = rel("ja")
content["ja"] = {
 "title": "NoArk vs ChatGPT：サインイン不要・マルチモデルのプライベートAIアプリ",
 "desc": "NoArk と ChatGPT を比較：サインイン、データが誰のために働くか、どのAIモデルか、価格。NoArk はアカウント不要で、すべての会話をあなたのデバイスに保ち、多数のフロンティアモデル — Claude Fable、DeepSeek、Mistral、Kimi、Gemini — を使い分け、歴史上の賢人のAI版を備えた Apple スーパーアプリです。iPhone・iPad・Mac・Apple Vision で無料。",
 "keywords": "NoArk vs ChatGPT, ChatGPT 代替, プライベート ChatGPT, サインイン不要 AI, アカウント不要 AI, オンデバイス AI, マルチモデルAIアプリ, ChatGPT 代替 iPhone, Claude Fable, DeepSeek, Mistral, Kimi, Gemini, 無料 ChatGPT 代替",
 "ogdesc": "NoArk が ChatGPT と違う点：アカウントもサインインも不要、会話はあなたのデバイスに残り、単一ではなく多数のフロンティアモデルを使い分け、しかも Apple スーパーアプリ — 単なるチャット画面ではありません。",
 "twdesc": "アカウント不要、会話はあなたのデバイスに残り、単一ではなく多数のフロンティアモデル、しかも Apple スーパーアプリ — 単なるチャット画面ではありません。",
 "h1": "NoArk vs ChatGPT",
 "subtitle": "どちらもほぼ何でも答えます。しかし、アカウントを求めず、すべての会話をデバイスに保ち、タスクごとに多数のAIモデルから最適なものを選ぶのは一方だけです。",
 "intro": "ChatGPT は対話型AIを広めました。<strong>NoArk — Infinity Memory</strong> はその良さを保ちつつ、人々が黙って受け入れている妥協を取り除きます。<strong>アカウント不要、収集なし、会話はあなた自身のデバイスに</strong>、そして単一ではなく<strong>多数のフロンティアモデル</strong>を使える自由。さらに歴史上の賢人のAI版を備えた Apple スーパーアプリでもあります。これが率直な比較です。",
 "glance": "ひと目でわかる比較",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("サインイン", "<span class='yes'>不要</span> — アカウントもメールも電話番号も不要", "利用にアカウントが必要"),
  ("あなたの会話", "<span class='yes'>あなたのデバイス</span>とあなた自身の iCloud だけに保存 — 蓄積も学習利用もされません", "企業のサーバーに送信。既定ではモデル改善に使われることがあります（オプトアウト可）"),
  ("データ収集", "<span class='yes'>なし</span> — Apple のプライバシーラベル：「データは収集されません」", "アカウント・利用状況・会話のデータを収集"),
  ("AIモデル", "<span class='yes'>多数のフロンティアモデル</span> — Claude Fable、DeepSeek、Mistral、Kimi、Gemini — タスクごとに最適なものを選択", "OpenAI 独自の GPT モデルのみ"),
  ("歴史上の賢人", "<span class='yes'>あり</span> — Fiat Lux：チャーリー・マンガー、スティーブ・ジョブズ、アインシュタイン、マルクス・アウレリウスほか40名以上のAI版。実際の考え方に基づく", "単一の汎用アシスタント"),
  ("チャットの先", "フル機能の Apple スーパーアプリ — ワンタップ分析つきライブニュース、市場、生産性、旅行、教育、40以上のワークフロー。iPhone・iPad・Mac・Vision 対応", "チャットと内蔵ツール"),
  ("ビジネスモデル", "あなただけに仕える — 注意もデータも収益化しません。利益の50%を教育に寄付", "サブスクと無料プラン、さらに拡大するエージェント・法人事業"),
  ("価格", "<span class='yes'>無料</span>（オプションのアプリ内課金あり）", "無料プラン。さらに使うには有料プラン"),
 ],
 "note": "本比較は2026年6月時点の公開情報に基づきます。ChatGPT は OpenAI の商標です。NoArk は独立したアプリであり、提携や承認はありません。",
 "sections": [
  ("アカウント不要、何も収集しない", [
   "ChatGPT を使うにはアカウントを作成し、会話は企業のサーバーに送られます — 既定ではモデル改善に使われることがあります。NoArk は逆です。<strong>サインインは一切不要</strong> — メールも電話番号もなく — あなたの会話は<strong>あなたのデバイスとあなた自身の iCloud だけに保存</strong>され、私たちのサーバーに蓄積されることも、誰のモデルの学習に使われることもありません。",
   "Apple 公式の NoArk のプライバシーラベルは <a href='" + pp + "'>「データは収集されません」</a> — 最も厳格なラベルです。AIに尋ねる最も個人的な問いが、他社の学習データになることは決してありません。",
  ]),
  ("多数のフロンティアモデル、ひとつに縛られない", [
   "ChatGPT は、OpenAI 自身の GPT モデルの良さ以上にはなれません。NoArk は単一のプロバイダーに縛られません。各リクエストを<strong>多数のフロンティアモデル</strong> — Anthropic の Claude（Fable）、DeepSeek、Mistral、Kimi、Google の Gemini など — の中で最適なものへ振り分けるため、各回答の背後にある思考は、ある研究所が最後に出したものではなく、そのタスクに対して利用できる最も強いものです。",
  ]),
  ("チャット画面以上：ネイティブな Apple スーパーアプリ", [
   "ChatGPT は本質的にチャット画面です。NoArk は iPhone・iPad・Mac・Apple Vision のための<strong>フル機能の Apple スーパーアプリ</strong>です。ワンタップ分析つきのライブ世界ニュース、市場・生産性・旅行・教育・生活の雑務にわたる40以上の即戦力ワークフロー、そして TradingTransformer チームが作り、クロード・シャノンのAI株式選択のビジョンに着想を得た投資する頭脳。<strong>Fiat Lux</strong> タブでは、本当の問いを歴史上の賢人のAI版 — チャーリー・マンガー、スティーブ・ジョブズ、マルクス・アウレリウスほか40名以上 — に持ち込めます。いずれも実際の考え方に基づいています。",
   "これは Manus のような製品が示す、能動的で自律的なAIエージェントへの同じ流れの一部です — ただしプライベートに、あなた自身のデバイスで、すでに使っているアプリに織り込まれています。",
  ]),
 ],
 "related_heading": "あわせて読む",
 "related": [
  (hp, "NoArk — Infinity Memory：インテリジェントAI OS・スーパーアプリ"),
  (cp, "NoArk vs Character.AI"),
  (hp + "noark-vs-gemini.html", "NoArk vs Gemini"),
  (ap, "NoArk vs Apple Intelligence"),
  (fp, "NoArk についてのよくある質問"),
 ],
 "faq": [
  ("NoArk はプライベートな ChatGPT の代替になりますか？", "はい。NoArk は ChatGPT ができることのほとんどに答えますが、アカウント不要・データ収集なしです。会話はあなた自身のデバイスとあなた自身の iCloud に残り、どのモデルの学習にも使われません。Apple のラベルは「データは収集されません」です。さらに多数のフロンティアモデルを使い分け、フル機能の Apple スーパーアプリでもあります。"),
  ("NoArk は ChatGPT のようにログインが必要ですか？", "いいえ。サインインはありません — メールも電話番号も、アカウントも一切不要です。NoArk をダウンロードしてすぐに始められ、あなたの尋ねることとあなたの身元を結び付けるものは何もありません。"),
  ("NoArk は ChatGPT と比べてどのAIモデルを使いますか？", "ChatGPT は OpenAI 自身の GPT モデルを使います。NoArk は単一のプロバイダーに縛られず、各リクエストを多数のフロンティアモデル — Anthropic の Claude（Fable）、DeepSeek、Mistral、Kimi、Google の Gemini を含む — の中で最適なものへ振り分けます。"),
  ("NoArk は私の会話で学習しますか？", "いいえ。あなたの会話はあなたのデバイスとあなた自身の iCloud だけに保存され、私たちのサーバーに蓄積されることも、モデルの学習に使われることもありません。NoArk が API 経由でフロンティアモデルを呼び出すときも、あなたのコンテンツは保存も学習利用もされません。"),
  ("NoArk は無料ですか？", "NoArk は iPhone・iPad・Mac・Apple Vision で無料で、オプションのアプリ内課金があります。始めるのにアカウントもデータ収集も不要です。"),
 ],
}

# ---------------- Simplified Chinese ----------------
hp, cp, ap, fp, pp = rel("zh-cn")
content["zh-cn"] = {
 "title": "NoArk 对比 ChatGPT：无需登录的私密多模型 AI 应用",
 "desc": "NoArk 与 ChatGPT 全面对比：登录、你的数据为谁服务、用哪些 AI 模型、价格。NoArk 无需账户，把每段对话都留在你自己的设备上，调用多个前沿模型——Claude Fable、DeepSeek、Mistral、Kimi、Gemini——并且是一款带有历史智者 AI 版本的 Apple 超级应用。iPhone、iPad、Mac 和 Apple Vision 免费下载。",
 "keywords": "NoArk 对比 ChatGPT, ChatGPT 替代品, 私密 ChatGPT, 无需登录的 AI, 无需账户的 AI, 端侧 AI, 多模型 AI 应用, ChatGPT 替代 iPhone, Claude Fable, DeepSeek, Mistral, Kimi, Gemini, 免费 ChatGPT 替代品",
 "ogdesc": "NoArk 与 ChatGPT 的不同：无需账户或登录，你的对话留在你自己的设备上，调用多个前沿模型而非单一一个，而且是一款 Apple 超级应用——不只是聊天框。",
 "twdesc": "无需账户，你的对话留在你自己的设备上，多个前沿模型而非单一一个，而且是一款 Apple 超级应用——不只是聊天框。",
 "h1": "NoArk 对比 ChatGPT",
 "subtitle": "两者几乎什么都能回答。但只有一个无需账户、把每段对话都留在你的设备上，并为每个任务从多个 AI 模型中挑选最合适的。",
 "intro": "ChatGPT 让对话式 AI 走向大众。<strong>NoArk — 无限记忆</strong>保留了它的优点，并去掉了人们默默接受的代价：<strong>无需账户、不收集、对话留在你自己的设备上</strong>，以及使用<strong>多个前沿模型</strong>而非单一一个的自由。它还是一款带有历史智者 AI 版本的 Apple 超级应用。下面是坦诚的对比。",
 "glance": "一览对比",
 "col_noark": "NoArk — 无限记忆",
 "rows": [
  ("是否需要登录", "<span class='yes'>不需要</span>——无账户、邮箱或手机号", "使用需要账户"),
  ("你的对话", "<span class='yes'>只保存在你的设备</span>和你自己的 iCloud 中——绝不堆放或用于训练", "发送到公司服务器；默认情况下可能用于改进其模型（可选择退出）"),
  ("数据收集", "<span class='yes'>无</span>——Apple 隐私标签：“不收集数据”", "收集账户、使用和对话数据"),
  ("AI 模型", "<span class='yes'>多个前沿模型</span>——Claude Fable、DeepSeek、Mistral、Kimi、Gemini——为每个任务挑选最合适的", "仅 OpenAI 自家的 GPT 模型"),
  ("历史上的智者", "<span class='yes'>有</span>——Fiat Lux：查理·芒格、史蒂夫·乔布斯、爱因斯坦、马可·奥勒留等 40 多位的 AI 版本，立足于他们真实的思考方式", "单一的通用助手"),
  ("聊天之外", "一款完整的 Apple 超级应用——带一键分析的实时头条、市场、生产力、旅行、教育和 40 多个工作流，支持 iPhone、iPad、Mac 和 Vision", "聊天加内置工具"),
  ("商业模式", "只为你服务——绝不把你的注意力或数据变现；将利润的 50% 捐给教育", "订阅与免费档，外加不断扩大的智能体与企业业务"),
  ("价格", "<span class='yes'>免费</span>下载（含可选的应用内购买）", "免费档；更多功能需付费"),
 ],
 "note": "对比基于截至 2026 年 6 月的公开信息。ChatGPT 是 OpenAI 的商标；NoArk 是独立应用，与其无关联，也未获其背书。",
 "sections": [
  ("无需账户，什么都不收集", [
   "使用 ChatGPT 需要创建账户，你的对话会发送到公司服务器——默认情况下它们可能用于改进其模型。NoArk 恰恰相反：<strong>完全无需登录</strong>——没有邮箱、没有手机号——你的对话<strong>只保存在你的设备和你自己的 iCloud 中</strong>，绝不堆放在我们的服务器上，也绝不用于训练任何人的模型。",
   "Apple 官方为 NoArk 出具的隐私标签写着 <a href='" + pp + "'>“不收集数据”</a>——最严格的一档。你向 AI 提出的最私密的问题，绝不会变成别人的训练数据。",
  ]),
  ("多个前沿模型，不被单一一个绑定", [
   "ChatGPT 再好，也只能和 OpenAI 自家的 GPT 模型一样好。NoArk 不绑定单一供应商：它把每个请求路由到<strong>多个前沿模型</strong>——包括 Anthropic 的 Claude（Fable）、DeepSeek、Mistral、Kimi 和谷歌的 Gemini——因此每个回答背后的思考都是该任务当下可用的最强者，而不是某个实验室最后发布的那个。",
  ]),
  ("不只是聊天框：一款原生的 Apple 超级应用", [
   "ChatGPT 本质上是一个聊天窗口。NoArk 则是一款面向 iPhone、iPad、Mac 和 Apple Vision 的<strong>完整 Apple 超级应用</strong>：带一键分析的实时全球头条，涵盖市场、生产力、旅行、教育和生活事务的 40 多个开箱即用工作流，以及由 TradingTransformer 团队打造、灵感来自克劳德·香农 AI 选股愿景的投资大脑。它的 <strong>Fiat Lux</strong> 标签让你把真实的问题带给历史上最有智慧的人的 AI 版本——查理·芒格、史蒂夫·乔布斯、马可·奥勒留等 40 多位——每一位都立足于他们真实的思考方式。",
   "这与 Manus 等产品所指向的、走向主动而自主的 AI 智能体的同一趋势一脉相承——但保持私密、留在你自己的设备上，并融入你已经在用的应用中。",
  ]),
 ],
 "related_heading": "继续阅读",
 "related": [
  (hp, "NoArk — 无限记忆：智能 AI 操作系统与超级应用"),
  (cp, "NoArk 对比 Character.AI"),
  (hp + "noark-vs-gemini.html", "NoArk 对比 Gemini"),
  (ap, "NoArk 对比 Apple Intelligence"),
  (fp, "关于 NoArk 的常见问题"),
 ],
 "faq": [
  ("NoArk 是私密的 ChatGPT 替代品吗？", "是的。NoArk 几乎能回答 ChatGPT 能回答的一切，但无需账户、不收集数据：你的对话留在你自己的设备和你自己的 iCloud 中，绝不用于训练任何模型。Apple 的标签是“不收集数据”。它还调用多个前沿模型，并且是一款完整的 Apple 超级应用。"),
  ("NoArk 像 ChatGPT 一样需要登录吗？", "不需要。没有登录——没有邮箱、没有手机号，也没有任何账户。你可以下载 NoArk 立即开始，没有任何东西把你提的问题和你的身份绑定。"),
  ("NoArk 相比 ChatGPT 用哪些 AI 模型？", "ChatGPT 用 OpenAI 自家的 GPT 模型。NoArk 不绑定单一供应商——它把每个请求路由到多个前沿模型中最合适的一个，包括 Anthropic 的 Claude（Fable）、DeepSeek、Mistral、Kimi 和谷歌的 Gemini。"),
  ("NoArk 会用我的对话训练吗？", "不会。你的对话只保存在你的设备和你自己的 iCloud 中——绝不堆放在我们的服务器上，也绝不用于训练模型。当 NoArk 通过 API 调用前沿模型时，你的内容同样不会被存储或用于训练它们。"),
  ("NoArk 免费吗？", "NoArk 在 iPhone、iPad、Mac 和 Apple Vision 上免费下载，含可选的应用内购买。开始使用无需账户，也不收集数据。"),
 ],
}

# ---------------- Traditional Chinese ----------------
hp, cp, ap, fp, pp = rel("zh-tw")
content["zh-tw"] = {
 "title": "NoArk 對比 ChatGPT：無需登入的私密多模型 AI 應用程式",
 "desc": "NoArk 與 ChatGPT 全面對比：登入、你的資料為誰服務、用哪些 AI 模型、價格。NoArk 無需帳號，把每段對話都留在你自己的裝置上，調用多個前沿模型——Claude Fable、DeepSeek、Mistral、Kimi、Gemini——並且是一款帶有歷史智者 AI 版本的 Apple 超級應用程式。iPhone、iPad、Mac 和 Apple Vision 免費下載。",
 "keywords": "NoArk 對比 ChatGPT, ChatGPT 替代品, 私密 ChatGPT, 無需登入的 AI, 無需帳號的 AI, 端側 AI, 多模型 AI 應用程式, ChatGPT 替代 iPhone, Claude Fable, DeepSeek, Mistral, Kimi, Gemini, 免費 ChatGPT 替代品",
 "ogdesc": "NoArk 與 ChatGPT 的不同：無需帳號或登入，你的對話留在你自己的裝置上，調用多個前沿模型而非單一一個，而且是一款 Apple 超級應用程式——不只是聊天框。",
 "twdesc": "無需帳號，你的對話留在你自己的裝置上，多個前沿模型而非單一一個，而且是一款 Apple 超級應用程式——不只是聊天框。",
 "h1": "NoArk 對比 ChatGPT",
 "subtitle": "兩者幾乎什麼都能回答。但只有一個無需帳號、把每段對話都留在你的裝置上，並為每個任務從多個 AI 模型中挑選最合適的。",
 "intro": "ChatGPT 讓對話式 AI 走向大眾。<strong>NoArk — 無限記憶</strong>保留了它的優點，並去掉了人們默默接受的代價：<strong>無需帳號、不收集、對話留在你自己的裝置上</strong>，以及使用<strong>多個前沿模型</strong>而非單一一個的自由。它還是一款帶有歷史智者 AI 版本的 Apple 超級應用程式。以下是坦誠的對比。",
 "glance": "一覽對比",
 "col_noark": "NoArk — 無限記憶",
 "rows": [
  ("是否需要登入", "<span class='yes'>不需要</span>——無帳號、電子郵件或手機號碼", "使用需要帳號"),
  ("你的對話", "<span class='yes'>只保存在你的裝置</span>和你自己的 iCloud 中——絕不堆放或用於訓練", "傳送到公司伺服器；預設情況下可能用於改進其模型（可選擇退出）"),
  ("資料收集", "<span class='yes'>無</span>——Apple 隱私標籤：「不收集資料」", "收集帳號、使用和對話資料"),
  ("AI 模型", "<span class='yes'>多個前沿模型</span>——Claude Fable、DeepSeek、Mistral、Kimi、Gemini——為每個任務挑選最合適的", "僅 OpenAI 自家的 GPT 模型"),
  ("歷史上的智者", "<span class='yes'>有</span>——Fiat Lux：查理·蒙格、史蒂夫·賈伯斯、愛因斯坦、馬可·奧理略等 40 多位的 AI 版本，立足於他們真實的思考方式", "單一的通用助手"),
  ("聊天之外", "一款完整的 Apple 超級應用程式——帶一鍵分析的即時頭條、市場、生產力、旅行、教育和 40 多個工作流程，支援 iPhone、iPad、Mac 和 Vision", "聊天加內建工具"),
  ("商業模式", "只為你服務——絕不把你的注意力或資料變現；將利潤的 50% 捐給教育", "訂閱與免費檔，外加不斷擴大的智慧代理與企業業務"),
  ("價格", "<span class='yes'>免費</span>下載（含可選的應用程式內購買）", "免費檔；更多功能需付費"),
 ],
 "note": "對比基於截至 2026 年 6 月的公開資訊。ChatGPT 是 OpenAI 的商標；NoArk 是獨立應用程式，與其無關聯，也未獲其背書。",
 "sections": [
  ("無需帳號，什麼都不收集", [
   "使用 ChatGPT 需要建立帳號，你的對話會傳送到公司伺服器——預設情況下它們可能用於改進其模型。NoArk 恰恰相反：<strong>完全無需登入</strong>——沒有電子郵件、沒有手機號碼——你的對話<strong>只保存在你的裝置和你自己的 iCloud 中</strong>，絕不堆放在我們的伺服器上，也絕不用於訓練任何人的模型。",
   "Apple 官方為 NoArk 出具的隱私標籤寫著 <a href='" + pp + "'>「不收集資料」</a>——最嚴格的一檔。你向 AI 提出的最私密的問題，絕不會變成別人的訓練資料。",
  ]),
  ("多個前沿模型，不被單一一個綁定", [
   "ChatGPT 再好，也只能和 OpenAI 自家的 GPT 模型一樣好。NoArk 不綁定單一供應商：它把每個請求路由到<strong>多個前沿模型</strong>——包括 Anthropic 的 Claude（Fable）、DeepSeek、Mistral、Kimi 和 Google 的 Gemini——因此每個回答背後的思考都是該任務當下可用的最強者，而不是某個實驗室最後發布的那個。",
  ]),
  ("不只是聊天框：一款原生的 Apple 超級應用程式", [
   "ChatGPT 本質上是一個聊天視窗。NoArk 則是一款面向 iPhone、iPad、Mac 和 Apple Vision 的<strong>完整 Apple 超級應用程式</strong>：帶一鍵分析的即時全球頭條，涵蓋市場、生產力、旅行、教育和生活事務的 40 多個開箱即用工作流程，以及由 TradingTransformer 團隊打造、靈感來自克勞德·夏農 AI 選股願景的投資大腦。它的 <strong>Fiat Lux</strong> 分頁讓你把真實的問題帶給歷史上最有智慧的人的 AI 版本——查理·蒙格、史蒂夫·賈伯斯、馬可·奧理略等 40 多位——每一位都立足於他們真實的思考方式。",
   "這與 Manus 等產品所指向的、走向主動而自主的 AI 智慧代理的同一趨勢一脈相承——但保持私密、留在你自己的裝置上，並融入你已經在用的應用程式中。",
  ]),
 ],
 "related_heading": "繼續閱讀",
 "related": [
  (hp, "NoArk — 無限記憶：智慧型 AI 作業系統與超級應用程式"),
  (cp, "NoArk 對比 Character.AI"),
  (hp + "noark-vs-gemini.html", "NoArk 對比 Gemini"),
  (ap, "NoArk 對比 Apple Intelligence"),
  (fp, "關於 NoArk 的常見問題"),
 ],
 "faq": [
  ("NoArk 是私密的 ChatGPT 替代品嗎？", "是的。NoArk 幾乎能回答 ChatGPT 能回答的一切，但無需帳號、不收集資料：你的對話留在你自己的裝置和你自己的 iCloud 中，絕不用於訓練任何模型。Apple 的標籤是「不收集資料」。它還調用多個前沿模型，並且是一款完整的 Apple 超級應用程式。"),
  ("NoArk 像 ChatGPT 一樣需要登入嗎？", "不需要。沒有登入——沒有電子郵件、沒有手機號碼，也沒有任何帳號。你可以下載 NoArk 立即開始，沒有任何東西把你提的問題和你的身分綁定。"),
  ("NoArk 相比 ChatGPT 用哪些 AI 模型？", "ChatGPT 用 OpenAI 自家的 GPT 模型。NoArk 不綁定單一供應商——它把每個請求路由到多個前沿模型中最合適的一個，包括 Anthropic 的 Claude（Fable）、DeepSeek、Mistral、Kimi 和 Google 的 Gemini。"),
  ("NoArk 會用我的對話訓練嗎？", "不會。你的對話只保存在你的裝置和你自己的 iCloud 中——絕不堆放在我們的伺服器上，也絕不用於訓練模型。當 NoArk 透過 API 呼叫前沿模型時，你的內容同樣不會被儲存或用於訓練它們。"),
  ("NoArk 免費嗎？", "NoArk 在 iPhone、iPad、Mac 和 Apple Vision 上免費下載，含可選的應用程式內購買。開始使用無需帳號，也不收集資料。"),
 ],
}

render(SLUG, COMP, content)
