import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit 페이지 설정
st.set_page_config(
    page_title="유리함수 그래프 교과서 (y=k/x)",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📚 유리함수 그래프 교과서 (고등학교 수학)")
st.header("1. 유리함수란 무엇인가?")

# 유리함수의 정의
st.markdown("""
**유리함수(Rational Function)**는 함수 $y=f(x)$에서 $f(x)$가 두 다항식 $P(x)$, $Q(x)$에 대하여 $\mathbf{f(x) = \frac{P(x)}{Q(x)}}$ ($Q(x) \neq 0$) 꼴로 나타내어지는 함수를 말합니다.
""")
# 유리함수의 예시
st.latex(r"y = \frac{x+1}{x^2-4}, \quad y = \frac{3}{x}, \quad y = 2x-1 \quad (\text{다항함수도 분모가 1인 유리함수입니다.})")

st.header("2. 유리함수의 정의역")

# 정의역 설명
st.markdown("""
유리함수 $f(x) = \frac{P(x)}{Q(x)}$의 **정의역**은 분모 $Q(x)$를 0으로 만들지 않는 실수 전체의 집합입니다.
즉, $\mathbf{\{ x \mid Q(x) \neq 0, x \text{는 실수} \}}$ 입니다.
""")
st.info(r"$\mathbf{y = \frac{k}{x}}$ ($k \neq 0$)의 경우, 분모가 $x$이므로 $\mathbf{x \neq 0}$인 모든 실수가 정의역입니다.")

st.markdown("---")

## 📊 $y = \frac{k}{x}$ 그래프 살펴보기

st.header("3. 기본형 유리함수 $y = \frac{k}{x}$ 의 그래프")

# k 값 조정을 위한 슬라이더
st.sidebar.title("⭐ 그래프 매개변수 설정")
k_value = st.sidebar.slider(
    "상수 k 값 조정 ($k \neq 0$)",
    min_value=-5.0,
    max_value=5.0,
    value=1.0,
    step=0.1,
    format="%.1f"
)

# k가 0인 경우 처리 (유리함수가 아니므로)
if k_value == 0:
    st.warning("k는 0이 아니어야 합니다. k=0이면 $y=0$이 되어 유리함수(분수함수)가 아닌 상수함수가 됩니다.")
    k_value = 0.001 # 그래프를 그리기 위해 0에 가까운 값으로 대체
    st.sidebar.markdown(f"**$\mathbf{k}$ 값**: $\mathbf{0.0}$ (그래프는 $\mathbf{k=0.001}$로 표시)")
else:
    st.sidebar.markdown(f"**$\mathbf{k}$ 값**: $\mathbf{{k\_value}}$")

st.latex(f"y = \\frac{{ {k_value:.1f} }}{{x}} \quad (k = {k_value:.1f})")

# 그래프 그리기
fig, ax = plt.subplots(figsize=(8, 8))
