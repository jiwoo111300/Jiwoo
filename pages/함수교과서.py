import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set page title
st.title('Quadratic Function Graph: y=ax^2 Analysis')

st.markdown("""
Use this app to explore how the coefficient 'a' affects the parabola $y=ax^2$.
""")

# Display the function formula
st.latex(r'y = ax^2')

st.markdown('---')

# 2. User input (coefficient a) widget setup
# Place slider in the sidebar
with st.sidebar:
    st.header('Set Coefficient "a"')
    # Set the range for 'a', avoiding a = 0
    a = st.slider('Select coefficient a:', min_value=-5.0, max_value=5.0, value=1.0, step=0.1, help="a cannot be zero for a quadratic function.")

# 3. Handle a close to zero
if abs(a) < 0.05:
    st.warning('Warning: "a" is close to 0. The function is nearly y = 0 (the x-axis).')
    # Prevent a literal 0 value just in case
    if a == 0:
        a = 0.001 

# 4. Generate graph data
x = np.linspace(-5, 5, 400) 
y = a * x**2 

# 5. Create the Matplotlib plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the graph
ax.plot(x, y, label=f'y = {a:.1f}x^2', color='blue', linewidth=2)

# Set axes, title, and grid
ax.set_title(f'Graph of: y = {a:.1f}x^2')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True, linestyle=':', alpha=0.7)

# Draw x and y axes
ax.axhline(0, color='gray', linewidth=1)
ax.axvline(0, color='gray', linewidth=1)

# Fix axis limits for consistent viewing
ax.set_xlim(-5, 5)
ax.set_ylim(-15, 15)

ax.legend()

# 6. Display the plot in Streamlit
st.pyplot(fig)

st.markdown('---')

# Observations Guide (ASCII only for safety)
st.subheader('Graph Observations and Inferences')

st.markdown('### 1. Concavity (Sign of a)')
st.markdown('The **sign of a** determines the concavity (which way the parabola opens).')
st.markdown('* **If a > 0 (Positive):** The parabola is **concave up** (opens upwards).')
st.markdown('* **If a < 0 (Negative):** The parabola is **concave down** (opens downwards).')

st.markdown('### 2. Width (Absolute Value of a)')
st.markdown('The **absolute value of a** ($|a|$) determines the **width** of the parabola.')
st.markdown('* As $|a|$ **increases** (e.g., $|2| > |1|$), the graph becomes **narrower** (closer to the y-axis).')
st.markdown('* As $|a|$ **decreases** (e.g., $|0.5| < |1|$), the graph becomes **wider** (closer to the x-axis).')
