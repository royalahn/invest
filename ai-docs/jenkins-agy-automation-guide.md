# Jenkins + Antigravity CLI 일일 투자 인사이트 자동화 가이드

> 이 문서는 Jenkins 스케줄러와 Antigravity CLI(agy)의 non-interactive 모드를 활용하여, 매일 투자 관련 뉴스를 수집하고 HTML 리포트를 자동 생성한 뒤 GitHub Pages로 배포하는 전체 파이프라인을 설명합니다.

---

## 목차

1. [아키텍처 개요](#1-아키텍처-개요)
2. [사전 준비](#2-사전-준비)
3. [agy CLI Non-Interactive 모드](#3-agy-cli-non-interactive-모드)
4. [프롬프트 설계](#4-프롬프트-설계)
5. [Jenkins Job 구성](#5-jenkins-job-구성)
6. [Git 자동화 (Commit & Push)](#6-git-자동화-commit--push)
7. [실행 흐름 요약](#7-실행-흐름-요약)
8. [트러블슈팅](#8-트러블슈팅)

---

## 1. 아키텍처 개요

```
┌──────────────────────────────────────────────────────────┐
│                     Jenkins Server                        │
│                                                           │
│  ┌─────────────┐    ┌──────────────┐    ┌──────────────┐ │
│  │  Cron 트리거  │───▶│  Shell 스크립트 │───▶│   agy -p     │ │
│  │ (매일 08:00) │    │  (Build Step) │    │ (non-inter.) │ │
│  └─────────────┘    └──────────────┘    └──────┬───────┘ │
│                                                 │         │
│                                      ┌──────────▼───────┐│
│                                      │ 1. 뉴스 검색      ││
│                                      │ 2. HTML 생성      ││
│                                      │ 3. daily.json 등록││
│                                      │ 4. git commit     ││
│                                      │ 5. git push       ││
│                                      └──────────────────┘│
└──────────────────────────────────────────────────────────┘
                              │
                              ▼
                    GitHub Pages 자동 배포
```

### 파일 흐름

| 단계 | 입력 | 출력 |
|------|------|------|
| 뉴스 수집 | 웹 검색 (`search_web`) | 뉴스 데이터 |
| HTML 생성 | `template/base_template.html` | `daily/daily_YYYY-MM-DD.html` |
| 레지스트리 등록 | - | `daily.json`에 항목 추가 |
| 배포 | git commit & push | GitHub Pages 반영 |

---

## 2. 사전 준비

### 2.1 Jenkins 서버 요구사항

| 항목 | 설명 | 확인 방법 |
|------|------|-----------|
| **agy 설치** | Antigravity CLI가 설치되어 있어야 함 | `agy --help` |
| **Git** | Git CLI 설치 및 인증 설정 | `git --version` |
| **SSH Key** | GitHub에 push 가능한 SSH key 등록 | `ssh -T git@github.com` |
| **LLM API Key** | agy가 사용하는 API key | Jenkins Credentials로 관리 |

### 2.2 agy 설치

```bash
# 설치 (최초 1회)
# 공식 설치 방법에 따라 설치

# 설치 확인
agy --help

# 환경 설정
agy install
```

### 2.3 Git 설정

```bash
# Jenkins agent에서 Git 사용자 정보 설정
git config --global user.name "Jenkins Bot"
git config --global user.email "jenkins@your-domain.com"

# SSH key 등록 확인
ssh -T git@github.com
# "Hi royalahn! You've successfully authenticated" 메시지 확인
```

### 2.4 API Key 설정

Jenkins에서 **Manage Jenkins → Credentials**에 LLM API Key를 등록합니다.

- **Kind**: Secret text
- **ID**: `GEMINI_API_KEY` (또는 사용하는 LLM 서비스에 맞게)
- **Secret**: API key 값

---

## 3. agy CLI Non-Interactive 모드

### 3.1 주요 플래그

```
Usage of agy:
  -p, --print                       non-interactive 모드로 실행 후 결과 출력
  --prompt                          --print의 alias
  --print-timeout                   타임아웃 설정 (기본값: 5m0s)
  --dangerously-skip-permissions    모든 권한 요청을 자동 승인
  --add-dir                         작업 디렉토리 추가
  -c, --continue                    가장 최근 대화 이어가기
```

### 3.2 기본 사용법

```bash
# 단순 프롬프트 실행
agy -p "한국 주식시장 오늘 주요 뉴스를 알려줘"

# 타임아웃 + 권한 자동 승인 (자동화 용도)
agy -p \
    --dangerously-skip-permissions \
    --print-timeout 15m0s \
    "프롬프트 내용"
```

### 3.3 자동화에서 필수 플래그

| 플래그 | 필수 여부 | 이유 |
|--------|----------|------|
| `-p` (또는 `--print`) | **필수** | 대화형이 아닌 단발성 실행 |
| `--dangerously-skip-permissions` | **필수** | 파일 생성, git 명령 등의 권한 요청을 자동 승인 |
| `--print-timeout` | **권장** | 심층 리포트 생성 시 기본 5분으로 부족할 수 있음. 10~15분 권장 |

> ⚠️ **주의**: `--dangerously-skip-permissions`는 모든 파일 I/O와 명령 실행을 자동 승인합니다. 프롬프트가 의도한 작업만 수행하도록 신중하게 설계해야 합니다.

---

## 4. 프롬프트 설계

### 4.1 프롬프트 전문

아래는 Jenkins에서 agy에 전달하는 전체 프롬프트입니다. Shell 변수 `${TODAY}`가 실행 시 자동 치환됩니다.

```text
오늘은 ${TODAY}이야. 한국과 미국 주식시장의 투자 인사이트 일일 리포트를 작성해줘.

## 수집 단계
다음 주제에 대해 웹에서 최신 뉴스와 데이터를 검색해줘:
1. 한국 시장: KOSPI, KOSDAQ 지수 동향, 주요 업종별 흐름, 외국인/기관 수급
2. 미국 시장: S&P500, NASDAQ, 다우존스 동향, 주요 빅테크 및 섹터 흐름
3. 매크로: 한미 금리 동향, 환율(USD/KRW), 유가, 주요 경제지표 발표
4. 이슈 종목: 급등/급락 종목과 그 배경

## 리포트 작성 규칙
- template/base_template.html을 복사하여 daily/daily_${TODAY}.html 로 생성
- Header 아이콘은 차트 관련 SVG, 타이틀은 "Daily Insight — ${TODAY}"
- <main> 영역에 아래 구조로 심층 리포트 작성:

### 리포트 구조
1. **한눈에 보기 (Executive Summary)**
   - 오늘의 핵심 3줄 요약 카드
   - 주요 지수 변동 테이블 (KOSPI, KOSDAQ, S&P500, NASDAQ, USD/KRW)

2. **한국 시장 분석**
   - 시장 개요 및 지수 동향
   - 업종별 흐름 (반도체, 바이오, 2차전지, 금융 등)
   - 주요 종목 하이라이트 (상승/하락 Top 종목)
   - 외국인/기관 수급 동향

3. **미국 시장 분석**
   - 시장 개요 및 지수 동향
   - 빅테크 동향 (AAPL, MSFT, NVDA, TSLA 등)
   - 주요 섹터 흐름
   - 실적 발표/이벤트 이슈

4. **매크로 & 글로벌 이슈**
   - 금리/통화정책 동향
   - 환율 및 원자재 동향
   - 주요 경제지표 리뷰

5. **투자 시사점 & 전략 제안**
   - 단기 주목할 섹터/테마
   - 리스크 요인 점검
   - 내일 주요 일정 미리보기

- 수치 데이터는 반드시 표(Table)로 정리
- 강조 포인트는 feature-card 스타일의 카드 UI 활용
- Tailwind CSS 클래스만 사용, 인라인 스타일 금지

## 등록 및 배포
- daily.json에 새 문서 등록 (category: "시장동향", date: "${TODAY}")
- 완료 후 다음 명령어 실행:
  git add -A
  git commit -m "docs: 일일 투자 인사이트 (${TODAY})"
  git push origin main
```

### 4.2 프롬프트 설계 핵심 원칙

| 원칙 | 설명 |
|------|------|
| **명확한 단계 구분** | 수집 → 작성 → 등록 → 배포 순서를 명시 |
| **구체적인 파일 경로** | `template/base_template.html`, `daily/daily_${TODAY}.html` 등 정확히 지정 |
| **디자인 규칙 명시** | Tailwind CSS, 카드 UI, 표 등 출력 형식을 구체화 |
| **git 명령어 포함** | commit 메시지 형식까지 프롬프트에 지정하여 일관성 유지 |

---

## 5. Jenkins Job 구성

### 5.1 Freestyle Job 생성

1. **Jenkins Dashboard** → **New Item** 클릭
2. **Item name**: `daily-invest-insight`
3. **Freestyle project** 선택 → **OK**

### 5.2 General 설정

- **Description**: `매일 오전 8시에 한국/미국 투자 인사이트 리포트를 자동 생성하고 GitHub Pages에 배포`

### 5.3 Build Triggers

**Build periodically** 체크 후 Cron 입력:

```
# 매일 오전 8시 (KST)
TZ=Asia/Seoul
0 8 * * *
```

> 💡 주말/공휴일 제외하려면:
> ```
> # 월~금만 실행
> TZ=Asia/Seoul
> 0 8 * * 1-5
> ```

### 5.4 Build Environment

- **Use secret text(s) or file(s)** 체크
  - **Secret text** 추가: Variable = `GEMINI_API_KEY`, Credentials = (등록한 API key)

### 5.5 Build Step (Execute Shell)

```bash
#!/bin/bash
set -e

# ── 환경 설정 ──
REPO_URL="git@github.com:royalahn/invest.git"
REPO_DIR="${WORKSPACE}/invest"
TODAY=$(date +%Y-%m-%d)
FILENAME="daily_${TODAY}.html"

echo "=========================================="
echo "📊 일일 투자 인사이트 생성 시작"
echo "📅 날짜: ${TODAY}"
echo "=========================================="

# ── Step 1: 저장소 준비 ──
echo "📥 저장소 준비 중..."
if [ -d "$REPO_DIR/.git" ]; then
    cd "$REPO_DIR"
    git fetch origin
    git reset --hard origin/main
    git clean -fd
else
    git clone "$REPO_URL" "$REPO_DIR"
    cd "$REPO_DIR"
fi

# ── Step 2: 중복 실행 방지 ──
if [ -f "daily/${FILENAME}" ]; then
    echo "⚠️ daily/${FILENAME} 이미 존재합니다. 스킵합니다."
    exit 0
fi

# ── Step 3: agy 실행 ──
echo "🤖 agy 실행 중... (타임아웃: 15분)"
agy -p \
    --dangerously-skip-permissions \
    --print-timeout 15m0s \
    "$(cat <<PROMPT
오늘은 ${TODAY}이야. 한국과 미국 주식시장의 투자 인사이트 일일 리포트를 작성해줘.

## 수집 단계
다음 주제에 대해 웹에서 최신 뉴스와 데이터를 검색해줘:
1. 한국 시장: KOSPI, KOSDAQ 지수 동향, 주요 업종별 흐름, 외국인/기관 수급
2. 미국 시장: S&P500, NASDAQ, 다우존스 동향, 주요 빅테크 및 섹터 흐름
3. 매크로: 한미 금리 동향, 환율(USD/KRW), 유가, 주요 경제지표 발표
4. 이슈 종목: 급등/급락 종목과 그 배경

## 리포트 작성 규칙
- template/base_template.html을 복사하여 daily/daily_${TODAY}.html 로 생성
- Header 아이콘은 차트 관련 SVG, 타이틀은 "Daily Insight — ${TODAY}"
- <main> 영역에 심층 리포트를 작성

### 리포트 구조
1. 한눈에 보기 (핵심 3줄 요약 + 주요 지수 테이블)
2. 한국 시장 분석 (지수, 업종, 종목 하이라이트, 수급)
3. 미국 시장 분석 (지수, 빅테크, 섹터, 실적 이벤트)
4. 매크로 & 글로벌 이슈 (금리, 환율, 원자재)
5. 투자 시사점 & 전략 제안 (주목 섹터, 리스크, 내일 일정)

- 수치 데이터는 표(Table), 강조는 카드 UI 활용
- Tailwind CSS 클래스만 사용, 인라인 스타일 금지

## 등록 및 배포
- daily.json에 새 문서 등록 (category: "시장동향", date: "${TODAY}")
- 완료 후:
  git add -A
  git commit -m "docs: 일일 투자 인사이트 (${TODAY})"
  git push origin main
PROMPT
)"

# ── Step 4: 결과 확인 ──
if [ -f "daily/${FILENAME}" ]; then
    echo "✅ 리포트 생성 완료: daily/${FILENAME}"
else
    echo "❌ 리포트 파일이 생성되지 않았습니다."
    exit 1
fi

echo "=========================================="
echo "🎉 일일 투자 인사이트 파이프라인 완료"
echo "=========================================="
```

### 5.6 Post-build Actions (선택)

필요에 따라 알림을 추가합니다:

- **Slack Notification**: 성공/실패 시 채널에 알림
- **Email Notification**: 실패 시 이메일 발송

---

## 6. Git 자동화 (Commit & Push)

### 6.1 커밋 컨벤션

```
docs: 일일 투자 인사이트 (YYYY-MM-DD)
```

- prefix `docs:` — 문서 추가를 의미
- 날짜를 포함하여 커밋 히스토리에서 즉시 식별 가능

### 6.2 자동 커밋되는 파일

| 파일 | 설명 |
|------|------|
| `daily/daily_YYYY-MM-DD.html` | 생성된 일일 리포트 |
| `daily.json` | 리포트 메타데이터 등록 |

### 6.3 GitHub Pages 배포

커밋이 `main` 브랜치에 push되면 GitHub Pages가 자동으로 재배포됩니다.

- **Settings → Pages → Source**: `Deploy from a branch`
- **Branch**: `main` / `/ (root)`

---

## 7. 실행 흐름 요약

```
1. Jenkins Cron 트리거 (매일 08:00 KST)
        │
2. Shell 스크립트 시작
        │
3. Git 저장소 clone/pull
        │
4. 중복 체크 (오늘 파일 이미 존재?)
        │   ├─ YES → 스킵, 정상 종료
        │   └─ NO  → 계속 진행
        │
5. agy -p 실행 (non-interactive)
        │   ├─ 웹 검색으로 뉴스 수집
        │   ├─ base_template.html 복사
        │   ├─ daily/daily_YYYY-MM-DD.html 생성
        │   ├─ daily.json 업데이트
        │   ├─ git add -A
        │   ├─ git commit
        │   └─ git push
        │
6. 결과 파일 존재 확인
        │   ├─ 존재 → ✅ 성공
        │   └─ 미존재 → ❌ 실패 (exit 1)
        │
7. (선택) 알림 발송 (Slack/Email)
```

---

## 8. 트러블슈팅

### agy 명령어를 찾을 수 없음

```
bash: agy: command not found
```

**해결**: agy 설치 경로를 확인하고 Jenkins의 `PATH`에 추가합니다.

```bash
# agy 위치 확인
which agy

# Jenkins Shell 스크립트 상단에 PATH 추가
export PATH="/usr/local/bin:$PATH"
```

### API Key 인증 실패

```
Error: API key not found or invalid
```

**해결**: Jenkins Credentials에 API Key가 올바르게 등록되었는지 확인하고, Build Environment에서 바인딩 설정을 점검합니다.

### Git Push 권한 오류

```
Permission denied (publickey)
```

**해결**: Jenkins agent의 SSH key가 GitHub에 등록되어 있는지 확인합니다.

```bash
# Jenkins agent에서 SSH 테스트
ssh -T git@github.com
```

### 타임아웃 초과

```
Error: print mode timed out
```

**해결**: `--print-timeout` 값을 늘립니다. 심층 리포트는 15~20분 정도 소요될 수 있습니다.

```bash
agy -p --print-timeout 20m0s ...
```

### 중복 실행 시 충돌

Jenkins가 동일 날짜에 두 번 실행될 경우, 스크립트의 중복 체크 로직이 자동으로 스킵합니다.

```bash
if [ -f "daily/${FILENAME}" ]; then
    echo "⚠️ 이미 존재합니다. 스킵합니다."
    exit 0
fi
```

---

## 부록: 관련 파일 경로

| 파일 | 경로 | 용도 |
|------|------|------|
| Base Template | `template/base_template.html` | HTML 문서 기본 골격 |
| Design Guide | `template/html_design_guide.md` | 디자인 시스템 레퍼런스 |
| 인사이트 레지스트리 | `pages.json` | 수동 인사이트 문서 메타데이터 |
| 일일 리포트 레지스트리 | `daily.json` | 자동 일일 리포트 메타데이터 |
| AI 가이드라인 | `AGENTS.md` | AI 코딩 어시스턴트 규칙 |
