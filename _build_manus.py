# -*- coding: utf-8 -*-
from _compare_lib import render

SLUG = "noark-vs-manus.html"
COMP = "Manus"

def rel(p):
    base = "/" + (p + "/" if p else "")
    return (base,
            base + "noark-vs-chatgpt.html",
            base + "noark-vs-character-ai.html",
            base + "noark-vs-gemini.html",
            base + "noark-vs-perplexity.html",
            base + "noark-vs-apple-intelligence.html",
            base + "#faq",
            base + "#data-privacy")

content = {}

# ---------------- English ----------------
hp, gp, cp, mp, pp, ap, fp, dp = rel("")
content[""] = {
 "title": "NoArk vs Manus: Unlimited AI Agents at $99.99/mo, Not Thousands in Credits",
 "desc": "NoArk vs Manus compared: agentic AI without credit anxiety. Manus charges per task in credits — heavy users routinely burn $1,000–$5,000+ a month on add-on packs. NoArk's Diamond plan is $99.99/month flat for unlimited agentic workflows, no credit meter, no sign-in, every conversation private on your own device. Free to download on iPhone, iPad, Mac & Apple Vision.",
 "keywords": "NoArk vs Manus, Manus alternative, cheap Manus alternative, unlimited AI agent, AI agent flat price, Manus credits expensive, agentic AI iPhone, private AI agent, Claude Fable, DeepSeek, $99 unlimited AI, Manus heavy user cost",
 "ogdesc": "How NoArk differs from Manus: a flat $99.99/month Diamond plan for unlimited agentic workflows instead of credit packs that drain $1,000–$5,000+ a month for heavy users — plus full privacy with no account.",
 "twdesc": "Flat $99.99/mo unlimited agents instead of Manus credit packs that drain thousands a month. No sign-in. Every conversation on your own device.",
 "h1": "NoArk vs Manus",
 "subtitle": "Both run AI agents that get real work done. Only one charges a flat $99.99/month for unlimited use — instead of a credit meter that can drain thousands a month.",
 "intro": "Manus is a capable autonomous AI agent — but it runs on a <strong>credit meter</strong>, and heavy users routinely report burning <strong>$1,000–$5,000+ per month</strong> on add-on credit packs once a single complex task can cost 500–1,000 credits and a runaway loop can chew through 88,000 in one sitting. <strong>NoArk — Infinity Memory</strong> takes the opposite approach: a <strong>flat $99.99/month Diamond plan</strong> with <strong>unlimited agentic workflows</strong>, no credit anxiety, no sign-in, and every conversation kept on your own device. Here's the honest comparison.",
 "glance": "At a glance",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("Pricing model", "<span class='yes'>Flat-rate, unlimited</span> — Diamond plan $99.99/month for unlimited agentic workflows; Gold from $49.99/month early-bird", "Credit meter — every task burns credits, heavy users add packs"),
  ("Heavy-user real cost", "<span class='yes'>$99.99/month, full stop</span> — same price whether you run 10 tasks or 10,000", "$1,000–$5,000+/month is common once add-on credit packs kick in"),
  ("Single complex task cost", "<span class='yes'>$0 marginal</span> — already covered by your flat plan", "500–1,000+ credits each; complex agents can hit 5,000+ on one job"),
  ("Predictability", "<span class='yes'>Fully predictable</span> — one bill, no surprise overages", "Unpredictable — users report burning a month's credits in an hour"),
  ("Sign-in required", "<span class='yes'>No</span> — no account, email, or phone number", "Account required"),
  ("Your conversations", "<span class='yes'>Stored only on your device</span> and your own iCloud — never warehoused or used to train", "Sent to the company's servers"),
  ("Data collection", "<span class='yes'>None</span> — Apple's App Privacy label: “Data Not Collected”", "Collects account, usage, and task data"),
  ("Beyond agents", "A full Apple super app — live news with one-tap analysis, counsel from history's wisest minds, 40+ workflows on iPhone, iPad, Mac &amp; Vision", "Primarily a single autonomous agent in a browser tab"),
 ],
 "note": "Comparison reflects publicly available information as of June 2026. Manus is a trademark of its respective owner; NoArk is an independent app and is not affiliated with or endorsed by it. Heavy-user cost figures for Manus reflect publicly reported user experience with credit consumption and add-on packs; your actual bill will vary with usage.",
 "sections": [
  ("The credit meter problem — and why a flat $99.99 changes the math", [
   "Manus's pricing is built around credits. The published tiers — $20 for 4,000 credits, $40 for 8,000, and $200 for 40,000 — look reasonable on paper, but the moment you actually use Manus the way it's marketed (as an autonomous agent that researches, writes, builds, and analyzes for hours), the meter runs hot. Users on Reddit consistently describe burning <strong>40% of a monthly allocation in a single hour</strong>, exhausting the free 1,000 starter credits on their <strong>first request</strong>, and watching looping tasks consume <strong>88,000 credits</strong> in one go. Once your monthly bucket is empty, the only way to keep working is to buy <strong>add-on credit packs</strong>, and that's where heavy agentic users routinely land at <strong>$1,000–$5,000+ per month</strong>.",
   "NoArk's <strong>Diamond plan is a flat $99.99/month for unlimited agentic workflows</strong>. There's no credit balance to watch, no surprise drain, and no incentive to write smaller prompts to save tokens. Run one task or ten thousand — the price is the same. For anyone using AI agents seriously, the math isn't close.",
  ]),
  ("Private by default — no account, nothing collected", [
   "Manus requires you to sign in, and your tasks and data are sent to the company's servers. NoArk takes the opposite path: there is <strong>no sign-in</strong> — no email, no phone number — and your conversations are <strong>stored only on your device and in your own iCloud</strong>, never warehoused on our servers and never used to train any model. Apple's official App Privacy label for NoArk reads <a href='" + dp + "'>“Data Not Collected”</a>, the strictest there is. The work your agents do for you stays yours.",
  ]),
  ("More than an agent: a full Apple super app", [
   "Manus is one thing — an autonomous agent in a browser tab. NoArk is a <strong>full Apple super app</strong> for iPhone, iPad, Mac, and Apple Vision: <strong>live global headlines with one-tap analysis</strong>, the <strong>Fiat Lux</strong> tab where you bring real questions to AI versions of history's wisest minds (Charlie Munger, Steve Jobs, Marcus Aurelius, and 40+ more), and <strong>40+ ready-made workflows</strong> across markets, productivity, travel, education, and life admin — with an investing brain built by the team behind TradingTransformer, inspired by Claude Shannon's vision of AI stock-picking. All powered by many frontier models — Claude Fable, DeepSeek, Mistral, Kimi, and Gemini.",
  ]),
 ],
 "related_heading": "Keep reading",
 "related": [
  (hp, "NoArk — Infinity Memory: the intelligent AI OS & super app"),
  (gp, "NoArk vs ChatGPT"),
  (mp, "NoArk vs Google Gemini"),
  (pp, "NoArk vs Perplexity"),
  (cp, "NoArk vs Character.AI"),
  (ap, "NoArk vs Apple Intelligence"),
  (fp, "Frequently asked questions about NoArk"),
 ],
 "faq": [
  ("Is NoArk a cheaper Manus alternative?", "Dramatically cheaper for heavy users. Manus charges by credits — a single complex task can cost 500–1,000+ credits, and Reddit users routinely report spending $1,000–$5,000+ a month once add-on credit packs kick in. NoArk's Diamond plan is a flat $99.99/month for unlimited agentic workflows, with Gold available from $49.99/month early-bird. Same price whether you run 10 tasks or 10,000."),
  ("Does NoArk have unlimited AI agents?", "Yes. The Diamond plan is $99.99/month flat for unlimited agentic functions — no credit meter, no per-task billing, and no surprise overages."),
  ("Why is Manus so expensive for heavy users?", "Manus runs on credits, and the published tiers cap monthly credits at 4,000, 8,000, or 40,000. Once a complex agentic task can burn 500–1,000+ credits — and looping tasks have been reported consuming 88,000 in one run — heavy users have to buy add-on credit packs to keep working, which is how monthly bills routinely reach $1,000–$5,000+."),
  ("Is my work private with NoArk?", "Yes. There's no sign-in and no data collection: your conversations and agent runs stay on your own device and in your own iCloud, never warehoused on our servers and never used to train models. Apple's App Privacy label reads “Data Not Collected.”"),
  ("Which AI models does NoArk use?", "NoArk routes each request to the best of many frontier models — Anthropic's Claude (Fable), DeepSeek, Mistral, Kimi, and Google's Gemini — instead of relying on a single one."),
  ("Is NoArk free?", "NoArk is free to download on iPhone, iPad, Mac, and Apple Vision, with optional in-app purchases. There's no account and no data collection required to start. The Diamond unlimited tier is $99.99/month; Gold from $49.99/month early-bird."),
 ],
}

