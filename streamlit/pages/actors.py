import streamlit as st
import pandas as pd
import sys
from pathlib import Path
import matplotlib.pyplot as plt

# Add etl_process to path
sys.path.append(str(Path(__file__).parent.parent.parent / "etl_process" / "src"))
from transform.best_selling_actors import get_best_selling_actors


def show_actors():
    """
        Displays statistics for the best selling actors
    """
    st.header("🎭 Best Selling Actors Analysis")

    # Load data from etl
    df = get_best_selling_actors()
    if df is None or df.empty:
        st.error("No data available")
        return

    # Sidebar filters
    st.sidebar.subheader("Filters")
    min_revenue = st.sidebar.slider("Minimum Revenue:", 0, int(df['total_revenue'].max()), 0)
    top_n = st.sidebar.number_input("Show Top N Actors:", min_value=5, max_value=len(df), value=20)

    # Filter data
    filtered_df = df[df['total_revenue'] >= min_revenue].head(top_n)

    # Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Selected Actors", len(filtered_df))
    with col2:
        st.metric("Total Revenue", f"${filtered_df['total_revenue'].sum():,.2f}")
    with col3:
        st.metric("Avg Revenue", f"${filtered_df['total_revenue'].mean():,.2f}")

    # Data display with styling
    st.subheader("📊 Actor Performance Data")

    # Style the dataframe
    styled_df = filtered_df.style.format({
        'total_revenue': '${:,.2f}'
    }).background_gradient(subset=['total_revenue'], cmap='Greens')

    st.dataframe(styled_df, use_container_width=True)

    # Top performers chart
    if not filtered_df.empty:
        st.subheader("🏆 Top Performers")
        filtered_df['full_name'] = filtered_df['first_name'] + ' ' + filtered_df['last_name']
        
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(filtered_df['full_name'], filtered_df['total_revenue'], 
                     color=plt.cm.viridis(filtered_df['total_revenue'] / filtered_df['total_revenue'].max()))
        ax.set_xlabel('Actor')
        ax.set_ylabel('Total Revenue ($)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(fig)