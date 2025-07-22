import streamlit as st

# Page configuration
st.set_page_config(page_title="Sum Calculator", page_icon="➕", layout="centered")

# Title and instructions
st.title("➕ Sum Calculator (1 to n) - Task 9")
st.markdown("This app calculates the **sum of all integers from 1 to n** using a loop.")

# Input
n = st.number_input("Enter a positive integer n:", min_value=1, step=1)

# Button to calculate
if st.button("🧮 Calculate Sum"):
    total = 0
    for i in range(1, n + 1):
        total += i

    st.success(f"✅ The sum of numbers from 1 to {n} is **{total}**")

# Floating Footer
from muthu_footer import add_footer

# ... your app code

add_footer()

