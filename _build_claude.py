# -*- coding: utf-8 -*-
from _compare_lib import render

SLUG = "noark-vs-claude.html"
COMP = "Claude Code &amp; Cowork"

def rel(p):
    base = "/" + (p + "/" if p else "")
    return (base,
            base + "noark-vs-chatgpt.html",
            base + "noark-vs-character-ai.html",
            base + "noark-vs-gemini.html",
            base + "noark-vs-perplexity.html",
            base + "noark-vs-manus.html",
            base + "noark-vs-apple-intelligence.html",
            base + "#faq",
            base + "#data-privacy")

content = {}

# ---------------- English ----------------
hp, gp, cp, mp, pp, mnp, ap, fp, dp = rel("")
content[""] = {
 "title": "NoArk vs Claude Code & Cowork: Decide What's Worth Doing, Not Just How to Do It",
 "desc": "NoArk vs Claude Code and Claude Cowork compared: NoArk is a different layer of the AI stack. Claude Code and Cowork focus on how to execute the tasks you've already chosen; NoArk helps you reason about which tasks deserve your attention in the first place — with live news interpretation, counsel from history's wisest minds, and 40+ priority-finding workflows. Free on iPhone, iPad, Mac & Apple Vision; uses Claude Fable internally.",
 "keywords": "NoArk vs Claude, NoArk vs Claude Code, NoArk vs Claude Cowork, decide what to do AI, AI for priorities, AI for reasoning, Claude alternative, Claude complement, Anthropic Claude, Claude Fable, AI coach iPhone, on-device AI, private AI",
 "ogdesc": "How NoArk differs from Claude Code & Cowork: they execute tasks you've defined; NoArk helps you reason about which tasks are worth doing first, using live news, counsel from history's wisest minds, and 40+ priority-finding workflows — built on Claude Fable and other frontier models.",
 "twdesc": "Claude Code & Cowork: how to do tasks. NoArk: what's worth doing in the first place — live news interpretation, counsel from the wisest minds, 40+ workflows. Built on Claude Fable and friends.",
 "h1": "NoArk vs Claude Code &amp; Claude Cowork",
 "subtitle": "Two different jobs, one stack. Claude Code and Claude Cowork are built to execute the tasks you give them. NoArk is built to help you decide which tasks deserve your attention in the first place.",
 "intro": "Anthropic's <strong>Claude Code</strong> and <strong>Claude Cowork</strong> are excellent at one thing: <em>once you know what you want done</em>, they do it — write the function, refactor the module, draft the report, run the workflow. <strong>NoArk — Infinity Memory</strong> sits one layer up: it's built for the question that comes <em>before</em> execution — <strong>what's actually worth doing right now, and why?</strong> Live global headlines with one-tap analysis tell you what's changing in the world, the <strong>Fiat Lux</strong> tab brings real questions to AI versions of history's wisest minds (Munger, Jobs, Marcus Aurelius, and 40+ more), and 40+ Apple-native workflows help you set priorities across markets, life, and work. NoArk routes internally to Claude's <strong>Fable</strong> model alongside DeepSeek, Mistral, Kimi, and Gemini — so it doesn't replace Claude, it stands on top of it.",
 "glance": "At a glance",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("Layer of the stack", "<span class='yes'>Decide</span> — what's worth doing, what matters most, why now", "Execute — once a task is defined, get it done well"),
  ("Core question answered", "<span class='yes'>“What should I do, and why?”</span> — orienting, prioritizing, sense-making", "“How do I do this task?” — coding, drafting, building, running tools"),
  ("Live world signal", "<span class='yes'>Live global headlines</span> with one-tap analysis that interprets what news <em>means</em> for you and the markets", "Not the focus — the user brings the situation in"),
  ("Counsel from wisest minds", "<span class='yes'>Yes</span> — Fiat Lux: AI versions of Charlie Munger, Steve Jobs, Einstein, Marcus Aurelius &amp; 40+ more, grounded in how they actually reasoned", "A general-purpose assistant; no curated council of mentors"),
  ("Priority-finding workflows", "<span class='yes'>40+ ready-made workflows</span> across markets, productivity, travel, education, life admin", "Task execution and tool use — workflows are user-defined"),
  ("Underlying models", "<span class='yes'>Many frontier models, including Claude</span> — Anthropic's Claude (Fable), DeepSeek, Mistral, Kimi, Gemini", "Anthropic's Claude family"),
  ("Sign-in required", "<span class='yes'>No</span> — no account, email, or phone number", "Anthropic account required"),
  ("Your conversations", "<span class='yes'>Stored only on your device</span> and your own iCloud — never warehoused or used to train", "Sent to Anthropic's servers"),
  ("Data collection", "<span class='yes'>None</span> — Apple's App Privacy label: “Data Not Collected”", "Account, usage, and conversation data"),
  ("Price", "<span class='yes'>Free</span> to download (optional in-app purchases)", "Pro plans for Claude Code &amp; Cowork (paid)"),
 ],
 "note": "Comparison reflects publicly available information as of June 2026. Claude, Claude Code, and Claude Cowork are products of Anthropic; NoArk is an independent app and is not affiliated with or endorsed by Anthropic. NoArk uses Anthropic's Claude (Fable) as one of several frontier models it routes to.",
 "sections": [
  ("Decide what to do — before you do it", [
   "The dominant story of agent products in 2026 is <strong>execution</strong>: Claude Code writes and refactors your code; Claude Cowork drives multi-step workflows in your browser. They're remarkably good at it. But execution presupposes that you already know what's worth executing — and for most people, most of the time, <em>that's the actual hard part</em>. Markets move, events break, your portfolio shifts, your week fills up with possibilities, and the question isn't “how do I do this task?” but <strong>“of all the things I could do right now, which one matters most, and why?”</strong>",
   "NoArk is built for that question. The home surface is a stream of <strong>live global headlines</strong>, and a single tap gives you analysis that interprets what a story <em>means</em> for you and the markets. The <strong>Fiat Lux</strong> tab lets you bring the same situation to an AI Charlie Munger for the inversion test, an AI Steve Jobs for the focus test, an AI Marcus Aurelius for the equanimity test — each grounded in how that person actually reasoned. And 40+ ready-made workflows help you turn raw signal into a short-list of things actually worth doing. By the time you hand a task off to Claude Code or Claude Cowork to execute, you've already chosen the right task.",
  ]),
  ("Built on Claude — not against it", [
   "NoArk is not a Claude alternative; it's a layer above. Internally, NoArk routes each request to the best of many frontier models — <strong>Anthropic's Claude (Fable)</strong>, DeepSeek, Mistral, Kimi, and Google's Gemini — instead of relying on one. So when you tap “analyze this headline” or ask Munger what he'd avoid this week, you're often getting a Claude-quality answer underneath, with NoArk doing the surrounding work of context, persona, memory, and Apple-native presentation. The two products complement each other: use NoArk to decide what's worth your attention, then let Claude Code or Claude Cowork carry it out.",
  ]),
  ("Private by default — no account, nothing collected", [
   "Claude Code and Claude Cowork require an Anthropic account, and your prompts and code are sent to Anthropic's servers. NoArk takes the opposite path on the privacy of your <em>thinking</em>: there's <strong>no sign-in</strong> — no email, no phone number — and your conversations, headline analyses, and Fiat Lux dialogues are <strong>stored only on your device and in your own iCloud</strong>, never warehoused on our servers and never used to train any model. Apple's official App Privacy label for NoArk reads <a href='" + dp + "'>“Data Not Collected”</a>, the strictest there is. The reasoning you do about your life stays yours.",
  ]),
  ("More than a model — a full Apple super app", [
   "Beyond the headlines and Fiat Lux, NoArk is a <strong>full Apple super app</strong> for iPhone, iPad, Mac, and Apple Vision: 40+ ready-made workflows across markets, productivity, travel, education, and life admin, with an investing brain built by the team behind TradingTransformer, inspired by Claude Shannon's vision of AI stock-picking. Claude Code &amp; Cowork are powerful in a developer's terminal and a knowledge worker's browser; NoArk is what you reach for in the moments <em>between</em> — when you're trying to figure out what to do next.",
  ]),
 ],
 "related_heading": "Keep reading",
 "related": [
  (hp, "NoArk — Infinity Memory: the intelligent AI OS & super app"),
  (gp, "NoArk vs ChatGPT"),
  (mp, "NoArk vs Google Gemini"),
  (pp, "NoArk vs Perplexity"),
  (mnp, "NoArk vs Manus"),
  (cp, "NoArk vs Character.AI"),
  (ap, "NoArk vs Apple Intelligence"),
  (fp, "Frequently asked questions about NoArk"),
 ],
 "faq": [
  ("Is NoArk a Claude alternative?", "Not exactly — NoArk is a different layer of the AI stack. Claude Code and Claude Cowork focus on how to execute tasks you've defined: writing code, running workflows, completing well-scoped jobs. NoArk focuses on the step before execution — helping you reason about which tasks are worth your attention in the first place — using live world news, counsel from AI versions of history's wisest minds (Munger, Jobs, Marcus Aurelius, and 40+ more), and 40+ priority-finding workflows. Internally, NoArk routes to many frontier models including Anthropic's Claude (Fable), so it stands on Claude rather than against it."),
  ("How is NoArk different from Claude Code?", "Claude Code is built to do programming tasks — write functions, refactor modules, run tests — once you've decided what to build. NoArk is built to help you decide what's worth building (or working on at all) in the first place: it surfaces what's changing in the world via live headlines with one-tap analysis, lets you bring real questions to AI Charlie Munger or Steve Jobs in the Fiat Lux tab, and provides 40+ workflows for setting priorities across markets and life. Use NoArk to choose the right task, then hand the execution to Claude Code."),
  ("How is NoArk different from Claude Cowork?", "Claude Cowork drives multi-step workflows — research, writing, browser automation — once a goal is given. NoArk helps you arrive at the right goal in the first place. Its home is a stream of live global headlines with one-tap interpretation; its Fiat Lux tab brings AI versions of history's wisest minds to bear on real questions; and its 40+ workflows help turn raw world signal into a short-list of things actually worth doing. Then Cowork can carry one out."),
  ("Does NoArk use Claude?", "Yes. NoArk routes each request to the best of many frontier models, and Anthropic's Claude (Fable) is one of them — alongside DeepSeek, Mistral, Kimi, and Google's Gemini. So when you tap one-touch analysis on a headline or ask a Fiat Lux mentor a question, the underlying answer is often Claude-powered."),
  ("Why focus on “what to do” instead of “how to do it”?", "Because for most people, most days, the bottleneck isn't execution — it's choosing what deserves attention. Markets move, headlines break, calendars fill up, and the cost of working hard on the wrong task is far greater than the cost of working slightly slower on the right one. NoArk's design assumes that helping you reason and prioritize before you act is more valuable than shaving minutes off the act itself."),
  ("Is my work private with NoArk?", "Yes. There's no sign-in and no data collection: your conversations, headline analyses, and Fiat Lux dialogues stay on your own device and in your own iCloud, never warehoused on our servers and never used to train models. Apple's App Privacy label reads “Data Not Collected.” That's stricter than Claude Code or Claude Cowork, which require an Anthropic account and send your prompts and code to Anthropic's servers."),
  ("Is NoArk free?", "NoArk is free to download on iPhone, iPad, Mac, and Apple Vision, with optional in-app purchases. There's no account and no data collection required to start."),
 ],
}

