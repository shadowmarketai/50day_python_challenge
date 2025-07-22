import streamlit as st

# 🎨 Gradient background and animated button styles
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f8ffae, #43c6ac);
    }
    .stButton button {
        background: linear-gradient(90deg, #1cb5e0, #000851);
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border: none;
        border-radius: 8px;
        transition: 0.3s ease;
    }
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 10px rgba(0,0,0,0.2);
    }
    .stApp h1 {
        animation: fadeInDown 1s ease-out;
    }
    @keyframes fadeInDown {
        0% {opacity: 0; transform: translateY(-20px);}
        100% {opacity: 1; transform: translateY(0);}
    }
    </style>
""", unsafe_allow_html=True)

# 🧾 Title
st.title("🧾 Stylish Shopping Bill Generator")

# 👤 Buyer
buyer_name = st.text_input("👤 Enter Buyer's Name")

# Helper to show item inputs
def item_input(index):
    st.subheader(f"🛒 Item {index}")
    name = st.text_input(f"Item {index} Name", key=f"name_{index}")
    price = st.number_input(f"Item {index} Price (₹)", min_value=0.0, format="%.2f", key=f"price_{index}")
    tax = st.number_input(f"Item {index} Tax (%)", min_value=0.0, max_value=100.0, format="%.2f", key=f"tax_{index}")
    return name, price, tax

# Capture 3 items
item1, price1, tax1 = item_input(1)
item2, price2, tax2 = item_input(2)
item3, price3, tax3 = item_input(3)

# Submit
if st.button("🧾 Generate Final Bill"):
    # Calculations
    total1 = price1 + (price1 * tax1 / 100)
    total2 = price2 + (price2 * tax2 / 100)
    total3 = price3 + (price3 * tax3 / 100)
    grand_total = total1 + total2 + total3

    # 💡 Output Section
    st.balloons()
    st.success("✅ Your detailed bill is ready!")

    st.markdown("## 🧾 **BILL SUMMARY**")
    st.markdown(f"**🧍 Buyer Name:** `{buyer_name if buyer_name else 'Guest'}`")
    st.markdown("---")

    # Individual item breakdown
    def show_line(item, price, tax, total):
        st.markdown(f"🔹 **{item if item else 'Unnamed Item'}**: ₹{price:.2f} + {tax:.0f}% tax = **₹{total:.2f}**")

    show_line(item1, price1, tax1, total1)
    show_line(item2, price2, tax2, total2)
    show_line(item3, price3, tax3, total3)

    st.markdown("---")
    st.markdown(f"### 💰 **Grand Total: ₹{grand_total:.2f}**")
    st.caption("🧾 Thank you for shopping with us!")

# Optional: Sticky footer
from muthu_footer import add_footer
add_footer()
