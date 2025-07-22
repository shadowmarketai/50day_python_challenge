import streamlit as st
import pandas as pd
import plotly.express as px

# Page setup
st.set_page_config(page_title="Name Collector & Analyzer", page_icon="📋", layout="centered")

st.title("📋 Name Collector & Analyzer")
st.markdown("Enter **5 names**. This app shows character counts, ranks them, and gives a visual overview.")

# Input form
with st.form("name_input_form"):
    name1 = st.text_input("Name 1")
    name2 = st.text_input("Name 2")
    name3 = st.text_input("Name 3")
    name4 = st.text_input("Name 4")
    name5 = st.text_input("Name 5")
    submitted = st.form_submit_button("✅ Click to Analyze")

if submitted:
    names = [name1, name2, name3, name4, name5]
    names = [name.strip() for name in names if name.strip() != ""]

    if not names:
        st.warning("🚨 Please enter at least one name.")
    else:
        lengths = [len(name) for name in names]
        df = pd.DataFrame({
            "Name": names,
            "Character Count": lengths
        })

        # Ranking: 1 = longest
        df["Rank"] = df["Character Count"].rank(ascending=False, method='min').astype(int)

        # Highlight category
        max_len = df["Character Count"].max()
        min_len = df["Character Count"].min()

        def get_label(length):
            if length == max_len:
                return "🟢 Longest"
            elif length == min_len:
                return "🔴 Shortest"
            return "⚪ Normal"

        df["Category"] = df["Character Count"].apply(get_label)

        # Display Table
        st.markdown("### 🧾 Names Table with Highlights and Ranking")

        def highlight_row(row):
            if row["Character Count"] == max_len:
                return ['background-color: #d4edda'] * 4
            elif row["Character Count"] == min_len:
                return ['background-color: #f8d7da'] * 4
            return ['background-color: #fff3cd'] * 4

        st.dataframe(df.sort_values("Rank").style.apply(highlight_row, axis=1), use_container_width=True)

        # Bar Chart
        st.markdown("### 📊 Character Count Chart")
        fig = px.bar(df.sort_values("Rank"),
                     x="Name", y="Character Count", color="Category", text="Rank",
                     color_discrete_map={
                         "🟢 Longest": "green",
                         "🔴 Shortest": "red",
                         "⚪ Normal": "gray"
                     },
                     title="Name Lengths and Ranking")
        fig.update_traces(textposition='outside')
        st.plotly_chart(fig, use_container_width=True)

        # Floating footer
        from muthu_footer import add_footer
        add_footer()

        
