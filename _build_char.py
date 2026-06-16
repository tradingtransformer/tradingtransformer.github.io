# -*- coding: utf-8 -*-
from _compare_lib import render

SLUG = "noark-vs-character-ai.html"
COMP = "Character.AI"

def rel(p):
    base = "/" + (p + "/" if p else "")
    return base, base + "noark-vs-apple-intelligence.html", base + "#faq", base + "#data-privacy"

content = {}

# ---------------- English ----------------
hp, ap, fp, pp = rel("")
content[""] = {
 "title": "NoArk vs Character.AI: A Private Way to Talk to History's Wisest Minds",
 "desc": "NoArk vs Character.AI compared: privacy, who your data serves, real historical minds vs fictional roleplay, AI models, and price. NoArk lets you ask AI versions of Charlie Munger, Steve Jobs, Einstein, Marcus Aurelius and 40+ more — keeping every conversation on your own device, with no sign-in. Free on iPhone, iPad, Mac & Apple Vision.",
 "keywords": "NoArk vs Character.AI, Character.AI alternative, private Character AI, talk to historical figures AI, AI Charlie Munger, AI Marcus Aurelius, on-device AI chat, AI without sign-in, multi-model AI app, Claude Fable, DeepSeek, Mistral, Kimi, Gemini",
 "ogdesc": "How NoArk differs from Character.AI: your chats stay on your own device, the minds are grounded in how real people actually reasoned, and it's a full life & markets super app — not just roleplay.",
 "twdesc": "Your chats stay on your own device, the minds are grounded in how real people actually reasoned, and it's a full super app — not just roleplay.",
 "h1": "NoArk vs Character.AI",
 "subtitle": "Both let you chat with a cast of characters. Only one keeps every conversation private — and grounds its minds in how real people actually thought.",
 "intro": "Character.AI made talking to AI personalities mainstream. <strong>NoArk — Infinity Memory</strong> takes the idea somewhere more useful and more private: instead of fictional roleplay, you bring the real questions in your life to AI versions of history's wisest minds — and nothing you say is harvested. Here's the honest comparison.",
 "glance": "At a glance",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("Who you talk to", "AI versions of <strong>real historical minds</strong> — Charlie Munger, Steve Jobs, Einstein, da Vinci, Marcus Aurelius &amp; 40+ more, grounded in how they actually reasoned", "User-created and fictional characters, of variable quality"),
  ("Your conversations", "<span class='yes'>Stored only on your device</span> and in your own iCloud — never warehoused or used to train", "Sent to company servers and used to improve and train the service"),
  ("Data collection", "<span class='yes'>None</span> — Apple's App Privacy label: “Data Not Collected”", "Collects account, usage, and conversation data"),
  ("Sign-in required", "<span class='yes'>No</span> — no account, email, or phone number", "Requires an account"),
  ("AI models", "<span class='yes'>Many frontier models</span> — Claude's Fable, DeepSeek, Mistral, Kimi, Gemini — the best picked per task", "Character.AI's own in-house models"),
  ("Beyond chat", "A full AI super app — markets, productivity, travel, education, live headlines &amp; 40+ workflows", "Primarily character chat and roleplay"),
  ("Business model", "Serves only you — never monetizes your attention or data; 50% of app profits pledged to education", "Subscription and ads, built around engagement"),
  ("Price", "<span class='yes'>Free</span> to download (optional in-app purchases)", "Free tier with a paid subscription"),
 ],
 "note": "Comparison reflects publicly available information as of June 2026. Character.AI is a trademark of its respective owner; NoArk is an independent app and is not affiliated with or endorsed by it.",
 "sections": [
  ("Privacy: your conversations stay yours", [
   "The questions you bring to an AI character are often the most personal things you'll ever type — doubts, decisions, things you can't say out loud. With Character.AI, those conversations live on company servers and help train the service. NoArk takes the opposite path: your chats are <strong>stored only on your device and in your own iCloud</strong>, never warehoused on our servers and never used to train anyone's model.",
   "There's <strong>no sign-in</strong> — no email, no phone number, nothing that ties what you said to who you are. Apple's official App Privacy label for NoArk reads <a href='" + pp + "'>“Data Not Collected”</a>, the strictest there is.",
  ]),
  ("Real minds, grounded — not fictional roleplay", [
   "Character.AI is built for open-ended roleplay with user-created bots of wildly variable quality. NoArk's <strong>Fiat Lux</strong> tab is built for <strong>counsel</strong>: you bring a real question to AI versions of history's wisest minds — Charlie Munger, Steve Jobs, Albert Einstein, Leonardo da Vinci, Marcus Aurelius, and 40+ more — each grounded in how that person actually reasoned, not an improvised persona.",
   "And because NoArk routes to many <strong>frontier models</strong> — Claude's Fable, DeepSeek, Mistral, Kimi, Gemini — the thinking behind each answer is as strong as today's best AI, not a single in-house model.",
  ]),
  ("More than a chat app: a full life & markets super app", [
   "Character.AI mostly stops at conversation. NoArk is also a <strong>full AI super app</strong>: live global headlines with one-tap analysis, 40+ ready-made workflows across markets, productivity, travel, education, and life admin, and an investing brain built by the team behind TradingTransformer, inspired by Claude Shannon's vision of AI stock-picking. You can chat by <strong>text, voice, photo, or file</strong> — including PDFs, spreadsheets, and URLs.",
  ]),
 ],
 "related_heading": "Keep reading",
 "related": [
  (hp, "NoArk — Infinity Memory: the intelligent AI OS & super app"),
  (hp + "noark-vs-chatgpt.html", "NoArk vs ChatGPT"),
  (hp + "noark-vs-gemini.html", "NoArk vs Gemini"),
  (hp + "noark-vs-perplexity.html", "NoArk vs Perplexity"),
  (ap, "NoArk vs Apple Intelligence"),
  (hp + "noark-vs-manus.html", "NoArk vs Manus"),
  (fp, "Frequently asked questions about NoArk"),
 ],
 "faq": [
  ("Is NoArk a good Character.AI alternative?", "Yes, especially if you care about privacy and substance. NoArk lets you talk to AI versions of history's wisest minds — Charlie Munger, Steve Jobs, Marcus Aurelius, and 40+ more — while keeping every conversation on your own device with no sign-in. It's also a full life and markets super app, not just roleplay. Apple labels it “Data Not Collected.”"),
  ("Does NoArk train on or store my chats?", "No. Your conversations are stored only on your device and in your own iCloud — never warehoused on our servers and never used to train models. When NoArk calls frontier models through their APIs, your content isn't stored or used to train them either."),
  ("Can I talk to real historical figures, not just fictional characters?", "Yes. NoArk's Fiat Lux tab focuses on AI versions of real historical minds — Charlie Munger, Steve Jobs, Albert Einstein, Leonardo da Vinci, Marcus Aurelius, and 40+ more — each grounded in how that person actually reasoned, rather than open-ended fictional roleplay."),
  ("Is NoArk free like Character.AI?", "NoArk is free to download on iPhone, iPad, Mac, and Apple Vision, with optional in-app purchases. There's no account and no data collection required to start."),
  ("Which AI models does NoArk use?", "NoArk routes each request to the best of many frontier models — Anthropic's Claude (Fable), DeepSeek, Mistral, Kimi, and Google's Gemini among them — instead of relying on a single in-house model."),
 ],
}

