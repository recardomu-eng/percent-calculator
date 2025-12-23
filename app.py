import streamlit as st

# Создаем две вкладки
tab1, tab2 = st.tabs(["Процентный калькулятор 🧮", "For Trader 📊"])

with tab1:
    st.title("Калькулятор процентов 🧮")
    
    operation = st.selectbox(
        "Выберите операцию:",
        ["Найти % от числа", "Прибавить % к числу", "Вычесть % из числа"],
        key="calc_op"
    )
    
    number = st.number_input("Введите число", value=0.0, key="calc_num")
    percent = st.number_input("Введите процент", value=0.0, key="calc_perc")
    
    if st.button("Рассчитать", key="calc_btn"):
        if operation == "Найти % от числа":
            result = (number * percent) / 100
            st.success(f"Результат: {result}")
        elif operation == "Прибавить % к числу":
            result = number + (number * percent) / 100
            st.success(f"Итоговая сумма: {result}")
        elif operation == "Вычесть % из числа":
            result = number - (number * percent) / 100
            st.success(f"Цена со скидкой: {result}")

with tab2:
    st.title("Trading Tools 📊")
    
    # Выбор инструмента внутри вкладки
    symbol = st.selectbox(
        "Выберите торговый инструмент:",
        ["S&P 500", "Forex", "Crypto"],
        key="trade_symbol"
    )
    
    risk = st.number_input("Сумма риска ($)", value=0.0, key="trade_risk")
    
    if symbol == "S&P 500":
        stop = st.number_input("Стоп-лосс (пункты)", value=0.0, key="sp500_stop")
        
        if st.button("Посчитать лот для S&P 500", key="sp_btn"):
            if stop > 0:
                lot = risk / stop
                st.info(f"Рекомендуемый лот для S&P 500: {lot}")
            else:
                st.error("Стоп-лосс должен быть больше нуля!")
                
    else:
        st.write(f"Раздел для {symbol} в разработке... 🏗️")
