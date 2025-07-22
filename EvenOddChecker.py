import streamlit as st
import pandas as pd

# 🎯 App Title
st.title("🔢 Even or Odd Checker")

# 📌 Single Number Checker
st.header("✅ Check a Single Number")

single_num = st.number_input("Enter a number:", step=1)

if st.button("Check Single Number"):
    if single_num % 2 == 0:
        st.success(f"🟢 {int(single_num)} is Even")
    else:
        st.error(f"🔴 {int(single_num)} is Odd")

# 📌 List of Numbers Checker
st.header("✅ Check a List of Numbers")

num_list = st.text_area(
    "Enter numbers separated by commas:",
    placeholder="e.g., 1, 2, 3, 4, 5"
)

if st.button("Check List"):
    if num_list.strip() == "":
        st.error("❌ Please enter at least one number.")
    else:
        try:
            numbers = [int(n.strip()) for n in num_list.split(",")]
            results = []

            for n in numbers:
                kind = "Even" if n % 2 == 0 else "Odd"
                results.append({"Number": n, "Type": kind})

            df = pd.DataFrame(results)

            # 🎨 Color the table rows
            def highlight_even_odd(row):
                color = 'background-color: lightgreen' if row.Type == "Even" else 'background-color: salmon'
                return [color] * len(row)

            st.write("📄 **Results Table:**")
            st.dataframe(
                df.style.apply(highlight_even_odd, axis=1)
            )

        except ValueError:
            st.error("❌ Invalid input! Please enter only numbers separated by commas.")

from muthu_footer import add_footer

# ... your app code

add_footer()
