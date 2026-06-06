#!/bin/bash

# YouTube 동영상 요약 리포트 자동화 스크립트
# 사용법: ./youtube_report_automation.sh "유튜브링크"

if [ -z "$1" ]; then
  echo "사용법: $0 <유튜브_링크>"
  exit 1
fi

YOUTUBE_URL="$1"
TODAY=$(date +"%Y-%m-%d")

# 필요한 파이썬 패키지 확인 및 설치
if ! python3 -c "import youtube_transcript_api" &> /dev/null; then
    echo "youtube-transcript-api 패키지가 필요합니다. 설치를 진행합니다..."
    pip3 install youtube-transcript-api
fi

echo "유튜브 자막(스크립트)을 추출하는 중입니다..."

# 파이썬 코드를 통해 자막 추출 (한국어/영어 우선)
TRANSCRIPT=$(python3 -c "
import sys
from youtube_transcript_api import YouTubeTranscriptApi

url = sys.argv[1]
# 비디오 ID 추출 로직
video_id = url.split('v=')[-1].split('&')[0]
if 'youtu.be/' in url:
    video_id = url.split('youtu.be/')[-1].split('?')[0]

try:
    ytt_api = YouTubeTranscriptApi()
    transcript_list = ytt_api.list(video_id)
    transcript = transcript_list.find_transcript(['ko', 'en'])
    fetched_data = transcript.fetch()
    text = ' '.join([t.text for t in fetched_data])
    print(text)
except Exception as e:
    print(f'자막을 가져올 수 없습니다: {e}', file=sys.stderr)
    sys.exit(1)
" "$YOUTUBE_URL")

if [ $? -ne 0 ]; then
  echo "자막 추출 실패. 스크립트를 종료합니다."
  exit 1
fi

echo "자막 추출 성공! 자막 길이: ${#TRANSCRIPT} 글자"
echo "Antigravity CLI(agy)를 통해 리포트 작성을 시작합니다..."

# agy non-interactive 모드로 프롬프트 전달
agy -p "$(cat <<PROMPT
오늘은 ${TODAY}이야. 다음은 유튜브 영상의 전체 자막(스크립트) 데이터야.
이 내용을 깊이 있게 분석해서, 투자 인사이트 리포트를 작성해줘.

[리포트 작성 필수 가이드라인]
1. 문서 구조:
   - 영상의 **핵심 주제 요약** (3줄 요약)
   - 영상에서 제시하는 **주요 논거 및 시장 동향 분석**
   - 이 영상이 투자자에게 주는 **시사점 및 투자 전략**
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
${TRANSCRIPT}
PROMPT
)"

echo "작업이 완료되었습니다!"
