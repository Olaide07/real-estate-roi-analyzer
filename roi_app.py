import streamlit as st
from roi_functions import (
    calculate_roi,
    payback_period,
    investment_rating,
    monthly_cashflow,
    estimate_rent,
    investment_insight
)

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(page_title="Lagos ROI Analyzer", layout="centered")

st.title("🏠 Lagos Real Estate ROI Analyzer")
st.write("Evaluate and compare property investments using Lagos market insights")
st.caption("📍 This tool is optimized for Lagos real estate market assumptions")

# ===============================
# OPTION
# ===============================
use_estimated_rent = st.checkbox("Use Smart Rent Estimation (Location-based)")

locations = [
    "Banana Island", "Ikoyi", "Victoria Island",
    "Lekki", "Ajah", "Yaba", "Ikeja"
]

# ===============================
# PROPERTY A INPUT
# ===============================
st.sidebar.header("Property A")

location_a = st.sidebar.selectbox("Location A", locations)
price_a = st.sidebar.number_input("Price A (₦)", min_value=0, step=100_000)

if use_estimated_rent:
    rent_a = estimate_rent(price_a, location_a)
    st.sidebar.write(f"Estimated Rent A: ₦{rent_a:,.0f}")
else:
    rent_a = st.sidebar.number_input("Annual Rent A (₦)", min_value=0, step=50_000)

expenses_a = st.sidebar.number_input("Expenses A (₦)", min_value=0, step=50_000)

st.sidebar.markdown("---")

# ===============================
# PROPERTY B INPUT
# ===============================
st.sidebar.header("Property B")

location_b = st.sidebar.selectbox("Location B", locations)
price_b = st.sidebar.number_input("Price B (₦)", min_value=0, step=100_000)

if use_estimated_rent:
    rent_b = estimate_rent(price_b, location_b)
    st.sidebar.write(f"Estimated Rent B: ₦{rent_b:,.0f}")
else:
    rent_b = st.sidebar.number_input("Annual Rent B (₦)", min_value=0, step=50_000)

expenses_b = st.sidebar.number_input("Expenses B (₦)", min_value=0, step=50_000)

# ===============================
# BUTTON
# ===============================
if st.button("Compare Investments"):

    # Input validation
    if price_a <= 0 or price_b <= 0:
        st.warning("Please enter valid property prices.")
        st.stop()

    with st.spinner("Analyzing investments..."):

        # Property A
        roi_a, profit_a = calculate_roi(price_a, rent_a, expenses_a)
        payback_a = payback_period(price_a, profit_a)
        rating_a = investment_rating(roi_a)
        monthly_a = monthly_cashflow(rent_a, expenses_a)
        insight_a = investment_insight(roi_a)

        # Property B
        roi_b, profit_b = calculate_roi(price_b, rent_b, expenses_b)
        payback_b = payback_period(price_b, profit_b)
        rating_b = investment_rating(roi_b)
        monthly_b = monthly_cashflow(rent_b, expenses_b)
        insight_b = investment_insight(roi_b)

    # ===============================
    # DISPLAY RESULTS
    # ===============================
    st.subheader("📊 Comparison Results")

    col1, col2 = st.columns(2)

    # Property A
    with col1:
        st.markdown("### 🅰️ Property A")
        st.metric("ROI (%)", f"{roi_a:.2f}%")
        st.metric("Annual Profit", f"₦{profit_a:,.0f}")
        st.metric("Monthly Cashflow", f"₦{monthly_a:,.0f}")

        if payback_a:
            st.metric("Payback Period", f"{payback_a:.1f} yrs")
        else:
            st.warning("No profit")

        st.write(insight_a)

        if rating_a == "Excellent":
            st.success(f"Rating: {rating_a}")
        elif rating_a == "Good":
            st.info(f"Rating: {rating_a}")
        else:
            st.error(f"Rating: {rating_a}")

    # Property B
    with col2:
        st.markdown("### 🅱️ Property B")
        st.metric("ROI (%)", f"{roi_b:.2f}%")
        st.metric("Annual Profit", f"₦{profit_b:,.0f}")
        st.metric("Monthly Cashflow", f"₦{monthly_b:,.0f}")

        if payback_b:
            st.metric("Payback Period", f"{payback_b:.1f} yrs")
        else:
            st.warning("No profit")

        st.write(insight_b)

        if rating_b == "Excellent":
            st.success(f"Rating: {rating_b}")
        elif rating_b == "Good":
            st.info(f"Rating: {rating_b}")
        else:
            st.error(f"Rating: {rating_b}")

    st.markdown("---")

    # ===============================
    # FINAL DECISION
    # ===============================
    if roi_a > roi_b:
        st.success("✅ Property A is the better investment")
    elif roi_b > roi_a:
        st.success("✅ Property B is the better investment")
    else:
        st.info("Both properties have similar investment value")
