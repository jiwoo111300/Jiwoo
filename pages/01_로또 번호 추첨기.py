import streamlit as st
import random
import requests
import pandas as pd
from typing import List, Tuple

# --- 로또 관련 설정 ---
MIN_NUM = 1
MAX_NUM = 45
COUNT = 6
LOTTO_API_URL = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="

# --- 함수 정의 ---

# 1. 로또 번호 생성 함수
def generate_lotto_numbers() -> List[int]:
    """1부터 45 중 중복 없는 6개의 숫자를 오름차순으로 생성합니다."""
    # random.sample()은 중복 없이 무작위로 숫자를 선택합니다.
    lotto_numbers = random.sample(range(MIN_NUM, MAX_NUM + 1), COUNT)
    lotto_numbers.sort()
    return lotto_numbers

# 2. 최신 당첨 번호 가져오기 함수 (캐싱 사용)
@st.cache_data
def get_latest_lotto_info(drw_no: int = 0) -> Tuple[int, List[int], int]:
    """
    동행복권 API에서 지정된 회차(drw_no=0이면 최신)의 당첨 번호와 보너스 번호를 가져옵니다.
    """
    if drw_no == 0:
        # 최신 회차 번호를 찾기 위한 임시 API 호출 (max_drwNo를 찾기 위함)
        temp_response = requests.get(LOTTO_API_URL + str(1)) 
        if temp_response.status_code != 200:
            return 0, [], 0
        latest_drw_no = 0
        # 실제로 최신 회차를 가져오려면 동행복권 메인 페이지 크롤링이 필요하지만, 
        # 여기서는 가장 최근에 성공한 회차를 가정하고 API를 호출합니다.
        # 실제 최신 회차를 가져오는 더 견고한 로직을 위해서는 HTML 파싱이 필요합니다.
        # 편의상, API에서 응답이 'success'일 때까지 회차를 줄여가며 검색할 수 있습니다.
        
        # 임시로 최신 회차 번호를 매우 큰 값으로 가정하고 줄여가며 검색하는 로직 (간소화)
        drw_no_search = 1100 # 예시로 최근 회차에 가까운 큰 번호부터 시작
        while drw_no_search > 0:
            response = requests.get(LOTTO_API_URL + str(drw_no_search))
            data = response.json()
            if data.get('returnValue') == 'success':
                drw_no = data['drwNo']
                break
            drw_no_search -= 1
        
        if drw_no == 0:
            st.error("최신 로또 회차 정보를 가져오는 데 실패했습니다. 잠시 후 다시 시도해 주세요.")
            return 0, [], 0

    response = requests.get(LOTTO_API_URL + str(drw_no))
    if response.status_code != 200:
        return drw_no, [], 0
        
    data = response.json()
    if data.get('returnValue') != 'success':
        st.error(f"{drw_no}회차 정보를 찾을 수 없습니다.")
        return drw_no, [], 0

    win_numbers = sorted([
        data['drwtNo1'], data['drwtNo2'], data['drwtNo3'], 
        data['drwtNo4'], data['drwtNo5'], data['drwtNo6']
    ])
    bonus_number = data['bnusNo']
    
    return data['drwNo'], win_numbers, bonus_number

# 3. 당첨 여부 비교 함수
def check_match(my_numbers: List[int], win_numbers: List[int], bonus_number: int) -> str:
    """내 번호와 당첨 번호를 비교하여 결과를 반환합니다."""
    
    # 겹치는 일반 번호 개수
    match_count = len(set(my_numbers) & set(win_numbers))
    
    # 보너스 번호 일치 여부
    is_bonus_match = bonus_number in my_numbers
    
    # 등수 판별
    if match_count == 6:
        return "🏆 **1등 당첨!** (6개 일치)"
    elif match_count == 5 and is_bonus_match:
        return "🥈 **2등 당첨!** (5개 일치 + 보너스 일치)"
    elif match_count == 5:
        return "🥉 **3등 당첨!** (5개 일치)"
    elif match_count == 4:
        return "🏅 **4등 당첨!** (4개 일치)"
    elif match_count == 3:
        return "💸 **5등 당첨!** (3개 일치)"
    else:
        return "😔 다음 기회에... (일치: " + str(match_count) + "개)"

# --- Streamlit UI 구현 ---

st.set_page_config(page_title="로또 번호 추첨기", layout="wide")
st.title("🔢 대한민국 로또 번호 추첨기")

# 사이드바에서 구매 세트 수 입력 받기
with st.sidebar:
    st.header("설정")
    # 1 세트부터 10 세트까지 선택 가능
    num_sets = st.slider("생성할 로또 세트 수", MIN_NUM, 10, 5) 
    st.write(f"총 **{num_sets}** 세트의 번호를 생성합니다.")
    
    # 최신 로또 번호 정보 가져오기 시도
    drw_no, win_numbers, bonus_number = get_latest_lotto_info(0)
    
    if drw_no:
        st.subheader("최신 당첨 번호")
        st.write(f"**제 {drw_no}회 추첨 결과**")
        st.markdown(
            f"**당첨 번호:** {'-'.join(map(str, win_numbers))}"
            f"<br>**보너스 번호:** **{bonus_number}**", 
            unsafe_allow_html=True
        )
        st.session_state['latest_win_numbers'] = win_numbers
        st.session_state['latest_bonus_number'] = bonus_number
        st.session_state['latest_drw_no'] = drw_no
    else:
        st.warning("최신 당첨 번호를 가져올 수 없습니다. 비교 기능이 제한됩니다.")
        st.session_state['latest_win_numbers'] = []
        st.session_state['latest_bonus_number'] = 0
        st.session_state['latest_drw_no'] = 0

# 메인 버튼
if st.button(f"🎉 행운의 번호 {num_sets} 세트 생성!"):
    st.subheader("✅ 생성된 로또 번호")
    st.balloons()
    
    results_df = []
    
    # 번호 생성 및 비교 결과 테이블 준비
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write("### 생성 번호")
        
    with col2:
        if st.session_state['latest_drw_no']:
            st.write(f"### 제 {st.session_state['latest_drw_no']}회 당첨 결과 비교")
        else:
            st.write("### 당첨 번호 비교 (정보 없음)")


    # 선택된 세트 수만큼 번호 생성
    for i in range(1, num_sets + 1):
        my_numbers = generate_lotto_numbers()
        
        # 비교 결과
        if st.session_state['latest_drw_no']:
            result = check_match(
                my_numbers, 
                st.session_state['latest_win_numbers'], 
                st.session_state['latest_bonus_number']
            )
        else:
            result = "비교 불가"

        # 결과를 DataFrame에 추가 (테이블 출력을 위해)
        results_df.append({
            '세트': i,
            '내 번호': ' '.join(f"**{n}**" for n in my_numbers),
            '비교 결과': result
        })

    # 결과를 Streamlit 테이블로 출력
    df = pd.DataFrame(results_df)
    
    # HTML 마크다운으로 깔끔하게 출력
    for index, row in df.iterrows():
        col1.markdown(f"**{row['세트']}세트:** {row['내 번호']}", unsafe_allow_html=True)
        col2.markdown(f"**{row['세트']}세트:** {row['비교 결과']}", unsafe_allow_html=True)
        
    st.markdown("---")
    st.success("새로운 행운이 당신에게 깃들기를 바랍니다!")

st.markdown("---")
st.caption("로또 번호는 무작위로 생성되며, 당첨을 보장하지 않습니다. 즐거운 마음으로 이용해 주세요.")
