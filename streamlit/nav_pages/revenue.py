import streamlit as st
import plotly.express as px
import sys
from pathlib import Path

# Add etl_process to path
sys.path.append(str(Path(__file__).parent.parent.parent / "etl_process" / "src"))
from transform.store_metrics import get_store_revenue
from transform.category_metrics import get_top_and_bottom_categories  # Add this import

def show_revenue():
    # Page config
    st.set_page_config(page_title="Store Revenue", layout="wide")
    st.title("🏪 Store Revenue Insights")

    # Store revenue chart
    df = get_store_revenue()
    if df is None or df.empty:
        st.error("No store revenue data available.")
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

    # Category pricing chart
    category_df = get_top_and_bottom_categories()
    if category_df is None or category_df.empty:
        st.error("No category pricing data available.")
    else:
        st.subheader("🎬 Top & Bottom Categories by Avg Rental Price")
        fig2 = px.bar(
            category_df,
            x="category",
            y="avg_price",
            color="Group",
            color_discrete_map={"Top 5": "green", "Bottom 5": "red"},
            title="Top & Bottom 5 Categories by Average Rental Price",
            labels={"category": "Category", "avg_price": "Average Price ($)"}
        )
        fig2.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig2, use_container_width=True)
