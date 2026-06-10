import streamlit as st
import sys
sys.path.append(".")
from etl.fetch import fetch_products
from etl.clean import clean_products
from etl.load import create_table, load_products
from analysis.gemini_insights import generate_insights

st.set_page_config(page_title="E-Commerce Insight Engine", layout="wide")
st.title("🛒 E-Commerce Product Insight Engine")
st.caption("Powered by Amazon Data + Groq LLaMA 3 + PostgreSQL")

keyword = st.sidebar.text_input("Search Keyword", value="laptop")
if st.sidebar.button("Fetch & Analyze"):
    with st.spinner("Fetching data from Amazon..."):
        raw = fetch_products(keyword)
        df = clean_products(raw)
        create_table()
        load_products(df, keyword)
    st.success(f"Loaded {len(df)} products!")

    st.subheader("📦 Product Data")
    st.dataframe(df[["product_title", "product_price",
                      "product_star_rating", "product_num_ratings"]])

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💰 Price Distribution")
        st.bar_chart(df.set_index("product_title")["product_price"])
    with col2:
        st.subheader("⭐ Rating Distribution")
        st.bar_chart(df["product_star_rating"].value_counts())

    st.subheader("🤖 AI Business Insights")
    with st.spinner("Generating insights..."):
        insights = generate_insights(df, keyword)
    st.markdown(insights)