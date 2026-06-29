import json
import os

with open('/home/ubuntu/Workspace/GitHub/invest/template/base_template.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

main_content = """    <main class="flex-grow pb-24 px-6 sm:px-12 lg:px-24 pt-12">
        <div class="max-w-7xl mx-auto space-y-12">
            
            <!-- 헤더 섹션 -->
            <div class="text-center pb-8 border-b border-slate-200 dark:border-gray-800 reveal active">
                <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-sky-100 dark:bg-sky-900/30 text-sky-600 dark:text-sky-400 text-sm font-semibold mb-4 border border-sky-200 dark:border-sky-800/50">
                    <i class="fa-solid fa-chart-line"></i> 시장동향 리포트
                </div>
                <h2 class="text-3xl md:text-5xl font-extrabold text-slate-900 dark:text-white mb-6">
                    2026년 6월 26일 <span class="gradient-text">일일 투자 인사이트</span>
                </h2>
                <p class="text-lg text-slate-600 dark:text-slate-400 max-w-3xl mx-auto leading-relaxed">
                    KOSPI 단기 과열에 따른 강력한 차익실현 출회와 미국 빅테크(M7)의 엇갈린 실적 장세 속에서 글로벌 시장의 자금 이동과 향후 투자 전략을 심층적으로 분석합니다.
                </p>
            </div>

            <!-- 한눈에 보기 -->
            <section class="reveal">
                <h3 class="text-2xl font-bold mb-6 flex items-center gap-2"><i class="fa-solid fa-bolt text-yellow-500"></i> 한눈에 보기</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div class="bg-white dark:bg-gray-800/50 rounded-2xl p-6 shadow-sm border border-slate-200 dark:border-gray-700/50 h-full flex flex-col justify-center">
                        <ul class="space-y-4 text-slate-700 dark:text-slate-300">
                            <li class="flex gap-3">
                                <i class="fa-solid fa-check-circle text-sky-500 mt-1"></i>
                                <span><strong>KOSPI 단기 조정:</strong> 전일 급등(5%+)에 따른 극심한 피로감 속 외국인의 1조 원 대 대규모 순매도세 출회.</span>
                            </li>
                            <li class="flex gap-3">
                                <i class="fa-solid fa-check-circle text-sky-500 mt-1"></i>
                                <span><strong>미국 증시 빅테크 혼조:</strong> 마이크론 어닝 서프라이즈로 16% 폭등, 애플(-6.12%) 등 M7은 AI 투자비용 우려로 하락.</span>
                            </li>
                            <li class="flex gap-3">
                                <i class="fa-solid fa-check-circle text-sky-500 mt-1"></i>
                                <span><strong>고환율 및 인플레이션 압력:</strong> 여전히 견고한 미국의 물가 지표와 달러 강세에 따른 1,415원 초고환율 고착화.</span>
                            </li>
                        </ul>
                    </div>
                    <div class="bg-white dark:bg-gray-800/50 rounded-2xl p-6 shadow-sm border border-slate-200 dark:border-gray-700/50 overflow-x-auto">
                        <table class="w-full text-sm text-left">
                            <thead class="text-xs text-slate-500 uppercase bg-slate-50 dark:bg-gray-900/50 dark:text-slate-400">
                                <tr>
                                    <th class="px-4 py-3 rounded-tl-lg">지수/항목</th>
                                    <th class="px-4 py-3">종가/수치</th>
                                    <th class="px-4 py-3">등락폭</th>
                                    <th class="px-4 py-3 rounded-tr-lg">등락률</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b dark:border-gray-700">
                                    <td class="px-4 py-3 font-semibold">KOSPI</td>
                                    <td class="px-4 py-3">8,813.18</td>
                                    <td class="px-4 py-3 text-blue-500">-116.82</td>
                                    <td class="px-4 py-3 text-blue-500">-1.31%</td>
                                </tr>
                                <tr class="border-b dark:border-gray-700">
                                    <td class="px-4 py-3 font-semibold">KOSDAQ</td>
                                    <td class="px-4 py-3">884.43</td>
                                    <td class="px-4 py-3 text-blue-500">-3.37</td>
                                    <td class="px-4 py-3 text-blue-500">-0.38%</td>
                                </tr>
                                <tr class="border-b dark:border-gray-700">
                                    <td class="px-4 py-3 font-semibold">S&P 500</td>
                                    <td class="px-4 py-3">5,820.50</td>
                                    <td class="px-4 py-3 text-blue-500">-0.58</td>
                                    <td class="px-4 py-3 text-blue-500">-0.01%</td>
                                </tr>
                                <tr class="border-b dark:border-gray-700">
                                    <td class="px-4 py-3 font-semibold">NASDAQ</td>
                                    <td class="px-4 py-3">18,410.22</td>
                                    <td class="px-4 py-3 text-blue-500">-85.12</td>
                                    <td class="px-4 py-3 text-blue-500">-0.46%</td>
                                </tr>
                                <tr>
                                    <td class="px-4 py-3 font-semibold">USD/KRW</td>
                                    <td class="px-4 py-3">1,415.20</td>
                                    <td class="px-4 py-3 text-red-500">+4.50</td>
                                    <td class="px-4 py-3 text-red-500">+0.32%</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>

            <!-- 한국 시장 분석 -->
            <section class="reveal">
                <h3 class="text-2xl font-bold mb-6 border-l-4 border-sky-500 pl-3">🇰🇷 한국 시장 심층 분석</h3>
                <div class="bg-white dark:bg-gray-800/30 rounded-2xl p-6 md:p-8 shadow-sm border border-slate-200 dark:border-gray-700/50 space-y-6 text-slate-700 dark:text-slate-300 leading-relaxed">
                    <p>
                        오늘 국내 증시는 전일 KOSPI가 5% 이상 폭등하며 꿈의 지수인 9,000선 언저리까지 수직 상승했던 것에 대한 강한 후폭풍을 맞이했습니다. KOSPI는 전 거래일 대비 1.31% 하락한 8,813.18 포인트에 개장한 이후, 한때 3%대까지 낙폭을 확대하며 극심한 변동성을 노출했습니다. 이러한 단기 롤러코스터 장세의 핵심 배경에는 어제 공격적으로 한국 주식을 사들였던 외국인 투자자들의 태도 돌변이 자리 잡고 있습니다. 외국인은 개장 직후부터 무려 1조 원이 넘는 매물 폭탄을 쏟아내며 시장의 하락을 주도했고, 기관이 방어에 나섰으나 역부족이었습니다. KOSDAQ 지수 역시 동반 하락하며 0.38% 내린 884.43 포인트로 거래를 마쳐 전반적인 투자 심리 위축을 증명했습니다.
                    </p>
                    <p>
                        업종별 흐름을 살펴보면, 시장을 주도했던 IT·반도체 대장주들의 약세 전환이 두드러졌습니다. 전날 시장 상승의 일등 공신이었던 삼성전자와 SK하이닉스는 고점 부담감을 이기지 못하고 대거 차익 매물이 출회되며 지수를 끌어내렸습니다. 반면 2차전지 섹터와 자동차(현대차, 기아) 업종은 환율 상승 효과와 더불어 저가 매수세가 일부 유입되면서 하락장에서 상대적으로 선방하는 모습을 보였습니다. 바이오 업종의 경우 개별 임상 결과에 따라 종목 장세가 연출되었고, 전반적으로는 방어주 성격을 띠는 통신과 유틸리티 업종으로 기관의 자금이 이동하는 순환매 양상이 포착되었습니다.
                    </p>
                    <p>
                        시장의 향후 전망에 대해 전문가들은 단기 과열 해소 과정으로 해석하고 있습니다. 외국인의 매도세가 펀더멘털의 훼손이라기보다는 단기간 너무 크게 오른 데 따른 기계적인 리밸런싱 성격이 짙다는 분석입니다. 따라서 당분간 KOSPI 지수는 넓은 박스권에서 지지력을 테스트할 것으로 보입니다. 투자자들은 지수 자체의 방향성보다는 외국인 수급이 재차 유입될 수 있는 밸류업 수혜주나 하반기 실적 가시성이 매우 높은 낙폭 과대 소부장(소재·부품·장비) 종목으로 시선을 좁혀야 할 시점입니다.
                    </p>
                </div>
            </section>

            <!-- 미국 시장 분석 -->
            <section class="reveal">
                <h3 class="text-2xl font-bold mb-6 border-l-4 border-indigo-500 pl-3">🇺🇸 미국 시장 심층 분석</h3>
                <div class="bg-white dark:bg-gray-800/30 rounded-2xl p-6 md:p-8 shadow-sm border border-slate-200 dark:border-gray-700/50 space-y-6 text-slate-700 dark:text-slate-300 leading-relaxed">
                    <p>
                        간밤의 미국 증시는 개별 기업들의 강력한 실적 모멘텀과 고질적인 매크로 불확실성이 충돌하며 극심한 혼조세를 연출했습니다. 다우존스 지수는 전통 산업재의 선방으로 0.14% 상승 마감했으나, 대형주 중심의 S&P 500 지수는 0.01% 하락한 5,820.50, 기술주 중심의 나스닥은 0.46% 하락한 18,410.22로 마감했습니다. 이번 장세의 가장 큰 특징은 철저한 '실적과 밸류에이션 기반의 옥석 가리기'입니다. 반도체 대표주 중 하나인 마이크론(Micron)은 시장의 예상을 훌쩍 뛰어넘는 어닝 서프라이즈와 긍정적인 가이던스를 발표하며 단숨에 주가가 16% 가까이 폭등했습니다. 이는 메모리 반도체 사이클이 여전히 탄탄하다는 점을 증명하며 반도체 산업 전체의 투심을 지지하는 역할을 했습니다.
                    </p>
                    <p>
                        그러나 마이크론의 축포에도 불구하고 시장 전반은 무거웠습니다. 특히 시장을 이끌어온 M7(매그니피센트 7) 종목들에서 강력한 차익실현 물량이 쏟아졌습니다. 애플(Apple)은 신제품의 가격 인상 우려와 더불어 중국 내 수요 부진 악재가 다시 부각되며 무려 6.12% 급락하는 충격을 안겨주었습니다. 마이크로소프트(-3.46%), 아마존(-3.10%), 메타(-2.65%) 등 나머지 빅테크 기업들도 일제히 약세를 면치 못했습니다. 시장 참여자들은 그동안 AI 인프라 구축에 천문학적인 자금을 쏟아부은 이들 빅테크 기업들이, 과연 언제쯤 이 투자를 회수할 수 있을지에 대한 '비용 대비 수익성(ROI)' 우려를 진지하게 가격에 반영하기 시작했습니다.
                    </p>
                    <p>
                        이러한 M7 종목의 약세는 미국 증시 내 주도권 변화의 신호탄으로도 해석됩니다. 과도하게 기술주에 집중되었던 쏠림 현상이 해소되면서, 헬스케어와 필수소비재, 에너지 섹터로 자금이 분산되고 있습니다. 애널리스트들은 다가오는 실적 발표 시즌에서 AI 기대감만으로는 더 이상 주가를 부양하기 어려울 것이며, 실제 숫자로 이익 성장을 증명하는 기업만이 살아남는 철저한 실적 장세가 도래할 것으로 예측하고 있습니다.
                    </p>
                </div>
            </section>

            <!-- 매크로 & 글로벌 이슈 -->
            <section class="reveal">
                <h3 class="text-2xl font-bold mb-6 border-l-4 border-purple-500 pl-3">🌍 매크로 & 글로벌 이슈</h3>
                <div class="bg-white dark:bg-gray-800/30 rounded-2xl p-6 md:p-8 shadow-sm border border-slate-200 dark:border-gray-700/50 space-y-6 text-slate-700 dark:text-slate-300 leading-relaxed">
                    <p>
                        주식시장을 흔드는 핵심 동력은 여전히 매크로(거시경제) 변수입니다. 미국 상무부가 발표한 5월 개인소비지출(PCE) 가격지수는 시장의 예상치에 대체로 부합하는 상승을 기록했습니다. 겉보기에는 물가가 안정을 찾아가는 듯 보이나, 주거비와 서비스 물가 등 근원 인플레이션의 하락 속도가 연준(Fed)의 기대에 미치지 못하고 있습니다. 이에 따라 국채금리는 하방 경직성을 강하게 보이며 증시의 밸류에이션 확장을 억제하고 있습니다. 금리 인하에 대한 시장의 과도한 기대가 서서히 현실적인 눈높이로 수정되는 과정입니다.
                    </p>
                    <p>
                        환율 시장 역시 주시해야 할 핵심 변수입니다. 달러 인덱스(DXY)가 강세를 유지하는 가운데, 원/달러 환율은 전일 대비 4.5원 상승한 1,415.20원에 마감하며 불안감을 키웠습니다. 1,400원을 훌쩍 넘긴 '초고환율' 시대가 고착화되면서 수입 물가 상승에 따른 국내 기업들의 마진 압박 우려가 커지고 있습니다. 또한, 이 같은 환율 수준은 외국인 투자자 입장에서 한국 증시의 매력도를 떨어뜨리는 결정적인 요인으로 작용하여 오늘 대규모 순매도의 빌미가 되었습니다. 단기적으로 중앙은행의 시장 개입 경계감이 존재하나 달러 강세 압력이 워낙 거세 환율 안정화에는 시간이 필요해 보입니다.
                    </p>
                    <p>
                        원자재 시장에서는 국제 유가(WTI 기준)가 상승 탄력을 받으며 움직이고 있습니다. 중동 지역의 지정학적 긴장이 지속되는 데다 여름철 성수기 진입으로 원유 수요가 견조하기 때문입니다. 유가의 점진적인 상승은 인플레이션 둔화 경로에 찬물을 끼얹을 수 있는 위험 요소입니다. 결론적으로 매크로 환경은 주식 시장에 비우호적이며, 투자자들은 매크로 지표의 미세한 변화에도 시장이 크게 요동칠 수 있는 극도의 민감도 구간에 진입했음을 명심해야 합니다.
                    </p>
                </div>
            </section>

            <!-- 투자 시사점 & 전략 -->
            <section class="reveal">
                <h3 class="text-2xl font-bold mb-6 border-l-4 border-emerald-500 pl-3">💡 투자 시사점 & 전략</h3>
                <div class="bg-white dark:bg-gray-800/30 rounded-2xl p-6 md:p-8 shadow-sm border border-slate-200 dark:border-gray-700/50 space-y-6 text-slate-700 dark:text-slate-300 leading-relaxed">
                    <p>
                        단기 급등에 따른 피로감과 매크로 불확실성이 겹친 현재 국면에서, 투자자들은 '추격 매수'를 철저히 지양해야 합니다. 지수가 급등 이후 심리적 저항선에서 발생하는 변동성은 매우 자연스러운 수순입니다. 향후 1주일간 가장 주의해야 할 리스크는 M7 기업들을 중심으로 번지고 있는 AI 밸류에이션 고평가 논란과 1,400원대에 안착해버린 고환율의 부작용입니다. 만약 외국인의 매도세가 단기적으로 지속될 경우, 시장은 보다 깊은 가격 조정에 들어갈 가능성이 높습니다. 따라서 주식 비중을 맹목적으로 늘리기보다는 일정 수준의 현금을 확보하여 변동성에 대비하는 자세가 필요합니다.
                    </p>
                    <p>
                        하지만 위기 속에서도 기회는 존재합니다. 마이크론의 실적에서 확인했듯이 반도체 업황 자체의 사이클은 흔들림이 없습니다. 단기 낙폭이 과대해진 국내 반도체 장비 및 소재 기업들은 훌륭한 저점 매수 기회가 될 수 있습니다. 또한, 고환율 환경에서 상대적으로 수익성이 개선되는 수출 주도형 자동차, 방산, 조선 섹터는 시장 하락을 훌륭하게 방어할 수 있는 대안입니다. 특히 뚜렷한 실적 모멘텀이 돋보이는 방산 및 밸류업 수혜주들은 하반기 주도주로 부상할 역량을 충분히 갖추고 있습니다.
                    </p>
                    <p>
                        결론적으로 현시점은 포트폴리오의 '방어력'을 점검하고 강화해야 할 때입니다. 뚜렷한 실적 개선 없이 기대감만으로 올랐던 모멘텀 주식들은 비중을 조절하고, 확실한 캐시카우(Cash Cow)를 보유한 우량주와 배당 매력이 높은 가치주로 포트폴리오의 중심을 이동할 것을 권고합니다. 이번 단기 과열 조정이 건강하게 마무리되고 나면 시장은 새로운 실적 장세 기반의 랠리를 도모할 것입니다. 지금은 그 도약을 위해 체력을 비축하며 시장의 자금 이동을 예의주시해야 하는 중요한 분기점입니다.
                    </p>
                </div>
            </section>

        </div>
    </main>"""

start_marker = '<main class="flex-grow pb-24 px-6 sm:px-12 lg:px-24 pt-12">'
end_marker = '</main>'

start_idx = html_content.find(start_marker)
end_idx = html_content.find(end_marker) + len(end_marker)

new_html = html_content[:start_idx] + main_content + html_content[end_idx:]

with open('/home/ubuntu/Workspace/GitHub/invest/daily/daily_2026-06-26.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

# Update daily.json
with open('/home/ubuntu/Workspace/GitHub/invest/daily.json', 'r', encoding='utf-8') as f:
    daily_data = json.load(f)

new_entry = {
    "title": "일일 투자 인사이트 — 2026-06-26",
    "filename": "daily/daily_2026-06-26.html",
    "description": "KOSPI 외국인 매물 폭탄과 미국 M7 차익실현, 환율 1,415원 등 글로벌 시장 심층 동향 리포트",
    "category": "시장동향",
    "date": "2026-06-26"
}

daily_data.insert(0, new_entry)

with open('/home/ubuntu/Workspace/GitHub/invest/daily.json', 'w', encoding='utf-8') as f:
    json.dump(daily_data, f, ensure_ascii=False, indent=2)
    
print("Successfully generated and updated files.")
