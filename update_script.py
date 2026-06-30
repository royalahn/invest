import json

# 1. Update daily.json
with open('daily.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_entry = {
    "title": "일일 투자 인사이트 — 2026-06-30",
    "filename": "daily/daily_2026-06-30.html",
    "description": "KOSPI 8,390선 약보합 및 코스닥 920선 급등, 미국 증시 스페이스X 상장 모멘텀 및 1,540원대 초고환율 장세 분석",
    "category": "시장동향",
    "date": "2026-06-30"
}

data.insert(0, new_entry)

with open('daily.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 2. Create daily/daily_2026-06-30.html
with open('template/base_template.html', 'r', encoding='utf-8') as f:
    template_content = f.read()

main_content = """
    <!-- Main Section -->
    <main class="flex-grow pb-24 px-6 sm:px-12 lg:px-24 pt-12">
        <div class="max-w-7xl mx-auto space-y-12">
            
            <!-- Title Section -->
            <div class="text-center py-12">
                <h2 class="text-4xl md:text-5xl font-extrabold text-slate-900 dark:text-white mb-6">
                    일일 투자 <span class="gradient-text">인사이트</span>
                </h2>
                <p class="text-lg text-slate-600 dark:text-slate-400">2026년 6월 30일 (화) 시장 동향 심층 분석 리포트</p>
            </div>

            <!-- 1. 한눈에 보기 -->
            <section class="reveal bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-slate-200 dark:border-gray-700 p-8">
                <h3 class="text-2xl font-bold mb-6 flex items-center gap-2"><i class="fa-solid fa-bolt text-sky-500"></i> 한눈에 보기</h3>
                
                <div class="grid md:grid-cols-2 gap-8">
                    <div class="space-y-4">
                        <div class="p-4 rounded-xl bg-slate-50 dark:bg-gray-900 border-l-4 border-sky-500">
                            <p class="font-medium text-slate-800 dark:text-slate-200">📌 한국: KOSPI는 외국인의 1조 원대 매도 폭탄으로 8,390선 약보합, KOSDAQ은 기관 매수세에 8.13%(920.57) 폭등하며 디커플링 심화.</p>
                        </div>
                        <div class="p-4 rounded-xl bg-slate-50 dark:bg-gray-900 border-l-4 border-indigo-500">
                            <p class="font-medium text-slate-800 dark:text-slate-200">📌 미국: 스페이스X 나스닥 상장과 기술적 반등으로 S&P 500(7,440.43, +1.2%)과 나스닥(25,820.14, +2.1%) 동반 랠리, M7은 차별화(테슬라 +8.5% 급등).</p>
                        </div>
                        <div class="p-4 rounded-xl bg-slate-50 dark:bg-gray-900 border-l-4 border-purple-500">
                            <p class="font-medium text-slate-800 dark:text-slate-200">📌 매크로: 1,540원대의 '초고환율' 공포가 국내 증시 수급을 압박하는 가운데, 연준의 매파적 스탠스와 지정학적 긴장 완화가 맞물린 장세.</p>
                        </div>
                    </div>
                    
                    <div class="overflow-hidden rounded-xl border border-slate-200 dark:border-gray-700">
                        <table class="w-full text-left border-collapse">
                            <thead>
                                <tr class="bg-slate-100 dark:bg-gray-900 text-slate-600 dark:text-slate-400 text-sm">
                                    <th class="p-4 font-semibold">지수/지표</th>
                                    <th class="p-4 font-semibold">현재가</th>
                                    <th class="p-4 font-semibold text-right">등락률/변동</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-200 dark:divide-gray-700 text-sm">
                                <tr class="hover:bg-slate-50 dark:hover:bg-gray-800/50 transition">
                                    <td class="p-4 font-medium">KOSPI</td>
                                    <td class="p-4">8,390.12</td>
                                    <td class="p-4 text-right text-blue-500 font-semibold">-0.15% ▼</td>
                                </tr>
                                <tr class="hover:bg-slate-50 dark:hover:bg-gray-800/50 transition">
                                    <td class="p-4 font-medium">KOSDAQ</td>
                                    <td class="p-4">920.57</td>
                                    <td class="p-4 text-right text-red-500 font-semibold">+8.13% ▲</td>
                                </tr>
                                <tr class="hover:bg-slate-50 dark:hover:bg-gray-800/50 transition">
                                    <td class="p-4 font-medium">S&P 500</td>
                                    <td class="p-4">7,440.43</td>
                                    <td class="p-4 text-right text-red-500 font-semibold">+1.20% ▲</td>
                                </tr>
                                <tr class="hover:bg-slate-50 dark:hover:bg-gray-800/50 transition">
                                    <td class="p-4 font-medium">NASDAQ</td>
                                    <td class="p-4">25,820.14</td>
                                    <td class="p-4 text-right text-red-500 font-semibold">+2.10% ▲</td>
                                </tr>
                                <tr class="hover:bg-slate-50 dark:hover:bg-gray-800/50 transition">
                                    <td class="p-4 font-medium">USD/KRW</td>
                                    <td class="p-4">1,540.50</td>
                                    <td class="p-4 text-right text-slate-600 dark:text-slate-300">고점 유지</td>
                                </tr>
                                <tr class="hover:bg-slate-50 dark:hover:bg-gray-800/50 transition">
                                    <td class="p-4 font-medium">WTI (유가)</td>
                                    <td class="p-4">$70.20</td>
                                    <td class="p-4 text-right text-slate-600 dark:text-slate-300">하향 안정화</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>

            <!-- 2. 한국 시장 심층 분석 -->
            <section class="reveal bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-slate-200 dark:border-gray-700 p-8">
                <h3 class="text-2xl font-bold mb-6 flex items-center gap-2 text-slate-900 dark:text-white"><span class="text-3xl">🇰🇷</span> 한국 시장 심층 분석</h3>
                <div class="space-y-6 text-slate-700 dark:text-slate-300 leading-relaxed">
                    <p>
                        6월 30일 국내 증시는 극심한 코스피·코스닥 디커플링 양상을 보였습니다. KOSPI는 외국인의 강도 높은 매도 공세 속에 장 초반 8,500선 회복 시도가 무산되며 8,390선에서 약보합 마감했습니다. 가장 큰 하락 배경은 1,540원이라는 기록적인 초고환율 장세가 장기화되면서 환차손을 우려한 외국인 자금이 대규모로 이탈한 데 있습니다. 전일 7.7조 원이라는 기록적인 매도 폭탄에 이어 이날도 1조 원 이상의 엑소더스가 진행되며 지수 상단을 강하게 압박했습니다.
                    </p>
                    <p>
                        반면, KOSDAQ은 전 거래일 대비 무려 8.13% 급등한 920.57에 마감하며 강한 반등 탄력을 보였습니다. 기관이 5,006억 원, 외국인이 266억 원을 동반 순매수하며 지수를 견인했습니다. 이러한 코스닥의 랠리는 낙폭 과대에 따른 저가 매수세의 유입과 더불어, 미국의 스페이스X 상장 이슈와 맞물려 우주항공 및 딥테크 관련 벤처 섹터로 투기적 자금이 급격히 쏠린 결과로 해석됩니다. 기관의 매수세가 대형주 방어보다 중소형 성장주로 집중된 점이 코스닥 8% 급등이라는 기형적인 장세를 연출했습니다.
                    </p>
                    <p>
                        주요 3개 업종별 흐름을 살펴보면, <strong>반도체 섹터</strong>는 삼성전자와 SK하이닉스 등 대형주 위주로 외국인 매도세의 직격탄을 맞았으나, AI 랠리 수혜 기대감에 하방 경직성을 확보하며 지수 추가 하락을 방어했습니다. <strong>자동차 및 수출주 섹터</strong>는 1,540원의 고환율이 실적 개선(마진율 상승)의 강력한 호재로 작용하며 현대차, 기아를 중심으로 견조한 상승 흐름을 유지했습니다. 반면, <strong>금융 및 지주사 섹터</strong>는 밸류업 프로그램에 대한 피로감과 외국인의 현물 매도 타겟이 되면서 전반적으로 2~3%대의 약세를 면치 못하며 시장에 부담을 주었습니다.
                    </p>
                </div>
            </section>

            <!-- 3. 미국 시장 심층 분석 -->
            <section class="reveal bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-slate-200 dark:border-gray-700 p-8">
                <h3 class="text-2xl font-bold mb-6 flex items-center gap-2 text-slate-900 dark:text-white"><span class="text-3xl">🇺🇸</span> 미국 시장 심층 분석</h3>
                <div class="space-y-6 text-slate-700 dark:text-slate-300 leading-relaxed">
                    <p>
                        미국 증시는 6월 말 겪었던 조정의 충격을 딛고 강력한 랠리를 시현했습니다. S&P 500은 1.2% 상승한 7,440.43, 나스닥은 2.1% 급등한 25,820.14를 기록했으며, 다우존스 산업평균지수는 사상 처음으로 52,000선을 돌파했습니다. 이번 상승장의 가장 큰 트리거는 스페이스X(SpaceX)의 나스닥 상장이라는 메가톤급 이벤트였습니다. 혁신 기업의 증시 데뷔가 투심을 크게 자극했으며, 이는 기술주 전반에 대한 매수세로 확산되었습니다.
                    </p>
                    <p>
                        하지만 빅테크를 대표하는 M7(Magnificent 7) 내에서는 극심한 <strong>차별화 장세</strong>가 펼쳐졌습니다. 이른바 'Lag-7'으로 불리며 6월 한 달간 시가총액 2조 달러를 증발시킨 M7은 이날 엇갈린 행보를 보였습니다. <strong>테슬라(Tesla)</strong>는 일론 머스크의 스페이스X 상장 후광 효과와 맞물려 8.5% 폭등했고, <strong>알파벳(Alphabet)</strong>은 다우 지수 편입 이슈가 부각되며 4.8% 상승했습니다. 아마존(3.2%), 메타(2.2%), 엔비디아(1.4%) 역시 준수한 상승을 보였으나, 시장을 주도하던 <strong>마이크로소프트(-1.1%)</strong>와 <strong>애플(-0.6%)</strong>은 'AI 투자 피로감(AI Fatigue)'과 차익실현 매물에 밀려 하락 마감했습니다.
                    </p>
                    <p>
                        시장은 이제 과거처럼 소수의 빅테크가 멱살을 잡고 끌어올리는 장세에서 벗어나, S&P 500 내 나머지 493개 기업(산업, 금융, 리츠 등)으로 매기가 확산되는 '종목 순환매(Broadening)'를 보여주고 있습니다. 투자자들은 하이퍼스케일러들의 천문학적인 AI 인프라 자본적 지출(CapEx)이 언제 실질적 수익으로 전환될지에 대해 의구심을 품고 있으며, 이는 당분간 M7 종목들의 변동성을 키우는 핵심 리스크 요인으로 작용할 전망입니다.
                    </p>
                </div>
            </section>

            <!-- 4. 매크로 & 글로벌 이슈 -->
            <section class="reveal bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-slate-200 dark:border-gray-700 p-8">
                <h3 class="text-2xl font-bold mb-6 flex items-center gap-2 text-slate-900 dark:text-white"><span class="text-3xl">🌍</span> 매크로 & 글로벌 이슈</h3>
                <div class="space-y-6 text-slate-700 dark:text-slate-300 leading-relaxed">
                    <p>
                        매크로 환경은 주식 시장의 향방을 가를 최대 뇌관으로 자리 잡고 있습니다. 가장 돋보이는 지표는 단연 <strong>원/달러 환율</strong>입니다. 1,540원이라는 수치는 2008년 글로벌 금융위기에 필적하는 수준으로, 강달러 기조가 꺾이지 않으면서 한국 증시 내 외국인 이탈을 가속화하고 있습니다. 연준(Fed)의 케빈 워시(Kevin Warsh) 신임 의장 체제에서 기준금리를 3.50~3.75%로 동결했으나, 점도표상 추가 인상 가능성을 열어두는 매파적 스탠스가 강달러를 지지하고 있습니다. 반면 한국은행은 물가와 환율 방어를 위해 7월 금리 인상 압박을 강하게 받고 있어, 한미 금리 동향이 국내 증시의 방향성을 결정할 핵심 지표가 될 전망입니다.
                    </p>
                    <p>
                        국제유가(WTI)는 배럴당 70.20달러 선으로 비교적 안정적인 흐름을 보이고 있습니다. 최근 미국과 이란 간의 호르무즈 해협을 둘러싼 무력 충돌 우려로 유가가 요동치기도 했으나, 양측의 무력 충돌 중단 합의와 평화 회담이 구체화되면서 지정학적 리스크 둔화가 유가 하락 안정화를 이끌었습니다. 이는 인플레이션 재점화 우려를 잠재워주는 매우 긍정적인 요인입니다.
                    </p>
                    <p>
                        다가오는 7월 초에는 미국의 6월 비농업 고용지표(NFP) 발표가 예정되어 있습니다. 현재 시장은 고용 둔화 시그널을 확인하여 연준의 금리 동결 혹은 인하 명분이 확보되기를 기대하고 있습니다. 고용 지표가 예상외의 호조를 보일 경우, 국채 금리 급등과 함께 글로벌 기술주에 큰 하방 압력을 가할 수 있으므로 시장 참여자들의 극도로 예민한 반응이 예상됩니다.
                    </p>
                </div>
            </section>

            <!-- 5. 투자 시사점 & 전략 -->
            <section class="reveal bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-slate-200 dark:border-gray-700 p-8">
                <h3 class="text-2xl font-bold mb-6 flex items-center gap-2 text-slate-900 dark:text-white"><span class="text-3xl">💡</span> 투자 시사점 & 전략</h3>
                <div class="space-y-6 text-slate-700 dark:text-slate-300 leading-relaxed">
                    <p>
                        향후 1주일간 시장은 <strong>'초고환율 방어'</strong>와 <strong>'미국 고용지표(NFP) 확인'</strong>이라는 두 가지 거대한 허들을 넘어야 합니다. 한국 증시의 경우 1,540원대 환율이 하향 안정화되지 않는 한 코스피 대형주로의 외국인 수급 복귀를 기대하기 어렵습니다. 따라서 방향성 베팅보다는, 고환율 수혜를 온전히 누릴 수 있는 자동차 및 방산, 화장품 등 수출 마진 개선 섹터로 포트폴리오를 압축하는 방어적 전략이 유효합니다. 코스닥의 단기 폭등(8.13%)은 수급 불균형에 의한 일시적 오버슈팅일 가능성이 농후하므로 맹목적인 뇌동 매매나 추격 매수는 심각한 리스크를 수반할 수 있습니다.
                    </p>
                    <p>
                        미국 증시는 스페이스X 상장과 다우 지수 편입 이슈 등 굵직한 테마가 투심을 방어하고 있으나, M7에 집중됐던 자금이 산업재, 금융 등 경기 민감주로 이동하는 순환매가 본격화되고 있음에 주목해야 합니다. 'AI 투자 피로감'으로 인해 핵심 대장주의 주가 탄력성이 예전 같지 않은 상황에서, 실적이 뒷받침되는 중소형 가치주나 인프라 관련주로 포트폴리오 다변화를 고려할 시점입니다.
                    </p>
                    <p>
                        <strong>핵심 리스크 및 기회 요인:</strong> 단기 최대 리스크는 주 후반 예정된 미국 고용보고서 쇼크 여부입니다. 지표가 강한 과열을 나타낼 경우 연준의 매파적 스탠스가 강화되며 증시 발작이 재현될 수 있습니다. 반대로 기회 요인은 중동발 지정학적 리스크 완화에 따른 유가 하향 안정화 지속입니다. 투자자들은 주식 비중을 중립 수준으로 조절하고, 충분한 현금 비중을 바탕으로 시장 변동성 장세 하단에서의 선별적 분할 매수 기회를 엿보는 인내심이 요구됩니다.
                    </p>
                </div>
            </section>

        </div>
    </main>
"""

# Extract pre and post main block
start_tag = '<!-- Main Section -->'
end_tag = '<!-- Footer Section -->'
start_idx = template_content.find(start_tag)
end_idx = template_content.find(end_tag)

if start_idx != -1 and end_idx != -1:
    new_html = template_content[:start_idx] + main_content + "\n    " + template_content[end_idx:]
    with open('daily/daily_2026-06-30.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully created daily/daily_2026-06-30.html")
else:
    print("Could not find main section in template")