# ---------------- Spanish ----------------
hp, gp, cp, mp, pp, ap, fp, dp = rel("es")
content["es"] = {
 "title": "NoArk vs Manus: agentes de IA ilimitados a $99,99/mes, no miles en créditos",
 "desc": "Comparativa NoArk vs Manus: IA agéntica sin angustia por créditos. Manus cobra por tarea en créditos — los usuarios intensivos suelen gastar entre $1.000 y $5.000+ al mes en paquetes adicionales. El plan Diamond de NoArk cuesta $99,99/mes plano para flujos de trabajo agénticos ilimitados, sin medidor, sin registro, y con cada conversación en tu propio dispositivo. Gratis en iPhone, iPad, Mac y Apple Vision.",
 "keywords": "NoArk vs Manus, alternativa a Manus, alternativa barata a Manus, agente de IA ilimitado, IA agéntica precio plano, Manus créditos caros, agente de IA iPhone, agente de IA privado, Claude Fable, DeepSeek, IA ilimitada $99, coste Manus usuario intensivo",
 "ogdesc": "En qué se diferencia NoArk de Manus: un plan Diamond plano de $99,99/mes para flujos agénticos ilimitados, en vez de paquetes de créditos que drenan $1.000–$5.000+ al mes a los usuarios intensivos — y privacidad total sin cuenta.",
 "twdesc": "$99,99/mes plano por agentes ilimitados en lugar de paquetes de créditos de Manus que drenan miles al mes. Sin registro. Cada conversación en tu propio dispositivo.",
 "h1": "NoArk vs Manus",
 "subtitle": "Ambos ejecutan agentes de IA que hacen trabajo real. Solo uno cobra $99,99/mes plano por uso ilimitado — en lugar de un medidor de créditos que puede drenar miles al mes.",
 "intro": "Manus es un agente de IA autónomo capaz, pero funciona con un <strong>medidor de créditos</strong>, y los usuarios intensivos informan habitualmente de gastar <strong>entre $1.000 y $5.000+ al mes</strong> en paquetes adicionales una vez que una sola tarea compleja puede costar 500–1.000 créditos y un bucle puede consumir 88.000 de una sentada. <strong>NoArk — Infinity Memory</strong> toma el camino contrario: un <strong>plan Diamond plano de $99,99/mes</strong> con <strong>flujos de trabajo agénticos ilimitados</strong>, sin angustia por créditos, sin registro y con cada conversación en tu propio dispositivo. Esta es la comparación honesta.",
 "glance": "De un vistazo",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("Modelo de precios", "<span class='yes'>Tarifa plana, ilimitada</span> — plan Diamond $99,99/mes por flujos agénticos ilimitados; Gold desde $49,99/mes early-bird", "Medidor de créditos — cada tarea consume créditos, los usuarios intensivos compran paquetes"),
  ("Coste real para usuario intensivo", "<span class='yes'>$99,99/mes, punto</span> — el mismo precio para 10 o 10.000 tareas", "$1.000–$5.000+/mes es habitual una vez que entran los paquetes de créditos"),
  ("Coste de una tarea compleja", "<span class='yes'>$0 marginal</span> — ya cubierto por tu plan plano", "500–1.000+ créditos cada una; agentes complejos pueden alcanzar 5.000+ en un trabajo"),
  ("Previsibilidad", "<span class='yes'>Totalmente previsible</span> — una factura, sin sorpresas", "Imprevisible — usuarios informan de quemar los créditos del mes en una hora"),
  ("Registro obligatorio", "<span class='yes'>No</span> — sin cuenta, correo ni número de teléfono", "Cuenta obligatoria"),
  ("Tus conversaciones", "<span class='yes'>Guardadas solo en tu dispositivo</span> y en tu propio iCloud — nunca almacenadas ni usadas para entrenar", "Enviadas a los servidores de la empresa"),
  ("Recopilación de datos", "<span class='yes'>Ninguna</span> — etiqueta de privacidad de Apple: «No se recopilan datos»", "Recopila datos de cuenta, uso y tareas"),
  ("Más allá de los agentes", "Una súper app de Apple completa — noticias en directo con análisis de un toque, consejo de las mentes más sabias, más de 40 flujos en iPhone, iPad, Mac y Vision", "Sobre todo un único agente autónomo en una pestaña del navegador"),
 ],
 "note": "Comparativa basada en información pública a junio de 2026. Manus es una marca de su titular; NoArk es una app independiente, no afiliada ni respaldada por aquella. Las cifras de coste para usuario intensivo de Manus reflejan la experiencia pública reportada con consumo de créditos y paquetes adicionales; tu factura real variará según el uso.",
 "sections": [
  ("El problema del medidor — y por qué un plano de $99,99 cambia la matemática", [
   "El precio de Manus se basa en créditos. Los planes publicados — $20 por 4.000 créditos, $40 por 8.000 y $200 por 40.000 — parecen razonables sobre el papel, pero en cuanto usas Manus como se anuncia (un agente autónomo que investiga, escribe, construye y analiza durante horas), el medidor se calienta. Los usuarios en Reddit describen sistemáticamente quemar <strong>el 40% de la asignación mensual en una hora</strong>, agotar los 1.000 créditos iniciales gratuitos en su <strong>primera petición</strong> y ver tareas en bucle consumir <strong>88.000 créditos</strong> de una vez. Cuando se vacía el cubo mensual, la única forma de seguir trabajando es comprar <strong>paquetes de créditos adicionales</strong>, y ahí es donde los usuarios agénticos intensivos aterrizan habitualmente en <strong>$1.000–$5.000+ al mes</strong>.",
   "El <strong>plan Diamond de NoArk es plano: $99,99/mes por flujos agénticos ilimitados</strong>. No hay saldo de créditos que vigilar, ni drenajes por sorpresa, ni incentivo para escribir prompts más cortos por ahorrar tokens. Ejecuta una tarea o diez mil: el precio es el mismo. Para quien usa agentes de IA en serio, la cuenta no está reñida.",
  ]),
  ("Privado por defecto — sin cuenta, sin recopilar nada", [
   "Manus exige iniciar sesión, y tus tareas y datos se envían a sus servidores. NoArk hace lo contrario: <strong>no hay registro</strong> — ni correo ni número de teléfono — y tus conversaciones se <strong>guardan solo en tu dispositivo y en tu propio iCloud</strong>, nunca almacenadas en nuestros servidores ni usadas para entrenar ningún modelo. La etiqueta oficial de privacidad de Apple para NoArk dice <a href='" + dp + "'>«No se recopilan datos»</a>, la más estricta que existe. El trabajo que tus agentes hacen por ti sigue siendo tuyo.",
  ]),
  ("Más que un agente: una súper app de Apple completa", [
   "Manus es una sola cosa — un agente autónomo en una pestaña del navegador. NoArk es una <strong>súper app de Apple completa</strong> para iPhone, iPad, Mac y Apple Vision: <strong>titulares globales en directo con análisis de un toque</strong>, la pestaña <strong>Fiat Lux</strong> donde llevas preguntas reales a versiones de IA de las mentes más sabias (Charlie Munger, Steve Jobs, Marco Aurelio y más de 40), y <strong>más de 40 flujos de trabajo</strong> listos para usar en mercados, productividad, viajes, educación y gestión diaria — con un cerebro inversor creado por el equipo de TradingTransformer, inspirado en la visión de Claude Shannon sobre la IA que elige acciones. Todo impulsado por muchos modelos de frontera — Claude Fable, DeepSeek, Mistral, Kimi y Gemini.",
  ]),
 ],
 "related_heading": "Sigue leyendo",
 "related": [
  (hp, "NoArk — Infinity Memory: el SO inteligente y súper app de IA"),
  (gp, "NoArk vs ChatGPT"),
  (mp, "NoArk vs Google Gemini"),
  (pp, "NoArk vs Perplexity"),
  (cp, "NoArk vs Character.AI"),
  (ap, "NoArk vs Apple Intelligence"),
  (fp, "Preguntas frecuentes sobre NoArk"),
 ],
 "faq": [
  ("¿Es NoArk una alternativa más barata a Manus?", "Mucho más barata para usuarios intensivos. Manus cobra por créditos — una sola tarea compleja puede costar 500–1.000+ créditos, y los usuarios de Reddit informan habitualmente de gastar $1.000–$5.000+ al mes una vez que entran los paquetes adicionales. El plan Diamond de NoArk es plano: $99,99/mes por flujos agénticos ilimitados, con Gold desde $49,99/mes early-bird. El mismo precio para 10 o 10.000 tareas."),
  ("¿NoArk tiene agentes de IA ilimitados?", "Sí. El plan Diamond cuesta $99,99/mes plano por funciones agénticas ilimitadas — sin medidor de créditos, sin facturación por tarea y sin sorpresas."),
  ("¿Por qué es Manus tan caro para usuarios intensivos?", "Manus funciona con créditos, y los planes publicados topan los créditos mensuales en 4.000, 8.000 o 40.000. Cuando una tarea agéntica compleja puede consumir 500–1.000+ créditos — y se han reportado bucles que consumen 88.000 en una sola ejecución —, los usuarios intensivos tienen que comprar paquetes adicionales para seguir trabajando, y por eso las facturas mensuales llegan habitualmente a $1.000–$5.000+."),
  ("¿Mi trabajo es privado con NoArk?", "Sí. No hay registro ni recopilación de datos: tus conversaciones y ejecuciones de agentes se quedan en tu propio dispositivo y en tu propio iCloud, nunca almacenadas en nuestros servidores ni usadas para entrenar modelos. La etiqueta de privacidad de Apple dice «No se recopilan datos»."),
  ("¿Qué modelos de IA usa NoArk?", "NoArk dirige cada petición al mejor de muchos modelos de frontera — Claude (Fable) de Anthropic, DeepSeek, Mistral, Kimi y Gemini de Google — en lugar de depender de uno solo."),
  ("¿Es NoArk gratis?", "NoArk es gratis en iPhone, iPad, Mac y Apple Vision, con compras opcionales dentro de la app. No hace falta cuenta ni recopilación de datos para empezar. El nivel Diamond ilimitado cuesta $99,99/mes; Gold desde $49,99/mes early-bird."),
 ],
}

