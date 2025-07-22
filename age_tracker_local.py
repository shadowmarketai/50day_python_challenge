import streamlit as st
import pandas as pd
import os

# 🎯 App Title
st.title("👥 Age Group Classifier & Tracker (Local Excel)")

# 📂 Excel file setup
excel_file = "age_groups.xlsx"

# 🔄 Load existing data or create new DataFrame
if os.path.exists(excel_file):
    df = pd.read_excel(excel_file)
else:
    df = pd.DataFrame(columns=["Name", "Age", "Group"])

# 📥 Get user input
name = st.text_input("Enter your Name:")
age = st.number_input("Enter your Age:", min_value=0, step=1, format="%d")

# 🖋 Process Age Group on Submit
if st.button("Submit"):
    if name.strip() == "":
        st.error("❌ Please enter your name.")
    else:
        # 🧠 Determine Age Group
        if age <= 12:
            group = "Child"
            color = "green"
        elif 13 <= age <= 19:
            group = "Teenager"
            color = "blue"
        elif 20 <= age <= 59:
            group = "Adult"
            color = "orange"
        else:
            group = "Senior"
            color = "red"

        # ✅ Display Result
        st.markdown(
            f"<h3 style='color:{color};'>Hi {name}! You are a {group}.</h3>",
            unsafe_allow_html=True
        )

        # 📥 Add to DataFrame and save
        new_record = {"Name": name, "Age": age, "Group": group}
        df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
        df.to_excel(excel_file, index=False)
        st.success("✅ Data saved to local Excel file!")

# 📊 Show Summary Chart
st.header("📈 Age Group Summary")
if not df.empty:
    group_count = df["Group"].value_counts()
    st.bar_chart(group_count)
else:
    st.info("No data yet. Enter a few records to see the chart.")

from muthu_footer import add_footer

# ... your app code

add_footer()
