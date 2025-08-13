import streamlit as st
import plotly.express as px
import sys
from pathlib import Path

# Add etl_process to path
sys.path.append(str(Path(__file__).parent.parent.parent / "etl_process" / "src"))
from transform.store_metrics import get_store_revenue

def show_revenue():
# Page config
    st.set_page_config(page_title="Store Revenue", layout="wide")
    st.title("🏪 Store Revenue Insights")

    # Load data
    df = get_store_revenue()

    if df is None or df.empty:
        st.error("No data available.")
    else:
        st.subheader("📊 Store Revenue Comparison")
        fig = px.bar(
            df,
            x='store_id',
            y='total_revenue',
            title='Total Revenue by Store',
            labels={'store_id': 'Store', 'total_revenue': 'Total Revenue ($)'},
            color='total_revenue',
            color_continuous_scale='Blues'
        )
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)