# ---------------- Spanish ----------------
hp, ap, fp, pp = rel("es")
content["es"] = {
 "title": "NoArk vs Character.AI: una forma privada de hablar con las mentes más sabias de la historia",
 "desc": "Comparativa NoArk vs Character.AI: privacidad, a quién sirven tus datos, mentes históricas reales frente a roleplay ficticio, modelos de IA y precio. NoArk te deja preguntar a versiones de IA de Charlie Munger, Steve Jobs, Einstein, Marco Aurelio y más de 40 — manteniendo cada conversación en tu propio dispositivo, sin registro. Gratis en iPhone, iPad, Mac y Apple Vision.",
 "keywords": "NoArk vs Character.AI, alternativa a Character.AI, Character AI privado, hablar con figuras históricas IA, IA Charlie Munger, IA Marco Aurelio, IA en el dispositivo, IA sin registro, app de IA multimodelo, Claude Fable, DeepSeek, Mistral, Kimi, Gemini",
 "ogdesc": "En qué se diferencia NoArk de Character.AI: tus chats se quedan en tu propio dispositivo, las mentes se basan en cómo razonaban las personas reales, y es una súper app de vida y mercados — no solo roleplay.",
 "twdesc": "Tus chats se quedan en tu dispositivo, las mentes se basan en personas reales, y es una súper app completa — no solo roleplay.",
 "h1": "NoArk vs Character.AI",
 "subtitle": "Ambas te dejan conversar con un elenco de personajes. Solo una mantiene cada conversación en privado — y basa sus mentes en cómo pensaban realmente las personas.",
 "intro": "Character.AI popularizó hablar con personalidades de IA. <strong>NoArk — Infinity Memory</strong> lleva la idea a un lugar más útil y más privado: en lugar de roleplay ficticio, llevas las preguntas reales de tu vida a versiones de IA de las mentes más sabias de la historia — y nada de lo que dices se recopila. Esta es la comparación honesta.",
 "glance": "De un vistazo",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("Con quién hablas", "Versiones de IA de <strong>mentes históricas reales</strong> — Charlie Munger, Steve Jobs, Einstein, da Vinci, Marco Aurelio y más de 40, basadas en cómo razonaban de verdad", "Personajes ficticios creados por usuarios, de calidad variable"),
  ("Tus conversaciones", "<span class='yes'>Guardadas solo en tu dispositivo</span> y en tu propio iCloud — nunca almacenadas ni usadas para entrenar", "Enviadas a servidores de la empresa y usadas para mejorar y entrenar el servicio"),
  ("Recopilación de datos", "<span class='yes'>Ninguna</span> — etiqueta de privacidad de Apple: «No se recopilan datos»", "Recopila datos de cuenta, uso y conversaciones"),
  ("Registro obligatorio", "<span class='yes'>No</span> — sin cuenta, correo ni número de teléfono", "Requiere una cuenta"),
  ("Modelos de IA", "<span class='yes'>Muchos modelos de frontera</span> — Claude Fable, DeepSeek, Mistral, Kimi, Gemini — el mejor para cada tarea", "Los modelos propios de Character.AI"),
  ("Más allá del chat", "Una súper app de IA completa — mercados, productividad, viajes, educación, titulares en directo y más de 40 flujos de trabajo", "Sobre todo chat de personajes y roleplay"),
  ("Modelo de negocio", "Te sirve solo a ti — nunca monetiza tu atención ni tus datos; el 50% de los beneficios se destina a educación", "Suscripción y anuncios, construido en torno a la interacción"),
  ("Precio", "<span class='yes'>Gratis</span> (compras opcionales dentro de la app)", "Nivel gratuito con suscripción de pago"),
 ],
 "note": "Comparativa basada en información pública a junio de 2026. Character.AI es una marca de su titular; NoArk es una app independiente, no afiliada ni respaldada por aquella.",
 "sections": [
  ("Privacidad: tus conversaciones siguen siendo tuyas", [
   "Las preguntas que le llevas a un personaje de IA suelen ser lo más personal que escribirás — dudas, decisiones, cosas que no puedes decir en voz alta. Con Character.AI, esas conversaciones viven en servidores de la empresa y ayudan a entrenar el servicio. NoArk hace lo contrario: tus chats se <strong>guardan solo en tu dispositivo y en tu propio iCloud</strong>, nunca almacenados en nuestros servidores ni usados para entrenar el modelo de nadie.",
   "No hay <strong>registro</strong> — ni correo, ni número de teléfono, nada que vincule lo que dijiste con quién eres. La etiqueta oficial de privacidad de Apple para NoArk dice <a href='" + pp + "'>«No se recopilan datos»</a>, la más estricta que existe.",
  ]),
  ("Mentes reales, fundamentadas — no roleplay ficticio", [
   "Character.AI está hecha para el roleplay abierto con bots creados por usuarios de calidad muy variable. La pestaña <strong>Fiat Lux</strong> de NoArk está hecha para el <strong>consejo</strong>: llevas una pregunta real a versiones de IA de las mentes más sabias de la historia — Charlie Munger, Steve Jobs, Albert Einstein, Leonardo da Vinci, Marco Aurelio y más de 40 — cada una basada en cómo razonaba de verdad esa persona, no en un personaje improvisado.",
   "Y como NoArk recurre a muchos <strong>modelos de frontera</strong> — Claude Fable, DeepSeek, Mistral, Kimi, Gemini — el razonamiento detrás de cada respuesta es tan fuerte como la mejor IA de hoy, no un único modelo propio.",
  ]),
  ("Más que una app de chat: una súper app de vida y mercados", [
   "Character.AI suele quedarse en la conversación. NoArk es además una <strong>súper app de IA completa</strong>: titulares globales en directo con análisis de un toque, más de 40 flujos de trabajo listos que abarcan mercados, productividad, viajes, educación y gestión diaria, y un cerebro inversor creado por el equipo de TradingTransformer, inspirado en la visión de Claude Shannon sobre la IA que elige acciones. Puedes conversar por <strong>texto, voz, foto o archivo</strong> — incluidos PDF, hojas de cálculo y URL.",
  ]),
 ],
 "related_heading": "Sigue leyendo",
 "related": [
  (hp, "NoArk — Infinity Memory: el SO inteligente y súper app de IA"),
  (hp + "noark-vs-chatgpt.html", "NoArk vs ChatGPT"),
  (hp + "noark-vs-gemini.html", "NoArk vs Gemini"),
  (hp + "noark-vs-perplexity.html", "NoArk vs Perplexity"),
  (ap, "NoArk vs Apple Intelligence"),
  (hp + "noark-vs-manus.html", "NoArk vs Manus"),
  (fp, "Preguntas frecuentes sobre NoArk"),
 ],
 "faq": [
  ("¿Es NoArk una buena alternativa a Character.AI?", "Sí, sobre todo si te importan la privacidad y el fondo. NoArk te deja hablar con versiones de IA de las mentes más sabias de la historia — Charlie Munger, Steve Jobs, Marco Aurelio y más de 40 — manteniendo cada conversación en tu propio dispositivo y sin registro. Además es una súper app de vida y mercados, no solo roleplay. Apple la etiqueta como «No se recopilan datos»."),
  ("¿NoArk entrena con mis chats o los almacena?", "No. Tus conversaciones se guardan solo en tu dispositivo y en tu propio iCloud — nunca almacenadas en nuestros servidores ni usadas para entrenar modelos. Cuando NoArk llama a modelos de frontera por sus API, tu contenido tampoco se almacena ni se usa para entrenarlos."),
  ("¿Puedo hablar con figuras históricas reales, no solo con personajes ficticios?", "Sí. La pestaña Fiat Lux de NoArk se centra en versiones de IA de mentes históricas reales — Charlie Munger, Steve Jobs, Albert Einstein, Leonardo da Vinci, Marco Aurelio y más de 40 — cada una basada en cómo razonaba de verdad esa persona, en vez de roleplay ficticio abierto."),
  ("¿Es NoArk gratis como Character.AI?", "NoArk es gratis en iPhone, iPad, Mac y Apple Vision, con compras opcionales dentro de la app. No hace falta cuenta ni recopilación de datos para empezar."),
  ("¿Qué modelos de IA usa NoArk?", "NoArk dirige cada petición al mejor de muchos modelos de frontera — Claude (Fable) de Anthropic, DeepSeek, Mistral, Kimi y Gemini de Google entre ellos — en lugar de depender de un único modelo propio."),
 ],
}

