# 📈 Invest Insight

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-blue?logo=github)](https://royalahn.github.io/invest/)

> **[🇺🇸 English Version](./README.md)**

투자 인사이트 리포트를 HTML 문서로 작성하고, GitHub Pages를 통해 호스팅하는 프로젝트입니다. 종목 분석, 시장 동향, 투자 전략 등 다양한 투자 관련 콘텐츠를 AI의 도움을 받아 제작합니다.

## 프로젝트 구조

```
invest/
├── index.html                  # 랜딩 페이지 (문서 카탈로그 허브)
├── pages.json                  # 문서 레지스트리 (모든 리포트의 메타데이터)
├── ai-html/                    # 투자 인사이트 HTML 문서 폴더
├── template/
│   ├── base_template.html      # 새 문서 작성용 기본 템플릿
│   └── html_design_guide.md    # 디자인 시스템 레퍼런스
├── assets/
│   └── icons/
│       └── favicon.svg
└── AGENTS.md                   # AI 코딩 어시스턴트 가이드라인
```

## 기술 스택

- **HTML** + **Tailwind CSS** (CDN) + **Vanilla JavaScript**
- **Pretendard** (본문 폰트) + **Cascadia Mono** (코드 폰트)
- **Font Awesome 6.5** (아이콘)
- **GitHub Pages** (호스팅)

## 작동 방식

1. 모든 투자 리포트는 `ai-html/` 디렉토리에 독립적인 HTML 파일로 저장됩니다.
2. 각 리포트는 `pages.json`에 메타데이터(제목, 설명, 카테고리, 날짜)와 함께 등록됩니다.
3. `index.html`이 `pages.json`을 읽어 검색 및 카테고리 필터링이 가능한 카탈로그를 렌더링합니다.

## 새 리포트 추가 방법

1. `template/base_template.html`을 복사하여 시작합니다.
2. `<main>` 영역을 원하는 콘텐츠로 수정합니다. 헤더의 아이콘과 타이틀도 주제에 맞게 변경합니다.
3. `ai-html/파일명.html`로 저장합니다.
4. `pages.json`에 등록합니다:

```json
{
  "title": "리포트 제목",
  "filename": "ai-html/파일명.html",
  "description": "리포트에 대한 간결한 설명 (1~2문장)",
  "category": "종목분석",
  "date": "2026-06-03"
}
```

## 리포트 카테고리

| 카테고리 | 설명 |
|---|---|
| 종목분석 | 개별 종목 심층 분석 |
| 시장동향 | 시장 트렌드 및 전망 |
| 투자전략 | 투자 전략 및 방법론 |
| 재무분석 | 재무제표 분석 |
| 섹터리포트 | 산업/섹터 분석 리포트 |
| ETF분석 | ETF 상품 분석 |
| 매크로 | 거시경제 분석 |
| 가이드 | 가이드 및 튜토리얼 |

## 라이선스

이 프로젝트는 오픈 소스입니다. 투자 리서치 허브 템플릿으로 자유롭게 활용하세요.
