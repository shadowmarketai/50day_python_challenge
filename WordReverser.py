import streamlit as st

# 🌟 App Configuration
st.set_page_config(page_title="🔄 Word Reverser", layout="centered")
st.title("🔄 Reverse Words in a Sentence")
st.caption("✨ Enter a sentence and watch each word reverse instantly!")

# 🎨 Styling for reversed words
def style_reversed_words(original, reversed_):
    styled = []
    for o, r in zip(original.split(), reversed_.split()):
        styled.append(f"<span style='color:#FF5733; font-weight:bold'>{r}</span>")
    return " ".join(styled)

# 🧠 Function to reverse individual words
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = ["".join(reversed(word)) for word in words]
    return " ".join(reversed_words)

# 📥 User Input
sentence = st.text_area("✍️ Enter your sentence here:", height=150, placeholder="Type something like: Hello World")

if sentence.strip():
    # 🔄 Reverse words
    reversed_sentence = reverse_words(sentence)

    # 🖋️ Display Results
    st.subheader("✨ Reversed Words:")
    st.markdown(f"<p style='font-size:20px'>{style_reversed_words(sentence, reversed_sentence)}</p>", unsafe_allow_html=True)

    st.text_area("📄 Plain Reversed Sentence:", value=reversed_sentence, height=100)

    # 📥 Download reversed sentence
    st.download_button(
        label="📥 Download Reversed Sentence",
        data=reversed_sentence,
        file_name="reversed_words.txt",
        mime="text/plain"
    )
else:
    st.info("👆 Enter a sentence above to see reversed words here.")

# 🔄 Reset Button
if st.button("🔄 Reset"):
    st.session_state.clear()
    st.rerun()

# 👣 Footer
st.caption("🚀 Made with ❤️ using Streamlit")

from muthu_footer import add_footer
add_footer()

