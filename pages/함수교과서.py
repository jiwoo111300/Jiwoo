import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. 페이지 제목 설정
st.title('이차함수의 그래프 기본형($y=ax^2$) 분석하기')

st.markdown("""
이 앱을 통해 이차함수 $y=ax^2$에서 **계수 $a$의 값 변화**가 그래프의 모양에 미치는 영향을 직접 확인해 보세요.
""")

# 함수 수식 표시
st.latex(r'y = ax^2')

st.markdown('---')

# 2. 사용자 입력(a 값) 위젯 설정
# 슬라이더를 사이드바에 배치하여 메인 화면을 깔끔하게 유지합니다.
with st.sidebar:
    st.header('계수 $a$ 값 설정')
    # a는 0이 아니어야 하므로, min/max 범위를 설정합니다.
    a = st.slider('계수 $a$ 선택:', min_value=-5.0, max_value=5.0, value=1.0, step=0.1, help="a가 0일 때 이차함수가 아닙니다.")

# 3. a가 0일 때의 예외 처리 및 경고 메시지
if abs(a) < 0.05: 
    st.warning('⚠️ 경고: $a$ 값이 0에 매우 가깝습니다. 이는 이차함수가 아닌 $y \\approx 0$ (x축)에 가까워집니다. 해석에 주의하세요.')
    # 그래프를 그릴 수 있도록 0이 되지 않게 아주 작은 값으로 조정
    if a == 0:
        a = 0.001 

# 4. 그래프 데이터 생성
x = np.linspace(-5, 5, 400) # x축 범위 (-5에서 5까지 400개 지점)
y = a * x**2 # 이차함수 y = ax^2 계산

# 5. Matplotlib을 사용하여 그래프 생성
# **중요: Matplotlib에서 한글이 깨지는 현상을 방지하기 위해 폰트 설정을 추가할 수 있지만, 
# 클라우드 환경에서는 폰트 파일이 없어 오류가 날 수 있어 일단 생략합니다.
fig, ax = plt.subplots(figsize=(8, 6))

# 그래프 그리기
ax.plot(x, y, label=f'y = {a:.1f}x^2', color='blue', linewidth=2)

# 축 및 제목 설정
ax.set_title(f'이차함수 그래프: $y = {a:.1f}x^2$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True, linestyle=':', alpha=0.7)

# x축(y=0)과 y축(x=0) 표시 (좌표축)
ax.axhline(0, color='gray', linewidth=1)
ax.axvline(0, color='gray', linewidth=1)

# 축 범위 고정 (일관된 시각적 비교를 위해)
ax.set_xlim(-5, 5)
ax.set_ylim(-15, 15)

ax.legend()

# 6. Streamlit에 그래프 표시
st.pyplot(fig)

st.markdown('---')

## 🧐 그래프 관찰 및 학습 가이드

### 1. 그래프의 볼록성 ($a$의 부호)
계수 $a$ 값의 부호에 따라 그래프의 **볼록성**이 결정됩니다. 사용자는 슬라이더를 통해 $a$의 부호를 바꿔가며 이 사실을 귀납적으로 추론할 수 있습니다.

* **$a > 0$ (양수):** 그래프는 **아래로 볼록**합니다. (최솟값을 가집니다)
* **$a < 0$ (음수):** 그래프는 **위로 볼록**합니다. (최댓값을 가집니다)

### 2. 그래프의 폭 ($a$의 절댓값 $|a|$)
계수 $a$ 값의 **절댓값 $|a|$**의 크기에 따라 그래프의 **폭**이 달라집니다.

* $|a|$가 **클수록** (예: $|2| > |1|$), 그래프는 y축에 가까워져 **폭이 좁아집니다**.
* $|a|$가 **작을수록** (예: $|0.5| < |1|$), 그래프는 x축에 가까워져 **폭이 넓어집니다**.
