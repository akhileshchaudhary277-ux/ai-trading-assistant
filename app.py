
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="AI Trading Assistant",
    page_icon="📈",
    layout="wide"
)

st.title("📈 AI Trading Assistant")
st.caption("Nifty • BankNifty • Sensex | Paper Trading")

st.warning(
    "Demo mode: नीचे का डेटा काल्पनिक है, "
    "यह Live Market Data नहीं है।"
)

market = st.selectbox(
    "Market चुनें",
    ["Nifty 50", "BankNifty", "Sensex"]
)

prices = {
    "Nifty 50": 25000,
    "BankNifty": 55000,
    "Sensex": 82000
}

base = prices[market]
rng = np.random.default_rng(42)
changes = rng.normal(0, 20, 40)
values = base + np.cumsum(changes)

chart = pd.DataFrame({
    "Price (Demo)": values
})

st.subheader(f"{market} — Demo Chart")
st.line_chart(chart)

last_price = float(values[-1])
previous_price = float(values[-2])

a, b, c = st.columns(3)
a.metric("Demo Price", f"{last_price:,.2f}")
b.metric(
    "Change",
    f"{last_price - previous_price:+.2f}"
)
b.caption("Demo points, not live market movement")

trend = "Bullish" if last_price > previous_price else "Bearish"
c.metric("Last-step trend", trend)

st.subheader("🧪 Paper Trading Practice")

side = st.radio(
    "Practice trade",
    ["CALL (Virtual)", "PUT (Virtual)"],
    horizontal=True
)

entry = st.number_input(
    "Virtual entry price",
    min_value=0.0,
    value=float(round(last_price, 2)),
    step=1.0
)

stop = st.number_input(
    "Virtual stop-loss price",
    min_value=0.0,
    value=float(round(last_price - 50, 2)),
    step=1.0
)

target = st.number_input(
    "Virtual target price",
    min_value=0.0,
    value=float(round(last_price + 100, 2)),
    step=1.0
)

if st.button("Check virtual trade"):
    if entry <= 0 or stop <= 0 or target <= 0:
        st.error("सभी कीमतें शून्य से अधिक रखें।")
    elif stop == entry or target == entry:
        st.error("Entry और SL/Target अलग रखें।")
    else:
        st.info(
            f"{market}: {side}\n\n"
            f"Virtual Entry: {entry:.2f}\n\n"
            f"Virtual SL: {stop:.2f}\n\n"
            f"Virtual Target: {target:.2f}"
        )
        st.caption(
            "यह केवल अभ्यास है, ट्रेडिंग सलाह या live signal नहीं।"
        )

st.divider()
st.subheader("🗣️ हिंदी निर्देश")
st.write(
    "यह शुरुआती dashboard है। "
    "Live data और voice सुविधा अभी जोड़ी नहीं गई है।"
)
st.write(
    "अगला चरण: dependencies, live data access "
    "और हिंदी voice setup।"
)