# ---------------- French ----------------
hp, gp, cp, mp, pp, ap, fp, dp = rel("fr")
content["fr"] = {
 "title": "NoArk vs Manus : des agents IA illimités à 99,99 $/mois, pas des milliers en crédits",
 "desc": "Comparatif NoArk vs Manus : IA agentique sans angoisse de crédits. Manus facture à la tâche en crédits — les utilisateurs intensifs dépensent couramment 1 000 à 5 000+ $ par mois en packs supplémentaires. Le plan Diamond de NoArk est à 99,99 $/mois forfaitaire pour des flux agentiques illimités, sans compteur, sans inscription, et chaque conversation reste sur votre propre appareil. Gratuit sur iPhone, iPad, Mac et Apple Vision.",
 "keywords": "NoArk vs Manus, alternative à Manus, alternative pas chère à Manus, agent IA illimité, IA agentique prix forfaitaire, crédits Manus chers, agent IA iPhone, agent IA privé, Claude Fable, DeepSeek, IA illimitée 99 $, coût Manus utilisateur intensif",
 "ogdesc": "En quoi NoArk diffère de Manus : un plan Diamond forfaitaire à 99,99 $/mois pour des flux agentiques illimités, au lieu de packs de crédits qui drainent 1 000 à 5 000+ $ par mois pour les utilisateurs intensifs — et une confidentialité totale sans compte.",
 "twdesc": "99,99 $/mois forfaitaire pour des agents illimités au lieu des packs de crédits Manus qui drainent des milliers par mois. Sans inscription. Chaque conversation sur votre propre appareil.",
 "h1": "NoArk vs Manus",
 "subtitle": "Les deux exécutent des agents IA qui font du vrai travail. Une seule facture 99,99 $/mois forfaitaire pour un usage illimité — au lieu d'un compteur de crédits qui peut drainer des milliers par mois.",
 "intro": "Manus est un agent IA autonome capable — mais il fonctionne avec un <strong>compteur de crédits</strong>, et les utilisateurs intensifs rapportent couramment dépenser <strong>1 000 à 5 000+ $ par mois</strong> en packs supplémentaires dès qu'une seule tâche complexe peut coûter 500 à 1 000 crédits et qu'une boucle peut en consommer 88 000 d'un coup. <strong>NoArk — Infinity Memory</strong> prend le chemin inverse : un <strong>plan Diamond forfaitaire à 99,99 $/mois</strong> avec <strong>des flux agentiques illimités</strong>, sans angoisse de crédits, sans inscription, et chaque conversation gardée sur votre propre appareil. Voici la comparaison honnête.",
 "glance": "En un coup d'œil",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("Modèle de prix", "<span class='yes'>Forfait, illimité</span> — plan Diamond 99,99 $/mois pour des flux agentiques illimités ; Gold à partir de 49,99 $/mois early-bird", "Compteur de crédits — chaque tâche consomme des crédits, les utilisateurs intensifs achètent des packs"),
  ("Coût réel utilisateur intensif", "<span class='yes'>99,99 $/mois, point final</span> — même prix pour 10 ou 10 000 tâches", "1 000 à 5 000+ $/mois est courant dès que les packs de crédits entrent en jeu"),
  ("Coût d'une tâche complexe", "<span class='yes'>0 $ marginal</span> — déjà couvert par votre forfait", "500 à 1 000+ crédits chacune ; des agents complexes peuvent atteindre 5 000+ sur un seul travail"),
  ("Prévisibilité", "<span class='yes'>Totalement prévisible</span> — une facture, aucune surprise", "Imprévisible — des utilisateurs rapportent avoir brûlé un mois de crédits en une heure"),
  ("Inscription requise", "<span class='yes'>Non</span> — pas de compte, d'e-mail ni de numéro de téléphone", "Compte requis"),
  ("Vos conversations", "<span class='yes'>Stockées uniquement sur votre appareil</span> et dans votre propre iCloud — jamais entreposées ni utilisées pour entraîner", "Envoyées aux serveurs de l'entreprise"),
  ("Collecte de données", "<span class='yes'>Aucune</span> — étiquette de confidentialité d'Apple : « Données non collectées »", "Collecte des données de compte, d'usage et de tâches"),
  ("Au-delà des agents", "Une super app Apple complète — actualité en direct avec analyse en un geste, conseil des plus grands esprits, plus de 40 flux sur iPhone, iPad, Mac et Vision", "Surtout un seul agent autonome dans un onglet de navigateur"),
 ],
 "note": "Comparaison fondée sur des informations publiques en juin 2026. Manus est une marque de son détenteur respectif ; NoArk est une app indépendante, ni affiliée ni approuvée par celle-ci. Les chiffres de coût utilisateur intensif pour Manus reflètent l'expérience publique rapportée avec la consommation de crédits et les packs supplémentaires ; votre facture réelle variera selon votre usage.",
 "sections": [
  ("Le problème du compteur — et pourquoi un forfait à 99,99 $ change le calcul", [
   "Le prix de Manus est bâti sur des crédits. Les paliers publiés — 20 $ pour 4 000 crédits, 40 $ pour 8 000, 200 $ pour 40 000 — semblent raisonnables sur le papier, mais dès que vous utilisez Manus comme il est vendu (un agent autonome qui cherche, écrit, construit et analyse pendant des heures), le compteur s'emballe. Sur Reddit, les utilisateurs décrivent systématiquement <strong>brûler 40 % de leur allocation mensuelle en une heure</strong>, épuiser les 1 000 crédits gratuits initiaux dès leur <strong>première requête</strong> et voir des tâches en boucle consommer <strong>88 000 crédits</strong> d'un coup. Une fois le seau mensuel vide, la seule façon de continuer est d'acheter des <strong>packs de crédits supplémentaires</strong>, et c'est là que les utilisateurs agentiques intensifs atterrissent couramment à <strong>1 000 à 5 000+ $ par mois</strong>.",
   "Le <strong>plan Diamond de NoArk est forfaitaire : 99,99 $/mois pour des flux agentiques illimités</strong>. Pas de solde à surveiller, pas de drainage surprise, et pas d'incitation à raccourcir vos prompts pour économiser des tokens. Lancez une tâche ou dix mille — le prix est identique. Pour qui utilise sérieusement des agents IA, le calcul ne souffre aucune ambiguïté.",
  ]),
  ("Privé par défaut — sans compte, rien de collecté", [
   "Manus exige une connexion, et vos tâches et données sont envoyées à ses serveurs. NoArk fait l'inverse : il n'y a <strong>aucune inscription</strong> — pas d'e-mail, pas de numéro de téléphone — et vos conversations sont <strong>stockées uniquement sur votre appareil et dans votre propre iCloud</strong>, jamais entreposées sur nos serveurs ni utilisées pour entraîner un modèle. L'étiquette officielle de confidentialité d'Apple pour NoArk indique <a href='" + dp + "'>« Données non collectées »</a>, la plus stricte qui soit. Le travail que vos agents font pour vous reste à vous.",
  ]),
  ("Plus qu'un agent : une super app Apple complète", [
   "Manus, c'est une seule chose — un agent autonome dans un onglet de navigateur. NoArk est une <strong>super app Apple complète</strong> pour iPhone, iPad, Mac et Apple Vision : <strong>actualité mondiale en direct avec analyse en un geste</strong>, l'onglet <strong>Fiat Lux</strong> où vous apportez de vraies questions à des versions IA des plus grands esprits (Charlie Munger, Steve Jobs, Marc Aurèle et plus de 40 autres) et <strong>plus de 40 flux de travail</strong> prêts à l'emploi couvrant marchés, productivité, voyage, éducation et gestion du quotidien — avec un cerveau d'investisseur créé par l'équipe de TradingTransformer, inspiré par la vision de Claude Shannon d'une IA qui choisit les actions. Le tout propulsé par de nombreux modèles de pointe — Claude Fable, DeepSeek, Mistral, Kimi et Gemini.",
  ]),
 ],
 "related_heading": "À lire ensuite",
 "related": [
  (hp, "NoArk — Infinity Memory : l'OS intelligent et la super app IA"),
  (gp, "NoArk vs ChatGPT"),
  (mp, "NoArk vs Google Gemini"),
  (pp, "NoArk vs Perplexity"),
  (cp, "NoArk vs Character.AI"),
  (ap, "NoArk vs Apple Intelligence"),
  (fp, "Questions fréquentes sur NoArk"),
 ],
 "faq": [
  ("NoArk est-elle une alternative moins chère à Manus ?", "Bien moins chère pour les utilisateurs intensifs. Manus facture aux crédits — une seule tâche complexe peut coûter 500 à 1 000+ crédits, et les utilisateurs Reddit rapportent couramment 1 000 à 5 000+ $/mois dès que les packs de crédits supplémentaires entrent en jeu. Le plan Diamond de NoArk est forfaitaire : 99,99 $/mois pour des flux agentiques illimités, avec Gold à partir de 49,99 $/mois early-bird. Même prix pour 10 ou 10 000 tâches."),
  ("NoArk a-t-elle des agents IA illimités ?", "Oui. Le plan Diamond est à 99,99 $/mois forfaitaire pour des fonctions agentiques illimitées — pas de compteur de crédits, pas de facturation à la tâche, pas de surprise."),
  ("Pourquoi Manus est-il si cher pour les utilisateurs intensifs ?", "Manus fonctionne aux crédits, et les paliers publiés plafonnent à 4 000, 8 000 ou 40 000 crédits par mois. Quand une tâche agentique complexe peut consommer 500 à 1 000+ crédits — et que des boucles ont été rapportées consommant 88 000 en une seule exécution —, les utilisateurs intensifs doivent acheter des packs supplémentaires pour continuer, et c'est ainsi que les factures mensuelles atteignent couramment 1 000 à 5 000+ $."),
  ("Mon travail est-il privé avec NoArk ?", "Oui. Aucune inscription ni collecte de données : vos conversations et exécutions d'agents restent sur votre propre appareil et dans votre propre iCloud, jamais entreposées sur nos serveurs ni utilisées pour entraîner des modèles. L'étiquette de confidentialité d'Apple indique « Données non collectées »."),
  ("Quels modèles d'IA NoArk utilise-t-elle ?", "NoArk route chaque requête vers le meilleur de nombreux modèles de pointe — Claude (Fable) d'Anthropic, DeepSeek, Mistral, Kimi et Gemini de Google — au lieu de dépendre d'un seul."),
  ("NoArk est-elle gratuite ?", "NoArk est gratuite sur iPhone, iPad, Mac et Apple Vision, avec des achats intégrés optionnels. Aucun compte ni aucune collecte de données n'est nécessaire pour commencer. Le palier Diamond illimité est à 99,99 $/mois ; Gold à partir de 49,99 $/mois early-bird."),
 ],
}

