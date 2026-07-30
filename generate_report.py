import json
import re

html_content = """
    <main class="flex-grow pb-24 px-6 sm:px-12 lg:px-24 pt-12">
        <div class="max-w-7xl mx-auto space-y-16">
            
            <!-- Header -->
            <div class="text-center py-10 reveal active">
                <div class="inline-block px-4 py-1.5 rounded-full bg-sky-100 dark:bg-sky-900/30 text-sky-600 dark:text-sky-400 text-sm font-bold tracking-wide mb-4 border border-sky-200 dark:border-sky-800 shadow-sm">2026년 7월 30일 일일 브리핑</div>
                <h2 class="text-4xl md:text-5xl font-extrabold text-slate-900 dark:text-white mb-6 leading-tight">
                    글로벌 증시 변동성 확대 속 <br class="hidden md:block" />
                    <span class="gradient-text">옥석 가리기 장세</span> 진입
                </h2>
                <p class="text-lg text-slate-600 dark:text-slate-400 max-w-2xl mx-auto">
                    FOMC 금리 동결과 지정학적 리스크, 그리고 빅테크 실적 우려가 교차하는 복합 위기 속 시장의 방향성을 상세히 짚어봅니다.
                </p>
            </div>

            <!-- 1. 한눈에 보기 -->
            <section class="reveal active">
                <h3 class="text-2xl font-bold text-slate-800 dark:text-slate-200 mb-6 flex items-center gap-3">
                    <i class="fa-solid fa-chart-pie text-sky-500 text-2xl"></i> 한눈에 보기
                </h3>
                
                <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
                    <!-- Summary Card -->
                    <div class="lg:col-span-1 feature-card light-card-hover dark:dark-card-hover p-8 rounded-3xl bg-white/70 dark:bg-gray-800/70 backdrop-blur-lg border border-slate-200 dark:border-gray-700 shadow-lg">
                        <h4 class="text-xl font-bold text-slate-900 dark:text-white mb-6 border-b border-slate-200 dark:border-gray-700 pb-3">핵심 요약</h4>
                        <ul class="space-y-5">
                            <li class="flex items-start gap-4">
                                <div class="mt-1 w-8 h-8 rounded-full bg-red-100 dark:bg-red-900/30 flex items-center justify-center text-red-600 dark:text-red-400 shrink-0 shadow-inner"><i class="fa-solid fa-building-columns text-sm"></i></div>
                                <p class="text-slate-700 dark:text-slate-300 leading-relaxed text-sm"><strong class="text-slate-900 dark:text-white block text-base mb-1">미국 FOMC 매파적 동결</strong> 기준금리 3.50~3.75% 동결에도 인플레 우려가 부각되며 미 30년물 국채금리가 5.21%를 돌파했습니다.</p>
                            </li>
                            <li class="flex items-start gap-4">
                                <div class="mt-1 w-8 h-8 rounded-full bg-blue-100 dark:bg-blue-900/30 flex items-center justify-center text-blue-600 dark:text-blue-400 shrink-0 shadow-inner"><i class="fa-solid fa-microchip text-sm"></i></div>
                                <p class="text-slate-700 dark:text-slate-300 leading-relaxed text-sm"><strong class="text-slate-900 dark:text-white block text-base mb-1">M7 빅테크 실적 쇼크 우려</strong> MS, 메타 등 주요 기업이 AI 자본지출 대비 수익성 우려로 시간외 급락하며 투자 심리가 크게 위축되었습니다.</p>
                            </li>
                            <li class="flex items-start gap-4">
                                <div class="mt-1 w-8 h-8 rounded-full bg-green-100 dark:bg-green-900/30 flex items-center justify-center text-green-600 dark:text-green-400 shrink-0 shadow-inner"><i class="fa-solid fa-arrow-trend-up text-sm"></i></div>
                                <p class="text-slate-700 dark:text-slate-300 leading-relaxed text-sm"><strong class="text-slate-900 dark:text-white block text-base mb-1">한국 증시 기술적 반등 시도</strong> 이틀 연속 서킷브레이커의 충격을 딛고 저가 매수세가 유입되며 방산, 해운주 위주로 강세를 보였습니다.</p>
                            </li>
                        </ul>
                    </div>
                    
                    <!-- Market Data Table -->
                    <div class="lg:col-span-2 feature-card light-card-hover dark:dark-card-hover p-8 rounded-3xl bg-white/70 dark:bg-gray-800/70 backdrop-blur-lg border border-slate-200 dark:border-gray-700 shadow-lg flex flex-col">
                        <h4 class="text-xl font-bold text-slate-900 dark:text-white mb-6 border-b border-slate-200 dark:border-gray-700 pb-3">주요 지수 및 매크로 동향</h4>
                        <div class="overflow-x-auto flex-grow">
                            <table class="w-full text-left border-collapse min-w-[500px]">
                                <thead>
                                    <tr class="border-b-2 border-slate-200 dark:border-gray-700 text-sm text-slate-500 dark:text-slate-400 uppercase tracking-wider">
                                        <th class="py-3 px-2 font-semibold">지수/항목</th>
                                        <th class="py-3 px-2 font-semibold">종가/수치</th>
                                        <th class="py-3 px-2 font-semibold">전일대비</th>
                                        <th class="py-3 px-2 font-semibold">등락률</th>
                                    </tr>
                                </thead>
                                <tbody class="text-slate-800 dark:text-slate-200">
                                    <tr class="border-b border-slate-100 dark:border-gray-750/50 hover:bg-slate-50 dark:hover:bg-gray-800/80 transition-colors group">
                                        <td class="py-3 px-2 font-medium flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-red-500 group-hover:scale-150 transition-transform"></span> 코스피 (KOSPI)</td>
                                        <td class="py-3 px-2 font-mono font-medium">6,540.23</td>
                                        <td class="py-3 px-2 text-red-500 font-medium">▲ 79.64</td>
                                        <td class="py-3 px-2"><span class="text-red-600 dark:text-red-400 font-bold bg-red-50 dark:bg-red-900/30 px-2.5 py-1 rounded-md text-sm">+1.23%</span></td>
                                    </tr>
                                    <tr class="border-b border-slate-100 dark:border-gray-750/50 hover:bg-slate-50 dark:hover:bg-gray-800/80 transition-colors group">
                                        <td class="py-3 px-2 font-medium flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-red-500 group-hover:scale-150 transition-transform"></span> 코스닥 (KOSDAQ)</td>
                                        <td class="py-3 px-2 font-mono font-medium">1,230.15</td>
                                        <td class="py-3 px-2 text-red-500 font-medium">▲ 17.58</td>
                                        <td class="py-3 px-2"><span class="text-red-600 dark:text-red-400 font-bold bg-red-50 dark:bg-red-900/30 px-2.5 py-1 rounded-md text-sm">+1.45%</span></td>
                                    </tr>
                                    <tr class="border-b border-slate-100 dark:border-gray-750/50 hover:bg-slate-50 dark:hover:bg-gray-800/80 transition-colors group">
                                        <td class="py-3 px-2 font-medium flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-blue-500 group-hover:scale-150 transition-transform"></span> S&P 500</td>
                                        <td class="py-3 px-2 font-mono font-medium">7,316.15</td>
                                        <td class="py-3 px-2 text-blue-500 font-medium">▼ 112.83</td>
                                        <td class="py-3 px-2"><span class="text-blue-600 dark:text-blue-400 font-bold bg-blue-50 dark:bg-blue-900/30 px-2.5 py-1 rounded-md text-sm">-1.52%</span></td>
                                    </tr>
                                    <tr class="border-b border-slate-100 dark:border-gray-750/50 hover:bg-slate-50 dark:hover:bg-gray-800/80 transition-colors group">
                                        <td class="py-3 px-2 font-medium flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-blue-500 group-hover:scale-150 transition-transform"></span> 나스닥 (NASDAQ)</td>
                                        <td class="py-3 px-2 font-mono font-medium">24,442.94</td>
                                        <td class="py-3 px-2 text-blue-500 font-medium">▼ 432.55</td>
                                        <td class="py-3 px-2"><span class="text-blue-600 dark:text-blue-400 font-bold bg-blue-50 dark:bg-blue-900/30 px-2.5 py-1 rounded-md text-sm">-1.74%</span></td>
                                    </tr>
                                    <tr class="border-b border-slate-100 dark:border-gray-750/50 hover:bg-slate-50 dark:hover:bg-gray-800/80 transition-colors group">
                                        <td class="py-3 px-2 font-medium flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-emerald-500 group-hover:scale-150 transition-transform"></span> 원/달러 환율</td>
                                        <td class="py-3 px-2 font-mono font-medium">1,442.50원</td>
                                        <td class="py-3 px-2 text-blue-500 font-medium">▼ 4.20원</td>
                                        <td class="py-3 px-2"><span class="text-emerald-600 dark:text-emerald-400 font-bold bg-emerald-50 dark:bg-emerald-900/30 px-2.5 py-1 rounded-md text-sm">-0.29%</span></td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 dark:hover:bg-gray-800/80 transition-colors group">
                                        <td class="py-3 px-2 font-medium flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-purple-500 group-hover:scale-150 transition-transform"></span> 브렌트유 (Brent)</td>
                                        <td class="py-3 px-2 font-mono font-medium">$90.74</td>
                                        <td class="py-3 px-2 text-red-500 font-medium">▲ $6.64</td>
                                        <td class="py-3 px-2"><span class="text-purple-600 dark:text-purple-400 font-bold bg-purple-50 dark:bg-purple-900/30 px-2.5 py-1 rounded-md text-sm">+7.90%</span></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 2. 한국 시장 심층 분석 -->
            <section class="reveal">
                <div class="feature-card light-card-hover dark:dark-card-hover p-8 md:p-10 rounded-3xl bg-white/70 dark:bg-gray-800/70 backdrop-blur-lg border border-slate-200 dark:border-gray-700 shadow-xl relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-64 h-64 bg-blue-400/10 rounded-full blur-3xl -mr-20 -mt-20"></div>
                    <h3 class="text-2xl md:text-3xl font-extrabold text-slate-900 dark:text-white mb-6 relative z-10 flex items-center gap-3">
                        <span class="text-3xl">🇰🇷</span> 한국 시장 심층 분석
                    </h3>
                    
                    <div class="space-y-6 text-slate-700 dark:text-slate-300 leading-loose relative z-10 text-lg">
                        <p>
                            30일 한국 증시는 극심한 변동성 속에서 방향성을 모색하는 치열한 공방전을 펼쳤습니다. 지난 28일과 29일, <strong>사상 초유의 이틀 연속 서킷브레이커 발동</strong>이라는 패닉 장세를 겪었던 코스피(KOSPI)는 전일의 충격에 따른 저가 매수세가 유입되며 상승 출발했습니다. 코스피는 최종적으로 전장 대비 <span class="font-bold text-red-500">1.23% 상승한 6,540.23</span>에 마감하였고, 코스닥(KOSDAQ) 역시 <span class="font-bold text-red-500">1.45% 오른 1,230.15</span>로 거래를 마치며 기술적 반등에 성공했습니다. 그러나 장중 내내 안도감보다는 불안감이 지배하며 지수는 큰 폭의 롤러코스터 장세를 연출했습니다.
                        </p>
                        <p>
                            시장의 이러한 극심한 변동성 배경에는 간밤 미국발 악재가 복합적으로 작용했습니다. 미 연준(Fed)의 7월 FOMC 금리 동결 결정과 파월 의장의 매파적 발언, 그리고 미국 장 마감 후 발표된 마이크로소프트(MS) 등 빅테크 기업들의 부진한 실적 및 시간외 주가 급락이 국내 투자 심리에 찬물을 끼얹었습니다. 특히 외국인과 기관이 개장 초반 각각 <span class="font-semibold text-slate-900 dark:text-white">4,500억 원, 3,200억 원의 순매수</span>를 기록하며 지수 방어에 나섰음에도 불구하고, 개인 투자자들이 <span class="font-semibold text-slate-900 dark:text-white">8,000억 원 규모의 패닉 셀링(매도)</span> 물량을 쏟아내며 시장의 하방 압력을 높였습니다. 
                        </p>
                        <p>
                            업종별로는 대외 불확실성 속에서도 실적 가시성이 뚜렷한 섹터로 수급이 쏠리는 '옥석 가리기' 장세가 뚜렷했습니다. 지정학적 리스크 부각에 따라 방산주가 <span class="font-bold text-red-500">+2.8%</span>의 강세를 보였고, 해운/물류 섹터 역시 운임 상승 기대감에 <span class="font-bold text-red-500">+1.5%</span> 상승하며 지수 하단을 지지했습니다. 반면, AI 반도체 관련주는 미국발 M7 충격에도 불구하고 SK하이닉스와 삼성전자를 중심으로 한 저가 매수세가 강력히 유입되며 섹터 전체적으로 <span class="font-bold text-red-500">+3.4%</span>의 놀라운 반등을 시현했습니다. 이는 최근 급락에 따른 과매도 인식과 함께 한국 반도체 기업들의 이익 체력이 여전히 견조하다는 시장의 긍정적 해석이 반영된 결과로 풀이됩니다.
                        </p>
                    </div>
                </div>
            </section>

            <!-- 3. 미국 시장 심층 분석 -->
            <section class="reveal">
                <div class="feature-card light-card-hover dark:dark-card-hover p-8 md:p-10 rounded-3xl bg-white/70 dark:bg-gray-800/70 backdrop-blur-lg border border-slate-200 dark:border-gray-700 shadow-xl relative overflow-hidden">
                    <div class="absolute bottom-0 left-0 w-64 h-64 bg-red-400/10 rounded-full blur-3xl -ml-20 -mb-20"></div>
                    <h3 class="text-2xl md:text-3xl font-extrabold text-slate-900 dark:text-white mb-6 relative z-10 flex items-center gap-3">
                        <span class="text-3xl">🇺🇸</span> 미국 시장 심층 분석
                    </h3>
                    
                    <div class="space-y-6 text-slate-700 dark:text-slate-300 leading-loose relative z-10 text-lg">
                        <p>
                            29일(현지시간) 뉴욕증시는 연준의 기준금리 동결이라는 예상된 결과에도 불구하고, 인플레이션 고착화에 대한 불안감과 빅테크 실적 우려가 겹치며 일제히 하락 마감했습니다. <strong>다우존스 지수는 <span class="font-bold text-blue-500">-2.19% 하락한 51,594.14</span>, S&P 500은 <span class="font-bold text-blue-500">-1.52% 내린 7,316.15</span>, 나스닥 종합지수는 <span class="font-bold text-blue-500">-1.74% 하락한 24,442.94</span></strong>를 기록했습니다. 시장은 당초 연준이 이번 회의를 통해 통화정책 완화의 시그널을 줄 것으로 기대했으나, 성명서와 파월 의장의 발언에서 인플레이션 억제에 대한 강경한 태도가 재확인되면서 실망 매물이 쏟아졌습니다.
                        </p>
                        <p>
                            가장 큰 타격을 입은 것은 증시를 견인해온 <strong>'매그니피센트 7(M7)'</strong> 빅테크 기업들이었습니다. 이번 주 M7 기업들의 실적 발표가 집중된 이른바 '빅위크'를 맞아, 투자자들은 AI 인프라에 대한 막대한 자본지출(Capex) 대비 잉여현금흐름과 수익성이 얼마나 훼손되는지를 매우 엄격한 잣대로 평가하고 있습니다. 이날 정규장 마감 후 실적을 발표한 마이크로소프트(MS)는 클라우드 부문 성장에 힘입어 시간외 거래에서 잠시 2%대 상승을 보이기도 했으나, 정규장에서는 <span class="font-bold text-blue-500">-0.71%</span> 하락 마감했습니다. 
                        </p>
                        <p>
                            특히 충격을 준 것은 메타(Meta)였습니다. 메타는 정규장에서 <span class="font-bold text-blue-500">-1.31%</span> 하락한 뒤, 공격적인 AI 투자로 인해 향후 마진율이 하락할 수 있다는 실적 가이던스를 내놓으면서 <strong>시간외 거래에서 주가가 10% 가까이 폭락</strong>했습니다. 앞서 알파벳(구글)이 대규모 AI 자본지출 계획을 발표한 직후 주가가 급락했던 사례가 오버랩되면서, AI 주도 랠리의 지속 가능성에 대한 본질적인 의구심이 확산되는 양상입니다. 시장의 이목은 이제 30일(현지시간)로 예정된 애플(Apple)과 아마존(Amazon)의 실적 발표로 쏠려 있으며, 이들의 실적에 따라 M7 지수의 단기 향방이 크게 좌우될 전망입니다.
                        </p>
                    </div>
                </div>
            </section>

            <!-- 4. 매크로 & 글로벌 이슈 -->
            <section class="reveal">
                <div class="feature-card light-card-hover dark:dark-card-hover p-8 md:p-10 rounded-3xl bg-white/70 dark:bg-gray-800/70 backdrop-blur-lg border border-slate-200 dark:border-gray-700 shadow-xl relative overflow-hidden">
                    <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-80 h-80 bg-emerald-400/10 rounded-full blur-3xl"></div>
                    <h3 class="text-2xl md:text-3xl font-extrabold text-slate-900 dark:text-white mb-6 relative z-10 flex items-center gap-3">
                        <span class="text-3xl">🌍</span> 매크로 & 글로벌 이슈
                    </h3>
                    
                    <div class="space-y-6 text-slate-700 dark:text-slate-300 leading-loose relative z-10 text-lg">
                        <p>
                            거시경제(Macro) 지표 측면에서는 <strong>'고금리와 고유가의 역습'</strong>이 주식 시장을 전방위적으로 압박하고 있습니다. 미 연준이 기준금리를 3.50~3.75%로 동결했으나, 연준 위원 3명이 오히려 금리 인상을 주장하는 등 내부의 매파적 기조가 부각되었습니다. 이로 인해 금리 인하 기대감이 후퇴하며 미국 국채 금리가 전 구간에서 발작적 급등세를 보였습니다. 특히 장기물인 <strong>30년 만기 미 국채 금리는 전장 대비 0.1%p 이상 급등하며 연 <span class="font-bold text-red-500">5.21%</span> 내외를 기록, 2007년 7월 이후 19년 만에 최고치</strong>를 경신했습니다. 10년물 금리도 연 <span class="font-bold text-red-500">4.67%</span>, 2년물 금리는 연 <span class="font-bold text-red-500">4.24%</span>로 뛰어올라 주식의 상대적 매력도를 급격히 떨어뜨리고 있습니다.
                        </p>
                        <p>
                            지정학적 리스크는 유가 급등을 촉발하며 시장의 인플레이션 우려에 기름을 부었습니다. 도널드 트럼프 미국 대통령이 이란의 미군 기지 공격에 대해 강력한 보복 조치를 시사하면서 중동 지역의 무력 충돌 우려가 재점화되었습니다. 이로 인해 29일 종가 기준 글로벌 벤치마크인 <strong>브렌트유는 배럴당 <span class="font-bold text-red-500">90.74달러 (+7.9%)</span>, 서부텍사스산원유(WTI)는 배럴당 <span class="font-bold text-red-500">84.46달러 (+6.6%)</span></strong>로 치솟으며 스태그플레이션(경기침체 속 물가상승) 우려를 자극하고 있습니다.
                        </p>
                        <p>
                            다만 외환시장에서는 다소 엇갈린 흐름이 나타났습니다. 30일 서울 외환시장에서 <strong>원/달러 환율은 전 거래일 종가 대비 4.2원 하락한 <span class="font-bold text-blue-500">1,442.5원</span></strong>을 기록했습니다. 이는 미국의 고금리 유지에도 불구하고, 최근 원화가 과도하게 절하되었다는 인식과 함께 국내 당국의 미세 조정(스무딩 오퍼레이션) 경계감이 작용한 결과로 해석됩니다. 하지만 국제 유가 급등에 따른 무역수지 악화 우려가 상존하고 있어, 환율의 유의미한 하락 추세 전환을 논하기에는 아직 시기상조라는 것이 전문가들의 중론입니다.
                        </p>
                    </div>
                </div>
            </section>

            <!-- 5. 투자 시사점 & 전략 -->
            <section class="reveal">
                <div class="feature-card light-card-hover dark:dark-card-hover p-8 md:p-10 rounded-3xl bg-gradient-to-br from-indigo-50 to-sky-50 dark:from-gray-800 dark:to-gray-900 backdrop-blur-lg border border-indigo-100 dark:border-gray-700 shadow-2xl relative overflow-hidden">
                    <h3 class="text-2xl md:text-3xl font-extrabold text-slate-900 dark:text-white mb-6 relative z-10 flex items-center gap-3">
                        <span class="text-3xl">💡</span> 투자 시사점 & 전략
                    </h3>
                    
                    <div class="space-y-6 text-slate-800 dark:text-slate-300 leading-loose relative z-10 text-lg">
                        <p>
                            향후 1주일간 주식 시장은 <strong>'지정학적 리스크'</strong>와 <strong>'빅테크 실적 검증'</strong>이라는 두 개의 거대한 파도 사이에서 높은 변동성을 수반한 횡보 장세를 보일 가능성이 큽니다. 투자자들은 단기적인 바닥 잡기(Bottom fishing)에 나서기보다는, 현금 비중을 30% 이상으로 확대하고 시장의 방향성이 명확해질 때까지 방어적인 포트폴리오를 구축해야 할 시점입니다.
                        </p>
                        <p>
                            <strong>리스크 요인:</strong> 당장 30일(현지시간) 예정된 애플과 아마존의 실적이 가장 큰 단기 뇌관입니다. 이들 기업마저 AI 투자 대비 가시적인 성과를 입증하지 못한다면, M7을 중심으로 한 나스닥의 추가 조정 폭은 5~10% 이상 확대될 수 있습니다. 또한 주말 사이 미국과 이란 간의 물리적 충돌이 현실화될 경우, 국제 유가가 배럴당 100달러를 돌파하며 글로벌 증시 전반에 스태그플레이션 공포를 불러일으킬 수 있으므로 뉴스 플로우에 극도로 주의해야 합니다.
                        </p>
                        <p>
                            <strong>기회 요인 및 대응 전략:</strong> 역설적으로 최근의 주가 급락은 밸류에이션(실적 대비 주가 수준) 부담을 상당 부분 해소시켜 주었습니다. 특히 한국 시장의 반도체 대형주(삼성전자, SK하이닉스)는 글로벌 동종 업계 대비 가격 매력도가 높아진 상태이므로, 지수 6,500선 초반에서는 분할 매수 관점으로 접근하는 것이 유효합니다. 아울러 고유가 수혜가 기대되는 에너지 및 정유주, 그리고 지정학적 갈등의 피난처 역할을 하는 방산 섹터에 대한 단기 트레이딩 전략도 훌륭한 대안이 될 수 있습니다. 
                        </p>
                    </div>
                </div>
            </section>
        </div>
    </main>
"""

with open('/home/ubuntu/Workspace/GitHub/invest/template/base_template.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

# Replace <main>...</main> with our content
new_html = re.sub(r'<main.*?</main>', html_content, base_html, flags=re.DOTALL)

with open('/home/ubuntu/Workspace/GitHub/invest/daily/daily_2026-07-30.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

# Update daily.json
with open('/home/ubuntu/Workspace/GitHub/invest/daily.json', 'r', encoding='utf-8') as f:
    daily_data = json.load(f)

new_entry = {
    "title": "일일 투자 인사이트 — 2026-07-30",
    "filename": "daily/daily_2026-07-30.html",
    "description": "한국 증시 반등 시도 속 이틀 연속 서킷브레이커 후폭풍 진단, 미국 M7 실적 쇼크 우려 및 FOMC 고금리 장기화(30년물 5.21%), 고유가 등 매크로 복합 위기 심층 분석 리포트",
    "category": "시장동향",
    "date": "2026-07-30"
}

daily_data.insert(0, new_entry)

with open('/home/ubuntu/Workspace/GitHub/invest/daily.json', 'w', encoding='utf-8') as f:
    json.dump(daily_data, f, ensure_ascii=False, indent=2)

print("HTML generated and daily.json updated.")
