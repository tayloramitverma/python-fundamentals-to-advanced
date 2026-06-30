import streamlit as st
import pandas as pd
import numpy as np

# -----------------------------------------------------------------------------
# Page configuration (must be the first Streamlit command)
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Streamlit Basics", page_icon="🎈", layout="centered")

# -----------------------------------------------------------------------------
# Sidebar - navigation between demo sections
# -----------------------------------------------------------------------------
st.sidebar.title("📚 Streamlit Basics")
st.sidebar.write("A tour of the most common components.")
section = st.sidebar.radio(
    "Go to section:",
    ["Text & Titles", "Input Widgets", "Data & Tables", "Charts", "Layout & Media"],
)

# -----------------------------------------------------------------------------
# 1. Text & Titles
# -----------------------------------------------------------------------------
if section == "Text & Titles":
    st.title("This is a web app using Streamlit! 🎈")
    st.header("1. Displaying Text")
    st.subheader("Different ways to show text")

    st.write("`st.write()` is the Swiss Army knife — it renders almost anything.")
    st.text("st.text() shows fixed-width plain text.")
    st.markdown("You can use **markdown**: *italics*, `code`, and [links](https://streamlit.io).")
    st.caption("st.caption() is for small helper text.")
    st.code("import streamlit as st\nst.write('Hello world')", language="python")
    st.latex(r"E = mc^2")

    st.success("✅ success message")
    st.info("ℹ️ info message")
    st.warning("⚠️ warning message")
    st.error("❌ error message")

# -----------------------------------------------------------------------------
# 2. Input Widgets
# -----------------------------------------------------------------------------
elif section == "Input Widgets":
    st.title("2. Input Widgets")
    st.write("Widgets return their current value — Streamlit re-runs the script on every change.")

    name = st.text_input("What's your name?", "Amit")
    if name:
        st.write(f"👋 Hello, **{name}**!")

    age = st.slider("Select your age", min_value=0, max_value=100, value=25)
    st.write(f"You are **{age}** years old.")

    number = st.number_input("Pick a number", min_value=0, max_value=1000, value=42)
    st.write(f"Number squared = **{number ** 2}**")

    language = st.selectbox("Favourite language", ["Python", "JavaScript", "Go", "Rust"])
    hobbies = st.multiselect("Pick your hobbies", ["Coding", "Reading", "Gaming", "Music"])

    is_agree = st.checkbox("I agree to the terms")
    mood = st.radio("How are you feeling?", ["😀 Great", "😐 Okay", "😞 Not good"])

    if st.button("Submit"):
        st.success(f"{name} ({age}) likes {language}. Hobbies: {', '.join(hobbies) or 'none'}.")
        st.write(f"Mood: {mood} | Agreed: {is_agree}")

# -----------------------------------------------------------------------------
# 3. Data & Tables
# -----------------------------------------------------------------------------
elif section == "Data & Tables":
    st.title("3. Working with Data")

    df = pd.DataFrame(
        {
            "Name": ["Alice", "Bob", "Charlie", "Diana"],
            "Age": [24, 30, 22, 28],
            "City": ["Delhi", "Mumbai", "Pune", "Chennai"],
        }
    )

    st.subheader("Interactive table — st.dataframe()")
    st.dataframe(df, use_container_width=True)

    st.subheader("Static table — st.table()")
    st.table(df)

    st.subheader("Metrics — st.metric()")
    col1, col2, col3 = st.columns(3)
    col1.metric("Average Age", f"{df['Age'].mean():.0f}", "+2")
    col2.metric("Records", len(df))
    col3.metric("Cities", df["City"].nunique())

    st.subheader("JSON — st.json()")
    st.json({"app": "Streamlit demo", "version": 1.0, "components": ["text", "widgets", "charts"]})

# -----------------------------------------------------------------------------
# 4. Charts
# -----------------------------------------------------------------------------
elif section == "Charts":
    st.title("4. Charts & Visualisation")

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    st.subheader("Line chart")
    st.line_chart(chart_data)

    st.subheader("Area chart")
    st.area_chart(chart_data)

    st.subheader("Bar chart")
    st.bar_chart(chart_data)

    st.subheader("Map")
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [28.61, 77.20],  # around Delhi
        columns=["lat", "lon"],
    )
    st.map(map_data)

# -----------------------------------------------------------------------------
# 5. Layout & Media
# -----------------------------------------------------------------------------
elif section == "Layout & Media":
    st.title("5. Layout & Extras")

    st.subheader("Columns")
    left, right = st.columns(2)
    left.write("👈 This is the left column.")
    right.write("👉 This is the right column.")

    st.subheader("Expander")
    with st.expander("Click to expand"):
        st.write("Hidden content lives inside an expander — great for details and FAQs.")

    st.subheader("Tabs")
    tab1, tab2 = st.tabs(["Chart", "Data"])
    data = pd.DataFrame(np.random.randn(10, 2), columns=["x", "y"])
    tab1.line_chart(data)
    tab2.dataframe(data)

    st.subheader("Progress & Status")
    if st.button("Run a task"):
        progress = st.progress(0)
        for i in range(100):
            progress.progress(i + 1)
        st.balloons()
        st.success("Done! 🎉")

# -----------------------------------------------------------------------------
# Footer
# -----------------------------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.caption("Run with: `streamlit run app.py`")
