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
    
    # 1. Выбор инструмента (убрали Крипто, добавили EUR/USD)
    symbol = st.selectbox(
        "Выберите торговый инструмент:",
        ["S&P 500", "EUR/USD"],
        key="trade_symbol"
    )
    
    # Общие поля для депозита и риска
    deposit = st.number_input("Ваш общий депозит ($)", value=1000.0, key="trade_deposit")
    
    risk_percent = st.slider(
        "Выберите % риска от депозита", 
        min_value=0.1, 
        max_value=5.0, 
        value=1.0, 
        step=0.1,
        key="trade_percent"
    )

    # Логика для S&P 500
    if symbol == "S&P 500":
        stop = st.number_input("Стоп-лосс (пункты)", value=0.0, key="sp500_stop")
        
        if st.button("Посчитать лот для S&P 500", key="sp_btn"):
            if stop > 0:
                risk_sum = deposit * (risk_percent / 100)
                lot = risk_sum / stop
                
                st.info(f"Сумма риска: ${risk_sum:.2f}")
                if risk_percent > 3.0:
                    st.error(f"⚠️ Слишком высокий риск ({risk_percent}%)!")
                else:
                    st.success(f"✅ Риск в норме ({risk_percent}%)")
                
                st.metric(label="Рекомендуемый лот", value=f"{lot:.4f}")
            else:
                st.error("Стоп-лосс должен быть больше нуля!")

    # 2. Новая логика для EUR/USD
    elif symbol == "EUR/USD":
        stop_pips = st.number_input("Стоп-лосс (в пипсах)", value=0.0, key="eurusd_stop")
        
        if st.button("Посчитать лот для EUR/USD", key="eurusd_btn"):
            if stop_pips > 0:
                risk_sum = deposit * (risk_percent / 100)
                
                # Сначала выводим сумму риска
                st.info(f"Сумма риска: ${risk_sum:.2f}")
                
                # 1. Добавляем проверку высокого риска (как в S&P 500)
                if risk_percent > 3.0:
                    st.error(f"⚠️ Слишком высокий риск ({risk_percent}%)!")
                else:
                    st.success(f"✅ Риск в норме ({risk_percent}%)")

                # 2. Считаем и выводим лот
                lot = risk_sum / (stop_pips * 10)
                st.metric(label="Рекомендуемый лот (Standard)", value=f"{lot:.2f}")
            else:
                st.error("Введите размер стоп-лосса!")
# Общая боковая панель для всего приложения
st.sidebar.header("О проекте ℹ️")
st.sidebar.write("Этот калькулятор создал @Durik66.")

