# ---------------- French ----------------
hp, ap, fp, pp = rel("fr")
content["fr"] = {
 "title": "NoArk vs Character.AI : une façon privée de parler aux plus grands esprits de l'histoire",
 "desc": "Comparatif NoArk vs Character.AI : confidentialité, à qui servent vos données, vrais esprits historiques contre jeu de rôle fictif, modèles d'IA et prix. NoArk vous laisse interroger des versions IA de Charlie Munger, Steve Jobs, Einstein, Marc Aurèle et plus de 40 autres — en gardant chaque conversation sur votre propre appareil, sans inscription. Gratuit sur iPhone, iPad, Mac et Apple Vision.",
 "keywords": "NoArk vs Character.AI, alternative à Character.AI, Character AI privé, parler aux figures historiques IA, IA Charlie Munger, IA Marc Aurèle, IA sur l'appareil, IA sans inscription, app IA multi-modèles, Claude Fable, DeepSeek, Mistral, Kimi, Gemini",
 "ogdesc": "En quoi NoArk diffère de Character.AI : vos conversations restent sur votre appareil, les esprits sont ancrés dans la façon dont les vraies personnes raisonnaient, et c'est une super app de vie et de marchés — pas seulement du jeu de rôle.",
 "twdesc": "Vos conversations restent sur votre appareil, les esprits sont ancrés dans de vraies personnes, et c'est une super app complète — pas seulement du jeu de rôle.",
 "h1": "NoArk vs Character.AI",
 "subtitle": "Les deux vous laissent discuter avec une galerie de personnages. Une seule garde chaque conversation privée — et ancre ses esprits dans la façon dont les gens pensaient vraiment.",
 "intro": "Character.AI a popularisé le fait de parler à des personnalités IA. <strong>NoArk — Infinity Memory</strong> pousse l'idée vers quelque chose de plus utile et de plus privé : au lieu d'un jeu de rôle fictif, vous apportez les vraies questions de votre vie à des versions IA des plus grands esprits de l'histoire — et rien de ce que vous dites n'est collecté. Voici la comparaison honnête.",
 "glance": "En un coup d'œil",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("Avec qui vous parlez", "Des versions IA d'<strong>esprits historiques réels</strong> — Charlie Munger, Steve Jobs, Einstein, da Vinci, Marc Aurèle et plus de 40 autres, ancrées dans leur vraie façon de raisonner", "Des personnages fictifs créés par les utilisateurs, de qualité variable"),
  ("Vos conversations", "<span class='yes'>Stockées uniquement sur votre appareil</span> et dans votre propre iCloud — jamais entreposées ni utilisées pour entraîner", "Envoyées aux serveurs de l'entreprise et utilisées pour améliorer et entraîner le service"),
  ("Collecte de données", "<span class='yes'>Aucune</span> — étiquette de confidentialité d'Apple : « Données non collectées »", "Collecte des données de compte, d'usage et de conversation"),
  ("Inscription requise", "<span class='yes'>Non</span> — pas de compte, d'e-mail ni de numéro de téléphone", "Nécessite un compte"),
  ("Modèles d'IA", "<span class='yes'>De nombreux modèles de pointe</span> — Claude Fable, DeepSeek, Mistral, Kimi, Gemini — le meilleur pour chaque tâche", "Les modèles maison de Character.AI"),
  ("Au-delà du chat", "Une super app IA complète — marchés, productivité, voyage, éducation, actualité en direct et plus de 40 flux de travail", "Surtout du chat de personnages et du jeu de rôle"),
  ("Modèle économique", "Ne sert que vous — ne monétise jamais votre attention ni vos données ; 50 % des profits promis à l'éducation", "Abonnement et publicité, bâti autour de l'engagement"),
  ("Prix", "<span class='yes'>Gratuit</span> (achats intégrés optionnels)", "Offre gratuite avec abonnement payant"),
 ],
 "note": "Comparaison fondée sur des informations publiques en juin 2026. Character.AI est une marque de son détenteur respectif ; NoArk est une app indépendante, ni affiliée ni approuvée par celui-ci.",
 "sections": [
  ("Confidentialité : vos conversations restent les vôtres", [
   "Les questions que vous apportez à un personnage IA comptent souvent parmi les choses les plus personnelles que vous écrirez — doutes, décisions, choses que vous ne pouvez dire à voix haute. Avec Character.AI, ces conversations vivent sur les serveurs de l'entreprise et aident à entraîner le service. NoArk fait l'inverse : vos conversations sont <strong>stockées uniquement sur votre appareil et dans votre propre iCloud</strong>, jamais entreposées sur nos serveurs ni utilisées pour entraîner le modèle de qui que ce soit.",
   "Il n'y a <strong>aucune inscription</strong> — pas d'e-mail, pas de numéro de téléphone, rien qui relie ce que vous avez dit à qui vous êtes. L'étiquette officielle de confidentialité d'Apple pour NoArk indique <a href='" + pp + "'>« Données non collectées »</a>, la plus stricte qui soit.",
  ]),
  ("De vrais esprits, ancrés — pas du jeu de rôle fictif", [
   "Character.AI est conçue pour le jeu de rôle libre avec des bots créés par les utilisateurs, de qualité très variable. L'onglet <strong>Fiat Lux</strong> de NoArk est conçu pour le <strong>conseil</strong> : vous apportez une vraie question à des versions IA des plus grands esprits de l'histoire — Charlie Munger, Steve Jobs, Albert Einstein, Léonard de Vinci, Marc Aurèle et plus de 40 autres — chacun ancré dans la vraie façon de raisonner de cette personne, et non un personnage improvisé.",
   "Et comme NoArk fait appel à de nombreux <strong>modèles de pointe</strong> — Claude Fable, DeepSeek, Mistral, Kimi, Gemini — le raisonnement derrière chaque réponse est aussi solide que la meilleure IA d'aujourd'hui, et non un unique modèle maison.",
  ]),
  ("Plus qu'une app de chat : une super app de vie et de marchés", [
   "Character.AI s'arrête le plus souvent à la conversation. NoArk est aussi une <strong>super app IA complète</strong> : actualité mondiale en direct avec analyse en un geste, plus de 40 flux de travail prêts à l'emploi couvrant marchés, productivité, voyage, éducation et gestion du quotidien, et un cerveau d'investisseur créé par l'équipe de TradingTransformer, inspiré par la vision de Claude Shannon d'une IA qui choisit les actions. Vous pouvez discuter par <strong>texte, voix, photo ou fichier</strong> — y compris PDF, feuilles de calcul et URL.",
  ]),
 ],
 "related_heading": "À lire ensuite",
 "related": [
  (hp, "NoArk — Infinity Memory : l'OS intelligent et la super app IA"),
  (hp + "noark-vs-chatgpt.html", "NoArk vs ChatGPT"),
  (hp + "noark-vs-gemini.html", "NoArk vs Gemini"),
  (hp + "noark-vs-perplexity.html", "NoArk vs Perplexity"),
  (ap, "NoArk vs Apple Intelligence"),
  (hp + "noark-vs-manus.html", "NoArk vs Manus"),
  (fp, "Questions fréquentes sur NoArk"),
 ],
 "faq": [
  ("NoArk est-elle une bonne alternative à Character.AI ?", "Oui, surtout si la confidentialité et le fond comptent pour vous. NoArk vous laisse parler à des versions IA des plus grands esprits de l'histoire — Charlie Munger, Steve Jobs, Marc Aurèle et plus de 40 autres — tout en gardant chaque conversation sur votre propre appareil, sans inscription. C'est aussi une super app de vie et de marchés, pas seulement du jeu de rôle. Apple l'étiquette « Données non collectées »."),
  ("NoArk s'entraîne-t-elle sur mes conversations ou les stocke-t-elle ?", "Non. Vos conversations sont stockées uniquement sur votre appareil et dans votre propre iCloud — jamais entreposées sur nos serveurs ni utilisées pour entraîner des modèles. Quand NoArk appelle des modèles de pointe via leurs API, votre contenu n'est pas non plus stocké ni utilisé pour les entraîner."),
  ("Puis-je parler à de vraies figures historiques, pas seulement à des personnages fictifs ?", "Oui. L'onglet Fiat Lux de NoArk se concentre sur des versions IA d'esprits historiques réels — Charlie Munger, Steve Jobs, Albert Einstein, Léonard de Vinci, Marc Aurèle et plus de 40 autres — chacun ancré dans la vraie façon de raisonner de cette personne, plutôt que du jeu de rôle fictif libre."),
  ("NoArk est-elle gratuite comme Character.AI ?", "NoArk est gratuite sur iPhone, iPad, Mac et Apple Vision, avec des achats intégrés optionnels. Aucun compte ni aucune collecte de données n'est nécessaire pour commencer."),
  ("Quels modèles d'IA NoArk utilise-t-elle ?", "NoArk route chaque requête vers le meilleur de nombreux modèles de pointe — Claude (Fable) d'Anthropic, DeepSeek, Mistral, Kimi et Gemini de Google notamment — au lieu de dépendre d'un seul modèle maison."),
 ],
}

