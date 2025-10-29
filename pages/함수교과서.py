import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. 페이지 제목 설정
st.title('이차함수의 그래프 기본형($y=ax^2$) 분석')
st.markdown("계수 $a$ 값을 변경하며 그래프의 모양을 관찰하세요.")
st.latex(r'y = ax^2')
st.markdown('---')

# 2. 계수 조정 슬라이더 (메인 화면으로 이동)
# a 값 선택 슬라이더를 메인 화면에 배치합니다.
a = st.slider('계수 $a$ 값 선택:', min_value=-5.0, max_value=5.0, value=1.0, step=0.1, help="a가 0일 때 이차함수가 아닙니다.")

# 3. a가 0일 때의 예외 처리 및 경고 메시지
if abs(a) < 0.05:
    st.warning('경고: a가 0에 가까워 x축에 가깝습니다. 해석에 주의하세요.')
    if a == 0:
        a = 0.001 

# 4. 그래프 데이터 생성
x = np.linspace(-5, 5, 400) # x축 범위 
y = a * x**2 # 이차함수 y = ax^2 계산

# 5. Matplotlib을 사용하여 그래프 생성
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

# 축 범위 고정
ax.set_xlim(-5, 5)
ax.set_ylim(-15, 15)

ax.legend()

# 6. Streamlit에 그래프 표시
st.pyplot(fig)

st.markdown('---')

## 🧐 그래프 관찰 및 학습 가이드

st.subheader('관찰 결과 및 학습 가이드')

st.markdown('### 1. 볼록성 ($a$의 부호)')
계수 $a$ 값의 부호에 따라 그래프의 **볼록성**이 결정됩니다.

* **$a > 0$ (양수):** 그래프는 **아래로 볼록**합니다. (최솟값을 가집니다)
* **$a < 0$ (음수):** 그래프는 **위로 볼록**합니다. (최댓값을 가집니다)

st.markdown('### 2. 폭 ($a$의 절댓값 $|a|$)')
계수 $a$ 값의 **절댓값 $|a|$**의 크기에 따라 그래프의 **폭**이 달라집니다.

* $|a|$가 **클수록** (예: $|2| > |1|$), 그래프는 y축에 가까워져 **폭이 좁아집니다**.
* $|a|$가 **작을수록** (예: $|0.5| < |1|$), 그래프는 x축에 가까워져 **폭이 넓어집니다**.')
