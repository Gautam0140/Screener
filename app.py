import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="US Stock Screener",
    layout="wide"
)

st.title("📈 US Stock Screener")

stocks = pd.DataFrame({
    "Ticker": ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL"],
    "Company": [
        "Apple",
        "Microsoft",
        "NVIDIA",
        "Amazon",
        "Google"
    ],
    "Price": [212, 445, 1080, 180, 175],
    "PE Ratio": [31, 38, 64, 55, 29],
    "Market Cap": ["3.1T", "3.2T", "2.8T", "1.9T", "2.1T"]
})

search = st.text_input("Search Stock")

if search:
    stocks = stocks[
        stocks["Ticker"].str.contains(search.upper())
    ]

st.dataframe(stocks, use_container_width=True)

st.subheader("Top Picks")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("AAPL", "$212")

with col2:
    st.metric("NVDA", "$1080")

with col3:
    st.metric("MSFT", "$445")