# ---------------- Spanish ----------------
hp, gp, cp, mp, pp, mnp, ap, fp, dp = rel("es")
content["es"] = {
 "title": "NoArk vs Claude Code y Cowork: decide qué vale la pena hacer, no solo cómo hacerlo",
 "desc": "Comparativa NoArk vs Claude Code y Claude Cowork: NoArk vive en otra capa de la pila de IA. Claude Code y Cowork se centran en cómo ejecutar las tareas que ya elegiste; NoArk te ayuda a razonar qué tareas merecen tu atención en primer lugar — con interpretación de noticias en directo, consejo de las mentes más sabias de la historia y más de 40 flujos para encontrar prioridades. Gratis en iPhone, iPad, Mac y Apple Vision; usa Claude Fable internamente.",
 "keywords": "NoArk vs Claude, NoArk vs Claude Code, NoArk vs Claude Cowork, IA para decidir qué hacer, IA para prioridades, IA para razonar, alternativa a Claude, complemento de Claude, Anthropic Claude, Claude Fable, coach de IA iPhone, IA en el dispositivo, IA privada",
 "ogdesc": "En qué se diferencia NoArk de Claude Code y Cowork: ellos ejecutan tareas que ya definiste; NoArk te ayuda a razonar qué tareas vale la pena hacer primero, con noticias en directo, consejo de las mentes más sabias y más de 40 flujos de prioridades — apoyado en Claude Fable y otros modelos de frontera.",
 "twdesc": "Claude Code y Cowork: cómo hacer tareas. NoArk: qué vale la pena hacer en primer lugar — interpretación de noticias en directo, consejo de las mentes más sabias, más de 40 flujos. Apoyado en Claude Fable y compañía.",
 "h1": "NoArk vs Claude Code y Claude Cowork",
 "subtitle": "Dos trabajos distintos, una misma pila. Claude Code y Claude Cowork están hechos para ejecutar las tareas que les das. NoArk está hecho para ayudarte a decidir qué tareas merecen tu atención en primer lugar.",
 "intro": "El <strong>Claude Code</strong> y <strong>Claude Cowork</strong> de Anthropic son excelentes en una cosa: <em>una vez que sabes qué quieres hecho</em>, lo hacen — escriben la función, refactorizan el módulo, redactan el informe, ejecutan el flujo. <strong>NoArk — Infinity Memory</strong> está una capa por encima: está hecho para la pregunta que viene <em>antes</em> de la ejecución — <strong>¿qué vale la pena hacer ahora mismo, y por qué?</strong> Los titulares globales en directo con análisis de un toque te dicen qué cambia en el mundo, la pestaña <strong>Fiat Lux</strong> lleva preguntas reales a versiones de IA de las mentes más sabias de la historia (Munger, Jobs, Marco Aurelio y más de 40), y más de 40 flujos nativos de Apple te ayudan a fijar prioridades entre mercados, vida y trabajo. NoArk dirige internamente al modelo <strong>Fable</strong> de Claude junto a DeepSeek, Mistral, Kimi y Gemini — así que no reemplaza a Claude, se apoya sobre él.",
 "glance": "De un vistazo",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("Capa de la pila", "<span class='yes'>Decidir</span> — qué vale la pena hacer, qué importa más, por qué ahora", "Ejecutar — una vez que la tarea está definida, hacerla bien"),
  ("Pregunta central", "<span class='yes'>«¿Qué debería hacer, y por qué?»</span> — orientar, priorizar, dar sentido", "«¿Cómo hago esta tarea?» — programar, redactar, construir, usar herramientas"),
  ("Señal del mundo en directo", "<span class='yes'>Titulares globales en directo</span> con análisis de un toque que interpreta lo que la noticia <em>significa</em> para ti y para los mercados", "No es el foco — el usuario aporta la situación"),
  ("Consejo de las mentes más sabias", "<span class='yes'>Sí</span> — Fiat Lux: versiones de IA de Charlie Munger, Steve Jobs, Einstein, Marco Aurelio y más de 40, basadas en cómo razonaban de verdad", "Un asistente generalista; sin consejo curado de mentores"),
  ("Flujos para priorizar", "<span class='yes'>Más de 40 flujos listos</span> en mercados, productividad, viajes, educación y gestión diaria", "Ejecución de tareas y uso de herramientas — los flujos los define el usuario"),
  ("Modelos subyacentes", "<span class='yes'>Muchos modelos de frontera, incluido Claude</span> — Claude (Fable) de Anthropic, DeepSeek, Mistral, Kimi, Gemini", "La familia Claude de Anthropic"),
  ("Registro obligatorio", "<span class='yes'>No</span> — sin cuenta, correo ni número de teléfono", "Cuenta de Anthropic obligatoria"),
  ("Tus conversaciones", "<span class='yes'>Guardadas solo en tu dispositivo</span> y en tu propio iCloud — nunca almacenadas ni usadas para entrenar", "Enviadas a los servidores de Anthropic"),
  ("Recopilación de datos", "<span class='yes'>Ninguna</span> — etiqueta de privacidad de Apple: «No se recopilan datos»", "Datos de cuenta, uso y conversación"),
  ("Precio", "<span class='yes'>Gratis</span> (compras opcionales dentro de la app)", "Planes Pro para Claude Code y Cowork (de pago)"),
 ],
 "note": "Comparativa basada en información pública a junio de 2026. Claude, Claude Code y Claude Cowork son productos de Anthropic; NoArk es una app independiente, no afiliada ni respaldada por Anthropic. NoArk utiliza Claude (Fable) de Anthropic como uno de varios modelos de frontera a los que dirige peticiones.",
 "sections": [
  ("Decide qué hacer — antes de hacerlo", [
   "La historia dominante de los productos agénticos en 2026 es la <strong>ejecución</strong>: Claude Code escribe y refactoriza tu código; Claude Cowork lleva flujos de varios pasos en tu navegador. Lo hacen notablemente bien. Pero ejecutar presupone que ya sabes qué vale la pena ejecutar — y para la mayoría de la gente, la mayor parte del tiempo, <em>esa es la parte difícil</em>. Los mercados se mueven, las noticias rompen, tu cartera cambia, tu semana se llena de posibilidades, y la pregunta no es «¿cómo hago esta tarea?» sino <strong>«de todas las cosas que podría hacer ahora, ¿cuál importa más, y por qué?»</strong>",
   "NoArk está hecho para esa pregunta. La pantalla principal es un flujo de <strong>titulares globales en directo</strong>, y un solo toque te da análisis que interpreta lo que una noticia <em>significa</em> para ti y para los mercados. La pestaña <strong>Fiat Lux</strong> te deja llevar la misma situación a una IA de Charlie Munger para la prueba de la inversión, a una IA de Steve Jobs para la prueba del foco, a una IA de Marco Aurelio para la prueba de la ecuanimidad — cada una basada en cómo razonaba esa persona. Y más de 40 flujos listos te ayudan a convertir la señal en una lista corta de cosas que de verdad merecen hacerse. Cuando le pasas una tarea a Claude Code o Claude Cowork para que la ejecute, ya elegiste la tarea correcta.",
  ]),
  ("Apoyado en Claude — no contra Claude", [
   "NoArk no es una alternativa a Claude; es una capa por encima. Internamente, NoArk dirige cada petición al mejor de muchos modelos de frontera — <strong>Claude (Fable) de Anthropic</strong>, DeepSeek, Mistral, Kimi y Gemini de Google — en lugar de depender de uno solo. Así que cuando tocas «analizar este titular» o le preguntas a Munger qué evitaría esta semana, a menudo recibes una respuesta de calidad Claude por debajo, con NoArk haciendo el trabajo de contexto, personaje, memoria y presentación nativa de Apple alrededor. Los dos productos se complementan: usa NoArk para decidir qué merece tu atención, y deja que Claude Code o Claude Cowork lo lleven a cabo.",
  ]),
  ("Privado por defecto — sin cuenta, sin recopilar nada", [
   "Claude Code y Claude Cowork requieren una cuenta de Anthropic, y tus prompts y tu código se envían a sus servidores. NoArk hace lo contrario con la privacidad de tu <em>pensamiento</em>: <strong>no hay registro</strong> — ni correo ni número de teléfono — y tus conversaciones, análisis de titulares y diálogos en Fiat Lux se <strong>guardan solo en tu dispositivo y en tu propio iCloud</strong>, nunca almacenados en nuestros servidores ni usados para entrenar ningún modelo. La etiqueta oficial de privacidad de Apple para NoArk dice <a href='" + dp + "'>«No se recopilan datos»</a>, la más estricta que existe. El razonamiento que haces sobre tu vida sigue siendo tuyo.",
  ]),
  ("Más que un modelo — una súper app de Apple completa", [
   "Más allá de los titulares y Fiat Lux, NoArk es una <strong>súper app de Apple completa</strong> para iPhone, iPad, Mac y Apple Vision: más de 40 flujos listos en mercados, productividad, viajes, educación y gestión diaria, con un cerebro inversor creado por el equipo de TradingTransformer, inspirado en la visión de Claude Shannon sobre la IA que elige acciones. Claude Code y Cowork son potentes en la terminal del programador y en el navegador del trabajador del conocimiento; NoArk es lo que sacas en los momentos <em>intermedios</em> — cuando intentas decidir qué hacer a continuación.",
  ]),
 ],
 "related_heading": "Sigue leyendo",
 "related": [
  (hp, "NoArk — Infinity Memory: el SO inteligente y súper app de IA"),
  (gp, "NoArk vs ChatGPT"),
  (mp, "NoArk vs Google Gemini"),
  (pp, "NoArk vs Perplexity"),
  (mnp, "NoArk vs Manus"),
  (cp, "NoArk vs Character.AI"),
  (ap, "NoArk vs Apple Intelligence"),
  (fp, "Preguntas frecuentes sobre NoArk"),
 ],
 "faq": [
  ("¿Es NoArk una alternativa a Claude?", "No exactamente — NoArk vive en otra capa de la pila de IA. Claude Code y Claude Cowork se centran en cómo ejecutar las tareas que ya definiste: escribir código, llevar flujos, completar trabajos bien acotados. NoArk se centra en el paso anterior — ayudarte a razonar qué tareas merecen tu atención en primer lugar — con noticias del mundo en directo, consejo de versiones de IA de las mentes más sabias de la historia (Munger, Jobs, Marco Aurelio y más de 40) y más de 40 flujos para encontrar prioridades. Internamente, NoArk dirige peticiones a muchos modelos de frontera, incluido Claude (Fable) de Anthropic, así que se apoya en Claude en vez de oponérsele."),
  ("¿En qué se diferencia NoArk de Claude Code?", "Claude Code está hecho para tareas de programación — escribir funciones, refactorizar módulos, ejecutar pruebas — una vez que decidiste qué construir. NoArk está hecho para ayudarte a decidir qué vale la pena construir (o trabajar) en primer lugar: muestra qué cambia en el mundo con titulares en directo y análisis de un toque, te deja llevar preguntas reales a una IA de Charlie Munger o Steve Jobs en la pestaña Fiat Lux y ofrece más de 40 flujos para fijar prioridades entre mercados y vida. Usa NoArk para elegir la tarea correcta, y luego pasa la ejecución a Claude Code."),
  ("¿En qué se diferencia NoArk de Claude Cowork?", "Claude Cowork lleva flujos de varios pasos — investigación, redacción, automatización del navegador — una vez que se le da un objetivo. NoArk te ayuda a llegar al objetivo correcto en primer lugar. Su pantalla principal es un flujo de titulares globales en directo con interpretación de un toque; su pestaña Fiat Lux trae versiones de IA de las mentes más sabias para preguntas reales; y sus más de 40 flujos ayudan a convertir la señal del mundo en una lista corta de cosas que de verdad merecen hacerse. Después, Cowork puede llevar una a cabo."),
  ("¿NoArk usa Claude?", "Sí. NoArk dirige cada petición al mejor de muchos modelos de frontera, y Claude (Fable) de Anthropic es uno de ellos — junto a DeepSeek, Mistral, Kimi y Gemini de Google. Así que cuando tocas el análisis de un toque sobre un titular o le haces una pregunta a un mentor de Fiat Lux, la respuesta de fondo a menudo viene de Claude."),
  ("¿Por qué centrarse en «qué hacer» en vez de «cómo hacerlo»?", "Porque para la mayoría de la gente, la mayoría de los días, el cuello de botella no es la ejecución — es elegir qué merece atención. Los mercados se mueven, las noticias rompen, las agendas se llenan, y el coste de trabajar duro en la tarea equivocada es mucho mayor que el de trabajar un poco más lento en la correcta. El diseño de NoArk asume que ayudarte a razonar y priorizar antes de actuar es más valioso que ahorrar minutos al acto en sí."),
  ("¿Mi trabajo es privado con NoArk?", "Sí. No hay registro ni recopilación de datos: tus conversaciones, análisis de titulares y diálogos en Fiat Lux se quedan en tu propio dispositivo y en tu propio iCloud, nunca almacenados en nuestros servidores ni usados para entrenar modelos. La etiqueta de privacidad de Apple dice «No se recopilan datos». Es más estricto que Claude Code o Claude Cowork, que requieren una cuenta de Anthropic y envían tus prompts y código a sus servidores."),
  ("¿Es NoArk gratis?", "NoArk es gratis en iPhone, iPad, Mac y Apple Vision, con compras opcionales dentro de la app. No hace falta cuenta ni recopilación de datos para empezar."),
 ],
}

