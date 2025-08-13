import streamlit as st
import pandas as pd
import sys
from pathlib import Path
import matplotlib.pyplot as plt
# Shows as unrecognised since the file is not in the same directory structure
# Does still work

# Add etl_process to path
sys.path.append(str(Path(__file__).parent.parent / "etl_process" / "src"))
from transform.best_selling_actors import get_best_selling_actors


def main():
    """
        Entry Point for the app,
        Initialises the page navigation
    """
    st.set_page_config(
        page_title="BluckBoster Analytics",
        page_icon="🎬",
        layout="wide"
    )
    
    st.title("🎬 BluckBoster Entertainment Analytics")
    
    # Sidebar navigation
    page = st.sidebar.selectbox(
        "Navigate to:",
        ["Home", "Best Selling Actors", "Film Analysis", "Revenue Insights"]
    )
    
    if page == "Home":
        show_home()
    elif page == "Best Selling Actors":
        show_actors()
    elif page == "Film Analysis":
        show_films()
    elif page == "Revenue Insights":
        show_revenue()

def show_home():
    st.header("Welcome to BluckBoster Analytics")
    st.write("Use the sidebar to navigate between different analysis pages.")


def show_actors():
    """
        Displays statistics for the best selling actors
    """
    st.header("🎭 Best Selling Actors Analysis")
    
    # Load data
    df = get_best_selling_actors()
    if df is None or df.empty:
        st.error("No data available")
        return
    
    # Sidebar filters
    st.sidebar.subheader("Filters")
    
    # Revenue filter
    min_revenue = st.sidebar.slider("Minimum Revenue:", 0, int(df['total_revenue'].max()), 0)
    
    # Top N filter
    top_n = st.sidebar.number_input("Show Top N Actors:", min_value=5, max_value=len(df), value=20)
    
    # Filter data
    filtered_df = df[df['total_revenue'] >= min_revenue].head(top_n)
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Actors", len(filtered_df))
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
        st.bar_chart(filtered_df.set_index('full_name')['total_revenue'])


def show_films():
    st.header("Film Performance Analysis")
    # Placeholder for film analysis
    st.write("Film revenue and rental data will be displayed here.")


def show_revenue():
    st.header("Revenue Insights")
    # Placeholder for revenue analysis
    st.write("Revenue trends and insights will be displayed here.")


if __name__ == "__main__":
    main()