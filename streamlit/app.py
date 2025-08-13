import streamlit as st
from nav_pages.home import show_home
from nav_pages.actors import show_actors
from nav_pages.films import show_films
from nav_pages.revenue import show_revenue


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
        [
            "Home",
            "Best Selling Actors",
            "Film Analysis",
            "Revenue Insights"
        ]
    )
    
    if page == "Home":
        show_home()
    elif page == "Best Selling Actors":
        show_actors()
    elif page == "Film Analysis":
        show_films()
    elif page == "Revenue Insights":
        show_revenue()




if __name__ == "__main__":
    main()