# ---------------- French ----------------
hp, gp, cp, mp, pp, mnp, ap, fp, dp = rel("fr")
content["fr"] = {
 "title": "NoArk vs Claude Code & Cowork : décider quoi faire, pas seulement comment le faire",
 "desc": "Comparatif NoArk vs Claude Code et Claude Cowork : NoArk vit à un autre étage de la pile d'IA. Claude Code et Cowork se concentrent sur la façon d'exécuter les tâches que vous avez choisies ; NoArk vous aide à raisonner sur les tâches qui méritent votre attention en premier lieu — avec interprétation de l'actualité en direct, conseil des plus grands esprits de l'histoire et plus de 40 flux pour trouver vos priorités. Gratuit sur iPhone, iPad, Mac et Apple Vision ; utilise Claude Fable en interne.",
 "keywords": "NoArk vs Claude, NoArk vs Claude Code, NoArk vs Claude Cowork, IA pour décider quoi faire, IA pour les priorités, IA pour raisonner, alternative à Claude, complément de Claude, Anthropic Claude, Claude Fable, coach IA iPhone, IA sur l'appareil, IA privée",
 "ogdesc": "En quoi NoArk diffère de Claude Code et Cowork : ils exécutent les tâches que vous avez définies ; NoArk vous aide à raisonner sur celles qui méritent d'être faites en premier, avec actualité en direct, conseil des plus grands esprits et plus de 40 flux de priorités — bâti sur Claude Fable et d'autres modèles de pointe.",
 "twdesc": "Claude Code & Cowork : comment faire les tâches. NoArk : ce qui mérite d'être fait en premier — interprétation de l'actualité en direct, conseil des plus grands esprits, plus de 40 flux. Bâti sur Claude Fable et compagnie.",
 "h1": "NoArk vs Claude Code et Claude Cowork",
 "subtitle": "Deux jobs différents, une seule pile. Claude Code et Claude Cowork sont faits pour exécuter les tâches que vous leur donnez. NoArk est fait pour vous aider à décider quelles tâches méritent votre attention en premier lieu.",
 "intro": "<strong>Claude Code</strong> et <strong>Claude Cowork</strong> d'Anthropic excellent dans une chose : <em>une fois que vous savez ce que vous voulez fait</em>, ils le font — écrivent la fonction, refactorisent le module, rédigent le rapport, lancent le flux. <strong>NoArk — Infinity Memory</strong> se situe un étage au-dessus : il est fait pour la question qui vient <em>avant</em> l'exécution — <strong>qu'est-ce qui vaut vraiment la peine d'être fait, et pourquoi maintenant ?</strong> L'actualité mondiale en direct avec analyse en un geste vous dit ce qui change dans le monde, l'onglet <strong>Fiat Lux</strong> apporte de vraies questions à des versions IA des plus grands esprits de l'histoire (Munger, Jobs, Marc Aurèle et plus de 40 autres), et plus de 40 flux Apple-natifs vous aident à fixer vos priorités entre marchés, vie et travail. NoArk route en interne vers le modèle <strong>Fable</strong> de Claude, aux côtés de DeepSeek, Mistral, Kimi et Gemini — il ne remplace donc pas Claude, il s'appuie dessus.",
 "glance": "En un coup d'œil",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("Étage de la pile", "<span class='yes'>Décider</span> — ce qui mérite d'être fait, ce qui compte le plus, pourquoi maintenant", "Exécuter — une fois la tâche définie, la mener à bien"),
  ("Question centrale", "<span class='yes'>« Que devrais-je faire, et pourquoi ? »</span> — s'orienter, prioriser, donner du sens", "« Comment fais-je cette tâche ? » — coder, rédiger, construire, utiliser des outils"),
  ("Signal du monde en direct", "<span class='yes'>Actualité mondiale en direct</span> avec analyse en un geste qui interprète ce que l'actualité <em>signifie</em> pour vous et les marchés", "Pas le focus — l'utilisateur apporte la situation"),
  ("Conseil des plus grands esprits", "<span class='yes'>Oui</span> — Fiat Lux : versions IA de Charlie Munger, Steve Jobs, Einstein, Marc Aurèle et plus de 40 autres, ancrées dans leur vraie façon de raisonner", "Un assistant généraliste ; pas de conseil de mentors curé"),
  ("Flux pour prioriser", "<span class='yes'>Plus de 40 flux prêts à l'emploi</span> couvrant marchés, productivité, voyage, éducation et gestion du quotidien", "Exécution de tâches et usage d'outils — les flux sont définis par l'utilisateur"),
  ("Modèles sous-jacents", "<span class='yes'>De nombreux modèles de pointe, dont Claude</span> — Claude (Fable) d'Anthropic, DeepSeek, Mistral, Kimi, Gemini", "La famille Claude d'Anthropic"),
  ("Inscription requise", "<span class='yes'>Non</span> — pas de compte, d'e-mail ni de numéro de téléphone", "Compte Anthropic requis"),
  ("Vos conversations", "<span class='yes'>Stockées uniquement sur votre appareil</span> et dans votre propre iCloud — jamais entreposées ni utilisées pour entraîner", "Envoyées aux serveurs d'Anthropic"),
  ("Collecte de données", "<span class='yes'>Aucune</span> — étiquette de confidentialité d'Apple : « Données non collectées »", "Données de compte, d'usage et de conversation"),
  ("Prix", "<span class='yes'>Gratuit</span> (achats intégrés optionnels)", "Plans Pro pour Claude Code et Cowork (payants)"),
 ],
 "note": "Comparaison fondée sur des informations publiques en juin 2026. Claude, Claude Code et Claude Cowork sont des produits d'Anthropic ; NoArk est une app indépendante, ni affiliée ni approuvée par Anthropic. NoArk utilise Claude (Fable) d'Anthropic comme l'un des nombreux modèles de pointe vers lesquels il route ses requêtes.",
 "sections": [
  ("Décider quoi faire — avant de le faire", [
   "L'histoire dominante des produits agentiques en 2026, c'est l'<strong>exécution</strong> : Claude Code écrit et refactorise votre code ; Claude Cowork mène des flux multi-étapes dans votre navigateur. Ils le font remarquablement bien. Mais exécuter présuppose que vous savez déjà ce qui vaut la peine d'être exécuté — et pour la plupart des gens, la plupart du temps, <em>c'est ça la vraie partie difficile</em>. Les marchés bougent, l'actualité éclate, votre portefeuille évolue, votre semaine se remplit de possibilités, et la question n'est pas « comment je fais cette tâche ? » mais <strong>« parmi tout ce que je pourrais faire maintenant, qu'est-ce qui compte le plus, et pourquoi ? »</strong>",
   "NoArk est fait pour cette question. L'écran principal est un flux d'<strong>actualité mondiale en direct</strong>, et un seul geste vous donne une analyse qui interprète ce qu'une nouvelle <em>signifie</em> pour vous et les marchés. L'onglet <strong>Fiat Lux</strong> vous laisse apporter la même situation à un IA Charlie Munger pour le test d'inversion, à un IA Steve Jobs pour le test du focus, à un IA Marc Aurèle pour le test de l'équanimité — chacun ancré dans la vraie façon de raisonner de la personne. Et plus de 40 flux prêts à l'emploi vous aident à transformer le signal en une liste courte de choses qui valent vraiment la peine. Au moment où vous confiez une tâche à Claude Code ou Claude Cowork pour qu'ils l'exécutent, vous avez déjà choisi la bonne tâche.",
  ]),
  ("Bâti sur Claude — pas contre Claude", [
   "NoArk n'est pas une alternative à Claude ; c'est une couche au-dessus. En interne, NoArk route chaque requête vers le meilleur de nombreux modèles de pointe — <strong>Claude (Fable) d'Anthropic</strong>, DeepSeek, Mistral, Kimi et Gemini de Google — au lieu de dépendre d'un seul. Ainsi, quand vous touchez « analyser ce titre » ou demandez à Munger ce qu'il éviterait cette semaine, vous obtenez souvent une réponse de qualité Claude en arrière-plan, NoArk faisant le travail autour : contexte, persona, mémoire et présentation Apple-native. Les deux produits se complètent : utilisez NoArk pour décider de ce qui mérite votre attention, puis laissez Claude Code ou Claude Cowork s'en charger.",
  ]),
  ("Privé par défaut — sans compte, rien de collecté", [
   "Claude Code et Claude Cowork exigent un compte Anthropic, et vos prompts et votre code sont envoyés à leurs serveurs. NoArk fait l'inverse pour la confidentialité de votre <em>réflexion</em> : il n'y a <strong>aucune inscription</strong> — pas d'e-mail, pas de numéro de téléphone — et vos conversations, analyses de titres et dialogues Fiat Lux sont <strong>stockés uniquement sur votre appareil et dans votre propre iCloud</strong>, jamais entreposés sur nos serveurs ni utilisés pour entraîner un modèle. L'étiquette officielle de confidentialité d'Apple pour NoArk indique <a href='" + dp + "'>« Données non collectées »</a>, la plus stricte qui soit. Le raisonnement que vous menez sur votre vie reste à vous.",
  ]),
  ("Plus qu'un modèle — une super app Apple complète", [
   "Au-delà des titres et de Fiat Lux, NoArk est une <strong>super app Apple complète</strong> pour iPhone, iPad, Mac et Apple Vision : plus de 40 flux prêts à l'emploi couvrant marchés, productivité, voyage, éducation et gestion du quotidien, avec un cerveau d'investisseur créé par l'équipe de TradingTransformer, inspiré par la vision de Claude Shannon d'une IA qui choisit les actions. Claude Code et Cowork sont puissants dans le terminal d'un développeur et le navigateur d'un travailleur du savoir ; NoArk, c'est ce que vous attrapez dans les moments <em>entre les deux</em> — quand vous essayez de décider quoi faire ensuite.",
  ]),
 ],
 "related_heading": "À lire ensuite",
 "related": [
  (hp, "NoArk — Infinity Memory : l'OS intelligent et la super app IA"),
  (gp, "NoArk vs ChatGPT"),
  (mp, "NoArk vs Google Gemini"),
  (pp, "NoArk vs Perplexity"),
  (mnp, "NoArk vs Manus"),
  (cp, "NoArk vs Character.AI"),
  (ap, "NoArk vs Apple Intelligence"),
  (fp, "Questions fréquentes sur NoArk"),
 ],
 "faq": [
  ("NoArk est-elle une alternative à Claude ?", "Pas exactement — NoArk vit à un autre étage de la pile d'IA. Claude Code et Claude Cowork se concentrent sur la façon d'exécuter les tâches que vous avez définies : écrire du code, mener des flux, terminer des travaux bien cadrés. NoArk se concentre sur l'étape précédente — vous aider à raisonner sur les tâches qui méritent votre attention en premier lieu — avec l'actualité mondiale en direct, le conseil de versions IA des plus grands esprits de l'histoire (Munger, Jobs, Marc Aurèle et plus de 40 autres) et plus de 40 flux pour trouver vos priorités. En interne, NoArk route vers de nombreux modèles de pointe dont Claude (Fable) d'Anthropic, donc il s'appuie sur Claude plutôt que de s'y opposer."),
  ("En quoi NoArk diffère-t-elle de Claude Code ?", "Claude Code est fait pour des tâches de programmation — écrire des fonctions, refactoriser des modules, lancer des tests — une fois que vous avez décidé quoi construire. NoArk est faite pour vous aider à décider quoi vaut la peine d'être construit (ou travaillé) en premier lieu : elle fait remonter ce qui change dans le monde via l'actualité en direct avec analyse en un geste, vous laisse apporter de vraies questions à un IA Charlie Munger ou Steve Jobs dans l'onglet Fiat Lux, et fournit plus de 40 flux pour fixer des priorités entre marchés et vie. Utilisez NoArk pour choisir la bonne tâche, puis confiez l'exécution à Claude Code."),
  ("En quoi NoArk diffère-t-elle de Claude Cowork ?", "Claude Cowork mène des flux multi-étapes — recherche, rédaction, automatisation de navigateur — une fois qu'un objectif est donné. NoArk vous aide à arriver au bon objectif en premier lieu. Son écran principal est un flux d'actualité mondiale en direct avec interprétation en un geste ; son onglet Fiat Lux apporte des versions IA des plus grands esprits sur de vraies questions ; et ses plus de 40 flux aident à transformer le signal du monde en une liste courte de choses qui valent vraiment la peine. Ensuite, Cowork peut en mener une à bien."),
  ("NoArk utilise-t-elle Claude ?", "Oui. NoArk route chaque requête vers le meilleur de nombreux modèles de pointe, et Claude (Fable) d'Anthropic en fait partie — aux côtés de DeepSeek, Mistral, Kimi et Gemini de Google. Donc, quand vous touchez l'analyse en un geste sur un titre ou que vous posez une question à un mentor Fiat Lux, la réponse sous-jacente vient souvent de Claude."),
  ("Pourquoi se concentrer sur « quoi faire » plutôt que « comment le faire » ?", "Parce que pour la plupart des gens, la plupart des jours, le goulot d'étranglement n'est pas l'exécution — c'est de choisir ce qui mérite l'attention. Les marchés bougent, l'actualité éclate, les agendas se remplissent, et le coût de travailler dur sur la mauvaise tâche est bien plus élevé que celui de travailler un peu plus lentement sur la bonne. Le design de NoArk suppose que vous aider à raisonner et à prioriser avant d'agir vaut plus que de gagner quelques minutes sur l'acte lui-même."),
  ("Mon travail est-il privé avec NoArk ?", "Oui. Aucune inscription ni collecte de données : vos conversations, analyses de titres et dialogues Fiat Lux restent sur votre propre appareil et dans votre propre iCloud, jamais entreposés sur nos serveurs ni utilisés pour entraîner des modèles. L'étiquette de confidentialité d'Apple indique « Données non collectées ». C'est plus strict que Claude Code ou Claude Cowork, qui exigent un compte Anthropic et envoient vos prompts et votre code à leurs serveurs."),
  ("NoArk est-elle gratuite ?", "NoArk est gratuite sur iPhone, iPad, Mac et Apple Vision, avec des achats intégrés optionnels. Aucun compte ni aucune collecte de données n'est nécessaire pour commencer."),
 ],
}

