import streamlit as st

st.title("Калькулятор процентов 🧮")

number = st.number_input("Введите число", value=0.0)
percent = st.number_input("Введите процент", value=0.0)

if st.button("Рассчитать"):
    result = (number * percent) / 100

    st.success(f"Результат: {percent}% от {number} равно {result}")
st.sidebar.header("О проекте ℹ️")
st.sidebar.write("Этот калькулятор создал In$Aide$4.")


