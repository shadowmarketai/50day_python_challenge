import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Find Largest Number", layout="centered")

# 🌟 App Title
st.title("🔢 Advanced Largest Number Finder (No max())")
st.caption("Visualizes step-by-step how the largest number is determined.")

# 🔄 Initialize session state
if 'stopped' not in st.session_state:
    st.session_state['stopped'] = False

# 🔄 Restart App Button
if st.button("🔄 Restart App"):
    st.session_state['stopped'] = False
    st.rerun()

# 🚦 Main App Logic
if not st.session_state['stopped']:
    numbers_str = st.text_input("Enter numbers separated by commas:")

    if st.button("🚀 Find Largest with Visualization"):
        try:
            numbers = [float(num.strip()) for num in numbers_str.split(',') if num.strip()]
            if numbers:
                # 🏁 Initialize
                largest = numbers[0]
                st.success(f"Initial largest: {largest}")
                
                # 📊 Step-by-step visualization
                progress_bar = st.progress(0)
                status_text = st.empty()

                fig, ax = plt.subplots()
                bars = ax.bar(range(len(numbers)), numbers, color='lightblue')
                ax.set_title("🔍 Step-by-step Visualization")
                ax.set_ylabel("Number Value")
                chart = st.pyplot(fig, clear_figure=True)

                for idx, num in enumerate(numbers[1:], start=1):
                    status_text.markdown(f"**Step {idx}: Compare {num} with current largest {largest}**")
                    if num > largest:
                        largest = num
                        bars[idx].set_color('green')  # Highlight updated bar
                        status_text.markdown(f"✅ Update largest to **{largest}**")
                    else:
                        bars[idx].set_color('red')  # Highlight rejected bar
                        status_text.markdown(f"❌ Keep largest as **{largest}**")
                    
                    # Update chart
                    chart.pyplot(fig, clear_figure=True)
                    progress_bar.progress(int((idx + 1) / len(numbers) * 100))
                    time.sleep(0.7)  # Delay for visualization

                progress_bar.empty()
                st.balloons()
                st.success(f"🎉 Final Result: The largest number is **{largest}**")

            else:
                st.warning("⚠️ Please enter at least one number.")
        except ValueError:
            st.error("❌ Invalid input! Please enter valid numbers separated by commas.")

    if st.button("🛑 Stop App"):
        st.session_state['stopped'] = True
else:
    st.warning("🚫 The application has been stopped. Click 'Restart App' to use it again.")

# 👣 Floating Footer
from muthu_footer import add_footer
add_footer()