# ---------------- Japanese ----------------
hp, gp, cp, mp, pp, mnp, ap, fp, dp = rel("ja")
content["ja"] = {
 "title": "NoArk vs Claude Code & Cowork：何をすべきかを決める。やり方を補うのではなく",
 "desc": "NoArk と Claude Code・Claude Cowork を比較：NoArk は AI スタックの別の層にいます。Claude Code と Cowork は、すでに選んだタスクを「どうやるか」に集中。NoArk はそもそも「どのタスクが注意に値するか」をあなたが考え抜くのを助けます — ライブニュースの解釈、歴史上の賢人の助言、優先順位を見つけるための40以上のワークフローで。iPhone・iPad・Mac・Apple Vision で無料。内部で Claude Fable を活用。",
 "keywords": "NoArk vs Claude, NoArk vs Claude Code, NoArk vs Claude Cowork, 何をすべきかを決める AI, 優先順位 AI, 推論する AI, Claude 代替, Claude 補完, Anthropic Claude, Claude Fable, AI コーチ iPhone, オンデバイス AI, プライベート AI",
 "ogdesc": "NoArk が Claude Code・Cowork と違う点：彼らは定義済みのタスクを実行する。NoArk はそもそも何をやる価値があるかをあなたが考えるのを助ける — ライブニュース、歴史上の賢人の助言、40以上の優先順位ワークフロー — Claude Fable やほかのフロンティアモデルの上に立っています。",
 "twdesc": "Claude Code & Cowork：タスクのやり方。NoArk：そもそも何をやる価値があるか — ライブニュース解釈、賢人の助言、40以上のワークフロー。Claude Fable と仲間たちの上で動きます。",
 "h1": "NoArk vs Claude Code・Claude Cowork",
 "subtitle": "ふたつの異なる仕事、ひとつのスタック。Claude Code と Claude Cowork は、あなたが渡したタスクを実行するために作られています。NoArk は、そもそもどのタスクが注意に値するかをあなたが決めるのを助けるために作られています。",
 "intro": "Anthropic の <strong>Claude Code</strong> と <strong>Claude Cowork</strong> はひとつのことに優れています。<em>何をしたいかが分かっていれば</em>、それをやってくれます — 関数を書き、モジュールをリファクタリングし、レポートを下書きし、ワークフローを走らせる。<strong>NoArk — Infinity Memory</strong> は一段上にいます。実行の<em>前</em>に来る問い — <strong>「いま本当にやる価値があるのは何で、なぜなのか？」</strong> のために作られています。ワンタップ分析つきのライブ世界ニュースが世界の変化を伝え、<strong>Fiat Lux</strong> タブは歴史上の賢人のAI版（マンガー、ジョブズ、マルクス・アウレリウスほか40名以上）に本当の問いを持ち込ませ、40以上の Apple ネイティブのワークフローが市場・暮らし・仕事の優先順位づけを助けます。NoArk は内部で Claude の <strong>Fable</strong> モデルに、DeepSeek・Mistral・Kimi・Gemini と並べてリクエストをルーティングします。だから Claude を置き換えるのではなく、その上に立ちます。",
 "glance": "ひと目でわかる比較",
 "col_noark": "NoArk — Infinity Memory",
 "rows": [
  ("スタックの層", "<span class='yes'>決める</span> — 何をやる価値があるか、何が一番大事か、なぜいまか", "実行する — タスクが定まれば、それをうまく仕上げる"),
  ("中心的な問い", "<span class='yes'>「私は何をすべきか、なぜか？」</span> — 方向づけ、優先順位、意味づけ", "「このタスクをどうやるか？」 — コード、文章、構築、ツール利用"),
  ("ライブな世界の信号", "<span class='yes'>ライブ世界ニュース</span>＋ワンタップ分析。記事があなたと市場にとって何を<em>意味するか</em>を解釈", "焦点ではない — 状況はユーザーが持ち込む"),
  ("賢人からの助言", "<span class='yes'>あり</span> — Fiat Lux：チャーリー・マンガー、スティーブ・ジョブズ、アインシュタイン、マルクス・アウレリウスほか40名以上のAI版。実際の考え方に基づく", "汎用アシスタント。キュレーションされたメンター評議会はなし"),
  ("優先順位づけのワークフロー", "<span class='yes'>40以上の即戦力ワークフロー</span> — 市場・生産性・旅行・教育・生活の雑務", "タスクの実行とツール利用 — ワークフローはユーザー定義"),
  ("基盤モデル", "<span class='yes'>Claude を含む多数のフロンティアモデル</span> — Anthropic の Claude（Fable）、DeepSeek、Mistral、Kimi、Gemini", "Anthropic の Claude ファミリー"),
  ("サインイン", "<span class='yes'>不要</span> — アカウントもメールも電話番号も不要", "Anthropic アカウントが必要"),
  ("あなたの会話", "<span class='yes'>あなたのデバイス</span>とあなた自身の iCloud だけに保存 — 蓄積も学習利用もされません", "Anthropic のサーバーに送信"),
  ("データ収集", "<span class='yes'>なし</span> — Apple のプライバシーラベル：「データは収集されません」", "アカウント・利用状況・会話のデータ"),
  ("価格", "<span class='yes'>無料</span>（オプションのアプリ内課金あり）", "Claude Code と Cowork の Pro プラン（有料）"),
 ],
 "note": "本比較は2026年6月時点の公開情報に基づきます。Claude、Claude Code、Claude Cowork は Anthropic の製品です。NoArk は独立したアプリであり、Anthropic との提携や承認はありません。NoArk はリクエストを多数のフロンティアモデルにルーティングしており、その一つとして Anthropic の Claude（Fable）を活用しています。",
 "sections": [
  ("実行の前に「何をするか」を決める", [
   "2026年のエージェント製品の中心テーマは<strong>実行</strong>です。Claude Code はあなたのコードを書きリファクタリングし、Claude Cowork はブラウザで多段階のワークフローを進める。とても上手にやってくれます。しかし実行は、何を実行する価値があるかをすでに知っていることを前提にします — そしてほとんどの人にとって、ほとんどの時間において、<em>そここそが本当の難所です</em>。市場は動き、ニュースは飛び込み、ポートフォリオは変わり、一週間は可能性で埋まる。問いは「このタスクをどうやるか」ではなく、<strong>「いまできることのなかで、最も重要なのは何で、なぜか？」</strong>です。",
   "NoArk はこの問いのために作られています。ホーム画面は<strong>ライブ世界ニュース</strong>の流れ。ワンタップで、その出来事があなたと市場にとって何を<em>意味するか</em>を解釈する分析が得られます。<strong>Fiat Lux</strong> タブでは、同じ状況を、逆転の問いには AI チャーリー・マンガー、フォーカスの問いには AI スティーブ・ジョブズ、平静の問いには AI マルクス・アウレリウスへと持ち込めます — それぞれが本人の考え方に基づきます。そして40以上の即戦力ワークフローが、生の信号を「本当にやる価値があることの短いリスト」に変えてくれます。Claude Code や Claude Cowork に実行を委ねる頃には、あなたはすでに正しいタスクを選び終えています。",
  ]),
  ("Claude を土台に — Claude に対抗するのではなく", [
   "NoArk は Claude の代替ではなく、その上のレイヤーです。内部では、リクエストごとに多数のフロンティアモデルから最適な一つにルーティングします — <strong>Anthropic の Claude（Fable）</strong>、DeepSeek、Mistral、Kimi、Google の Gemini。だから「この見出しを分析」をタップしたり、「マンガーなら今週何を避けるか？」と尋ねたりすると、Claude 品質の答えが下にあり、その周りで NoArk がコンテキスト、ペルソナ、メモリ、Apple ネイティブの提示を担います。ふたつの製品は補い合います — 何が注意に値するかは NoArk で決め、その実行は Claude Code または Claude Cowork に任せる。",
  ]),
  ("既定でプライベート — アカウントなし、何も収集しない", [
   "Claude Code と Claude Cowork は Anthropic アカウントを必要とし、プロンプトとコードは Anthropic のサーバーに送られます。NoArk はあなたの<em>思考</em>のプライバシーで逆を行きます。<strong>サインインは不要</strong> — メールも電話番号もなく — 会話・見出し分析・Fiat Lux での対話は<strong>あなたのデバイスとあなた自身の iCloud だけに保存</strong>され、私たちのサーバーに蓄積されることも、どのモデルの学習に使われることもありません。Apple 公式の NoArk のプライバシーラベルは <a href='" + dp + "'>「データは収集されません」</a> — 最も厳格なラベルです。あなたが自分の人生について行う推論は、あなたのものです。",
  ]),
  ("モデル以上 — フル機能の Apple スーパーアプリ", [
   "ニュースと Fiat Lux の先で、NoArk は iPhone・iPad・Mac・Apple Vision のための<strong>フル機能の Apple スーパーアプリ</strong>です。市場・生産性・旅行・教育・生活の雑務にわたる40以上の即戦力ワークフロー、TradingTransformer チームが作り、クロード・シャノンの AI 株式選択のビジョンに着想を得た投資する頭脳。Claude Code と Cowork は開発者のターミナルとナレッジワーカーのブラウザで力を発揮します。NoArk は、その<em>あいだ</em> — 次に何をするかを決めようとしているとき — に手にとるアプリです。",
  ]),
 ],
 "related_heading": "あわせて読む",
 "related": [
  (hp, "NoArk — Infinity Memory：インテリジェントAI OS・スーパーアプリ"),
  (gp, "NoArk vs ChatGPT"),
  (mp, "NoArk vs Google Gemini"),
  (pp, "NoArk vs Perplexity"),
  (mnp, "NoArk vs Manus"),
  (cp, "NoArk vs Character.AI"),
  (ap, "NoArk vs Apple Intelligence"),
  (fp, "NoArk についてのよくある質問"),
 ],
 "faq": [
  ("NoArk は Claude の代替ですか？", "厳密には違います — NoArk は AI スタックの別の層にいます。Claude Code と Claude Cowork は、あなたが定義したタスク（コードを書く、ワークフローを進める、よく区切られた仕事を完成させる）を「どう実行するか」に集中します。NoArk はその一段前 — そもそもどのタスクが注意に値するかをあなたが考え抜くのを助けます — ライブな世界のニュース、歴史上の賢人のAI版（マンガー、ジョブズ、マルクス・アウレリウスほか40名以上）の助言、優先順位を見つけるための40以上のワークフローを使って。内部では NoArk は Anthropic の Claude（Fable）を含む多数のフロンティアモデルにルーティングするので、Claude に対抗するのではなくその上に立ちます。"),
  ("NoArk は Claude Code とどう違いますか？", "Claude Code は、何を作るかを決めたあとのプログラミング作業（関数を書く、モジュールをリファクタリングする、テストを走らせる）のためのものです。NoArk は、そもそも何を作る（あるいは取り組む）価値があるかをあなたが決めるのを助けるためのものです：ワンタップ分析つきのライブ見出しで世界の変化を浮かび上がらせ、Fiat Lux タブで AI チャーリー・マンガーやスティーブ・ジョブズに本当の問いを持ち込ませ、市場と暮らしの優先順位づけのための40以上のワークフローを提供します。NoArk で正しいタスクを選び、そして実行は Claude Code に渡しましょう。"),
  ("NoArk は Claude Cowork とどう違いますか？", "Claude Cowork は、目標が与えられたあとに多段階のワークフロー（リサーチ、執筆、ブラウザ自動化）を進めます。NoArk は、そもそも正しい目標にたどり着くのを助けます。ホームはワンタップ解釈つきのライブ世界ニュース、Fiat Lux タブは歴史上の賢人のAI版を本当の問いに当て、40以上のワークフローが世界の生信号を「本当にやる価値があることの短いリスト」に変えてくれます。そのあと Cowork が一つを実行できます。"),
  ("NoArk は Claude を使っていますか？", "はい。NoArk はリクエストごとに多数のフロンティアモデルから最適な一つにルーティングしており、Anthropic の Claude（Fable）はそのうちのひとつです — DeepSeek、Mistral、Kimi、Google の Gemini と並んで。だから見出しのワンタップ分析をタップしたり、Fiat Lux のメンターに質問したりするとき、その下の答えはしばしば Claude が動かしています。"),
  ("なぜ「やり方」ではなく「何をするか」に焦点を当てるのですか？", "ほとんどの人にとって、ほとんどの日において、ボトルネックは実行ではなく、何が注意に値するかを選ぶことだからです。市場は動き、ニュースは飛び込み、予定は埋まり、間違ったタスクで一生懸命に働くコストは、正しいタスクで少し遅く働くコストよりはるかに大きい。NoArk の設計は、行動の前に推論と優先順位づけを助けることが、行動そのものから数分を削ることよりも価値があるという前提に立っています。"),
  ("NoArk で私の作業はプライベートですか？", "はい。サインインもデータ収集もありません。会話・見出し分析・Fiat Lux の対話はあなた自身のデバイスとあなた自身の iCloud に残り、私たちのサーバーに蓄積されることも、モデルの学習に使われることもありません。Apple のプライバシーラベルは「データは収集されません」です。これは Anthropic のアカウントを必要とし、プロンプトとコードを Anthropic のサーバーに送る Claude Code や Claude Cowork よりも厳格です。"),
  ("NoArk は無料ですか？", "NoArk は iPhone・iPad・Mac・Apple Vision で無料で、オプションのアプリ内課金があります。始めるのにアカウントもデータ収集も不要です。"),
 ],
}

