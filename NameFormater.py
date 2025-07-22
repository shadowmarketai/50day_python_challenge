import streamlit as st

# 🌟 App Title
st.set_page_config(page_title="Name Formatter", layout="centered")
st.title("📝 Name Formatter")
st.caption("Enter your name details and see it in different styles!")

# 📥 Separate Name Inputs
st.subheader("✍️ Enter Your Name:")
first_name = st.text_input("First Name (Required):")
middle_name = st.text_input("Middle Name (Optional):")
last_name = st.text_input("Last Name (Required):")

# 🧠 Function to format name
def format_name(first, middle, last):
    if not first or not last:
        return None, "⚠️ Please enter both First and Last name."

    full_name = f"{first} {middle} {last}".strip()
    return {
        "🔄 Last, First": f"{last}, {first} {middle}".strip(),
        "👤 First Last": f"{first} {middle} {last}".strip(),
        "🔡 Uppercase": f"{first.upper()} {middle.upper()} {last.upper()}".strip(),
        "🔡 Lowercase": f"{first.lower()} {middle.lower()} {last.lower()}".strip(),
        "✒️ Initials": f"{first[0].upper()}.{middle[0].upper() + '.' if middle else ''}{last[0].upper()}."
    }, None

# 🚦 Process Input
if first_name or last_name:
    result, error = format_name(first_name.strip(), middle_name.strip(), last_name.strip())
    if error:
        st.error(error)
    else:
        st.success(f"✅ Name formats for: **{first_name} {middle_name} {last_name}**")
        for label, value in result.items():
            st.markdown(f"**{label}:** {value}")
else:
    st.info("👆 Enter your First and Last name to see different formats.")

# 🔄 Reset Button
if st.button("🔄 Reset"):
    st.session_state.clear()
    st.rerun()

# 👣 Floating Footer
try:
    from muthu_footer import add_footer
    add_footer()
except:
    st.caption("Made with ❤️ by Muthu")