# ---------------- Japanese ----------------
hp, ap, fp, pp = rel("ja")
content["ja"] = {
 "title": "NoArk vs Character.AI：歴史上の賢人とプライベートに話せるアプリ",
 "desc": "NoArk と Character.AI を比較：プライバシー、データが誰のために働くか、実在の歴史的知性か架空のロールプレイか、AIモデル、価格。NoArk はチャーリー・マンガー、スティーブ・ジョブズ、アインシュタイン、マルクス・アウレリウスほか40名以上のAI版に相談でき、すべての会話をあなたのデバイスに保ち、サインインも不要。iPhone・iPad・Mac・Apple Vision で無料。",
 "keywords": "NoArk vs Character.AI, Character.AI 代替, プライベート Character AI, 歴史上の人物と話す AI, AI チャーリー・マンガー, AI マルクス・アウレリウス, オンデバイス AI チャット, サインイン不要 AI, マルチモデルAIアプリ, Claude Fable, DeepSeek, Mistral, Kimi, Gemini",
 "ogdesc": "NoArk が Character.AI と違う点：会話はあなたのデバイスに残り、知性は実在の人物の実際の考え方に基づき、しかも人生と市場のスーパーアプリ — 単なるロールプレイではありません。",
 "twdesc": "会話はあなたのデバイスに残り、知性は実在の人物に基づき、しかもフル機能のスーパーアプリ — 単なるロールプレイではありません。",
 "h1": "NoArk vs Character.AI",
 "subtitle": "どちらもキャラクターと話せます。しかし、すべての会話を非公開に保ち、知性を実在の人物の実際の思考に基づかせるのは一方だけです。",
 "intro": "Character.AI は、AIキャラクターと話す体験を広めました。<strong>NoArk — Infinity Memory</strong> はその発想を、より役立ち、よりプライベートな方向へ進めます。架空のロールプレイではなく、人生の本当の問いを歴史上の賢人のAI版に持ち込めて、しかもあなたの発言は一切収集されません。これが率直な比較です。",
 "glance": "ひと目でわかる比較",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("話す相手", "<strong>実在の歴史的知性</strong>のAI版 — チャーリー・マンガー、スティーブ・ジョブズ、アインシュタイン、ダ・ヴィンチ、マルクス・アウレリウスほか40名以上。実際の考え方に基づく", "ユーザー作成の架空キャラクター。品質はさまざま"),
  ("あなたの会話", "<span class='yes'>あなたのデバイス</span>とあなた自身の iCloud だけに保存 — 蓄積も学習利用もされません", "企業のサーバーに送られ、サービスの改善・学習に利用"),
  ("データ収集", "<span class='yes'>なし</span> — Apple のプライバシーラベル：「データは収集されません」", "アカウント・利用状況・会話のデータを収集"),
  ("サインイン", "<span class='yes'>不要</span> — アカウントもメールも電話番号も不要", "アカウントが必要"),
  ("AIモデル", "<span class='yes'>多数のフロンティアモデル</span> — Claude Fable、DeepSeek、Mistral、Kimi、Gemini — タスクごとに最適なものを選択", "Character.AI 独自のモデル"),
  ("チャットの先", "フル機能のAIスーパーアプリ — 市場、生産性、旅行、教育、ライブ世界ニュース、40以上のワークフロー", "主にキャラクターチャットとロールプレイ"),
  ("ビジネスモデル", "あなただけに仕える — 注意もデータも収益化しません。利益の50%を教育に寄付", "サブスクと広告。エンゲージメント中心"),
  ("価格", "<span class='yes'>無料</span>（オプションのアプリ内課金あり）", "無料プランと有料サブスク"),
 ],
 "note": "本比較は2026年6月時点の公開情報に基づきます。Character.AI は各権利者の商標です。NoArk は独立したアプリであり、提携や承認はありません。",
 "sections": [
  ("プライバシー：あなたの会話はあなたのもの", [
   "AIキャラクターに持ち込む問いは、しばしばあなたが書く中で最も個人的なもの — 迷い、決断、声に出して言えないこと — です。Character.AI ではそうした会話が企業のサーバーに保存され、サービスの学習に使われます。NoArk は逆です。あなたの会話は<strong>あなたのデバイスとあなた自身の iCloud だけに保存</strong>され、私たちのサーバーに蓄積されることも、誰のモデルの学習に使われることもありません。",
   "<strong>サインインは不要</strong>です — メールも電話番号も、あなたの発言と身元を結び付けるものは何もありません。Apple 公式の NoArk のプライバシーラベルは <a href='" + pp + "'>「データは収集されません」</a> — 最も厳格なラベルです。",
  ]),
  ("実在の知性に基づく — 架空のロールプレイではなく", [
   "Character.AI は、品質がさまざまなユーザー作成ボットとの自由なロールプレイのために作られています。NoArk の <strong>Fiat Lux</strong> タブは<strong>助言</strong>のために作られています。本当の問いを、歴史上の賢人のAI版 — チャーリー・マンガー、スティーブ・ジョブズ、アインシュタイン、レオナルド・ダ・ヴィンチ、マルクス・アウレリウスほか40名以上 — に持ち込めます。それぞれが、その人物の実際の考え方に基づいており、即興のキャラクターではありません。",
   "さらに NoArk は多数の<strong>フロンティアモデル</strong> — Claude Fable、DeepSeek、Mistral、Kimi、Gemini — を使い分けるため、各回答の背後にある思考は、単一の自社モデルではなく、今日最高のAIと同じ強さです。",
  ]),
  ("チャットアプリ以上：人生と市場のフルスーパーアプリ", [
   "Character.AI はたいてい会話で止まります。NoArk はさらに<strong>フル機能のAIスーパーアプリ</strong>です。ワンタップ分析つきのライブ世界ニュース、市場・生産性・旅行・教育・生活の雑務にわたる40以上の即戦力ワークフロー、そして TradingTransformer チームが作り、クロード・シャノンのAI株式選択のビジョンに着想を得た投資する頭脳。<strong>テキスト・音声・写真・ファイル</strong>（PDF、表計算、URL を含む）で対話できます。",
  ]),
 ],
 "related_heading": "あわせて読む",
 "related": [
  (hp, "NoArk — Infinity Memory：インテリジェントAI OS・スーパーアプリ"),
  (hp + "noark-vs-chatgpt.html", "NoArk vs ChatGPT"),
  (hp + "noark-vs-gemini.html", "NoArk vs Gemini"),
  (hp + "noark-vs-perplexity.html", "NoArk vs Perplexity"),
  (ap, "NoArk vs Apple Intelligence"),
  (hp + "noark-vs-manus.html", "NoArk vs Manus"),
  (fp, "NoArk についてのよくある質問"),
 ],
 "faq": [
  ("NoArk は Character.AI の良い代替になりますか？", "はい。特にプライバシーと中身を重視するならおすすめです。NoArk では、歴史上の賢人のAI版 — チャーリー・マンガー、スティーブ・ジョブズ、マルクス・アウレリウスほか40名以上 — と話せて、すべての会話をあなたのデバイスに保ち、サインインも不要です。単なるロールプレイではなく、人生と市場のスーパーアプリでもあります。Apple のラベルは「データは収集されません」です。"),
  ("NoArk は私の会話で学習したり、保存したりしますか？", "いいえ。あなたの会話はあなたのデバイスとあなた自身の iCloud だけに保存され、私たちのサーバーに蓄積されることも、モデルの学習に使われることもありません。NoArk が API 経由でフロンティアモデルを呼び出すときも、あなたのコンテンツは保存も学習利用もされません。"),
  ("架空のキャラクターではなく、実在の歴史上の人物と話せますか？", "はい。NoArk の Fiat Lux タブは、実在の歴史的知性のAI版 — チャーリー・マンガー、スティーブ・ジョブズ、アインシュタイン、レオナルド・ダ・ヴィンチ、マルクス・アウレリウスほか40名以上 — に焦点を当てています。自由な架空のロールプレイではなく、その人物の実際の考え方に基づいています。"),
  ("NoArk は Character.AI のように無料ですか？", "NoArk は iPhone・iPad・Mac・Apple Vision で無料で、オプションのアプリ内課金があります。始めるのにアカウントもデータ収集も不要です。"),
  ("NoArk はどのAIモデルを使っていますか？", "NoArk はリクエストごとに、Anthropic の Claude（Fable）、DeepSeek、Mistral、Kimi、Google の Gemini など多数のフロンティアモデルから最適なものを選びます。単一の自社モデルに頼りません。"),
 ],
}

