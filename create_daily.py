import json

base_html_path = '/home/ubuntu/Workspace/GitHub/invest/template/base_template.html'
daily_html_path = '/home/ubuntu/Workspace/GitHub/invest/daily/daily_2026-06-29.html'
daily_json_path = '/home/ubuntu/Workspace/GitHub/invest/daily.json'

with open(base_html_path, 'r', encoding='utf-8') as f:
    template = f.read()

main_content = """
            <div class="space-y-12">
                <!-- Header -->
                <div class="text-center py-10 border-b border-slate-200 dark:border-gray-800">
                    <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 dark:text-white mb-4">
                        일일 투자 <span class="gradient-text">인사이트</span>
                    </h2>
                    <p class="text-lg text-slate-600 dark:text-slate-400">
                        2026년 6월 29일 - 롤러코스터 장세 속 변동성 점검 및 하반기 전략
                    </p>
                </div>

                <!-- 1. 한눈에 보기 -->
                <section class="reveal">
                    <h3 class="text-2xl font-bold mb-6 flex items-center gap-2">
                        <span class="text-sky-500"><i class="fa-solid fa-bolt"></i></span> 한눈에 보기
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="bg-white dark:bg-gray-800 rounded-2xl p-6 shadow-sm border border-slate-100 dark:border-gray-700">
                            <ul class="space-y-4 text-slate-700 dark:text-slate-300">
                                <li class="flex items-start gap-3">
                                    <i class="fa-solid fa-check text-sky-500 mt-1"></i>
                                    <span><strong>한국 증시 극심한 변동성:</strong> 코스피는 외국인의 1.2조 원 대규모 매도세에 8,400선으로 후퇴하며 지난주 서킷브레이커 여파가 지속됨.</span>
                                </li>
                                <li class="flex items-start gap-3">
                                    <i class="fa-solid fa-check text-sky-500 mt-1"></i>
                                    <span><strong>미국 기술주 차익실현 및 M7 혼조세:</strong> 연준의 매파적 스탠스와 AI 수익화 의구심으로 S&P500 및 나스닥 5거래일 연속 하락, 애플/엔비디아 약세.</span>
                                </li>
                                <li class="flex items-start gap-3">
                                    <i class="fa-solid fa-check text-sky-500 mt-1"></i>
                                    <span><strong>매크로 압박 심화:</strong> 원/달러 환율은 17년 만에 최고치인 1,545.2원으로 마감하며 수급에 부담을 주고 있으나, 국제 유가는 64달러대 안정화.</span>
                                </li>
                            </ul>
                        </div>
                        <div class="bg-white dark:bg-gray-800 rounded-2xl p-6 shadow-sm border border-slate-100 dark:border-gray-700 overflow-x-auto">
                            <table class="w-full text-left border-collapse">
                                <thead>
                                    <tr class="border-b border-slate-200 dark:border-gray-700 text-slate-500 dark:text-slate-400 text-sm">
                                        <th class="py-2 px-4 font-medium">지수/지표</th>
                                        <th class="py-2 px-4 font-medium">종가</th>
                                        <th class="py-2 px-4 font-medium">등락률</th>
                                    </tr>
                                </thead>
                                <tbody class="text-slate-700 dark:text-slate-200 font-mono text-sm">
                                    <tr class="border-b border-slate-100 dark:border-gray-750">
                                        <td class="py-3 px-4 font-sans font-medium">KOSPI</td>
                                        <td class="py-3 px-4">8,412.30</td>
                                        <td class="py-3 px-4 text-blue-500">-1.50%</td>
                                    </tr>
                                    <tr class="border-b border-slate-100 dark:border-gray-750">
                                        <td class="py-3 px-4 font-sans font-medium">KOSDAQ</td>
                                        <td class="py-3 px-4">921.50</td>
                                        <td class="py-3 px-4 text-blue-500">-2.10%</td>
                                    </tr>
                                    <tr class="border-b border-slate-100 dark:border-gray-750">
                                        <td class="py-3 px-4 font-sans font-medium">S&P 500</td>
                                        <td class="py-3 px-4">5,612.45</td>
                                        <td class="py-3 px-4 text-blue-500">-1.20%</td>
                                    </tr>
                                    <tr class="border-b border-slate-100 dark:border-gray-750">
                                        <td class="py-3 px-4 font-sans font-medium">NASDAQ</td>
                                        <td class="py-3 px-4">18,245.10</td>
                                        <td class="py-3 px-4 text-blue-500">-1.80%</td>
                                    </tr>
                                    <tr>
                                        <td class="py-3 px-4 font-sans font-medium">USD/KRW</td>
                                        <td class="py-3 px-4">1,545.20</td>
                                        <td class="py-3 px-4 text-red-500">+13.2원</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>

                <!-- 2. 한국 시장 심층 분석 -->
                <section class="reveal">
                    <h3 class="text-2xl font-bold mb-4 flex items-center gap-2">
                        <span>🇰🇷</span> 한국 시장 심층 분석
                    </h3>
                    <div class="prose dark:prose-invert max-w-none text-slate-700 dark:text-slate-300 space-y-4">
                        <p>
                            6월 말 국내 증시는 전례 없는 변동성을 보여주고 있습니다. 코스피 지수는 전 거래일 대비 1.50% 하락한 8,412.30으로 마감했으며, 코스닥은 2.10% 하락한 921.50을 기록했습니다. 지난주 서킷브레이커와 사이드카가 연이어 발동되며 시장의 공포 심리가 극에 달했던 여파가 가시지 않은 모습입니다. 이러한 하락의 가장 큰 원인은 원/달러 환율 급등에 따른 <strong>외국인 투자자들의 거센 매도세</strong>입니다. 이날 외국인은 유가증권시장에서만 약 1조 2천억 원을 순매도하며 지수 하락을 주도했고, 기관이 8,000억 원을 순매수하며 방어에 나섰으나 역부족이었습니다.
                        </p>
                        <p>
                            업종별 흐름을 살펴보면, <strong>반도체 섹터의 약세</strong>가 두드러졌습니다. 애플발 메모리 수요 둔화 우려와 미국 기술주 차익실현에 연동되며 삼성전자와 SK하이닉스가 각각 2%대 하락을 기록했습니다. 반면, 낙폭 과대 인식에 따른 저가 매수세가 유입된 <strong>이차전지 섹터</strong>(+1.2%)와, 수출 호조세가 지속되며 환율 상승의 수혜를 기대할 수 있는 <strong>자동차 섹터</strong>(+0.8%)는 상대적으로 강세를 보였습니다. 시장에서는 금리 인하 기대감이 후퇴하는 가운데 수출 실적이 뒷받침되는 업종으로의 자금 쏠림 현상이 뚜렷하게 나타나고 있습니다.
                        </p>
                        <p>
                            증권가에서는 현재의 지수 급락이 펀더멘털의 훼손보다는 수급적 꼬임과 심리적 공포에 기인한 것으로 평가하고 있습니다. 다가오는 7월 초 삼성전자의 2분기 잠정 실적 발표를 기점으로 실적 장세가 본격화될 경우, 반도체를 중심으로 한 주도주들의 이익 개선세가 확인되며 분위기 반전을 시도할 수 있을 것으로 전망됩니다. 따라서 8,400선 부근에서는 추가적인 투매보다는 실적 호전주에 대한 선별적인 접근이 필요한 시점입니다.
                        </p>
                    </div>
                </section>

                <!-- 3. 미국 시장 심층 분석 -->
                <section class="reveal">
                    <h3 class="text-2xl font-bold mb-4 flex items-center gap-2">
                        <span>🇺🇸</span> 미국 시장 심층 분석
                    </h3>
                    <div class="prose dark:prose-invert max-w-none text-slate-700 dark:text-slate-300 space-y-4">
                        <p>
                            미국 뉴욕 증시는 고점 부담과 인플레이션 고착화 우려 속에 약세 흐름을 이어가고 있습니다. S&P 500은 1.20% 하락한 5,612.45, 나스닥은 1.80% 하락한 18,245.10을 기록하며 주요 지수 모두 5거래일 연속 하락 마감했습니다. 6월 FOMC에서 확인된 연준의 매파적 스탠스와 연내 추가 금리 인상 가능성이 국채 금리를 자극하면서, 밸류에이션 부담이 높은 기술주에 직격탄이 되었습니다. 또한, 7월 초 예정된 고용보고서 발표를 앞두고 시장 전반에 관망세가 짙게 깔려 있습니다.
                        </p>
                        <p>
                            특히 시장을 이끌어온 <strong>매그니피센트 7(M7) 종목들의 차별화와 조정</strong>이 눈에 띕니다. AI 수익화 지연 우려와 오픈AI의 IPO 연기 검토 소식에 엔비디아가 -3.2% 큰 폭으로 하락했고, 아이폰 수요 둔화 루머가 돌고 있는 애플도 -2.5% 하락하며 지수 하락을 주도했습니다. 마이크로소프트(-1.8%), 메타(-1.5%), 아마존(-1.2%) 등도 약세를 면치 못했습니다. 반면, 알파벳(+0.5%)과 테슬라(+2.1%)는 개별적인 호재와 저가 매수세에 힘입어 상승 마감하며 그룹 내에서도 주가 흐름이 엇갈리는 모습입니다.
                        </p>
                        <p>
                            이러한 빅테크의 조정은 단순한 차익실현을 넘어, 'AI 버블론'에 대한 시장의 현실적인 검증 과정으로 해석됩니다. 투자자들은 이제 막연한 성장 기대감보다는 실제 숫자로 증명되는 매출과 이익률에 더욱 집중하고 있습니다. 다가오는 2분기 빅테크 실적 발표에서 클라우드 부문의 성장세와 AI 투자의 구체적인 성과 지표가 향후 나스닥의 방향성을 결정짓는 핵심 트리거가 될 것입니다.
                        </p>
                    </div>
                </section>

                <!-- 4. 매크로 & 글로벌 이슈 -->
                <section class="reveal">
                    <h3 class="text-2xl font-bold mb-4 flex items-center gap-2">
                        <span>🌍</span> 매크로 & 글로벌 이슈
                    </h3>
                    <div class="prose dark:prose-invert max-w-none text-slate-700 dark:text-slate-300 space-y-4">
                        <p>
                            매크로 환경은 주식 시장에 가장 강력한 하방 압력으로 작용하고 있습니다. 특히 <strong>원/달러 환율</strong>은 전 거래일 대비 13.2원 폭등한 1,545.2원으로 마감하며, 2009년 글로벌 금융위기 직후인 2009년 3월(1,549원) 이후 17년 3개월 만에 최고치를 경신했습니다. 미국 기준금리(상단 3.75%)의 장기화 우려 속에 달러인덱스가 강세를 보이고, 중동 지역의 지정학적 긴장(호르무즈 해협 등)으로 인한 안전자산 선호 심리가 원화 가치를 크게 끌어내리고 있습니다. 초고환율 상황은 외국인 투자자의 환차손 우려를 자극하여 대규모 자금 이탈을 초래하고 있습니다.
                        </p>
                        <p>
                            <strong>국제 유가</strong>의 경우, 사우디아라비아의 공급 정상화 기대감과 미국-이란 간 종전 협상 타결 소식에 힘입어 두바이유 기준 배럴당 64달러대까지 하락 안정화되었습니다. 지난 5월 90달러대에서 큰 폭으로 하락한 것으로, 이는 글로벌 인플레이션 압력을 다소 완화시켜주는 긍정적인 요인입니다. 그러나 잠재적인 무력 충돌 재개 등 지정학적 리스크가 완전히 해소된 것은 아니므로 유가의 변동성 리스크는 여전히 남아 있습니다.
                        </p>
                        <p>
                            <strong>금리 동향</strong>을 보면, 연준은 인플레이션 지표가 목표치인 2%로 확실히 수렴하기 전까지는 섣불리 통화정책을 완화하지 않겠다는 의지를 피력하고 있습니다. 시장은 당초 예상했던 상반기 금리 인하 시나리오를 전면 수정하여, 고금리 환경이 내년까지 이어질 수 있다는 'Higher for Longer'에 완전히 적응해가는 과도기에 놓여 있습니다. 이는 증시 전반의 밸류에이션 멀티플을 낮추는 구조적 요인으로 작용하고 있습니다.
                        </p>
                    </div>
                </section>

                <!-- 5. 투자 시사점 & 전략 -->
                <section class="reveal">
                    <h3 class="text-2xl font-bold mb-4 flex items-center gap-2">
                        <span>💡</span> 투자 시사점 & 전략
                    </h3>
                    <div class="bg-slate-100 dark:bg-gray-800/50 rounded-2xl p-6 md:p-8 border border-slate-200 dark:border-gray-700">
                        <div class="prose dark:prose-invert max-w-none text-slate-700 dark:text-slate-300 space-y-4">
                            <p>
                                <strong>단기적 관망 속 3분기 실적주 매집 기회:</strong> 이번 주 시장은 7월 초로 예정된 미국의 주요 경제 지표(고용보고서, ISM 제조업 지수 등)와 FOMC 의사록 공개 전까지 방향성 탐색 구간이 이어질 것입니다. 환율 1,540원대 이상의 초고환율 구간에서는 외국인 수급의 추세적 유입을 기대하기 어려우므로, 지수의 V자 반등보다는 하방 지지력을 확인하는 과정이 선행될 것입니다.
                            </p>
                            <p>
                                <strong>주목해야 할 리스크:</strong> 가장 큰 리스크는 '실적에 대한 눈높이'입니다. 최근의 주가 하락에도 불구하고 여전히 높은 멀티플을 적용받고 있는 기술주와 반도체 섹터는 실적 발표에서 시장의 높은 기대치를 충족시키지 못할 경우 2차 하락 파동을 겪을 위험이 있습니다. 또한, 환율의 오버슈팅이 국내 수입 물가 상승으로 이어져 소비 위축을 초래할 매크로 둔화 리스크도 점검해야 합니다.
                            </p>
                            <p>
                                <strong>투자 전략:</strong> 지수 8,400선 이하에서는 매도 실익이 크지 않습니다. 오히려 하반기 실적 가시성이 높은 섹터로 포트폴리오를 압축할 기회입니다. 환율 상승에 따른 영업이익 증가가 확실시되는 <strong>자동차 및 기계/방산</strong> 섹터, 그리고 단기 조정폭이 컸으나 중장기 성장성이 유효한 <strong>AI 반도체 밸류체인</strong> 내 핵심 종목들에 대해 분할 매수하는 전략이 유효합니다. 불확실성 구간에서는 현금 비중을 일정 수준(20~30%) 유지하며 시장 변동성을 역이용하는 인내심이 필요합니다.
                            </p>
                        </div>
                    </div>
                </section>
            </div>
"""

