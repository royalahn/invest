# AGENTS.md

This file contains project-specific guidelines for AI coding assistants.

## 0. Project Overview
- **프로젝트 목적**: 투자 관련 종목 인사이트 및 분석 리포트를 HTML 문서로 작성하고, GitHub Pages를 통해 호스팅하는 프로젝트입니다.
- **주요 콘텐츠**: 종목 분석, 시장 동향, 투자 전략, 재무제표 분석, 섹터 리포트 등
- **기술 스택**: HTML + Tailwind CSS (CDN) + Vanilla JavaScript, GitHub Pages 호스팅

## 1. UI/UX & HTML Design
- **HTML 문서 생성의 절대 규칙**: 새로운 HTML 페이지를 만들 때는 스크래치부터 작성하지 마십시오. 반드시 **`template/base_template.html`** 파일의 전체 코드를 복사(Base 템플릿으로 사용)한 뒤, 기본적으로 `<main>` 태그 내부 영역을 중심적으로 수정하십시오. 단, Header 영역의 로고 아이콘(`<svg>`)과 Title 텍스트(`<h1>`)는 생성하는 페이지 성격에 맞게 변경해야 합니다. 그 외의 Footer, Head 설정 등 기본 구조는 변경을 금지합니다.
- **HTML 랜딩 페이지/UI 생성 시**: 반드시 `template/html_design_guide.md` 파일에 정의된 "Modern Startup / SaaS 스타일" 가이드라인(Tailwind CSS, Glassmorphism, Animations 등)을 참고하여 `<main>` 내부를 디자인할 것.
- 인라인 스타일은 피하고, 제공된 가이드에 명시된 설정 및 구조(Tailwind config, CDN)를 따를 것.
- **Favicon 설정**: `template/base_template.html`에 이미 `assets/icons/favicon.svg`가 적용되어 있습니다. 임의로 변경하지 마십시오.

## 2. HTML Files Management
- **ai-html 폴더 내 HTML 생성 시**: 새로운 HTML 파일을 `ai-html` 폴더에 생성하거나 추가할 경우, 반드시 루트의 `pages.json` 파일을 확인하고 새로운 페이지 정보를 함께 업데이트(등록)할 것. `pages.json`의 `filename` 필드에는 `ai-html/` 경로 prefix를 포함하여 기록할 것.

## 3. 투자 문서 작성 가이드라인
- **권장 카테고리**: `종목분석`, `시장동향`, `투자전략`, `재무분석`, `섹터리포트`, `ETF분석`, `매크로`, `가이드`
- **pages.json 등록 형식**:
  ```json
  {
    "title": "문서 제목",
    "filename": "ai-html/파일명.html",
    "description": "문서에 대한 간결한 설명 (1~2문장)",
    "category": "카테고리명",
    "date": "YYYY-MM-DD"
  }
  ```
- **문서 내 데이터 표현**: 투자 관련 수치는 표(Table), 차트 형태의 시각적 요소, 강조 카드 등을 적극 활용하여 가독성을 높일 것.
