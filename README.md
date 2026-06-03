# 📈 Invest Insight

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-blue?logo=github)](https://royalahn.github.io/invest/)

> **[🇰🇷 한국어 버전 (Korean)](./README_ko.md)**

A curated collection of investment insight reports hosted via GitHub Pages. Each report is an HTML document covering stock analysis, market trends, investment strategies, and more — all crafted with AI assistance.

## Project Structure

```
invest/
├── index.html                  # Landing page (document catalog hub)
├── pages.json                  # Document registry (metadata for all reports)
├── ai-html/                    # Investment insight HTML documents
├── template/
│   ├── base_template.html      # Base template for new documents
│   └── html_design_guide.md    # Design system reference
├── assets/
│   └── icons/
│       └── favicon.svg
└── AGENTS.md                   # AI coding assistant guidelines
```

## Tech Stack

- **HTML** + **Tailwind CSS** (CDN) + **Vanilla JavaScript**
- **Pretendard** (body font) + **Cascadia Mono** (code font)
- **Font Awesome 6.5** (icons)
- **GitHub Pages** (hosting)

## How It Works

1. All investment reports live in the `ai-html/` directory as standalone HTML files.
2. Each report is registered in `pages.json` with metadata (title, description, category, date).
3. `index.html` dynamically reads `pages.json` and renders a searchable, filterable catalog.

## Adding a New Report

1. Copy `template/base_template.html` as your starting point.
2. Edit the `<main>` section with your content. Update the header icon and title to match the report topic.
3. Save the file to `ai-html/your_report.html`.
4. Register it in `pages.json`:

```json
{
  "title": "Report Title",
  "filename": "ai-html/your_report.html",
  "description": "Brief description of the report.",
  "category": "종목분석",
  "date": "2026-06-03"
}
```

## Report Categories

| Category | Description |
|---|---|
| 종목분석 | Individual stock analysis |
| 시장동향 | Market trends & outlook |
| 투자전략 | Investment strategies |
| 재무분석 | Financial statement analysis |
| 섹터리포트 | Sector reports |
| ETF분석 | ETF analysis |
| 매크로 | Macro economics |
| 가이드 | Guides & tutorials |

## License

This project is open source. Feel free to use it as a template for your own investment research hub.
