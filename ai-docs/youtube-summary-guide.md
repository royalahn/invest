# YouTube 요약 및 자동 문서화 프롬프트 가이드

이 문서는 유튜브 영상 링크로부터 전체 자막(스크립트)을 추출하고, Antigravity CLI(`agy`)의 `non-interactive` 모드를 사용하여 상세 리포트를 자동으로 작성하는 파이프라인에 대해 설명합니다.

## 개요
유튜브 링크만을 활용해 수동으로 `agy`에게 컨텍스트를 주려면 자막을 직접 가져오는 등의 번거로움이 있습니다. 이를 자동화하기 위해 파이썬 기반의 자막 추출 기능과 `agy` 프롬프트를 쉘 스크립트로 하나로 결합했습니다.

## 실행 방법 (자동화 스크립트)

`ai-docs/youtube_report_automation.sh` 스크립트를 통해 원클릭으로 진행할 수 있습니다.

```bash
# 사용법
cd /Users/hyogeun.ahn/Workspace/GitHub/invest
./ai-docs/youtube_report_automation.sh "https://www.youtube.com/watch?v=..."
```

### 작동 원리 (Pipeline)
1. **자막 추출:** 입력된 유튜브 링크에서 Video ID를 파싱하고 `youtube-transcript-api`(Python)를 사용해 자막을 텍스트로 추출합니다.
2. **프롬프트 생성:** 추출된 스크립트를 Bash의 `Here-Document(<<PROMPT)` 기능을 활용해 프롬프트 안으로 통째로 주입합니다.
3. **AI 리포트 작성 (`agy -p`):** `agy` 에이전트가 부여된 프롬프트를 바탕으로 다음을 수행합니다.
   - HTML 리포트를 `ai-html/` 폴더에 Base 템플릿 기반으로 작성합니다.
   - `pages.json`을 수정하여 생성된 문서를 등록합니다.
   - `git commit`을 진행하여 문서화를 완료합니다.

---

## 핵심 프롬프트 구조 (Prompt Architecture)

`agy`에게 전달되는 실제 프롬프트의 기본 구조는 다음과 같습니다. 만약 스크립트를 거치지 않고 직접 프롬프트를 작성하고 싶다면 아래 내용을 참고하세요.

```text
오늘은 ${TODAY}이야. 다음은 유튜브 영상의 전체 자막(스크립트) 데이터야.
이 내용을 깊이 있게 분석해서, 투자 인사이트 리포트를 작성해줘.

[리포트 작성 필수 가이드라인]
1. 문서 구조:
   - 영상의 핵심 주제 요약 (3줄 요약)
   - 영상에서 제시하는 주요 논거 및 시장 동향 분석
   - 이 영상이 투자자에게 주는 시사점 및 투자 전략
2. HTML 디자인 및 규칙:
   - \`template/base_template.html\`을 Base로 복사하여 사용할 것.
   - \`<main>\` 태그 내부에 Tailwind CSS(Modern Startup / SaaS 스타일)를 적용하여 가독성을 극대화할 것.
   - 긴 텍스트의 나열을 피하고 카드 UI, 목록(List), 인용구 등을 적극 활용할 것.
3. 파일 저장 및 등록:
   - 생성된 파일은 \`ai-html/youtube_report_\$(date +%Y%m%d%H%M%S).html\` 로 저장할 것. (이름은 내용에 맞게 변경 가능)
   - 반드시 프로젝트 루트의 \`pages.json\`에 새로운 페이지 정보를 추가할 것 (카테고리는 내용에 맞게 '매크로', '투자전략', '종목분석' 등 적용).
4. 마무리:
   - Conventional Commits 규격(예: feat: 유튜브 인사이트 리포트 추가)에 따라 git commit 까지 수행할 것.

[유튜브 영상 스크립트 전문]
(여기에 유튜브 자막 텍스트 전체가 삽입됩니다)
```

## 필수 의존성
- `python3`
- `youtube-transcript-api` (스크립트 실행 시 없으면 자동 설치됩니다: `pip install youtube-transcript-api`)