# ---------------- Japanese ----------------
hp, gp, cp, mp, pp, ap, fp, dp = rel("ja")
content["ja"] = {
 "title": "NoArk vs Manus：月額99.99ドルでAIエージェント無制限、クレジットに何千ドルも払わない",
 "desc": "NoArk と Manus を比較：クレジットに不安のないエージェント型 AI。Manus はタスクごとにクレジットで課金され、ヘビーユーザーは追加パックで月に1,000～5,000ドル超を払うことも珍しくありません。NoArk の Diamond プランは月額99.99ドル定額でエージェント型ワークフロー無制限、メーターなし、サインインなし、すべての会話をあなた自身のデバイスで非公開に。iPhone・iPad・Mac・Apple Vision で無料。",
 "keywords": "NoArk vs Manus, Manus 代替, 安い Manus 代替, AI エージェント 無制限, エージェント型 AI 定額, Manus クレジット 高い, AI エージェント iPhone, プライベート AI エージェント, Claude Fable, DeepSeek, 月額99ドル 無制限 AI, Manus ヘビーユーザー コスト",
 "ogdesc": "NoArk が Manus と違う点：ヘビーユーザーから月1,000～5,000ドル超を吸い上げるクレジットパックではなく、月額99.99ドル定額でエージェント型ワークフローが無制限。さらにアカウント不要で完全プライベート。",
 "twdesc": "数千ドルを吸い上げる Manus のクレジットパックの代わりに、月額99.99ドル定額でエージェント無制限。サインイン不要。すべての会話があなた自身のデバイスに。",
 "h1": "NoArk vs Manus",
 "subtitle": "どちらも実務をこなす AI エージェントを動かします。しかし、月に何千ドルも吸い取りかねないクレジットメーターではなく、月額99.99ドル定額で無制限利用を提供するのは一方だけです。",
 "intro": "Manus は有能な自律型 AI エージェントですが、<strong>クレジットメーター</strong>で動きます。複雑なタスク1件で500～1,000クレジット、暴走ループ1回で88,000クレジットを使い切る事例もあり、ヘビーユーザーは追加パックで<strong>月1,000～5,000ドル超</strong>を払う事例が珍しくありません。<strong>NoArk — Infinity Memory</strong> は逆の道を行きます。<strong>月額99.99ドル定額の Diamond プラン</strong>で<strong>エージェント型ワークフローが無制限</strong>。クレジットの不安なし、サインインなし、すべての会話をあなた自身のデバイスに保ちます。これが率直な比較です。",
 "glance": "ひと目でわかる比較",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("価格モデル", "<span class='yes'>定額・無制限</span> — Diamond プラン月額99.99ドルでエージェント型ワークフロー無制限、Gold は早期割で月額49.99ドルから", "クレジットメーター — タスクごとに消費、ヘビーユーザーは追加パックを購入"),
  ("ヘビーユーザーの実コスト", "<span class='yes'>月99.99ドル、それだけ</span> — 10タスクでも10,000タスクでも同じ価格", "追加クレジットパックを買い始めると月1,000～5,000ドル超は一般的"),
  ("複雑なタスク1件のコスト", "<span class='yes'>追加0ドル</span> — 定額プランに含まれる", "1件あたり500～1,000クレジット超。複雑なエージェントは1ジョブで5,000クレジット超に達することも"),
  ("予測可能性", "<span class='yes'>完全に予測可能</span> — 1本の請求、想定外の超過なし", "予測不能 — 1か月分のクレジットを1時間で使い切る報告も"),
  ("サインイン", "<span class='yes'>不要</span> — アカウントもメールも電話番号も不要", "アカウントが必要"),
  ("あなたの会話", "<span class='yes'>あなたのデバイス</span>とあなた自身の iCloud だけに保存 — 蓄積も学習利用もされません", "企業のサーバーに送信"),
  ("データ収集", "<span class='yes'>なし</span> — Apple のプライバシーラベル：「データは収集されません」", "アカウント・利用状況・タスクのデータを収集"),
  ("エージェントの先", "フル機能の Apple スーパーアプリ — ライブニュース＋ワンタップ分析、歴史上の賢人の助言、iPhone・iPad・Mac・Vision で40以上のワークフロー", "主にブラウザタブで動く単一の自律エージェント"),
 ],
 "note": "本比較は2026年6月時点の公開情報に基づきます。Manus は各権利者の商標です。NoArk は独立したアプリであり、提携や承認はありません。Manus のヘビーユーザーのコスト数値は、クレジット消費と追加パックに関して公開報告されたユーザー体験を反映したものです。実際の請求額は利用状況により変動します。",
 "sections": [
  ("メーター問題 — そして月99.99ドル定額が計算を変える理由", [
   "Manus の価格はクレジットを軸に組まれています。公開ティア — 4,000クレジットで20ドル、8,000で40ドル、40,000で200ドル — は紙の上では妥当に見えますが、宣伝どおりの使い方（数時間にわたって調査・執筆・構築・分析を行う自律エージェント）をした瞬間、メーターは過熱します。Reddit のユーザーは一様に、<strong>月の割り当ての40％を1時間で焼き切る</strong>、無料スターター1,000クレジットを<strong>初回リクエスト</strong>で使い切る、ループしたタスクが<strong>88,000クレジット</strong>を一気に消費する、と報告しています。月のバケツが空になれば、続けるには<strong>追加クレジットパックを買う</strong>しかなく、ヘビーなエージェント利用者はそこから<strong>月1,000～5,000ドル超</strong>に着地するのが通例です。",
   "<strong>NoArk の Diamond プランは月額99.99ドル定額でエージェント型ワークフロー無制限</strong>です。残高を気にする必要も、不意の枯渇も、トークン節約のためにプロンプトを縮める動機もありません。1タスクでも10,000タスクでも価格は同じ。AI エージェントを真剣に使う人にとって、この計算に競争はありません。",
  ]),
  ("既定でプライベート — アカウントなし、何も収集しない", [
   "Manus はサインインを必須とし、タスクとデータは企業のサーバーに送られます。NoArk は逆です。<strong>サインインは不要</strong> — メールも電話番号もなく — あなたの会話は<strong>あなたのデバイスとあなた自身の iCloud だけに保存</strong>され、私たちのサーバーに蓄積されることも、どのモデルの学習に使われることもありません。Apple 公式の NoArk のプライバシーラベルは <a href='" + dp + "'>「データは収集されません」</a> — 最も厳格なラベルです。エージェントがあなたのために行った仕事は、あなたのものです。",
  ]),
  ("エージェント以上：フル機能の Apple スーパーアプリ", [
   "Manus はひとつのこと — ブラウザタブの中の自律エージェント — です。NoArk は iPhone・iPad・Mac・Apple Vision のための<strong>フル機能の Apple スーパーアプリ</strong>です。<strong>ライブ世界ニュース＋ワンタップ分析</strong>、本物の問いを歴史上の賢人のAI版（チャーリー・マンガー、スティーブ・ジョブズ、マルクス・アウレリウスほか40名以上）に持ち込める <strong>Fiat Lux</strong> タブ、市場・生産性・旅行・教育・生活の雑務にわたる<strong>40以上の即戦力ワークフロー</strong>、そして TradingTransformer チームが作り、クロード・シャノンのAI株式選択のビジョンに着想を得た投資する頭脳。すべてが多数のフロンティアモデル — Claude Fable、DeepSeek、Mistral、Kimi、Gemini — で動きます。",
  ]),
 ],
 "related_heading": "あわせて読む",
 "related": [
  (hp, "NoArk — Infinity Memory：インテリジェントAI OS・スーパーアプリ"),
  (gp, "NoArk vs ChatGPT"),
  (mp, "NoArk vs Google Gemini"),
  (pp, "NoArk vs Perplexity"),
  (cp, "NoArk vs Character.AI"),
  (ap, "NoArk vs Apple Intelligence"),
  (fp, "NoArk についてのよくある質問"),
 ],
 "faq": [
  ("NoArk は Manus より安い代替になりますか？", "ヘビーユーザーには圧倒的に安価です。Manus はクレジット課金で、複雑なタスク1件で500～1,000クレジット超になることもあり、Reddit のユーザーは追加パックを買い始めると月1,000～5,000ドル超を払う事例が珍しくありません。NoArk の Diamond プランは月額99.99ドル定額でエージェント型ワークフロー無制限。Gold は早期割で月額49.99ドルから。10タスクでも10,000タスクでも同じ価格です。"),
  ("NoArk には無制限の AI エージェントがありますか？", "あります。Diamond プランは月額99.99ドル定額でエージェント機能が無制限 — クレジットメーターも、タスクごとの課金も、想定外の超過もありません。"),
  ("なぜ Manus はヘビーユーザーにとって高くつくのですか？", "Manus はクレジットで動き、公開ティアは月4,000・8,000・40,000クレジットでキャップされます。複雑なエージェント型タスク1件で500～1,000クレジット超を消費しうること、そして1回の実行で88,000クレジットを消費したループの報告もあることから、ヘビーユーザーは追加パックを買って続行するしかなく、月の請求が1,000～5,000ドル超に達するのが通例になります。"),
  ("NoArk で私の作業はプライベートですか？", "はい。サインインもデータ収集もありません。会話とエージェントの実行はあなた自身のデバイスとあなた自身の iCloud に残り、私たちのサーバーに蓄積されることも、モデルの学習に使われることもありません。Apple のプライバシーラベルは「データは収集されません」です。"),
  ("NoArk はどの AI モデルを使いますか？", "NoArk はリクエストごとに、Anthropic の Claude（Fable）、DeepSeek、Mistral、Kimi、Google の Gemini など多数のフロンティアモデルから最適なものを選びます。単一のモデルに頼りません。"),
  ("NoArk は無料ですか？", "NoArk は iPhone・iPad・Mac・Apple Vision で無料で、オプションのアプリ内課金があります。始めるのにアカウントもデータ収集も不要です。Diamond の無制限ティアは月額99.99ドル、Gold は早期割で月額49.99ドルから。"),
 ],
}

