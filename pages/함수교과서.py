import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 페이지 제목
st.title("이차함수의 그래프 기본형인 (y = ax²) 분석하기")

# 설명
st.write("""
이 앱은 **이차함수의 기본형**인  
\\( y = ax^2 \\) 의 그래프를 탐구하기 위한 학습 도구입니다.

슬라이더를 움직여 `a` 값을 바꾸면서,
- **a > 0** 일 때는 아래로 볼록한 그래프  
- **a < 0** 일 때는 위로 볼록한 그래프  
- **|a|** 값이 커질수록 그래프가 **더 가파르게(폭이 좁게)**  
되는 현상을 직접 확인해보세요!
""")

# 사용자 입력 - a값 슬라이더
a = st.slider("a 값 선택", min_value=-5.0, max_value=5.0, value=1.0, step=0.1)

# 데이터 생성
x = np.linspace(-5, 5, 400)
y = a * x**2

# 그래프 그리기
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y, label=f"y = {a:.2f}x²", color='blue')
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(f"이차함수 y = {a:.2f}x² 의 그래프")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# 귀납적 탐구 질문
st.subheader("생각해보기 🤔")
st.markdown("""
- `a` 값이 **양수일 때** 그래프의 모양은 어떤가요?  
- `a` 값이 **음수일 때**는요?  
- `a`의 **절댓값이 커질수록** 그래프의 폭(가파름)은 어떻게 변하나요?  
""")

st.info("💡 관찰을 통해 직접 규칙을 찾아보세요!")
