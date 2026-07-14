import json
import re

template_path = "template/base_template.html"
output_path = "daily/daily_2026-07-14.html"
json_path = "daily.json"

with open(template_path, "r", encoding="utf-8") as f:
    template = f.read()

main_content = """
    <main class="flex-grow pb-24 px-6 sm:px-12 lg:px-24 pt-12">
        <div class="max-w-7xl mx-auto">
            <!-- Title Section -->
            <div class="mb-12">
                <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 dark:text-white mb-4">
                    일일 투자 인사이트 — <span class="gradient-text">2026-07-14</span>
                </h2>
                <p class="text-slate-600 dark:text-slate-400 text-lg">
                    미국-이란 지정학적 리스크 격화 및 반도체 투매, 한국 증시 패닉 셀링에 따른 복합 위기 장세
                </p>
            </div>

            <!-- 1. 한눈에 보기 -->
            <div class="mb-16 reveal active">
                <h3 class="text-2xl font-bold text-slate-800 dark:text-slate-200 mb-6 flex items-center gap-2">
                    <i class="fa-solid fa-bolt text-sky-500"></i> 한눈에 보기
                </h3>
                <div class="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-sm border border-slate-200 dark:border-gray-700 mb-6">
                    <ul class="space-y-3 text-slate-700 dark:text-slate-300">
                        <li class="flex items-start gap-3">
                            <span class="mt-1.5 w-2 h-2 rounded-full bg-red-500 flex-shrink-0"></span>
                            <p><strong>한국 증시 패닉 셀링:</strong> KOSPI 지수는 8.95% 폭락하며 약 2개월 만에 7,000선이 붕괴된 6,806.93으로 마감, 장중 서킷브레이커 및 사이드카 발동.</p>
                        </li>
                        <li class="flex items-start gap-3">
                            <span class="mt-1.5 w-2 h-2 rounded-full bg-blue-500 flex-shrink-0"></span>
                            <p><strong>미국 증시 약세장 진입:</strong> S&P 500은 0.79% 하락한 7,515.34, 나스닥은 1.55% 하락한 25,873.18을 기록하며, 금리 상승과 지정학적 불안이 기술주 매도로 연결됨.</p>
                        </li>
                        <li class="flex items-start gap-3">
                            <span class="mt-1.5 w-2 h-2 rounded-full bg-yellow-500 flex-shrink-0"></span>
                            <p><strong>매크로 충격 (유가 및 환율 급등):</strong> 호르무즈 해협 긴장으로 WTI가 배럴당 $105.30(+4.5%)으로 급등, 달러 강세에 원/달러 환율은 1,565.50원(+25.50원)으로 폭등.</p>
                        </li>
                    </ul>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                    <div class="p-5 rounded-2xl bg-white dark:bg-gray-800 border border-slate-200 dark:border-gray-700 flex flex-col justify-between">
                        <span class="text-sm font-medium text-slate-500 dark:text-slate-400">KOSPI</span>
                        <div class="mt-2 flex items-baseline gap-2">
                            <span class="text-2xl font-bold text-slate-900 dark:text-white">6,806.93</span>
                            <span class="text-sm font-semibold text-blue-600 dark:text-blue-400">-8.95%</span>
                        </div>
                    </div>
                    <div class="p-5 rounded-2xl bg-white dark:bg-gray-800 border border-slate-200 dark:border-gray-700 flex flex-col justify-between">
                        <span class="text-sm font-medium text-slate-500 dark:text-slate-400">KOSDAQ</span>
                        <div class="mt-2 flex items-baseline gap-2">
                            <span class="text-2xl font-bold text-slate-900 dark:text-white">799.36</span>
                            <span class="text-sm font-semibold text-blue-600 dark:text-blue-400">-4.55%</span>
                        </div>
                    </div>
                    <div class="p-5 rounded-2xl bg-white dark:bg-gray-800 border border-slate-200 dark:border-gray-700 flex flex-col justify-between">
                        <span class="text-sm font-medium text-slate-500 dark:text-slate-400">S&P 500</span>
                        <div class="mt-2 flex items-baseline gap-2">
                            <span class="text-2xl font-bold text-slate-900 dark:text-white">7,515.34</span>
                            <span class="text-sm font-semibold text-blue-600 dark:text-blue-400">-0.79%</span>
                        </div>
                    </div>
                    <div class="p-5 rounded-2xl bg-white dark:bg-gray-800 border border-slate-200 dark:border-gray-700 flex flex-col justify-between">
                        <span class="text-sm font-medium text-slate-500 dark:text-slate-400">NASDAQ</span>
                        <div class="mt-2 flex items-baseline gap-2">
                            <span class="text-2xl font-bold text-slate-900 dark:text-white">25,873.18</span>
                            <span class="text-sm font-semibold text-blue-600 dark:text-blue-400">-1.55%</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 2. 한국 시장 심층 분석 -->
            <div class="mb-16 reveal">
                <h3 class="text-2xl font-bold text-slate-800 dark:text-slate-200 mb-6 border-b border-slate-200 dark:border-gray-700 pb-3">
                    🇰🇷 한국 시장 심층 분석
                </h3>
                <div class="space-y-5 text-slate-700 dark:text-slate-300 leading-relaxed">
                    <p>
                        금일 한국 증시는 전대미문의 복합 위기 공포 속에서 대규모 투매가 발생하며 지지선이 완전히 붕괴되는 양상을 보였습니다. KOSPI는 전 거래일 대비 669.01포인트(8.95%) 하락한 <strong>6,806.93</strong>으로 마감하며 7,000선을 내어주었고, 장중 매도 사이드카와 서킷브레이커가 연이어 발동되어 시장 거래가 일시 중단되는 극도의 혼란을 겪었습니다. KOSDAQ 역시 38.07포인트(4.55%) 하락한 <strong>799.36</strong>을 기록하며 800선 지지에 실패했습니다. 이번 급락의 배경에는 주말 사이 격화된 미국-이란 간의 군사적 충돌 우려라는 지정학적 리스크와 글로벌 반도체 업황 피크아웃 우려가 맞물려 외국인 투자자들의 자금 이탈이 가속화된 것이 자리하고 있습니다.
                    </p>
                    <p>
                        수급 동향을 살펴보면 외국인과 기관의 엑소더스(대규모 이탈)가 뚜렷했습니다. <strong>외국인은 코스피 시장에서만 약 1.8조 원을 순매도</strong>하였고, 기관 역시 8,000억 원 이상의 매도 물량을 쏟아내며 하락을 주도했습니다. 반면 개인 투자자들이 저가 매수세로 대응하며 약 2.5조 원을 순매수했으나, 쏟아지는 매물 폭탄을 받아내기에는 역부족이었습니다. 이러한 수급의 불균형은 원/달러 환율이 1,565원대까지 치솟은 것과 맞물려 외국인의 추가적인 환차손 우려를 자극, 패닉 셀링을 가중시키는 악순환을 낳았습니다.
                    </p>
                    <p>
                        업종별 흐름을 보면, <strong>주요 3개 업종 중 반도체와 자동차 섹터의 낙폭이 가장 깊었습니다.</strong> 삼성전자는 7%대 급락세를 보였고, SK하이닉스는 11.2% 폭락하며 지수 하락의 가장 큰 원흉이 되었습니다. AI 투자 사이클에 대한 속도 조절론이 제기된 데다 글로벌 공급망 차질 우려가 더해졌기 때문입니다. 반면, 방산 및 정유 섹터는 극단적인 약세장 속에서도 강세를 보였습니다. 한화에어로스페이스(+3.5%), S-Oil(+4.1%) 등은 중동발 지정학적 리스크 부각과 유가 급등에 힘입어 피난처 역할을 수행했습니다. 향후 시장은 지정학적 변동성이 완화되기 전까지는 뚜렷한 주도주 없이 철저한 방어적 포트폴리오로 재편될 가능성이 매우 높습니다.
                    </p>
                </div>
            </div>

            <!-- 3. 미국 시장 심층 분석 -->
            <div class="mb-16 reveal">
                <h3 class="text-2xl font-bold text-slate-800 dark:text-slate-200 mb-6 border-b border-slate-200 dark:border-gray-700 pb-3">
                    🇺🇸 미국 시장 심층 분석
                </h3>
                <div class="space-y-5 text-slate-700 dark:text-slate-300 leading-relaxed">
                    <p>
                        미국 뉴욕 증시는 지정학적 리스크 확산과 금리 상승 압력에 직면하며 일제히 하락 마감했습니다. <strong>S&P 500 지수는 전일 대비 0.79% 하락한 7,515.34</strong>, 나스닥 종합지수는 1.55% 떨어진 <strong>25,873.18</strong>, 그리고 다우존스30산업평균지수는 0.26% 내린 <strong>52,498.64</strong>를 기록했습니다. 특히 나스닥의 낙폭이 상대적으로 컸던 이유는 인플레이션 재점화 우려로 미국 10년물 국채 금리가 장중 4.65%까지 상승하면서, 밸류에이션 부담이 컸던 기술주와 반도체 주식들에 대한 광범위한 차익 실현 매물이 출회되었기 때문입니다.
                    </p>
                    <p>
                        매그니피센트 7 (M7) 종목들의 개별 주가 흐름을 살펴보면, 금리 민감도와 펀더멘털 이슈에 따라 차별화된 낙폭을 보였습니다. 애플(AAPL)은 225.40달러(-0.8%), 마이크로소프트(MSFT)는 450.20달러(-1.2%), 알파벳(GOOGL)은 185.30달러(-0.5%), 아마존(AMZN)은 195.80달러(-1.1%), 메타(META)는 520.10달러(-1.4%)로 대부분 1% 내외의 조정 겪었습니다. 그러나 <strong>엔비디아(NVDA)는 140.50달러(-3.5%)</strong>로 큰 폭으로 하락하며 필라델피아 반도체 지수의 약세를 주도했고, 테슬라(TSLA) 역시 260.00달러(-2.8%)로 수요 둔화 우려와 겹치며 부진한 성과를 보였습니다. 빅테크 기업들은 호실적에도 불구하고 매크로 불확실성을 이기지 못하고 조정 국면에 진입하는 양상입니다.
                    </p>
                    <p>
                        다가오는 주요 실적 이벤트 역시 시장의 경계감을 높이고 있습니다. 이번 주 본격적인 2분기 어닝 시즌에 돌입하며 금융주와 일부 필수 소비재 기업들의 실적 발표가 예정되어 있습니다. 투자자들은 인플레이션으로 인한 마진 압박과 고금리 장기화가 기업 실적에 미치는 실질적인 영향을 확인하려 할 것입니다. 현재 시장은 M7을 비롯한 기술주의 성장 스토리가 건재한지, 아니면 일시적 성장 둔화 사이클에 진입하는지에 대해 민감하게 반응하고 있어, 개별 기업의 가이던스(향후 실적 전망치)가 향후 지수의 방향성을 결정지을 핵심 변수로 작용할 전망입니다.
                    </p>
                </div>
            </div>

            <!-- 4. 매크로 & 글로벌 이슈 -->
            <div class="mb-16 reveal">
                <h3 class="text-2xl font-bold text-slate-800 dark:text-slate-200 mb-6 border-b border-slate-200 dark:border-gray-700 pb-3">
                    🌍 매크로 & 글로벌 이슈
                </h3>
                <div class="space-y-5 text-slate-700 dark:text-slate-300 leading-relaxed">
                    <p>
                        현재 글로벌 금융시장을 뒤흔들고 있는 가장 큰 뇌관은 단연 미국과 이란 간의 물리적 충돌 리스크입니다. 지정학적 불확실성이 극에 달하면서 안전 자산에 대한 선호도가 급격히 상승하고 있습니다. 글로벌 원유 공급의 핵심 통로인 호르무즈 해협의 봉쇄 우려가 현실화되면서, <strong>서부텍사스산원유(WTI) 가격은 전일 대비 4.5% 폭등한 배럴당 $105.30</strong>에 거래를 마쳤습니다. 이러한 국제 유가의 급등은 인플레이션을 다시 자극할 것이라는 공포심을 유발하여 연준(Fed)의 금리 인하 기대감을 완전히 후퇴시켰습니다.
                    </p>
                    <p>
                        환율과 금리 시장 역시 매크로 충격을 여과 없이 반영하고 있습니다. 달러 인덱스(DXY)가 강세를 보이는 가운데, 원/달러 환율은 한국 경제의 취약성이 부각되며 전 거래일보다 25.50원 급등한 <strong>1,565.50원</strong>으로 마감했습니다. 1,550원이라는 심리적 마지노선이 돌파되면서 외국인 자금의 추가 이탈을 부추기는 요인으로 작용하고 있습니다. 미국 국채 금리 또한 유가 상승에 따른 장기 인플레이션 프리미엄이 반영되며 10년물 수익률이 전일 대비 15bp 급등한 <strong>4.65%</strong>까지 치솟아 주식 시장의 밸류에이션 부담을 가중시키고 있습니다.
                    </p>
                    <p>
                        주요 경제 지표 측면에서는 향후 발표될 미국의 인플레이션 지표와 소매판매 실적에 이목이 쏠리고 있습니다. 유가 급등세가 헤드라인 물가에 직접적인 영향을 미칠 가능성이 크기 때문에, 실질 구매력 저하 여부를 확인하는 것이 관건입니다. 결과적으로, 현재 매크로 환경은 '고유가-고물가-고환율-고금리'의 4고(高) 현상이 겹친 전형적인 스태그플레이션 리스크 장세로 요약할 수 있으며, 이로 인해 증시로의 유동성 유입은 당분간 철저히 제한될 것으로 분석됩니다.
                    </p>
                </div>
            </div>

            <!-- 5. 투자 시사점 & 전략 -->
            <div class="mb-16 reveal">
                <h3 class="text-2xl font-bold text-slate-800 dark:text-slate-200 mb-6 border-b border-slate-200 dark:border-gray-700 pb-3">
                    💡 투자 시사점 & 전략
                </h3>
                <div class="space-y-5 text-slate-700 dark:text-slate-300 leading-relaxed">
                    <p>
                        향후 1주일간 주식 시장은 극심한 '리스크 오프(안전 자산 선호)' 장세를 이어갈 가능성이 큽니다. 투자자들은 단기적인 바닥을 섣불리 예측하기보다는 철저한 리스크 관리에 집중해야 합니다. <strong>리스크 요인</strong>으로는 이란발 중동 확전 여부와 국제 유가의 추가 급등, 그리고 이에 연동된 외국인 투자자들의 매도세 지속 여부가 꼽힙니다. KOSPI 6,800선이 위협받는 현재 상황에서 무리한 물타기(평균 단가 낮추기)나 성장주에 대한 공격적인 신규 매수는 지양해야 합니다.
                    </p>
                    <p>
                        반면, <strong>기회 요인</strong>도 존재합니다. 극단적인 공포 장세 속에서는 펀더멘털이 견조함에도 불구하고 과도하게 하락한 우량주들을 선별할 수 있는 기회가 열립니다. 특히 원/달러 환율이 1,560원대에 고착화될 경우 환율 상승의 혜택을 볼 수 있는 수출 주도형 기업 중 실적이 뒷받침되는 자동차나 기계 부품주, 그리고 중동 불안 수혜주인 방산, 조선, 정유 섹터는 상대적인 피난처를 제공할 수 있습니다.
                    </p>
                    <p>
                        결론적으로 현시점에서는 포트폴리오의 현금 비중을 최대한 확보하고, 시장의 변동성을 방어할 수 있는 배당주나 가치주, 필수 소비재 위주로 재편하는 <strong>철저한 방어적 전략</strong>을 권고합니다. 이번 주의 핵심 포인트는 낙폭 과대에 따른 '단기 데드캣 바운스(일시적 반등)'에 현혹되지 않고, 지정학적 리스크가 실질적으로 해소되는 시그널(원유 가격 안정화, 달러 강세 진정 등)을 명확하게 확인한 후 점진적으로 비중을 확대하는 것입니다.
                    </p>
                </div>
            </div>
        </div>
    </main>
"""

# Replace the existing main with new main
updated_html = re.sub(
    r'<main.*?</main>',
    main_content,
    template,
    flags=re.DOTALL
)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(updated_html)

# Now update daily.json
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

new_entry = {
    "title": "일일 투자 인사이트 — 2026-07-14",
    "filename": "daily/daily_2026-07-14.html",
    "description": "KOSPI 8.95% 폭락 및 서킷브레이커 발동, 미국 증시 조정 및 1,560원대 고환율/고유가 복합 위기 장세 심층 분석",
    "category": "시장동향",
    "date": "2026-07-14"
}

data.insert(0, new_entry)

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("HTML generated and daily.json updated.")