# Extract the template parts before and after the placeholder
start_marker = "<!-- 여기에 새로운 콘텐츠를 추가하세요 -->"
end_marker = "<!-- Footer Section -->"

if start_marker in template and end_marker in template:
    start_idx = template.find(start_marker) + len(start_marker)
    end_idx = template.find(end_marker)
    
    # We will replace what's between start_idx and end_idx (specifically inside max-w-7xl)
    # The template has <div class="max-w-7xl mx-auto"> around it, let's just replace the exact text in template
    # Let's use string replace
    
    # Find the block to replace
    placeholder_block = """<div class="text-center py-20">
                <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 dark:text-white mb-4">
                    새로운 <span class="gradient-text">페이지</span>
                </h2>
                <p class="text-slate-600 dark:text-slate-400">
                    template/base_template.html 파일을 복사하여 이 &lt;main&gt; 영역을 수정하세요.
                </p>
            </div>"""
            
    final_html = template.replace(placeholder_block, main_content)
    
    with open(daily_html_path, 'w', encoding='utf-8') as out_f:
        out_f.write(final_html)
    print("HTML created successfully.")
    
    # Now update JSON
    with open(daily_json_path, 'r', encoding='utf-8') as json_f:
        data = json.load(json_f)
        
    new_entry = {
        "title": "일일 투자 인사이트 — 2026-06-29",
        "filename": "daily/daily_2026-06-29.html",
        "description": "KOSPI 8,400선 조정 및 미국 M7 혼조세, 1,545원 초고환율 매크로 심층 분석 리포트",
        "category": "시장동향",
        "date": "2026-06-29"
    }
    
    data.insert(0, new_entry)
    
    with open(daily_json_path, 'w', encoding='utf-8') as json_f:
        json.dump(data, json_f, ensure_ascii=False, indent=2)
    print("JSON updated successfully.")
else:
    print("Could not find markers in template.")
