import streamlit as st
import pandas as pd
import sys
from pathlib import Path
from transform.best_selling_actors import get_best_selling_actors

# Add etl_process to path
sys.path.append(str(Path(__file__).parent.parent / "etl_process" / "src"))

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
    st.header("Best Selling Actors Analysis")
    # Placeholder for actor analysis
    st.write("Actor performance metrics will be displayed here.")
    st.dataframe(get_best_selling_actors())


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