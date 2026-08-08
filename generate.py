import os
import json

base_path = '/home/ubuntu/Workspace/GitHub/invest'
template_path = os.path.join(base_path, 'template', 'base_template.html')
target_html_path = os.path.join(base_path, 'daily', 'daily_2026-08-08.html')
target_json_path = os.path.join(base_path, 'daily.json')

os.makedirs(os.path.dirname(target_html_path), exist_ok=True)

with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

main_content = """
            <div class="space-y-12 animate-fade-in-up">
                <!-- 1. 한눈에 보기 -->
                <section class="reveal active bg-white/60 dark:bg-gray-800/60 backdrop-blur-xl rounded-3xl p-8 shadow-xl border border-white/20 dark:border-gray-700/50">
                    <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 dark:text-white mb-6">
                        <span class="gradient-text">2026년 8월 8일</span> 글로벌 증시 브리핑
                    </h2>
                    <div class="space-y-4 text-lg text-slate-700 dark:text-slate-300 font-medium">
                        <p>📌 <strong class="text-slate-900 dark:text-white">한국 증시:</strong> KOSPI 6,258.77 (-0.6%), 반도체 섹터 압박 및 외국인 매도세로 인한 단기 숨고르기 장세.</p>
                        <p>📌 <strong class="text-slate-900 dark:text-white">미국 증시:</strong> S&P500 7,756.44 (사상 최고치 경신), 고용 지표 둔화에 따른 금리 인하 기대감이 기술주 중심의 강력한 랠리를 견인.</p>
                        <p>📌 <strong class="text-slate-900 dark:text-white">주요 매크로:</strong> M7 실적 차별화 심화 속, 유가 안정화 및 국채 금리 하락으로 인한 매크로 환경 호전.</p>
                    </div>
                    
                    <div class="mt-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                        <!-- 지수 테이블/카드 -->
                        <div class="feature-card light-card-hover dark-card-hover bg-white dark:bg-gray-900 rounded-2xl p-6 border border-slate-200 dark:border-gray-700">
                            <div class="text-sm text-slate-500 dark:text-slate-400 mb-1 font-semibold">KOSPI</div>
                            <div class="text-3xl font-bold text-slate-900 dark:text-white">6,258.77</div>
                            <div class="text-blue-500 font-bold mt-2 flex items-center gap-1">
                                <i class="fa-solid fa-arrow-down"></i> -0.60%
                            </div>
                        </div>
                        <div class="feature-card light-card-hover dark-card-hover bg-white dark:bg-gray-900 rounded-2xl p-6 border border-slate-200 dark:border-gray-700">
                            <div class="text-sm text-slate-500 dark:text-slate-400 mb-1 font-semibold">KOSDAQ</div>
                            <div class="text-3xl font-bold text-slate-900 dark:text-white">1,024.50</div>
                            <div class="text-blue-500 font-bold mt-2 flex items-center gap-1">
                                <i class="fa-solid fa-arrow-down"></i> -0.80%
                            </div>
                        </div>
                        <div class="feature-card light-card-hover dark-card-hover bg-white dark:bg-gray-900 rounded-2xl p-6 border border-slate-200 dark:border-gray-700">
                            <div class="text-sm text-slate-500 dark:text-slate-400 mb-1 font-semibold">S&P 500</div>
                            <div class="text-3xl font-bold text-slate-900 dark:text-white">7,756.44</div>
                            <div class="text-red-500 font-bold mt-2 flex items-center gap-1">
                                <i class="fa-solid fa-arrow-up"></i> +1.20%
                            </div>
                        </div>
                        <div class="feature-card light-card-hover dark-card-hover bg-white dark:bg-gray-900 rounded-2xl p-6 border border-slate-200 dark:border-gray-700">
                            <div class="text-sm text-slate-500 dark:text-slate-400 mb-1 font-semibold">NASDAQ</div>
                            <div class="text-3xl font-bold text-slate-900 dark:text-white">24,150.80</div>
                            <div class="text-red-500 font-bold mt-2 flex items-center gap-1">
                                <i class="fa-solid fa-arrow-up"></i> +1.80%
                            </div>
                        </div>
                    </div>
                </section>
                
                <!-- 2. 한국 시장 -->
                <section class="reveal bg-white/60 dark:bg-gray-800/60 backdrop-blur-xl rounded-3xl p-8 shadow-xl border border-white/20 dark:border-gray-700/50">
                    <h3 class="text-2xl font-bold text-slate-900 dark:text-white mb-6 border-b border-slate-200 dark:border-gray-700 pb-4">🇰🇷 한국 시장 심층 분석</h3>
                    <div class="space-y-6 text-slate-700 dark:text-slate-300 leading-relaxed text-lg">
                        <p>한국 증시는 전일 대비 하락 마감하며 KOSPI 지수가 6,258.77(-0.6%)로 거래를 마쳤습니다. KOSDAQ 역시 1,024.50(-0.8%)으로 동반 약세를 기록했습니다. 지난 7월 말 발생했던 역대급 폭락 이후 시장은 점진적인 회복을 시도해왔으나, 최근 외국인의 강한 매도세가 출회되면서 지수 상단이 제한되는 모습입니다. 특히, 반도체 대장주인 SK하이닉스가 -2.4% 하락한 245,000원에 마감하며 지수 하락을 주도했습니다.</p>
                        <p>주요 3개 업종별 흐름을 살펴보면, 반도체 업종은 글로벌 AI CAPEX(설비투자) 속도 조절 우려와 함께 차익실현 매물이 쏟아지며 약세를 면치 못했습니다. 반면, 2차전지 섹터는 LG에너지솔루션(+1.5%)을 중심으로 저가 매수세가 유입되며 상대적으로 견조한 흐름을 보였습니다. 금융업종의 경우, 최근 정부의 밸류업 프로그램 관련 후속 조치 기대감 속에서 외국인 매수세가 집중되며 +1.2% 상승 마감하여 증시 하단을 방어하는 역할을 수행했습니다.</p>
                        <p>수급 측면에서 외국인과 기관의 엇갈린 행보가 눈에 띄었습니다. 유가증권시장에서 외국인은 약 6,500억 원 규모의 대규모 순매도를 기록하며 지수 하방 압력을 높였습니다. 이는 주로 전기전자 업종에 집중된 매도 물량입니다. 반면, 기관은 연기금을 중심으로 4,200억 원, 개인은 2,100억 원을 순매수하며 외국인의 물량을 소화해냈습니다. 시장 참여자들은 중동 지정학적 리스크와 글로벌 경기 침체 우려라는 두 가지 거시적 요인이 맞물리면서 외국인의 리스크 오프(Risk-Off) 심리가 자극된 것으로 해석하고 있습니다.</p>
                        <p>향후 한국 시장의 전망은 외국인 수급의 턴어라운드 여부에 달려 있습니다. 현재 KOSPI의 밸류에이션은 역사적 평균 대비 여전히 매력적인 구간에 위치하고 있으며, 상장사들의 하반기 이익 추정치 상향 조정이 지속되고 있다는 점은 긍정적입니다. 그러나 글로벌 거시 경제의 불확실성이 해소되기 전까지는 지수 전체의 추세적 상승보다는 개별 종목과 섹터 중심의 차별화된 순환매 장세가 이어질 가능성이 높습니다.</p>
                    </div>
                </section>

                <!-- 3. 미국 시장 -->
                <section class="reveal bg-white/60 dark:bg-gray-800/60 backdrop-blur-xl rounded-3xl p-8 shadow-xl border border-white/20 dark:border-gray-700/50">
                    <h3 class="text-2xl font-bold text-slate-900 dark:text-white mb-6 border-b border-slate-200 dark:border-gray-700 pb-4">🇺🇸 미국 시장 심층 분석</h3>
                    <div class="space-y-6 text-slate-700 dark:text-slate-300 leading-relaxed text-lg">
                        <p>미국 뉴욕 증시는 강력한 랠리를 펼치며 주요 지수가 사상 최고치를 경신했습니다. S&P500 지수는 7,756.44(+1.2%)로 마감하며 새로운 역사를 썼고, 기술주 중심의 NASDAQ 지수는 24,150.80(+1.8%)으로 급등하며 시장의 긍정적인 분위기를 주도했습니다. 주간 기준으로 S&P500은 3.5%, NASDAQ은 5.2% 상승하여 올 4월 이후 주간 최대 상승폭을 기록했습니다. 이러한 강세의 근저에는 미국의 7월 고용 지표 둔화가 자리 잡고 있습니다.</p>
                        <p>최근 발표된 7월 미국 비농업 부문 고용은 예상과 달리 23,000개 일자리 감소를 기록했습니다. 이는 노동 시장의 과열이 확연히 진정되고 있음을 시사하는 지표로, 시장은 이를 연방준비제도(Fed)의 금리 인하 명분으로 즉각 해석했습니다. 그 결과 미국 국채 금리가 급락하며 주식 시장, 특히 고금리에 취약한 기술주와 성장주에 강력한 상승 모멘텀을 제공했습니다. '나쁜 뉴스가 곧 좋은 뉴스(Bad news is good news)'라는 금융 시장의 역설이 다시 한번 증명된 하루였습니다.</p>
                        <p>M7(매그니피센트 7)으로 불리는 빅테크 기업들의 개별 종목 흐름은 뚜렷한 차별화 양상을 보였습니다. 마이크로소프트(MSFT)는 +2.5% 상승한 580.20달러, 알파벳(GOOGL)은 +1.9% 상승한 235.50달러로 마감하며 견조한 2분기 실적과 AI 벤처 투자 수익이 긍정적으로 작용했습니다. 반면, 최근 AI 인프라 투자 비용(CAPEX) 대비 수익화 지연 우려가 제기된 메타(META)는 -0.8%, 테슬라(TSLA)는 개별 악재가 겹치며 -1.5% 하락 마감했습니다. 이는 M7이라는 하나의 거대한 테마가 해체되고, 개별 기업의 펀더멘털과 실제 수익 창출 능력에 따라 주가가 철저히 엇갈리고 있음을 보여줍니다.</p>
                        <p>시장 전문가들은 향후 미국 증시가 양호한 거시 경제 환경 속에서 당분간 우상향 기조를 유지할 것으로 전망하고 있습니다. 다만, 과거처럼 M7 전체가 지수 상승을 무차별적으로 견인하기보다는, AI 기술을 통해 즉각적인 실적 개선을 보여주는 하드웨어 기업 및 현금 창출력이 우수한 특정 플랫폼 기업으로 매수세가 압축될 것으로 예상됩니다. 또한 다가오는 9월 FOMC에서의 구체적인 금리 인하 폭에 따라 단기적인 변동성이 확대될 수 있습니다.</p>
                    </div>
                </section>

                <!-- 4. 매크로 -->
                <section class="reveal bg-white/60 dark:bg-gray-800/60 backdrop-blur-xl rounded-3xl p-8 shadow-xl border border-white/20 dark:border-gray-700/50">
                    <h3 class="text-2xl font-bold text-slate-900 dark:text-white mb-6 border-b border-slate-200 dark:border-gray-700 pb-4">🌍 매크로 & 글로벌 이슈</h3>
                    <div class="space-y-6 text-slate-700 dark:text-slate-300 leading-relaxed text-lg">
                        <p>한미 금리 동향은 증시 랠리의 가장 강력한 촉매제로 작용했습니다. 미국 10년물 국채 금리는 고용 지표 쇼크 직후 15bp 이상 급락하며 3.85% 수준까지 내려왔습니다. 이는 인플레이션 압력이 상당 부분 완화되었으며, 연준이 빠르면 9월부터 금리 인하 사이클에 진입할 것이라는 시장의 확신을 반영한 결과입니다. 한국의 국채 3년물 금리 역시 미국 금리 하락에 동조화되며 3.12%까지 하락, 국내 자금 시장의 경색 우려를 크게 덜어주었습니다.</p>
                        <p>외환 시장에서 원/달러 환율(USD/KRW)은 전일 대비 8.5원 하락한 1,352.40원에 마감했습니다. 최근 1,380원대까지 치솟으며 외국인 자금 이탈을 부추겼던 환율이 달러화 약세와 함께 안정을 찾으면서, 국내 증시의 하방 경직성을 확보하는 데 기여했습니다. 연준의 금리 인하 기대감이 선반영되면서 글로벌 달러 인덱스가 하락 압력을 받고 있어, 당분간 환율은 1,340원~1,360원 박스권 내에서 하향 안정화 흐름을 보일 것으로 전망됩니다.</p>
                        <p>원자재 시장, 특히 국제 유가의 흐름도 증시에 우호적으로 작용했습니다. 서부텍사스산원유(WTI)는 전장 대비 1.2% 하락한 배럴당 76.80달러에 거래를 마쳤습니다. 중동 지역, 특히 호르무즈 해협을 둘러싼 지정학적 긴장이 상존하고 있음에도 불구하고, 최대 원유 소비국인 미국과 중국의 경기 둔화 우려가 수요 감소 전망으로 이어지며 유가 상승을 억제하고 있습니다. 이는 인플레이션 재점화 우려를 차단하여 중앙은행들의 통화 정책 운용에 여유를 주고 있습니다.</p>
                        <p>이외에도 ISM 비제조업 구매관리자지수(PMI) 등 주요 경제지표들이 경기 연착륙(Soft-landing) 시나리오를 뒷받침하는 결과값으로 발표되면서 매크로 환경은 주식 등 위험자산에 극히 유리하게 조성되고 있습니다. 다만, 실물 경기의 둔화 속도가 예상보다 가파를 경우, 현재의 금리 인하 환호가 경기 침체(Recession) 공포로 돌변할 수 있다는 점에서 향후 발표될 소매판매 지표와 물가 지표(CPI, PCE)에 대한 면밀한 모니터링이 필수적입니다.</p>
                    </div>
                </section>

                <!-- 5. 투자 시사점 -->
                <section class="reveal bg-white/60 dark:bg-gray-800/60 backdrop-blur-xl rounded-3xl p-8 shadow-xl border border-white/20 dark:border-gray-700/50">
                    <h3 class="text-2xl font-bold text-slate-900 dark:text-white mb-6 border-b border-slate-200 dark:border-gray-700 pb-4">💡 투자 시사점 & 전략</h3>
                    <div class="space-y-6 text-slate-700 dark:text-slate-300 leading-relaxed text-lg">
                        <p>현재 시장은 금리 인하라는 강력한 호재와 실물 경기 둔화 우려 사이에서 아슬아슬한 줄타기를 하고 있습니다. 향후 1주일간 가장 주목해야 할 핵심 기회 요인은 '금리 민감주'의 반등입니다. 금리 인하 사이클 진입이 가시화됨에 따라 그동안 고금리로 인해 밸류에이션이 억눌려 있던 바이오, 헬스케어, 그리고 친환경 인프라 섹터로의 자금 이동이 가속화될 수 있습니다. 특히 2분기 호실적을 발표한 낙폭 과대 우량주를 중심으로 한 선별적인 바텀피싱(Bottom-fishing) 전략이 유효해 보입니다.</p>
                        <p>반면, 최대 리스크 요인은 'AI 투자에 대한 피로감'과 '외국인 수급의 이탈'입니다. 미국 M7에서 나타나듯, 명확한 실적 가이던스 없이 기대감만으로 올랐던 기술주들은 강력한 조정에 직면할 위험이 있습니다. 또한, 한국 시장의 경우 환율 안정에도 불구하고 외국인의 반도체 엑소더스가 지속된다면 지수 전체의 반등은 요원할 수 있습니다. 따라서 반도체 단일 섹터에 대한 과도한 비중 확대를 경계하고, 포트폴리오의 변동성을 낮추는 방어적 관점도 병행해야 합니다.</p>
                        <p>구체적인 전략 측면에서는, 한국 시장의 경우 밸류업 프로그램 수혜가 기대되는 저PBR 배당주(금융, 지주사)와 이익 체력이 검증된 자동차 섹터에 포트폴리오의 30% 수준을 방어적으로 배분할 것을 권고합니다. 미국 시장은 M7 전체에 대한 패시브 투자보다는 실질적인 AI 수익 창출 생태계를 주도하는 하드웨어 팹리스 및 클라우드 서비스 제공자(CSP) 최선호주로 압축하는 액티브(Active) 대응이 필요합니다. 더불어 헷지 차원에서 장기 채권 ETF 비중을 일정 부분 유지하는 것도 훌륭한 대안입니다.</p>
                        <p>요약하자면, 시장의 색깔이 '매크로 중심'에서 '실적과 현금흐름 중심'으로 빠르게 전환되고 있습니다. 무차별적인 강세장이 종료되고 옥석 가리기가 본격화된 만큼, 기업의 본질 가치에 집중하는 정석 투자가 그 어느 때보다 빛을 발할 시점입니다. 다가오는 옵션 만기일의 변동성 확대를 오히려 우량주 저가 매수의 기회로 활용하는 지혜가 필요합니다.</p>
                    </div>
                </section>
            </div>
"""

start_tag = '<!-- 여기에 새로운 콘텐츠를 추가하세요 -->'

start_idx = template_content.find(start_tag)
end_idx = template_content.find('</div>\n    </main>', start_idx)

if start_idx != -1 and end_idx != -1:
    new_html = template_content[:start_idx] + main_content + template_content[end_idx:]
    # update title
    new_html = new_html.replace('<title>Page Title - Invest Insight</title>', '<title>일일 투자 인사이트 - 2026-08-08</title>')
    with open(target_html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)

with open(target_json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_entry = {
    "title": "일일 투자 인사이트 — 2026-08-08",
    "filename": "daily/daily_2026-08-08.html",
    "description": "한국 KOSPI 단기 조정 및 외국인 매도세, 미국 S&P500 사상 최고치 경신과 고용 둔화에 따른 금리 인하 기대감, M7 종목별 차별화 심층 분석 리포트",
    "category": "시장동향",
    "date": "2026-08-08"
}

data.insert(0, new_entry)

with open(target_json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("success")
