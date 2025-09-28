import streamlit as st

st.set_page_config(page_title="Ro-Live Scanner", layout="wide")


st.title("Calculator")
mathin = st.text_input("Input",value="1+1")
submit = st.button("=")

if submit and mathin:
    try:

        chartholder = st.empty()
        equation = str(mathin)
        answer = eval(equation)
        chartholder.success(answer)
    except Exception as e:
        st.error(f"Error: {e}")
