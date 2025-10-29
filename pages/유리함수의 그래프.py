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
if abs(k_value) < 0.1: # 0에 가까운 값도 0으로 간주
    st.warning("k는 0이 아니어야 합니다. k=0이면 $y=0$이 되어 유리함수(분수함수)가 아닌 상수함수가 됩니다.")
    
    # 그래프를 그리기 위해 0에 가까운 값으로 대체 (매우 작은 양수)
    k_plot = 0.001 
    st.sidebar.markdown(f"**$\mathbf{{k}}$ 값**: $\mathbf{{k\_value:.1f}}$ (그래프는 $\mathbf{{k={k_plot}}}$로 표시)")
else:
    k_plot = k_value
    st.sidebar.markdown(f"**$\mathbf{{k}}$ 값**: $\mathbf{{k\_value:.1f}}$")

# 그래프 수식 표시
st.latex(f"y = \\frac{{ {k_plot:.1f} }}{{x}} \quad (k = {k_value:.1f})")

# 그래프 그리기
fig, ax = plt.subplots(figsize=(8, 8))
# x_range를 점근선 근처를 피해서 정의
x1 = np.linspace(-8, -0.1, 100) # 음의 무한대에서 0 근처까지
x2 = np.linspace(0.1, 8, 100)   # 0 근처에서 양의 무한대까지

# 그래프 그리기
ax.plot(x1, k_plot / x1, color='blue', label=r'$y = k/x$')
ax.plot(x2, k_plot / x2, color='blue')

# 점근선 표시 (x=0, y=0)
ax.axhline(0, color='gray', linewidth=1, linestyle='--', label="점근선") # x축 (y=0)
ax.axvline(0, color='gray', linewidth=1, linestyle='--') # y축 (x=0)

# 축 및 격자 설정
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)
ax.set_xticks(np.arange(-8, 9, 2))
ax.set_yticks(np.arange(-8, 9, 2))
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_aspect('equal', adjustable='box')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(f"$y = {k_plot:.1f} / x$ 그래프 개형")


st.pyplot(fig)

st.markdown("---")

### 💡 그래프의 주요 특징

#### 1. 지나는 사분면 (개형)
if k_value > 0.1:
    st.success(f"**k > 0 ({k_value:.1f} > 0)**: 그래프는 **제1사분면**과 **제3사분면**을 지납니다.")
elif k_value < -0.1:
    st.error(f"**k < 0 ({k_value:.1f} < 0)**: 그래프는 **제2사분면**과 **제4사분면**을 지납니다.")
else:
    st.warning("k가 0에 매우 가깝습니다. 실제 그래프는 x축(y=0)과 y축(x=0)에 한없이 가까워집니다.")

#### 2. 점근선 (Asymptotes)
st.markdown("""
그래프가 한없이 가까워지지만 만나지 않는 직선을 **점근선**이라고 합니다.
$y = \frac{k}{x}$ 그래프의 점근선은 다음과 같습니다.
* **x축** ($\mathbf{y=0}$)
* **y축** ($\mathbf{x=0}$)
""")

#### 3. 대칭성 (Symmetry)
st.markdown("""
$y = \frac{k}{x}$ 그래프는 다음 세 가지에 대해 대칭입니다.
* **원점** $(0, 0)$에 대하여 **점대칭**
* 두 직선 **$\mathbf{y=x}$** 및 **$\mathbf{y=-x}$**에 대하여 **선대칭**
""")

#### 4. $|k|$의 값과 그래프의 관계
abs_k = np.abs(k_value)
st.markdown(f"""
현재 $|k|$의 값은 $\mathbf{{abs_k:.1f}}$입니다.
* $|k|$의 값이 **커질수록** (슬라이더를 양쪽 끝으로 움직일수록), 그래프의 두 곡선은 **원점에서 점점 멀어집니다**.
* $|k|$의 값이 **작아질수록** (슬라이더를 0에 가까이 움직일수록), 그래프의 두 곡선은 **원점에 점점 가까워집니다**.
""")

st.markdown("---")
st.subheader("마무리 학습")
st.success(r"유리함수 $y=\frac{k}{x}$의 특징을 k값 변화를 통해 잘 이해했습니다! $\mathbf{k \neq 0}$이라는 조건과 **점근선** 및 **대칭성**을 기억하세요.")
