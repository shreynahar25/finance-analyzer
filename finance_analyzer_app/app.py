# app.py
import streamlit as st
import pandas as pd
from utils import pdf_parser, csv_parser, categorizer, insights

st.set_page_config(page_title="Personal Finance Analyzer", layout="wide")

st.title("💳 Personal Finance Analyzer")
st.write("Upload your bank or credit card statement to analyze your expenses.")

uploaded_file = st.file_uploader("Upload PDF or CSV", type=["pdf", "csv"])

if uploaded_file is not None:
    file_type = uploaded_file.name.split(".")[-1]

    with st.spinner("Parsing file..."):
        if file_type == "pdf":
            df = pdf_parser.parse(uploaded_file)
        elif file_type == "csv":
            df = csv_parser.parse(uploaded_file)
        else:
            st.error("Unsupported file type.")
            st.stop()

    df = categorizer.categorize(df)
    st.success("File parsed and categorized successfully!")

    with st.expander("🔍 Preview Transactions"):
        st.dataframe(df)

    st.header("📊 Insights Dashboard")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Category-wise Expense Breakdown")
        pie_chart = insights.get_pie_chart(df)
        st.pyplot(pie_chart)

    with col2:
        st.subheader("Monthly Expense Trend")
        trend_chart = insights.get_trend_chart(df)
        st.pyplot(trend_chart)

    st.subheader("🔠 Smart Categorization Suggestions")
    uncategorized = df[df['Category'] == 'Uncategorized']
    if not uncategorized.empty:
        st.write("AI-powered tag suggestions for uncategorized rows")
        suggestions = categorizer.suggest_tags(uncategorized)
        st.dataframe(suggestions)
    else:
        st.write("All transactions are categorized!")

    st.caption("Note: Your corrections will help improve future accuracy (learning mode coming soon!)")
else:
    st.info("Please upload a PDF or CSV file to begin.")