# ---------------- Simplified Chinese ----------------
hp, gp, cp, mp, pp, mnp, ap, fp, dp = rel("zh-cn")
content["zh-cn"] = {
 "title": "NoArk 对比 Claude Code 与 Cowork：决定值得做什么,而不仅仅是怎么做",
 "desc": "NoArk 与 Claude Code、Claude Cowork 全面对比：NoArk 处于 AI 技术栈的不同一层。Claude Code 和 Cowork 专注于如何执行你已经选好的任务;NoArk 帮你思考究竟哪些任务最值得你关注 —— 通过实时新闻解读、历史智者的建议,以及 40 多个用于发现优先级的工作流。iPhone、iPad、Mac 和 Apple Vision 免费下载;内部使用 Claude Fable。",
 "keywords": "NoArk 对比 Claude, NoArk 对比 Claude Code, NoArk 对比 Claude Cowork, 决定做什么的 AI, 优先级 AI, 用于推理的 AI, Claude 替代品, Claude 互补品, Anthropic Claude, Claude Fable, AI 教练 iPhone, 端侧 AI, 私密 AI",
 "ogdesc": "NoArk 与 Claude Code、Cowork 的不同:它们执行你定义好的任务;NoArk 帮你先想清楚哪些任务最值得做 —— 凭借实时新闻、历史智者的建议、40 多个优先级工作流 —— 构建在 Claude Fable 与其他前沿模型之上。",
 "twdesc": "Claude Code 与 Cowork:怎么做任务。NoArk:首先值得做什么 —— 实时新闻解读、最有智慧者的建议、40 多个工作流。构建在 Claude Fable 与同伴之上。",
 "h1": "NoArk 对比 Claude Code 与 Claude Cowork",
 "subtitle": "两件不同的工作,同一套技术栈。Claude Code 和 Claude Cowork 是为执行你交给它们的任务而生。NoArk 是为帮你决定哪些任务首先值得你关注而生。",
 "intro": "Anthropic 的 <strong>Claude Code</strong> 和 <strong>Claude Cowork</strong> 把一件事做得很好:<em>一旦你知道想要什么</em>,它们就把它做完 —— 写函数、重构模块、起草报告、跑工作流。<strong>NoArk — 无限记忆</strong>位于上一层:它为执行<em>之前</em>的那个问题而生 —— <strong>当下究竟值得做什么、为什么?</strong> 带一键分析的实时全球头条告诉你世界正在如何变化,<strong>Fiat Lux</strong> 标签让你把真实问题带给历史上最有智慧者的 AI 版本(芒格、乔布斯、马可·奥勒留等 40 多位),40 多个 Apple 原生工作流帮你在市场、生活和工作之间设定优先级。NoArk 内部把请求路由到 Claude 的 <strong>Fable</strong> 模型,与 DeepSeek、Mistral、Kimi、Gemini 一起使用 —— 所以它不取代 Claude,而是站在 Claude 之上。",
 "glance": "一览对比",
 "col_noark": "NoArk — 无限记忆",
 "rows": [
  ("技术栈的层级", "<span class='yes'>决定</span>—— 什么值得做、什么最重要、为什么是现在", "执行 —— 任务定义好之后,把它做好"),
  ("回答的核心问题", "<span class='yes'>“我应该做什么,为什么?”</span> —— 定向、排序、理解", "“这件事怎么做?” —— 写代码、起草、构建、调用工具"),
  ("世界的实时信号", "<span class='yes'>实时全球头条</span>+一键分析,解读新闻对你和市场<em>意味着什么</em>", "不是焦点 —— 由用户带入情境"),
  ("最有智慧者的建议", "<span class='yes'>有</span>—— Fiat Lux:查理·芒格、史蒂夫·乔布斯、爱因斯坦、马可·奥勒留等 40 多位的 AI 版本,基于他们真实的思考方式", "通用助手;没有精心策划的导师议会"),
  ("用于排序的工作流", "<span class='yes'>40 多个开箱即用工作流</span>—— 涵盖市场、生产力、旅行、教育、生活事务", "任务执行与工具调用 —— 工作流由用户定义"),
  ("底层模型", "<span class='yes'>多个前沿模型,包括 Claude</span>—— Anthropic 的 Claude(Fable)、DeepSeek、Mistral、Kimi、Gemini", "Anthropic 的 Claude 系列"),
  ("是否需要登录", "<span class='yes'>不需要</span>—— 无账户、邮箱或手机号", "需要 Anthropic 账户"),
  ("你的对话", "<span class='yes'>只保存在你的设备</span>和你自己的 iCloud 中 —— 绝不堆放或用于训练", "发送到 Anthropic 的服务器"),
  ("数据收集", "<span class='yes'>无</span>—— Apple 隐私标签:“不收集数据”", "账户、使用、对话数据"),
  ("价格", "<span class='yes'>免费</span>下载(含可选的应用内购买)", "Claude Code 与 Cowork 的 Pro 套餐(付费)"),
 ],
 "note": "对比基于截至 2026 年 6 月的公开信息。Claude、Claude Code 与 Claude Cowork 是 Anthropic 的产品;NoArk 是独立应用,与 Anthropic 无关联,也未获其背书。NoArk 把请求路由到多个前沿模型,Anthropic 的 Claude(Fable)是其中之一。",
 "sections": [
  ("决定要做什么 —— 在动手之前", [
   "2026 年智能体类产品的主旋律是<strong>执行</strong>:Claude Code 给你写代码和重构,Claude Cowork 在你的浏览器里跑多步工作流。它们做得相当出色。但执行的前提是你已经知道什么值得执行 —— 而对大多数人、大多数时间来说,<em>那才是真正的难处</em>。市场在动,新闻在爆,组合在变,一周被各种可能填满,问题不是“这件事怎么做”,而是 <strong>“在我现在能做的所有事情里,哪一件最重要,为什么?”</strong>",
   "NoArk 就是为这个问题而生。主界面是一条<strong>实时全球头条</strong>的信息流,轻轻一点,就能得到解读一条新闻对你和市场究竟<em>意味着什么</em>的分析。<strong>Fiat Lux</strong> 标签让你把同一件事带给 AI 查理·芒格做反向检验,带给 AI 史蒂夫·乔布斯做聚焦检验,带给 AI 马可·奥勒留做平静检验 —— 每一位都立足于他们真实的思考方式。再加上 40 多个开箱即用的工作流,把原始信号转成一份“真正值得做的事情”短名单。当你把任务交给 Claude Code 或 Claude Cowork 去执行时,你已经选对了任务。",
  ]),
  ("构建在 Claude 之上 —— 而不是与之对抗", [
   "NoArk 不是 Claude 的替代品,它是 Claude 之上的一层。在内部,NoArk 把每个请求路由到众多前沿模型中最合适的一个 —— <strong>Anthropic 的 Claude(Fable)</strong>、DeepSeek、Mistral、Kimi 和谷歌的 Gemini —— 而不是依赖单一一个。所以当你点击“分析这条头条”或问芒格本周该躲开什么时,你常常拿到的是底层 Claude 级别的答案,NoArk 在外围承担上下文、人设、记忆和 Apple 原生呈现。两件产品互补:用 NoArk 决定什么值得你的注意力,然后让 Claude Code 或 Claude Cowork 去执行。",
  ]),
  ("默认私密 —— 无需账户,什么都不收集", [
   "Claude Code 与 Claude Cowork 需要 Anthropic 账户,你的提示词和代码会被发送到它们的服务器。NoArk 在你<em>思考</em>的隐私上反着来:<strong>无需登录</strong>—— 没有邮箱、没有手机号 —— 你的对话、头条分析与 Fiat Lux 对话<strong>只保存在你的设备和你自己的 iCloud 中</strong>,绝不堆放在我们的服务器上,也绝不用于训练任何模型。Apple 官方为 NoArk 出具的隐私标签写着 <a href='" + dp + "'>“不收集数据”</a>—— 最严格的一档。你为自己的人生所做的推理,依然属于你。",
  ]),
  ("不只是模型 —— 一款完整的 Apple 超级应用", [
   "在头条与 Fiat Lux 之外,NoArk 还是一款面向 iPhone、iPad、Mac 和 Apple Vision 的<strong>完整 Apple 超级应用</strong>:涵盖市场、生产力、旅行、教育和生活事务的 40 多个开箱即用工作流,以及由 TradingTransformer 团队打造、灵感来自克劳德·香农 AI 选股愿景的投资大脑。Claude Code 与 Cowork 在开发者的终端和知识工作者的浏览器里强大得很;NoArk 是你在<em>之间</em>的那些时刻 —— 当你想弄清楚下一步该做什么时 —— 想要拿出来用的那一款。",
  ]),
 ],
 "related_heading": "继续阅读",
 "related": [
  (hp, "NoArk — 无限记忆:智能 AI 操作系统与超级应用"),
  (gp, "NoArk 对比 ChatGPT"),
  (mp, "NoArk 对比 Google Gemini"),
  (pp, "NoArk 对比 Perplexity"),
  (mnp, "NoArk 对比 Manus"),
  (cp, "NoArk 对比 Character.AI"),
  (ap, "NoArk 对比 Apple Intelligence"),
  (fp, "关于 NoArk 的常见问题"),
 ],
 "faq": [
  ("NoArk 是 Claude 的替代品吗?", "并不完全是 —— NoArk 处于 AI 技术栈的另一层。Claude Code 与 Claude Cowork 专注于如何执行你已经定义好的任务:写代码、跑工作流、完成范围清晰的工作。NoArk 关心的是更早的一步 —— 帮你思考首先哪些任务值得你的关注 —— 通过实时世界新闻、来自历史最有智慧者(芒格、乔布斯、马可·奥勒留等 40 多位)AI 版本的建议,以及 40 多个用于发现优先级的工作流。在内部,NoArk 把请求路由到包括 Anthropic 的 Claude(Fable)在内的多个前沿模型,所以它是站在 Claude 之上,而不是与之对抗。"),
  ("NoArk 与 Claude Code 有什么不同?", "Claude Code 是为编程任务而生 —— 写函数、重构模块、跑测试 —— 前提是你已经决定要做什么。NoArk 则是帮你决定首先什么值得做(或值得花时间)的:它通过带一键分析的实时头条把世界的变化呈现给你,在 Fiat Lux 标签里让你把真实问题带给 AI 查理·芒格或史蒂夫·乔布斯,并提供 40 多个用于在市场与生活之间设定优先级的工作流。用 NoArk 选对任务,然后把执行交给 Claude Code。"),
  ("NoArk 与 Claude Cowork 有什么不同?", "Claude Cowork 在被赋予一个目标之后,会去跑多步工作流(研究、写作、浏览器自动化)。NoArk 帮你首先到达正确的目标。它的主界面是带一键解读的实时全球头条信息流;它的 Fiat Lux 标签把历史最有智慧者的 AI 版本带到真实问题上;它的 40 多个工作流帮你把世界的原始信号变成一份真正值得做的事情的短名单。然后,Cowork 可以去执行其中一件。"),
  ("NoArk 用了 Claude 吗?", "用了。NoArk 把每个请求路由到众多前沿模型中最合适的一个,而 Anthropic 的 Claude(Fable)就是其中之一 —— 与 DeepSeek、Mistral、Kimi 和谷歌的 Gemini 并列。所以当你对一条头条点了一键分析,或者向 Fiat Lux 中的某位导师提问时,底层的答案常常由 Claude 驱动。"),
  ("为什么聚焦于“做什么”而不是“怎么做”?", "因为对大多数人来说,大多数日子里,瓶颈不是执行 —— 而是选出值得做的事。市场在动,新闻在爆,日程被填满,而在错的事情上下苦功,代价远比在对的事情上慢一点要大。NoArk 的设计前提是:在行动之前帮你推理和排序,比从行动本身省下几分钟更有价值。"),
  ("我的工作在 NoArk 里是私密的吗?", "是的。没有登录、也不收集数据:你的对话、头条分析与 Fiat Lux 对话都留在你自己的设备和你自己的 iCloud 中,绝不堆放在我们的服务器上,也绝不用于训练模型。Apple 的隐私标签写着“不收集数据”。这比 Claude Code 或 Claude Cowork 更严格 —— 后者需要 Anthropic 账户,并将你的提示词和代码发送到它们的服务器。"),
  ("NoArk 免费吗?", "NoArk 在 iPhone、iPad、Mac 和 Apple Vision 上免费下载,含可选的应用内购买。开始使用无需账户,也不收集数据。"),
 ],
}