# ---------------- Simplified Chinese ----------------
hp, gp, cp, mp, pp, ap, fp, dp = rel("zh-cn")
content["zh-cn"] = {
 "title": "NoArk 对比 Manus：99.99 美元/月即享无限 AI 智能体，而不是数千美元的积分",
 "desc": "NoArk 与 Manus 全面对比：没有积分焦虑的智能体 AI。Manus 按任务消耗积分计费——重度用户每月在加购积分包上常常花掉 1,000–5,000 美元以上。NoArk 的 Diamond 套餐月费 99.99 美元，所有智能体工作流不限量，没有计费表，无需登录，每段对话都留在你自己的设备上。iPhone、iPad、Mac 和 Apple Vision 免费下载。",
 "keywords": "NoArk 对比 Manus, Manus 替代品, 便宜 Manus 替代品, 无限 AI 智能体, 智能体 AI 包月, Manus 积分太贵, AI 智能体 iPhone, 私密 AI 智能体, Claude Fable, DeepSeek, 99 美元 无限 AI, Manus 重度用户成本",
 "ogdesc": "NoArk 与 Manus 的不同：用 99.99 美元/月的 Diamond 包月套餐换取无限智能体工作流，而不是让重度用户每月被掏走 1,000–5,000 美元以上的积分包——并且无需账户、完全私密。",
 "twdesc": "用 99.99 美元/月的包月套餐换取无限智能体，而不是 Manus 那种每月吸走数千美元的积分包。无需登录。每段对话都留在你自己的设备上。",
 "h1": "NoArk 对比 Manus",
 "subtitle": "两者都能跑 AI 智能体做真活。但只有一个用 99.99 美元/月的包月价格提供无限使用——而不是一个可能每月吸走数千美元的积分计费表。",
 "intro": "Manus 是一款能力出色的自主 AI 智能体——但它运行在<strong>积分计费表</strong>上。一项复杂任务就能耗掉 500–1,000 积分，跑飞的循环一次能吃掉 88,000 积分，重度用户在加购积分包上每月花掉 <strong>1,000–5,000 美元以上</strong>是常态。<strong>NoArk — 无限记忆</strong>走的是相反的路：<strong>Diamond 包月套餐 99.99 美元/月</strong>，<strong>智能体工作流不限量</strong>，没有积分焦虑，无需登录，每段对话都留在你自己的设备上。下面是坦诚的对比。",
 "glance": "一览对比",
 "col_noark": "NoArk — 无限记忆",
 "rows": [
  ("计费模式", "<span class='yes'>包月不限量</span>——Diamond 套餐 99.99 美元/月，智能体工作流不限量；Gold 早鸟价 49.99 美元/月起", "积分计费表——每项任务消耗积分，重度用户加购积分包"),
  ("重度用户真实开销", "<span class='yes'>就 99.99 美元/月</span>——10 个任务和 10,000 个任务一个价", "一旦开始加购积分包，每月 1,000–5,000 美元以上很常见"),
  ("一项复杂任务的成本", "<span class='yes'>边际成本 0 美元</span>——已包含在你的包月套餐里", "每项 500–1,000 积分以上；复杂智能体一个任务可能高达 5,000 积分以上"),
  ("可预测性", "<span class='yes'>完全可预测</span>——一张账单，没有意外超额", "不可预测——有用户报告一个小时烧光一个月的积分"),
  ("是否需要登录", "<span class='yes'>不需要</span>——无账户、邮箱或手机号", "需要账户"),
  ("你的对话", "<span class='yes'>只保存在你的设备</span>和你自己的 iCloud 中——绝不堆放或用于训练", "发送到公司服务器"),
  ("数据收集", "<span class='yes'>无</span>——Apple 隐私标签：“不收集数据”", "收集账户、使用和任务数据"),
  ("智能体之外", "一款完整的 Apple 超级应用——实时新闻＋一键分析，历史智者的建议，iPhone、iPad、Mac 和 Vision 上的 40 多个工作流", "主要是浏览器标签页里的一个自主智能体"),
 ],
 "note": "对比基于截至 2026 年 6 月的公开信息。Manus 是其各自所有者的商标；NoArk 是独立应用，与其无关联，也未获其背书。Manus 重度用户成本数据来自公开报道的用户体验（积分消耗与加购积分包），你的真实账单将随使用情况变化。",
 "sections": [
  ("积分计费表的问题——以及包月 99.99 美元为何改变了这道算术题", [
   "Manus 的定价是围绕积分搭起来的。公开档位——4,000 积分 20 美元、8,000 积分 40 美元、40,000 积分 200 美元——纸面看起来还算合理，可一旦你按它宣传的方式去用（一个连续数小时做研究、写作、构建和分析的自主智能体），计费表就会发烫。Reddit 上的用户一致描述了这些场景：<strong>一个小时烧掉本月 40% 的额度</strong>、<strong>第一次请求</strong>就用光 1,000 个免费积分、循环跑飞的任务一次吞掉 <strong>88,000 积分</strong>。当月度桶被掏空，你唯一能继续干活的办法就是买<strong>加购积分包</strong>，重度智能体用户也正是在这里稳稳落到 <strong>每月 1,000–5,000 美元以上</strong>。",
   "NoArk 的 <strong>Diamond 套餐是 99.99 美元/月包月，智能体工作流不限量</strong>。没有积分余额要盯着，没有意外被掏空，也没有动机去为了省 token 而把 prompt 写短。跑一个任务，还是跑一万个——价格一样。对于真正认真使用 AI 智能体的人，这道算术题没有悬念。",
  ]),
  ("默认私密——无需账户，什么都不收集", [
   "Manus 要求你登录，而你的任务和数据会被发送到它的服务器。NoArk 恰恰相反：<strong>无需登录</strong>——没有邮箱、没有手机号——你的对话<strong>只保存在你的设备和你自己的 iCloud 中</strong>，绝不堆放在我们的服务器上，也绝不用于训练任何模型。Apple 官方为 NoArk 出具的隐私标签写着 <a href='" + dp + "'>“不收集数据”</a>——最严格的一档。智能体替你做的工作，依然属于你。",
  ]),
  ("不只是一个智能体：一款完整的 Apple 超级应用", [
   "Manus 就是一件事——浏览器标签页里的一个自主智能体。NoArk 是一款面向 iPhone、iPad、Mac 和 Apple Vision 的<strong>完整 Apple 超级应用</strong>：<strong>带一键分析的实时全球头条</strong>、把真实问题带给历史最有智慧者 AI 版本（查理·芒格、史蒂夫·乔布斯、马可·奥勒留等 40 多位）的 <strong>Fiat Lux</strong> 标签，以及涵盖市场、生产力、旅行、教育和生活事务的 <strong>40 多个开箱即用工作流</strong>，外加由 TradingTransformer 团队打造、灵感来自克劳德·香农 AI 选股愿景的投资大脑。一切由众多前沿模型驱动——Claude Fable、DeepSeek、Mistral、Kimi 和 Gemini。",
  ]),
 ],
 "related_heading": "继续阅读",
 "related": [
  (hp, "NoArk — 无限记忆：智能 AI 操作系统与超级应用"),
  (gp, "NoArk 对比 ChatGPT"),
  (mp, "NoArk 对比 Google Gemini"),
  (pp, "NoArk 对比 Perplexity"),
  (cp, "NoArk 对比 Character.AI"),
  (ap, "NoArk 对比 Apple Intelligence"),
  (fp, "关于 NoArk 的常见问题"),
 ],
 "faq": [
  ("NoArk 是更便宜的 Manus 替代品吗？", "对重度用户而言便宜得多。Manus 按积分计费——一项复杂任务就能烧掉 500–1,000 积分以上，Reddit 用户一旦开始加购积分包，每月 1,000–5,000 美元以上是常态。NoArk 的 Diamond 套餐为 99.99 美元/月包月，智能体工作流不限量，Gold 早鸟价 49.99 美元/月起。10 个任务和 10,000 个任务一个价。"),
  ("NoArk 提供无限的 AI 智能体吗？", "提供。Diamond 套餐为 99.99 美元/月包月，智能体功能不限量——没有积分计费表，没有按任务计费，也没有意外超额。"),
  ("为什么 Manus 对重度用户来说这么贵？", "Manus 跑在积分上，公开档位把月度积分上限定在 4,000、8,000 或 40,000。一项复杂的智能体任务可能消耗 500–1,000 积分以上——而循环跑飞一次就消耗 88,000 积分的报告也存在——重度用户只能买加购积分包才能继续工作，于是每月账单经常落到 1,000–5,000 美元以上。"),
  ("我的工作在 NoArk 里是私密的吗？", "是的。没有登录、也不收集数据：你的对话和智能体执行都留在你自己的设备和你自己的 iCloud 中，绝不堆放在我们的服务器上，也绝不用于训练模型。Apple 的隐私标签写着“不收集数据”。"),
  ("NoArk 用哪些 AI 模型？", "NoArk 将每个请求路由到众多前沿模型中最合适的一个——Anthropic 的 Claude（Fable）、DeepSeek、Mistral、Kimi 和谷歌的 Gemini——而不是依赖单一一个。"),
  ("NoArk 免费吗？", "NoArk 在 iPhone、iPad、Mac 和 Apple Vision 上免费下载，含可选的应用内购买。开始使用无需账户，也不收集数据。Diamond 不限量档为 99.99 美元/月；Gold 早鸟价 49.99 美元/月起。"),
 ],
}