# ---------------- Simplified Chinese ----------------
hp, ap, fp, pp = rel("zh-cn")
content["zh-cn"] = {
 "title": "NoArk 对比 Character.AI：私密地与历史智者对话",
 "desc": "NoArk 与 Character.AI 全面对比：隐私、你的数据为谁服务、真实历史智者还是虚构角色扮演、AI 模型与价格。NoArk 让你向查理·芒格、史蒂夫·乔布斯、爱因斯坦、马可·奥勒留等 40 多位的 AI 版本请教，把每段对话都留在你自己的设备上，无需登录。iPhone、iPad、Mac 和 Apple Vision 免费下载。",
 "keywords": "NoArk 对比 Character.AI, Character.AI 替代品, 私密 Character AI, 与历史人物对话 AI, AI 查理·芒格, AI 马可·奥勒留, 端侧 AI 聊天, 无需登录的 AI, 多模型 AI 应用, Claude Fable, DeepSeek, Mistral, Kimi, Gemini",
 "ogdesc": "NoArk 与 Character.AI 的不同：你的对话留在你自己的设备上，智者立足于真实人物的真实思考方式，而且它是一款人生与市场的超级应用——不只是角色扮演。",
 "twdesc": "你的对话留在你自己的设备上，智者立足于真实人物，而且是一款完整的超级应用——不只是角色扮演。",
 "h1": "NoArk 对比 Character.AI",
 "subtitle": "两者都让你与一众角色对话。但只有一个让每段对话都保持私密——并让其智者立足于人们真实的思考方式。",
 "intro": "Character.AI 让“与 AI 角色对话”走向大众。<strong>NoArk — 无限记忆</strong>把这个想法带到了更有用、更私密的方向：不是虚构的角色扮演，而是把你人生中真实的问题带给历史上最有智慧的人的 AI 版本——而且你所说的一切都不会被收集。下面是坦诚的对比。",
 "glance": "一览对比",
 "col_noark": "NoArk — 无限记忆",
 "rows": [
  ("和谁对话", "<strong>真实历史智者</strong>的 AI 版本——查理·芒格、史蒂夫·乔布斯、爱因斯坦、达·芬奇、马可·奥勒留等 40 多位，立足于他们真实的思考方式", "用户创建的虚构角色，质量参差不齐"),
  ("你的对话", "<span class='yes'>只保存在你的设备</span>和你自己的 iCloud 中——绝不堆放或用于训练", "发送到公司服务器，并用于改进和训练服务"),
  ("数据收集", "<span class='yes'>无</span>——Apple 隐私标签：“不收集数据”", "收集账户、使用和对话数据"),
  ("是否需要登录", "<span class='yes'>不需要</span>——无账户、邮箱或手机号", "需要账户"),
  ("AI 模型", "<span class='yes'>多个前沿模型</span>——Claude Fable、DeepSeek、Mistral、Kimi、Gemini——为每个任务挑选最合适的", "Character.AI 自家的模型"),
  ("聊天之外", "一款完整的 AI 超级应用——市场、生产力、旅行、教育、实时头条和 40 多个工作流", "主要是角色聊天与角色扮演"),
  ("商业模式", "只为你服务——绝不把你的注意力或数据变现；将利润的 50% 捐给教育", "订阅与广告，围绕用户黏性构建"),
  ("价格", "<span class='yes'>免费</span>下载（含可选的应用内购买）", "免费档加付费订阅"),
 ],
 "note": "对比基于截至 2026 年 6 月的公开信息。Character.AI 是其各自所有者的商标；NoArk 是独立应用，与其无关联，也未获其背书。",
 "sections": [
  ("隐私：你的对话依然属于你", [
   "你带给 AI 角色的问题，往往是你会写下的最私密的东西——困惑、抉择、说不出口的话。在 Character.AI 上，这些对话存放在公司服务器上，并帮助训练服务。NoArk 恰恰相反：你的对话<strong>只保存在你的设备和你自己的 iCloud 中</strong>，绝不堆放在我们的服务器上，也绝不用于训练任何人的模型。",
   "这里<strong>无需登录</strong>——没有邮箱、没有手机号，没有任何东西把你说的话和你的身份绑定。Apple 官方为 NoArk 出具的隐私标签写着 <a href='" + pp + "'>“不收集数据”</a>——最严格的一档。",
  ]),
  ("真实的智者，有据可依——而非虚构的角色扮演", [
   "Character.AI 为与质量参差不齐的用户创建机器人进行开放式角色扮演而生。NoArk 的 <strong>Fiat Lux</strong> 标签则为<strong>建议</strong>而生：你把一个真实的问题带给历史上最有智慧的人的 AI 版本——查理·芒格、史蒂夫·乔布斯、爱因斯坦、列奥纳多·达·芬奇、马可·奥勒留等 40 多位——每一位都立足于这个人真实的思考方式，而不是即兴的人设。",
   "而且由于 NoArk 会调用多个<strong>前沿模型</strong>——Claude Fable、DeepSeek、Mistral、Kimi、Gemini——每个回答背后的思考都与当今最好的 AI 一样强，而不是单一的自家模型。",
  ]),
  ("不只是聊天应用：一款人生与市场的超级应用", [
   "Character.AI 大多止步于对话。NoArk 还是一款<strong>完整的 AI 超级应用</strong>：带一键分析的实时全球头条，覆盖市场、生产力、旅行、教育和生活事务的 40 多个开箱即用工作流，以及由 TradingTransformer 团队打造、灵感来自克劳德·香农 AI 选股愿景的投资大脑。你可以用<strong>文字、语音、照片或文件</strong>（包括 PDF、表格和网址）对话。",
  ]),
 ],
 "related_heading": "继续阅读",
 "related": [
  (hp, "NoArk — 无限记忆：智能 AI 操作系统与超级应用"),
  (hp + "noark-vs-chatgpt.html", "NoArk 对比 ChatGPT"),
  (hp + "noark-vs-gemini.html", "NoArk 对比 Gemini"),
  (hp + "noark-vs-perplexity.html", "NoArk 对比 Perplexity"),
  (ap, "NoArk 对比 Apple Intelligence"),
  (hp + "noark-vs-manus.html", "NoArk 对比 Manus"),
  (fp, "关于 NoArk 的常见问题"),
 ],
 "faq": [
  ("NoArk 是 Character.AI 的好替代品吗？", "是的，尤其当你在意隐私和内容深度时。NoArk 让你与历史上最有智慧的人的 AI 版本对话——查理·芒格、史蒂夫·乔布斯、马可·奥勒留等 40 多位——同时把每段对话都留在你自己的设备上，无需登录。它还是一款人生与市场的超级应用，不只是角色扮演。Apple 的标签是“不收集数据”。"),
  ("NoArk 会用我的对话训练或存储它们吗？", "不会。你的对话只保存在你的设备和你自己的 iCloud 中——绝不堆放在我们的服务器上，也绝不用于训练模型。当 NoArk 通过 API 调用前沿模型时，你的内容同样不会被存储或用于训练它们。"),
  ("我能和真实的历史人物对话，而不只是虚构角色吗？", "可以。NoArk 的 Fiat Lux 标签专注于真实历史智者的 AI 版本——查理·芒格、史蒂夫·乔布斯、爱因斯坦、列奥纳多·达·芬奇、马可·奥勒留等 40 多位——每一位都立足于这个人真实的思考方式，而不是开放式的虚构角色扮演。"),
  ("NoArk 像 Character.AI 一样免费吗？", "NoArk 在 iPhone、iPad、Mac 和 Apple Vision 上免费下载，含可选的应用内购买。开始使用无需账户，也不收集数据。"),
  ("NoArk 用哪些 AI 模型？", "NoArk 将每个请求路由到众多前沿模型中最合适的一个——包括 Anthropic 的 Claude（Fable）、DeepSeek、Mistral、Kimi 和谷歌的 Gemini——而不是依赖单一的自家模型。"),
 ],
}

