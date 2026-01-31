import streamlit as st
import pandas as pd

st.set_page_config(page_title="Snowflake AI Q&A Predictor", layout="wide")

st.title("📊 AI-Powered Earnings Call Q&A Predictor")

st.markdown("""
This tool synthesizes:
- Snowflake financial performance  
- Peer benchmarks  
- Unstructured analyst commentary & earnings transcripts  

to predict likely investor questions and generate executive-ready responses.
""")

qa_data = {
    "Question": [
        "Peer performance: Snowflake grew 8.9% QoQ versus peers. What drove outperformance?",
        "AI adoption is a dominant theme. How is Snowflake monetizing AI workloads?",
        "Peers and hyperscalers are aggressively investing. Where is Snowflake gaining share?",
        "Profitability and free cash flow are key themes. What efficiency levers are driving margins?"
    ],
    "AI-Generated Answer": [
        "Snowflake delivered $734.2M revenue with 8.9% QoQ growth supported by strong enterprise demand and AI workloads.",
        "Management should emphasize Cortex adoption, expanding AI consumption, and pipeline traction.",
        "Management should cite workload-level differentiation and competitive wins.",
        "Management should focus on infrastructure efficiency and disciplined investment."
    ]
}

df = pd.DataFrame(qa_data)

st.subheader("Predicted Investor Questions & AI-Generated Responses")

for i, row in df.iterrows():
    st.markdown(f"### ❓ {row['Question']}")
    st.markdown(f"**Answer:** {row['AI-Generated Answer']}")
    st.markdown("---")