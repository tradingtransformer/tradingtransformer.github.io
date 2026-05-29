/*
 * Shared multilingual switcher for tradingtransformer.github.io
 * - Injects a floating language picker (no per-page markup needed).
 * - Shows an Apple-style, dismissible "view in your language?" banner on first visit.
 * - Never hard-redirects; the requested URL is always served as-is (SEO-safe).
 *
 * Each page declares its locale via <html lang="...">. Localized copies live in
 * top-level folders; English lives at the site root.
 */
(function () {
  "use strict";

  // locale code (matches <html lang>) -> { path prefix, native label }
  var LOCALES = [
    { code: "en",      prefix: "",        label: "English" },
    { code: "es",      prefix: "es",      label: "Español" },
    { code: "zh-Hans", prefix: "zh-cn",   label: "简体中文" },
    { code: "zh-Hant", prefix: "zh-tw",   label: "繁體中文" },
    { code: "fr",      prefix: "fr",      label: "Français" },
    { code: "ja",      prefix: "ja",      label: "日本語" }
  ];

  // Short prompt shown in the suggestion banner, written in the *target* language.
  var BANNER = {
    "en":      { msg: "View this page in English?",   cta: "Switch", close: "Dismiss" },
    "es":      { msg: "¿Ver esta página en español?", cta: "Cambiar", close: "Cerrar" },
    "zh-Hans": { msg: "用简体中文查看本页面？",          cta: "切换", close: "关闭" },
    "zh-Hant": { msg: "用繁體中文檢視此頁面？",          cta: "切換", close: "關閉" },
    "fr":      { msg: "Afficher cette page en français ?", cta: "Changer", close: "Fermer" },
    "ja":      { msg: "このページを日本語で表示しますか？", cta: "切り替え", close: "閉じる" }
  };

  var PREFIXES = LOCALES.map(function (l) { return l.prefix; }).filter(Boolean);

  function localeByCode(code) {
    for (var i = 0; i < LOCALES.length; i++) {
      if (LOCALES[i].code === code) return LOCALES[i];
    }
    return LOCALES[0];
  }

  var currentCode = (document.documentElement.getAttribute("lang") || "en").trim();
  var current = localeByCode(currentCode);

  // Strip any known locale prefix from the current path -> base path relative to root.
  // e.g. "/es/wsw_ai/privacy-policy.html" -> "/wsw_ai/privacy-policy.html"; "/es/" -> "/"
  function basePath() {
    var p = window.location.pathname;
    for (var i = 0; i < PREFIXES.length; i++) {
      var pre = "/" + PREFIXES[i];
      if (p === pre || p === pre + "/") return "/";
      if (p.indexOf(pre + "/") === 0) return p.slice(pre.length); // keep leading slash
    }
    return p === "" ? "/" : p;
  }

  // Build the URL for the equivalent page in a target locale.
  function urlFor(locale) {
    var base = basePath();
    if (!locale.prefix) return base; // English at root
    if (base === "/") return "/" + locale.prefix + "/";
    return "/" + locale.prefix + base;
  }

  // Map the browser's preferred languages to one of our locales (or null).
  function detectBrowserLocale() {
    var langs = navigator.languages && navigator.languages.length
      ? navigator.languages
      : [navigator.language || ""];
    for (var i = 0; i < langs.length; i++) {
      var l = (langs[i] || "").toLowerCase();
      if (!l) continue;
      if (l.indexOf("zh") === 0) {
        // Traditional for tw/hk/mo or explicit Hant; otherwise Simplified.
        if (l.indexOf("hant") !== -1 || l.indexOf("tw") !== -1 ||
            l.indexOf("hk") !== -1 || l.indexOf("mo") !== -1) {
          return localeByCode("zh-Hant");
        }
        return localeByCode("zh-Hans");
      }
      if (l.indexOf("es") === 0) return localeByCode("es");
      if (l.indexOf("fr") === 0) return localeByCode("fr");
      if (l.indexOf("ja") === 0) return localeByCode("ja");
      if (l.indexOf("en") === 0) return localeByCode("en");
    }
    return null;
  }

  function injectStyles() {
    var css =
      ".ttx-lang{position:fixed;top:10px;right:12px;z-index:2147483000;}" +
      ".ttx-lang select{font:500 13px/1.2 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;" +
        "color:#1d1d1f;background:rgba(255,255,255,0.9);-webkit-backdrop-filter:saturate(180%) blur(12px);" +
        "backdrop-filter:saturate(180%) blur(12px);border:1px solid rgba(0,0,0,0.15);border-radius:980px;" +
        "padding:6px 30px 6px 14px;cursor:pointer;appearance:none;-webkit-appearance:none;" +
        "background-image:url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%231d1d1f' stroke-width='2'><path d='M6 9l6 6 6-6'/></svg>\");" +
        "background-repeat:no-repeat;background-position:right 11px center;box-shadow:0 2px 10px rgba(0,0,0,0.08);}" +
      ".ttx-lang select:focus{outline:2px solid #0071e3;outline-offset:1px;}" +
      ".ttx-banner{position:fixed;left:0;right:0;bottom:0;z-index:2147483000;display:flex;gap:14px;" +
        "align-items:center;justify-content:center;flex-wrap:wrap;padding:12px 16px;" +
        "background:rgba(20,20,22,0.92);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);" +
        "color:#f5f5f7;font:500 15px/1.4 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;" +
        "box-shadow:0 -2px 16px rgba(0,0,0,0.2);}" +
      ".ttx-banner a.ttx-cta{background:#0071e3;color:#fff;text-decoration:none;padding:8px 18px;border-radius:980px;font-weight:500;}" +
      ".ttx-banner a.ttx-cta:hover{background:#0077ed;}" +
      ".ttx-banner button.ttx-x{background:transparent;border:1px solid rgba(255,255,255,0.4);color:#f5f5f7;" +
        "padding:8px 16px;border-radius:980px;cursor:pointer;font:inherit;}" +
      ".ttx-banner button.ttx-x:hover{border-color:rgba(255,255,255,0.8);}" +
      "@media(max-width:768px){.ttx-lang{top:auto;bottom:74px;right:10px;}}";
    var s = document.createElement("style");
    s.textContent = css;
    document.head.appendChild(s);
  }

  function injectPicker() {
    var wrap = document.createElement("div");
    wrap.className = "ttx-lang";
    var sel = document.createElement("select");
    sel.setAttribute("aria-label", "Select language");
    LOCALES.forEach(function (loc) {
      var opt = document.createElement("option");
      opt.value = loc.code;
      opt.textContent = loc.label;
      if (loc.code === current.code) opt.selected = true;
      sel.appendChild(opt);
    });
    sel.addEventListener("change", function () {
      var target = localeByCode(sel.value);
      try { localStorage.setItem("preferredLang", target.code); } catch (e) {}
      window.location.href = urlFor(target);
    });
    wrap.appendChild(sel);
    document.body.appendChild(wrap);
  }

  function showBanner(target) {
    var t = BANNER[target.code] || BANNER.en;
    var bar = document.createElement("div");
    bar.className = "ttx-banner";

    var msg = document.createElement("span");
    msg.textContent = t.msg;

    var cta = document.createElement("a");
    cta.className = "ttx-cta";
    cta.href = urlFor(target);
    cta.textContent = t.cta;
    cta.addEventListener("click", function () {
      try { localStorage.setItem("preferredLang", target.code); } catch (e) {}
    });

    var x = document.createElement("button");
    x.className = "ttx-x";
    x.type = "button";
    x.textContent = t.close;
    x.addEventListener("click", function () {
      try { localStorage.setItem("langBannerDismissed", "1"); } catch (e) {}
      bar.parentNode && bar.parentNode.removeChild(bar);
    });

    bar.appendChild(msg);
    bar.appendChild(cta);
    bar.appendChild(x);
    document.body.appendChild(bar);
  }

  function maybeSuggest() {
    var pref = null, dismissed = null;
    try {
      pref = localStorage.getItem("preferredLang");
      dismissed = localStorage.getItem("langBannerDismissed");
    } catch (e) {}

    // If the user already chose a language and we're not on it, offer to switch.
    if (pref && pref !== current.code) {
      showBanner(localeByCode(pref));
      return;
    }
    if (pref === current.code) return; // already where they want to be

    if (dismissed) return;

    var detected = detectBrowserLocale();
    if (detected && detected.code !== current.code) {
      showBanner(detected);
    }
  }

  function init() {
    injectStyles();
    injectPicker();
    maybeSuggest();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
