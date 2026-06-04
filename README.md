# TradingTransformer Technologies - Website

A professional investment fund website for TradingTransformer Technologies LLC, showcasing AI-powered investment strategies and portfolio management services.

**Official Website**: [www.tradingtransformer.com](https://www.tradingtransformer.com)

## 🚀 Overview

TradingTransformer Technologies is an investment fund that leverages proprietary "Transformer" AI technology to analyze market data and optimize portfolio allocations. This website serves as the primary digital presence for the fund, providing information about investment strategies, performance, and contact details for potential investors.

## 📁 Project Structure

```
tradingtransformer.github.io/
├── index.html              # Main website homepage
├── annual-letter-2025.html # Annual investor letter
├── wswai.jpeg             # WSW AI company logo/image
└── README.md              # This file
```

## 🎯 Key Features

- **Responsive Design**: Mobile-friendly layout that adapts to all screen sizes
- **Professional Styling**: Clean, modern design with a financial industry aesthetic
- **Investment Strategy Showcase**: Detailed explanation of AI-powered investment approach
- **Risk Management Emphasis**: Clear communication of no-leverage, long-only strategy
- **WSW AI Integration**: Direct link to WSW AI - Company Finder tool
- **Contact Information**: Easy access to fund contact details
- **Performance Metrics**: Highlighted investment performance data
- **Compliance Ready**: Includes appropriate investment disclaimers

## 🛠 Technology Stack

- **HTML5**: Semantic markup structure
- **CSS3**: Custom styling with CSS variables and responsive design
- **Vanilla JavaScript**: Interactive elements and smooth scrolling
- **GitHub Pages**: Static site hosting

## 🎨 Design Elements

- **Color Scheme**: Professional blue palette with accent colors
- **Typography**: Clean, readable fonts optimized for financial content
- **Layout**: Grid-based responsive design
- **Interactive Elements**: Hover effects and smooth transitions
- **Mobile Optimization**: Touch-friendly navigation and responsive breakpoints

## 📊 Content Sections

1. **Hero Section**: Company introduction and key value proposition
2. **Investment Strategy**: Detailed explanation of AI-powered approach
3. **Performance**: Key metrics and investment results
4. **Risk Management**: Emphasis on conservative, no-leverage approach
5. **WSW AI Integration**: Link to company finder tool
6. **Contact**: Investor inquiry information
7. **Legal Disclaimers**: Required investment fund disclosures

## 🔗 External Integrations

- **WSW AI**: Direct integration with company finder tool at [wsw.ai](https://wsw.ai)
- **Email Contact**: Direct mailto links for investor inquiries

## 📱 Responsive Breakpoints

- **Desktop**: 1200px and above
- **Tablet**: 768px - 1199px
- **Mobile**: Below 768px

## 🚀 Deployment

This site is designed for GitHub Pages deployment:

1. Push changes to the main branch
2. GitHub Pages automatically builds and deploys the site
3. Site is accessible at the configured GitHub Pages URL

## 📝 Content Updates

To update content:

1. Edit `index.html` for main website content
2. Edit `annual-letter-2025.html` for annual investor communications
3. Replace `wswai.jpeg` for updated company imagery
4. Commit and push changes for automatic deployment

## 🔒 Compliance Notes

- All investment disclaimers are included as required
- Performance data should be updated regularly
- Contact information must remain current
- Any material changes should be reviewed for regulatory compliance

## 🌐 Multilingual SEO (Bing & others)

The site ships in six languages — English (root), `es/`, `fr/`, `ja/`, `zh-cn/`
(Simplified), `zh-tw/` (Traditional). Each locale page has correct on-page SEO
(self-referencing `canonical`, full `hreflang` block, localized title/description) and
is listed in `sitemap.xml`.

**Why non-English pages weren't appearing in Bing:** the locale pages had no crawlable
inbound `<a href>` links — the only way to reach them was the JavaScript language picker
(`lang-switcher.js`). Bing barely executes JS and uses `hreflang`/sitemaps only as weak
discovery hints, so it treated the locale pages as orphans and never indexed them. The
fix: a static **footer language switcher** (`nav.ttx-lang-links`) with real anchor links
to all six languages now lives on every content page. Keep adding it to any new page.

### After each deploy — push URLs to Bing instantly

```bash
./indexnow-submit.sh      # POSTs every sitemap URL to IndexNow (Bing, Yandex, …)
```

- IndexNow key file: `89cbebd9dc814ded8ba7e82926a405bf.txt` at the repo root (must stay
  reachable at `https://tradingtransformer.github.io/89cbebd9dc814ded8ba7e82926a405bf.txt`).
- Bump the relevant `<lastmod>` dates in `sitemap.xml` when you change pages, so Bing
  re-crawls.

### One-time — Bing Webmaster Tools (account: w@wsw.ai)

The public `robots.txt` `Sitemap:` line alone is not enough for a new low-authority
`github.io` site. Submit directly:

1. Sign in at <https://www.bing.com/webmasters> and add
   `https://tradingtransformer.github.io/`. Fastest verification: **import from Google
   Search Console** if already verified there; otherwise paste the provided
   `<meta name="msvalidate.01" content="…">` into the root `index.html` `<head>`, or
   upload their `BingSiteAuth.xml` to the repo root.
2. **Sitemaps → Submit** `https://tradingtransformer.github.io/sitemap.xml`.
3. **URL Inspection → Submit** the six locale homepages to force a first crawl.

Then confirm: `site:tradingtransformer.github.io/zh-cn/` in Bing returns the page, and
the localized hero snippet becomes searchable. Indexing latency after this is on Bing's
side — the repo-side changes above are what unblock discovery.

## 📧 Contact

For technical issues with the website or content updates, contact the development team through the standard company channels.

---

*Last updated: June 2026*