# ---------------- Traditional Chinese ----------------
hp, gp, cp, mp, pp, mnp, ap, fp, dp = rel("zh-tw")
content["zh-tw"] = {
 "title": "NoArk 對比 Claude Code 與 Cowork:決定值得做什麼,而不只是怎麼做",
 "desc": "NoArk 與 Claude Code、Claude Cowork 全面對比:NoArk 處於 AI 技術堆疊的不同一層。Claude Code 和 Cowork 專注於如何執行你已經選好的任務;NoArk 幫你思考究竟哪些任務最值得你關注 —— 透過即時新聞解讀、歷史智者的建議,以及 40 多個用於發現優先順序的工作流程。iPhone、iPad、Mac 和 Apple Vision 免費下載;內部使用 Claude Fable。",
 "keywords": "NoArk 對比 Claude, NoArk 對比 Claude Code, NoArk 對比 Claude Cowork, 決定做什麼的 AI, 優先順序 AI, 用於推理的 AI, Claude 替代品, Claude 互補品, Anthropic Claude, Claude Fable, AI 教練 iPhone, 端側 AI, 私密 AI",
 "ogdesc": "NoArk 與 Claude Code、Cowork 的不同:它們執行你定義好的任務;NoArk 幫你先想清楚哪些任務最值得做 —— 憑藉即時新聞、歷史智者的建議、40 多個優先順序工作流程 —— 建構在 Claude Fable 與其他前沿模型之上。",
 "twdesc": "Claude Code 與 Cowork:怎麼做任務。NoArk:首先值得做什麼 —— 即時新聞解讀、最有智慧者的建議、40 多個工作流程。建構在 Claude Fable 與同伴之上。",
 "h1": "NoArk 對比 Claude Code 與 Claude Cowork",
 "subtitle": "兩件不同的工作,同一套技術堆疊。Claude Code 和 Claude Cowork 是為執行你交給它們的任務而生。NoArk 是為幫你決定哪些任務首先值得你關注而生。",
 "intro": "Anthropic 的 <strong>Claude Code</strong> 和 <strong>Claude Cowork</strong> 把一件事做得很好:<em>一旦你知道想要什麼</em>,它們就把它做完 —— 寫函式、重構模組、起草報告、跑工作流程。<strong>NoArk — 無限記憶</strong>位於上一層:它為執行<em>之前</em>的那個問題而生 —— <strong>當下究竟值得做什麼、為什麼?</strong> 帶一鍵分析的即時全球頭條告訴你世界正在如何變化,<strong>Fiat Lux</strong> 分頁讓你把真實問題帶給歷史上最有智慧者的 AI 版本(蒙格、賈伯斯、馬可·奧理略等 40 多位),40 多個 Apple 原生工作流程幫你在市場、生活和工作之間設定優先順序。NoArk 內部把請求路由到 Claude 的 <strong>Fable</strong> 模型,與 DeepSeek、Mistral、Kimi、Gemini 一起使用 —— 所以它不取代 Claude,而是站在 Claude 之上。",
 "glance": "一覽對比",
 "col_noark": "NoArk — 無限記憶",
 "rows": [
  ("技術堆疊的層級", "<span class='yes'>決定</span>—— 什麼值得做、什麼最重要、為什麼是現在", "執行 —— 任務定義好之後,把它做好"),
  ("回答的核心問題", "<span class='yes'>「我應該做什麼,為什麼?」</span>—— 定向、排序、理解", "「這件事怎麼做?」—— 寫程式、起草、建構、呼叫工具"),
  ("世界的即時訊號", "<span class='yes'>即時全球頭條</span>+一鍵分析,解讀新聞對你和市場<em>意味著什麼</em>", "不是焦點 —— 由使用者帶入情境"),
  ("最有智慧者的建議", "<span class='yes'>有</span>—— Fiat Lux:查理·蒙格、史蒂夫·賈伯斯、愛因斯坦、馬可·奧理略等 40 多位的 AI 版本,基於他們真實的思考方式", "通用助理;沒有精心策劃的導師議會"),
  ("用於排序的工作流程", "<span class='yes'>40 多個開箱即用工作流程</span>—— 涵蓋市場、生產力、旅行、教育、生活事務", "任務執行與工具呼叫 —— 工作流程由使用者定義"),
  ("底層模型", "<span class='yes'>多個前沿模型,包括 Claude</span>—— Anthropic 的 Claude(Fable)、DeepSeek、Mistral、Kimi、Gemini", "Anthropic 的 Claude 系列"),
  ("是否需要登入", "<span class='yes'>不需要</span>—— 無帳號、電子郵件或手機號碼", "需要 Anthropic 帳號"),
  ("你的對話", "<span class='yes'>只保存在你的裝置</span>和你自己的 iCloud 中 —— 絕不堆放或用於訓練", "傳送到 Anthropic 的伺服器"),
  ("資料收集", "<span class='yes'>無</span>—— Apple 隱私標籤:「不收集資料」", "帳號、使用、對話資料"),
  ("價格", "<span class='yes'>免費</span>下載(含可選的應用程式內購買)", "Claude Code 與 Cowork 的 Pro 方案(付費)"),
 ],
 "note": "對比基於截至 2026 年 6 月的公開資訊。Claude、Claude Code 與 Claude Cowork 是 Anthropic 的產品;NoArk 是獨立應用程式,與 Anthropic 無關聯,也未獲其背書。NoArk 把請求路由到多個前沿模型,Anthropic 的 Claude(Fable)是其中之一。",
 "sections": [
  ("決定要做什麼 —— 在動手之前", [
   "2026 年代理人類產品的主旋律是<strong>執行</strong>:Claude Code 給你寫程式碼和重構,Claude Cowork 在你的瀏覽器裡跑多步工作流程。它們做得相當出色。但執行的前提是你已經知道什麼值得執行 —— 而對大多數人、大多數時間來說,<em>那才是真正的難處</em>。市場在動,新聞在爆,組合在變,一週被各種可能填滿,問題不是「這件事怎麼做」,而是 <strong>「在我現在能做的所有事情裡,哪一件最重要,為什麼?」</strong>",
   "NoArk 就是為這個問題而生。主介面是一條<strong>即時全球頭條</strong>的資訊流,輕輕一點,就能得到解讀一條新聞對你和市場究竟<em>意味著什麼</em>的分析。<strong>Fiat Lux</strong> 分頁讓你把同一件事帶給 AI 查理·蒙格做反向檢驗,帶給 AI 史蒂夫·賈伯斯做聚焦檢驗,帶給 AI 馬可·奧理略做平靜檢驗 —— 每一位都立足於他們真實的思考方式。再加上 40 多個開箱即用的工作流程,把原始訊號轉成一份「真正值得做的事情」短名單。當你把任務交給 Claude Code 或 Claude Cowork 去執行時,你已經選對了任務。",
  ]),
  ("建構在 Claude 之上 —— 而不是與之對抗", [
   "NoArk 不是 Claude 的替代品,它是 Claude 之上的一層。在內部,NoArk 把每個請求路由到眾多前沿模型中最合適的一個 —— <strong>Anthropic 的 Claude(Fable)</strong>、DeepSeek、Mistral、Kimi 和 Google 的 Gemini —— 而不是依賴單一一個。所以當你點擊「分析這條頭條」或問蒙格本週該躲開什麼時,你常常拿到的是底層 Claude 級別的答案,NoArk 在外圍承擔上下文、人設、記憶和 Apple 原生呈現。兩件產品互補:用 NoArk 決定什麼值得你的注意力,然後讓 Claude Code 或 Claude Cowork 去執行。",
  ]),
  ("預設私密 —— 無需帳號,什麼都不收集", [
   "Claude Code 與 Claude Cowork 需要 Anthropic 帳號,你的提示詞和程式碼會被傳送到它們的伺服器。NoArk 在你<em>思考</em>的隱私上反著來:<strong>無需登入</strong>—— 沒有電子郵件、沒有手機號碼 —— 你的對話、頭條分析與 Fiat Lux 對話<strong>只保存在你的裝置和你自己的 iCloud 中</strong>,絕不堆放在我們的伺服器上,也絕不用於訓練任何模型。Apple 官方為 NoArk 出具的隱私標籤寫著 <a href='" + dp + "'>「不收集資料」</a>—— 最嚴格的一檔。你為自己的人生所做的推理,依然屬於你。",
  ]),
  ("不只是模型 —— 一款完整的 Apple 超級應用程式", [
   "在頭條與 Fiat Lux 之外,NoArk 還是一款面向 iPhone、iPad、Mac 和 Apple Vision 的<strong>完整 Apple 超級應用程式</strong>:涵蓋市場、生產力、旅行、教育和生活事務的 40 多個開箱即用工作流程,以及由 TradingTransformer 團隊打造、靈感來自克勞德·夏農 AI 選股願景的投資大腦。Claude Code 與 Cowork 在開發者的終端機和知識工作者的瀏覽器裡強大得很;NoArk 是你在<em>之間</em>的那些時刻 —— 當你想搞清楚下一步該做什麼時 —— 想要拿出來用的那一款。",
  ]),
 ],
 "related_heading": "繼續閱讀",
 "related": [
  (hp, "NoArk — 無限記憶:智慧型 AI 作業系統與超級應用程式"),
  (gp, "NoArk 對比 ChatGPT"),
  (mp, "NoArk 對比 Google Gemini"),
  (pp, "NoArk 對比 Perplexity"),
  (mnp, "NoArk 對比 Manus"),
  (cp, "NoArk 對比 Character.AI"),
  (ap, "NoArk 對比 Apple Intelligence"),
  (fp, "關於 NoArk 的常見問題"),
 ],
 "faq": [
  ("NoArk 是 Claude 的替代品嗎?", "並不完全是 —— NoArk 處於 AI 技術堆疊的另一層。Claude Code 與 Claude Cowork 專注於如何執行你已經定義好的任務:寫程式碼、跑工作流程、完成範圍清晰的工作。NoArk 關心的是更早的一步 —— 幫你思考首先哪些任務值得你的關注 —— 透過即時世界新聞、來自歷史最有智慧者(蒙格、賈伯斯、馬可·奧理略等 40 多位)AI 版本的建議,以及 40 多個用於發現優先順序的工作流程。在內部,NoArk 把請求路由到包括 Anthropic 的 Claude(Fable)在內的多個前沿模型,所以它是站在 Claude 之上,而不是與之對抗。"),
  ("NoArk 與 Claude Code 有什麼不同?", "Claude Code 是為程式設計任務而生 —— 寫函式、重構模組、跑測試 —— 前提是你已經決定要做什麼。NoArk 則是幫你決定首先什麼值得做(或值得花時間)的:它透過帶一鍵分析的即時頭條把世界的變化呈現給你,在 Fiat Lux 分頁裡讓你把真實問題帶給 AI 查理·蒙格或史蒂夫·賈伯斯,並提供 40 多個用於在市場與生活之間設定優先順序的工作流程。用 NoArk 選對任務,然後把執行交給 Claude Code。"),
  ("NoArk 與 Claude Cowork 有什麼不同?", "Claude Cowork 在被賦予一個目標之後,會去跑多步工作流程(研究、寫作、瀏覽器自動化)。NoArk 幫你首先到達正確的目標。它的主介面是帶一鍵解讀的即時全球頭條資訊流;它的 Fiat Lux 分頁把歷史最有智慧者的 AI 版本帶到真實問題上;它的 40 多個工作流程幫你把世界的原始訊號變成一份真正值得做的事情的短名單。然後,Cowork 可以去執行其中一件。"),
  ("NoArk 用了 Claude 嗎?", "用了。NoArk 把每個請求路由到眾多前沿模型中最合適的一個,而 Anthropic 的 Claude(Fable)就是其中之一 —— 與 DeepSeek、Mistral、Kimi 和 Google 的 Gemini 並列。所以當你對一條頭條點了一鍵分析,或者向 Fiat Lux 中的某位導師提問時,底層的答案常常由 Claude 驅動。"),
  ("為什麼聚焦於「做什麼」而不是「怎麼做」?", "因為對大多數人來說,大多數日子裡,瓶頸不是執行 —— 而是選出值得做的事。市場在動,新聞在爆,行程被填滿,而在錯的事情上下苦工,代價遠比在對的事情上慢一點要大。NoArk 的設計前提是:在行動之前幫你推理和排序,比從行動本身省下幾分鐘更有價值。"),
  ("我的工作在 NoArk 裡是私密的嗎?", "是的。沒有登入、也不收集資料:你的對話、頭條分析與 Fiat Lux 對話都留在你自己的裝置和你自己的 iCloud 中,絕不堆放在我們的伺服器上,也絕不用於訓練模型。Apple 的隱私標籤寫著「不收集資料」。這比 Claude Code 或 Claude Cowork 更嚴格 —— 後者需要 Anthropic 帳號,並將你的提示詞和程式碼傳送到它們的伺服器。"),
  ("NoArk 免費嗎?", "NoArk 在 iPhone、iPad、Mac 和 Apple Vision 上免費下載,含可選的應用程式內購買。開始使用無需帳號,也不收集資料。"),
 ],
}

render(SLUG, COMP, content)
