import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('이차함수의 그래프 기본형 분석')
st.markdown("계수 $a$ 값을 변경하며 그래프의 모양을 관찰하세요.")
st.latex(r'y = ax^2')
st.markdown('---')

with st.sidebar:
    st.header('계수 a 설정')
    a = st.slider('a 값 선택:', min_value=-5.0, max_value=5.0, value=1.0, step=0.1)

if abs(a) < 0.05:
    st.warning('경고: a가 0에 가까워 x축에 가깝습니다.')
    if a == 0:
        a = 0.001 

x = np.linspace(-5, 5, 400) 
y = a * x**2 

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, label=f'y = {a:.1f}x^2', color='blue', linewidth=2)
ax.set_title(f'그래프: y = {a:.1f}x^2')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True, linestyle=':', alpha=0.7)
ax.axhline(0, color='gray', linewidth=1)
ax.axvline(0, color='gray', linewidth=1)
ax.set_xlim(-5, 5)
ax.set_ylim(-15, 15)
ax.legend()
st.pyplot(fig)

st.markdown('---')

st.subheader('관찰 결과')
st.markdown('### 1. 볼록성')
st.markdown('* **a > 0:** 아래로 볼록')
st.markdown('* **a < 0:** 위로 볼록')

st.markdown('### 2. 폭')
st.markdown('* $|a|$가 **클수록** 폭이 **좁아집니다**.')
st.markdown('* $|a|$가 **작을수록** 폭이 **넓어집니다**.')
