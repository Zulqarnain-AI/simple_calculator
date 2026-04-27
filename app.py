# app.py
import streamlit as st

# Page Config
st.set_page_config(
    page_title="Beautiful Calculator",
    page_icon="🧮",
    layout="centered"
)

# Custom CSS for Beautiful UI
st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #1e1e2f, #252542);
            color: white;
        }
        .stApp {
            background: linear-gradient(135deg, #1e1e2f, #252542);
        }
        .title {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            color: #cfcfe8;
            font-size: 18px;
            margin-bottom: 30px;
        }
        .result-box {
            background-color: #2f2f4f;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #00ffcc;
            margin-top: 20px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
        }
        .stButton>button {
            width: 100%;
            border-radius: 12px;
            height: 3em;
            font-size: 18px;
            font-weight: bold;
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            color: white;
            border: none;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #0072ff, #00c6ff);
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🧮 Beautiful Calculator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">A modern calculator built with Streamlit</div>', unsafe_allow_html=True)

# Input Fields
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter First Number", value=0.0, step=1.0)

with col2:
    num2 = st.number_input("Enter Second Number", value=0.0, step=1.0)

# Operation Selector
operation = st.selectbox(
    "Choose Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Calculate Button
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        symbol = "+"
    elif operation == "Subtraction":
        result = num1 - num2
        symbol = "-"
    elif operation == "Multiplication":
        result = num1 * num2
        symbol = "×"
    elif operation == "Division":
        if num2 == 0:
            result = "❌ Cannot divide by zero"
            symbol = "/"
        else:
            result = num1 / num2
            symbol = "/"

    st.markdown(
        f'<div class="result-box">{num1} {symbol} {num2} = {result}</div>',
        unsafe_allow_html=True
    )

# Footer
st.markdown(
    """
    <hr style="margin-top:40px; border:1px solid #444;">
    <div style='text-align:center; color:#aaaaaa; font-size:14px;'>
        Built with ❤️ using Streamlit
    </div>
    """,
    unsafe_allow_html=True
)