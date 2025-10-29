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

# --- CSS 함수: 배경색 변경 ---
def set_pink_background():
    """앱 전체 배경색을 연한 핑크색으로 설정하는 CSS를 삽입합니다."""
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #ffe4e1; /* MistyRose (연한 핑크색 계열) */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# --- 함수 정의 (이전 코드와 동일, API 호출 함수는 캐싱 유지) ---

# 1. 로또 번호 생성 함수
def generate_lotto_numbers() -> List[int]:
    """1부터 45 중 중복 없는 6개의 숫자를 오름차순으로 생성합니다."""
    lotto_numbers = random.sample(range(MIN_NUM, MAX_NUM + 1), COUNT)
    lotto_numbers.sort()
    return lotto_numbers

# 2. 최신 당첨 번호 가져오기 함수 (캐싱 사용)
@st.cache_data
def get_latest_lotto_info(drw_no: int = 0) -> Tuple[int, List[int], int]:
    """동행복권 API에서 지정된 회차(drw_no=0이면 최신)의 당첨 번호와 보너스 번호를 가져옵니다."""
    if drw_no == 0:
        # 최신 회차 번호를 찾기 위한 로직 (간소화)
        drw_no_search = 1100 # 예시로 최근 회차에 가까운 큰 번호부터 시작 (실제 회차에 따라 조정 필요)
        current_drw_no = 0
        while drw_no_search > 0:
            try:
                response = requests.get(LOTTO_API_URL + str(drw_no_search), timeout=5)
                data = response.json()
                if data.get('returnValue') == 'success':
                    current_drw_no = data['drwNo']
                    break
                drw_no_search -= 1
            except requests.exceptions.RequestException:
                drw_no_search -= 1
        
        if current_drw_no == 0:
            return 0, [], 0
        drw_no = current_drw_no

    try:
        response = requests.get(LOTTO_API_URL + str(drw_no), timeout=5)
        data = response.json()
    except requests.exceptions.RequestException:
        return drw_no, [], 0 # 요청 실패 시 빈 값 반환

    if data.get('returnValue') != 'success':
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
    
    match_count = len(set(my_numbers) & set(win_numbers))
    is_bonus_match = bonus_number in my_numbers
    
    # 등수 판별
    if match_count == 6:
        return "🏆 **1등 당첨!**"
    elif match_count == 5 and is_bonus_match:
        return "🥈 **2등 당첨!**"
    elif match_count == 5:
        return "🥉 **3등 당첨!**"
    elif match_count == 4:
        return "🏅 **4등 당첨!**"
    elif match_count == 3:
        return "💸 **5등 당첨!**"
    else:
        return "😔 다음 기회에... (일치: " + str(match_count) + "개)"

# --- Streamlit UI 구현 ---

# 1. 배경색 설정
set_pink_background()

st.set_page_config(page_title="로또 번호 추첨기 (핑크)", layout="wide")
st.title("💖 행운의 로또 번호 추첨기")

# 사이드바에서 구매 세트 수 입력 받기 (Number Input으로 변경)
with st.sidebar:
    st.header("설정")
    
    # 숫자 입력 위젯 사용 (min_value와 max_value 설정)
    num_sets = st.number_input(
        "생성할 로또 세트 수 (1~100)", 
        min_value=1, 
        max_value=100, 
        value=5, 
        step=1
    )
    st.write(f"총 **{num_sets}** 세트의 번호를 생성합니다.")
    
    st.markdown("---")
    
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
        # 세션 상태에 저장
        st.session_state['latest_win_numbers'] = win_numbers
        st.session_state['latest_bonus_number'] = bonus_number
        st.session_state['latest_drw_no'] = drw_no
    else:
        st.warning("최신 당첨 번호를 가져올 수 없습니다. 비교 기능이 제한됩니다.")
        st.session_state['latest_drw_no'] = 0


# 메인 버튼
if st.button(f"✨ 행운의 번호 {num_sets} 세트 생성 및 비교!"):
    st.subheader("✅ 생성된 로또 번호")
    st.balloons()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write("### 생성 번호")
        
    with col2:
        if st.session_state['latest_drw_no']:
            st.write(f"### 제 {st.session_state['latest_drw_no']}회 당첨 결과 비교")
        else:
            st.write("### 당첨 번호 비교 (정보 없음)")


    # 선택된 세트 수만큼 번호 생성 및 결과 출력
    for i in range(1, num_sets + 1):
        my_numbers = generate_lotto_numbers()
        
        # 비교 결과
        result = "비교 불가"
        if st.session_state['latest_drw_no']:
            result = check_match(
                my_numbers, 
                st.session_state['latest_win_numbers'], 
                st.session_state['latest_bonus_number']
            )

        # HTML 마크다운으로 깔끔하게 출력 (번호는 굵게 표시)
        formatted_numbers = ' '.join(f"<span style='font-size: 18px; font-weight: bold;'>{n}</span>" for n in my_numbers)
        
        col1.markdown(f"**{i}세트:** {formatted_numbers}", unsafe_allow_html=True)
        col2.markdown(f"**{i}세트:** {result}", unsafe_allow_html=True)
        
    st.markdown("---")
    st.success("새로운 행운이 당신에게 깃들기를 바랍니다! 🍀")

st.markdown("---")
st.caption("로또 번호는 무작위로 생성되며, 당첨을 보장하지 않습니다. 즐거운 마음으로 이용해 주세요.")
