import datetime

import pandas as pd
import streamlit as st


CSV_FILE_PATH = "data.csv"

# streamlit config
st.set_page_config(
    page_title="Анкета",
    page_icon="💻",
)

# region Main form
st.title("Предпочтения в технологиях ❓")
st.write("---")
st.write(
    "Это веб-приложение создано с помощью Streamlit. "
    "Streamlit - библиотека Python с открытым кодом. Она позволяет с легкостью создавать разные "
    "красивые веб-приложения для инженеров машинного обучения. Всего за несколько минут и пару "
    "строк кода можно создать стильные приложения."
)

form = st.form("form")
name = form.text_input("Как вас зовут?")
age = form.selectbox(
    "Сколько вам лет?", ["До 18", "18-25", "26-35", "36-45", "Старше 45"]
)
phone_os = form.radio(
    "📱 Какая ОС на вашем телефоне?",
    ["Android", "iOS", "Другая"],
    horizontal=True,
)
computer_os = form.radio(
    "💻 Какая ОС на вашем компьютере / ноутбуке?",
    ["Windows", "macOS", "Linux", "Другая"],
    horizontal=True,
)

search_engine = form.radio(
    "🕸️ Каким поисковиком вы пользуетесь?",
    ["Google", "Yandex", "Bing", "Yahoo!", "Другой"],
    horizontal=True,
)

browser = form.selectbox(
    "🌐 Какими браузерами вы пользуетесь?",
    ["Chrome", "Edge", "Firefox", "Opera", "Safari", "Другой"],
)

prefer_big_techs = form.multiselect(
    "📈 Выберите предпочитаемые Big Tech корпорации",
    ["Meta", "Apple", "Amazon", "Netflix", "Google"],
)

tech_level = form.slider(
    "⚙️ Насколько вы уверенно владеете технологиями? (1 - новичок, 10 - эксперт)",
    min_value=1,
    max_value=10,
    value=5,
)

submitted = form.form_submit_button("Отправить ответы")

# endregion

# region When submitted form
if submitted:
    st.success("✅ Анкета сохранена! Спасибо!")
    st.balloons()

    user_data = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "name": name,
        "age": age,
        "phone_os": phone_os,
        "computer_os": computer_os,
        "search_engine": search_engine,
        "browser": browser,
        "prefer_big_techs": prefer_big_techs,
        "tech_level": tech_level,
    }

    new_df = pd.DataFrame([user_data])

    st.write("### Ваши данные в таблице:")
    st.dataframe(new_df)

    try:
        existing_df = pd.read_csv(CSV_FILE_PATH)
        updated_df = pd.concat([existing_df, new_df])
        updated_df.to_csv(CSV_FILE_PATH)

    except FileNotFoundError:
        new_df.to_csv(CSV_FILE_PATH, index=False)

    st.info("💾 Данные сохранены в файл!")

# endregion

# region Statistics
st.write("---")
try:
    df = pd.read_csv(CSV_FILE_PATH)
    st.write("### Статистика")
    st.write(f"Уже заполнили анкету: {len(df)} человек")

    st.write("**Статистика по ОС на телефонах:**")
    st.bar_chart(df["phone_os"].value_counts())

    st.write("**Статистика по ОС на компьютерах:**")
    st.bar_chart(df["computer_os"].value_counts())

    col1, col2 = st.columns(2)
    col1.write("**Статистика по браузерам:**")
    col1.area_chart(df["browser"].value_counts())

    col2.write("**Статистика по поисковикам:**")
    col2.area_chart(df["search_engine"].value_counts())

    st.write("### Вся статистика")
    st.dataframe(df)

except FileNotFoundError:
    st.write("Пока никто не заполнил анкету. Будьте первым!")

# endregion