# ---------------- Traditional Chinese ----------------
hp, gp, cp, mp, pp, ap, fp, dp = rel("zh-tw")
content["zh-tw"] = {
 "title": "NoArk 對比 Manus：99.99 美元/月即享無限 AI 代理人,而不是數千美元的點數",
 "desc": "NoArk 與 Manus 全面對比：沒有點數焦慮的代理人式 AI。Manus 按任務消耗點數計費——重度使用者每月在加購點數包上常常花掉 1,000–5,000 美元以上。NoArk 的 Diamond 方案月費 99.99 美元,所有代理人式工作流程不限量,沒有計費表,無需登入,每段對話都留在你自己的裝置上。iPhone、iPad、Mac 和 Apple Vision 免費下載。",
 "keywords": "NoArk 對比 Manus, Manus 替代品, 便宜 Manus 替代品, 無限 AI 代理人, 代理人式 AI 包月, Manus 點數太貴, AI 代理人 iPhone, 私密 AI 代理人, Claude Fable, DeepSeek, 99 美元 無限 AI, Manus 重度使用者成本",
 "ogdesc": "NoArk 與 Manus 的不同:用 99.99 美元/月的 Diamond 包月方案換取無限代理人式工作流程,而不是讓重度使用者每月被掏走 1,000–5,000 美元以上的點數包——並且無需帳號、完全私密。",
 "twdesc": "用 99.99 美元/月的包月方案換取無限代理人,而不是 Manus 那種每月吸走數千美元的點數包。無需登入。每段對話都留在你自己的裝置上。",
 "h1": "NoArk 對比 Manus",
 "subtitle": "兩者都能跑 AI 代理人做真實工作。但只有一個用 99.99 美元/月的包月價格提供無限使用——而不是一個可能每月吸走數千美元的點數計費表。",
 "intro": "Manus 是一款能力出色的自主 AI 代理人——但它運行在<strong>點數計費表</strong>上。一項複雜任務就能耗掉 500–1,000 點數,跑飛的迴圈一次能吃掉 88,000 點數,重度使用者在加購點數包上每月花掉 <strong>1,000–5,000 美元以上</strong>是常態。<strong>NoArk — 無限記憶</strong>走的是相反的路：<strong>Diamond 包月方案 99.99 美元/月</strong>,<strong>代理人式工作流程不限量</strong>,沒有點數焦慮,無需登入,每段對話都留在你自己的裝置上。以下是坦誠的對比。",
 "glance": "一覽對比",
 "col_noark": "NoArk — 無限記憶",
 "rows": [
  ("計費模式", "<span class='yes'>包月不限量</span>——Diamond 方案 99.99 美元/月,代理人式工作流程不限量;Gold 早鳥價 49.99 美元/月起", "點數計費表——每項任務消耗點數,重度使用者加購點數包"),
  ("重度使用者真實開銷", "<span class='yes'>就 99.99 美元/月</span>——10 個任務和 10,000 個任務一個價", "一旦開始加購點數包,每月 1,000–5,000 美元以上很常見"),
  ("一項複雜任務的成本", "<span class='yes'>邊際成本 0 美元</span>——已包含在你的包月方案裡", "每項 500–1,000 點數以上;複雜代理人一個任務可能高達 5,000 點數以上"),
  ("可預測性", "<span class='yes'>完全可預測</span>——一張帳單,沒有意外超額", "不可預測——有使用者回報一個小時燒光一個月的點數"),
  ("是否需要登入", "<span class='yes'>不需要</span>——無帳號、電子郵件或手機號碼", "需要帳號"),
  ("你的對話", "<span class='yes'>只保存在你的裝置</span>和你自己的 iCloud 中——絕不堆放或用於訓練", "傳送到公司伺服器"),
  ("資料收集", "<span class='yes'>無</span>——Apple 隱私標籤：「不收集資料」", "收集帳號、使用和任務資料"),
  ("代理人之外", "一款完整的 Apple 超級應用程式——即時新聞＋一鍵分析,歷史智者的建議,iPhone、iPad、Mac 和 Vision 上的 40 多個工作流程", "主要是瀏覽器分頁裡的一個自主代理人"),
 ],
 "note": "對比基於截至 2026 年 6 月的公開資訊。Manus 是其各自所有者的商標;NoArk 是獨立應用程式,與其無關聯,也未獲其背書。Manus 重度使用者成本資料來自公開報導的使用者體驗（點數消耗與加購點數包）,你的真實帳單將隨使用情況變化。",
 "sections": [
  ("點數計費表的問題——以及包月 99.99 美元為何改變了這道算術題", [
   "Manus 的定價是圍繞點數搭起來的。公開檔位——4,000 點數 20 美元、8,000 點數 40 美元、40,000 點數 200 美元——紙面看起來還算合理,可一旦你按它宣傳的方式去用（一個連續數小時做研究、寫作、建構和分析的自主代理人）,計費表就會發燙。Reddit 上的使用者一致描述了這些場景：<strong>一個小時燒掉本月 40% 的額度</strong>、<strong>第一次請求</strong>就用光 1,000 個免費點數、迴圈跑飛的任務一次吞掉 <strong>88,000 點數</strong>。當月度桶被掏空,你唯一能繼續工作的辦法就是買<strong>加購點數包</strong>,重度代理人使用者也正是在這裡穩穩落到 <strong>每月 1,000–5,000 美元以上</strong>。",
   "NoArk 的 <strong>Diamond 方案是 99.99 美元/月包月,代理人式工作流程不限量</strong>。沒有點數餘額要盯著,沒有意外被掏空,也沒有動機去為了省 token 而把 prompt 寫短。跑一個任務,還是跑一萬個——價格一樣。對於真正認真使用 AI 代理人的人,這道算術題沒有懸念。",
  ]),
  ("預設私密——無需帳號,什麼都不收集", [
   "Manus 要求你登入,而你的任務和資料會被傳送到它的伺服器。NoArk 恰恰相反：<strong>無需登入</strong>——沒有電子郵件、沒有手機號碼——你的對話<strong>只保存在你的裝置和你自己的 iCloud 中</strong>,絕不堆放在我們的伺服器上,也絕不用於訓練任何模型。Apple 官方為 NoArk 出具的隱私標籤寫著 <a href='" + dp + "'>「不收集資料」</a>——最嚴格的一檔。代理人替你做的工作,依然屬於你。",
  ]),
  ("不只是一個代理人：一款完整的 Apple 超級應用程式", [
   "Manus 就是一件事——瀏覽器分頁裡的一個自主代理人。NoArk 是一款面向 iPhone、iPad、Mac 和 Apple Vision 的<strong>完整 Apple 超級應用程式</strong>：<strong>帶一鍵分析的即時全球頭條</strong>、把真實問題帶給歷史最有智慧者 AI 版本（查理·蒙格、史蒂夫·賈伯斯、馬可·奧理略等 40 多位）的 <strong>Fiat Lux</strong> 分頁,以及涵蓋市場、生產力、旅行、教育和生活事務的 <strong>40 多個開箱即用工作流程</strong>,外加由 TradingTransformer 團隊打造、靈感來自克勞德·夏農 AI 選股願景的投資大腦。一切由眾多前沿模型驅動——Claude Fable、DeepSeek、Mistral、Kimi 和 Gemini。",
  ]),
 ],
 "related_heading": "繼續閱讀",
 "related": [
  (hp, "NoArk — 無限記憶：智慧型 AI 作業系統與超級應用程式"),
  (gp, "NoArk 對比 ChatGPT"),
  (mp, "NoArk 對比 Google Gemini"),
  (pp, "NoArk 對比 Perplexity"),
  (cp, "NoArk 對比 Character.AI"),
  (ap, "NoArk 對比 Apple Intelligence"),
  (fp, "關於 NoArk 的常見問題"),
 ],
 "faq": [
  ("NoArk 是更便宜的 Manus 替代品嗎？", "對重度使用者而言便宜得多。Manus 按點數計費——一項複雜任務就能燒掉 500–1,000 點數以上,Reddit 使用者一旦開始加購點數包,每月 1,000–5,000 美元以上是常態。NoArk 的 Diamond 方案為 99.99 美元/月包月,代理人式工作流程不限量,Gold 早鳥價 49.99 美元/月起。10 個任務和 10,000 個任務一個價。"),
  ("NoArk 提供無限的 AI 代理人嗎？", "提供。Diamond 方案為 99.99 美元/月包月,代理人式功能不限量——沒有點數計費表,沒有按任務計費,也沒有意外超額。"),
  ("為什麼 Manus 對重度使用者來說這麼貴？", "Manus 跑在點數上,公開檔位把月度點數上限定在 4,000、8,000 或 40,000。一項複雜的代理人式任務可能消耗 500–1,000 點數以上——而迴圈跑飛一次就消耗 88,000 點數的回報也存在——重度使用者只能買加購點數包才能繼續工作,於是每月帳單經常落到 1,000–5,000 美元以上。"),
  ("我的工作在 NoArk 裡是私密的嗎？", "是的。沒有登入、也不收集資料：你的對話和代理人執行都留在你自己的裝置和你自己的 iCloud 中,絕不堆放在我們的伺服器上,也絕不用於訓練模型。Apple 的隱私標籤寫著「不收集資料」。"),
  ("NoArk 用哪些 AI 模型？", "NoArk 將每個請求路由到眾多前沿模型中最合適的一個——Anthropic 的 Claude（Fable）、DeepSeek、Mistral、Kimi 和 Google 的 Gemini——而不是依賴單一一個。"),
  ("NoArk 免費嗎？", "NoArk 在 iPhone、iPad、Mac 和 Apple Vision 上免費下載,含可選的應用程式內購買。開始使用無需帳號,也不收集資料。Diamond 不限量檔為 99.99 美元/月;Gold 早鳥價 49.99 美元/月起。"),
 ],
}

render(SLUG, COMP, content)