# ---------------- Traditional Chinese ----------------
hp, ap, fp, pp = rel("zh-tw")
content["zh-tw"] = {
 "title": "NoArk 對比 Character.AI：私密地與歷史智者對話",
 "desc": "NoArk 與 Character.AI 全面對比：隱私、你的資料為誰服務、真實歷史智者還是虛構角色扮演、AI 模型與價格。NoArk 讓你向查理·蒙格、史蒂夫·賈伯斯、愛因斯坦、馬可·奧理略等 40 多位的 AI 版本請教，把每段對話都留在你自己的裝置上，無需登入。iPhone、iPad、Mac 和 Apple Vision 免費下載。",
 "keywords": "NoArk 對比 Character.AI, Character.AI 替代品, 私密 Character AI, 與歷史人物對話 AI, AI 查理·蒙格, AI 馬可·奧理略, 端側 AI 聊天, 無需登入的 AI, 多模型 AI 應用程式, Claude Fable, DeepSeek, Mistral, Kimi, Gemini",
 "ogdesc": "NoArk 與 Character.AI 的不同：你的對話留在你自己的裝置上，智者立足於真實人物的真實思考方式，而且它是一款人生與市場的超級應用程式——不只是角色扮演。",
 "twdesc": "你的對話留在你自己的裝置上，智者立足於真實人物，而且是一款完整的超級應用程式——不只是角色扮演。",
 "h1": "NoArk 對比 Character.AI",
 "subtitle": "兩者都讓你與一眾角色對話。但只有一個讓每段對話都保持私密——並讓其智者立足於人們真實的思考方式。",
 "intro": "Character.AI 讓「與 AI 角色對話」走向大眾。<strong>NoArk — 無限記憶</strong>把這個想法帶到了更有用、更私密的方向：不是虛構的角色扮演，而是把你人生中真實的問題帶給歷史上最有智慧的人的 AI 版本——而且你所說的一切都不會被收集。以下是坦誠的對比。",
 "glance": "一覽對比",
 "col_noark": "NoArk — 無限記憶",
 "rows": [
  ("和誰對話", "<strong>真實歷史智者</strong>的 AI 版本——查理·蒙格、史蒂夫·賈伯斯、愛因斯坦、達文西、馬可·奧理略等 40 多位，立足於他們真實的思考方式", "使用者建立的虛構角色，品質參差不齊"),
  ("你的對話", "<span class='yes'>只保存在你的裝置</span>和你自己的 iCloud 中——絕不堆放或用於訓練", "傳送到公司伺服器，並用於改進和訓練服務"),
  ("資料收集", "<span class='yes'>無</span>——Apple 隱私標籤：「不收集資料」", "收集帳號、使用和對話資料"),
  ("是否需要登入", "<span class='yes'>不需要</span>——無帳號、電子郵件或手機號碼", "需要帳號"),
  ("AI 模型", "<span class='yes'>多個前沿模型</span>——Claude Fable、DeepSeek、Mistral、Kimi、Gemini——為每個任務挑選最合適的", "Character.AI 自家的模型"),
  ("聊天之外", "一款完整的 AI 超級應用程式——市場、生產力、旅行、教育、即時頭條和 40 多個工作流程", "主要是角色聊天與角色扮演"),
  ("商業模式", "只為你服務——絕不把你的注意力或資料變現；將利潤的 50% 捐給教育", "訂閱與廣告，圍繞使用者黏著度構建"),
  ("價格", "<span class='yes'>免費</span>下載（含可選的應用程式內購買）", "免費檔加付費訂閱"),
 ],
 "note": "對比基於截至 2026 年 6 月的公開資訊。Character.AI 是其各自所有者的商標；NoArk 是獨立應用程式，與其無關聯，也未獲其背書。",
 "sections": [
  ("隱私：你的對話依然屬於你", [
   "你帶給 AI 角色的問題，往往是你會寫下的最私密的東西——困惑、抉擇、說不出口的話。在 Character.AI 上，這些對話存放在公司伺服器上，並幫助訓練服務。NoArk 恰恰相反：你的對話<strong>只保存在你的裝置和你自己的 iCloud 中</strong>，絕不堆放在我們的伺服器上，也絕不用於訓練任何人的模型。",
   "這裡<strong>無需登入</strong>——沒有電子郵件、沒有手機號碼，沒有任何東西把你說的話和你的身分綁定。Apple 官方為 NoArk 出具的隱私標籤寫著 <a href='" + pp + "'>「不收集資料」</a>——最嚴格的一檔。",
  ]),
  ("真實的智者，有據可依——而非虛構的角色扮演", [
   "Character.AI 為與品質參差不齊的使用者建立機器人進行開放式角色扮演而生。NoArk 的 <strong>Fiat Lux</strong> 分頁則為<strong>建議</strong>而生：你把一個真實的問題帶給歷史上最有智慧的人的 AI 版本——查理·蒙格、史蒂夫·賈伯斯、愛因斯坦、李奧納多·達文西、馬可·奧理略等 40 多位——每一位都立足於這個人真實的思考方式，而不是即興的人設。",
   "而且由於 NoArk 會調用多個<strong>前沿模型</strong>——Claude Fable、DeepSeek、Mistral、Kimi、Gemini——每個回答背後的思考都與當今最好的 AI 一樣強，而不是單一的自家模型。",
  ]),
  ("不只是聊天應用程式：一款人生與市場的超級應用程式", [
   "Character.AI 大多止步於對話。NoArk 還是一款<strong>完整的 AI 超級應用程式</strong>：帶一鍵分析的即時全球頭條，涵蓋市場、生產力、旅行、教育和生活事務的 40 多個開箱即用工作流程，以及由 TradingTransformer 團隊打造、靈感來自克勞德·夏農 AI 選股願景的投資大腦。你可以用<strong>文字、語音、照片或檔案</strong>（包括 PDF、試算表和網址）對話。",
  ]),
 ],
 "related_heading": "繼續閱讀",
 "related": [
  (hp, "NoArk — 無限記憶：智慧型 AI 作業系統與超級應用程式"),
  (hp + "noark-vs-chatgpt.html", "NoArk 對比 ChatGPT"),
  (hp + "noark-vs-gemini.html", "NoArk 對比 Gemini"),
  (hp + "noark-vs-perplexity.html", "NoArk 對比 Perplexity"),
  (ap, "NoArk 對比 Apple Intelligence"),
  (hp + "noark-vs-manus.html", "NoArk 對比 Manus"),
  (fp, "關於 NoArk 的常見問題"),
 ],
 "faq": [
  ("NoArk 是 Character.AI 的好替代品嗎？", "是的，尤其當你在意隱私和內容深度時。NoArk 讓你與歷史上最有智慧的人的 AI 版本對話——查理·蒙格、史蒂夫·賈伯斯、馬可·奧理略等 40 多位——同時把每段對話都留在你自己的裝置上，無需登入。它還是一款人生與市場的超級應用程式，不只是角色扮演。Apple 的標籤是「不收集資料」。"),
  ("NoArk 會用我的對話訓練或儲存它們嗎？", "不會。你的對話只保存在你的裝置和你自己的 iCloud 中——絕不堆放在我們的伺服器上，也絕不用於訓練模型。當 NoArk 透過 API 呼叫前沿模型時，你的內容同樣不會被儲存或用於訓練它們。"),
  ("我能和真實的歷史人物對話，而不只是虛構角色嗎？", "可以。NoArk 的 Fiat Lux 分頁專注於真實歷史智者的 AI 版本——查理·蒙格、史蒂夫·賈伯斯、愛因斯坦、李奧納多·達文西、馬可·奧理略等 40 多位——每一位都立足於這個人真實的思考方式，而不是開放式的虛構角色扮演。"),
  ("NoArk 像 Character.AI 一樣免費嗎？", "NoArk 在 iPhone、iPad、Mac 和 Apple Vision 上免費下載，含可選的應用程式內購買。開始使用無需帳號，也不收集資料。"),
  ("NoArk 用哪些 AI 模型？", "NoArk 將每個請求路由到眾多前沿模型中最合適的一個——包括 Anthropic 的 Claude（Fable）、DeepSeek、Mistral、Kimi 和 Google 的 Gemini——而不是依賴單一的自家模型。"),
 ],
}

render(SLUG, COMP, content)
