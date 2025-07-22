import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 🌟 App Title
st.set_page_config(page_title="Live Vowel Analyzer", layout="centered")
st.title("📝 Live Vowel Analyzer")
st.caption("✨ Type a word or sentence and watch it analyze vowels in real time!")

# 🔤 User Input
text = st.text_input("Type a word or sentence:")

# 🎯 Vowel Set
vowels = 'aeiou'
vowel_counts = {v: 0 for v in vowels}

# 🧠 Process Input
if text:
    text_lower = text.lower()
    total_letters = len([char for char in text_lower if char.isalpha()])

    for char in text_lower:
        if char in vowels:
            vowel_counts[char] += 1

    total_vowels = sum(vowel_counts.values())
    total_consonants = total_letters - total_vowels

    st.markdown(f"🔠 Total Letters: **{total_letters}**")
    st.markdown(f"🗣️ Total Vowels: **{total_vowels}**")
    st.markdown(f"🔤 Total Consonants: **{total_consonants}**")

    # 🎨 Bar Chart Visualization
    st.subheader("📊 Vowel Frequency Chart")
    fig, ax = plt.subplots()
    bars = ax.bar(vowel_counts.keys(), vowel_counts.values(), color='skyblue')
    ax.set_ylabel("Frequency")
    ax.set_title("Vowel Distribution")
    st.pyplot(fig)

    # 📝 Vowel Summary
    st.subheader("📝 Vowel Breakdown")
    for v in vowels:
        count = vowel_counts[v]
        if count > 0:
            st.markdown(f"✅ **{v.upper()}**: {count} time(s)")
        else:
            st.markdown(f"❌ **{v.upper()}**: Not found")

    # 🌟 Highlight Most Frequent Vowel
    if total_vowels > 0:
        most_frequent = max(vowel_counts, key=vowel_counts.get)
        st.success(f"🏆 Most frequent vowel: **{most_frequent.upper()}** ({vowel_counts[most_frequent]} times)")
    else:
        st.warning("😅 No vowels found in the input!")
else:
    st.info("👆 Start typing above to see live vowel analysis.")

# 🔄 Restart Button
if st.button("🔄 Restart"):
    st.experimental_rerun()

# 👣 Floating Footer    
from muthu_footer import add_footer
add_footer()

