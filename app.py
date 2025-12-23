import streamlit as st

st.title("Калькулятор процентов 🧮")
operation = st.selectbox(
    "Выберите операцию:",
    ["Найти % от числа", "Прибавить % к числу", "Вычесть % из числа"]
)
number = st.number_input("Введите число", value=0.0)
percent = st.number_input("Введите процент", value=0.0)

if st.button("Рассчитать"):
   if operation == "Найти % от числа":
        result = (number * percent) / 100
        st.success(f"Результат: {result}")
    elif operation == "Прибавить % к числу":
        result = number + (number * percent) / 100
        st.success(f"Итоговая сумма: {result}")
    elif operation == "Вычесть % из числа":
        result = number - (number * percent) / 100
        st.success(f"Цена со скидкой: {result}")
        
st.sidebar.header("О проекте ℹ️")
st.sidebar.write("Этот калькулятор создал In$Aide$4.")



