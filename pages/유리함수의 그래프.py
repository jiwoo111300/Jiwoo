import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 제목
st.title("📈 유리함수 y = k/x 그래프 학습")

# 설명
st.markdown("""
## 🔍 유리함수의 성질 정리

- **정의역:** x ≠ 0  
- **치역:** y ≠ 0  
- **점근선:** x축(y=0), y축(x=0)  
- **대칭성:** 원점에 대하여 점대칭, y=x, y=-x에 대하여 대칭  
- **그래프의 위치:**  
  - k > 0 → 제1, 제3사분면  
  - k < 0 → 제2, 제4사분면  
- **|k|의 변화:** |k|이 커질수록 그래프는 원점에서 멀어짐
""")

# 슬라이더로 k 값 조절
k = st.slider("📏 k 값 조절 (k ≠ 0)", -10.0, 10.0, 1.0, 0.1)
if k == 0:
    st.warning("k는 0이 될 수 없습니다. 다른 값을 선택하세요.")
else:
    # 그래프 그리기
    x = np.linspace(-10, 10, 400)
    x = x[x != 0]
    y = k / x

    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"y = {k:.2f}/x", color="blue")
    ax.axhline(0, color="gray", linestyle="--", linewidth=1)
    ax.axvline(0, color="gray", linestyle="--", linewidth=1)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

    # k의 부호에 따른 설명
    if k > 0:
        st.success("k > 0 이므로 그래프는 제1, 제3사분면에 위치합니다.")
    else:
        st.info("k < 0 이므로 그래프는 제2, 제4사분면에 위치합니다.")

# 구분선
st.markdown("---")

# 확인문제
st.header("📝 확인문제")

st.markdown("""
**1️⃣ 개념 확인 문제**  
유리함수 y = k/x의 정의역과 치역을 각각 쓰시오.

**2️⃣ 유형 문제**  
k = -3일 때, 그래프가 지나는 사분면을 쓰시오.

**3️⃣ 심화 문제**  
|k|의 값이 커질수록 그래프가 원점에서 멀어지는 이유를 설명하시오.
""")
