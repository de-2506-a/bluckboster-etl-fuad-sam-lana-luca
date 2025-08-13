import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Add etl_process to path
sys.path.append(str(Path(__file__).parent.parent.parent / "etl_process" / "src"))
from transform.best_selling_actors import get_best_selling_movies_with_actors


def show_movies_with_actors():
    """
    Displays a list of movies and shows actors when a movie is selected
    """
    # Add CSS for hover effects
    st.markdown("""
    <style>
    .actor-card {
        background-color: #e8f4fd;
        padding: 15px;
        border-radius: 8px;
        margin: 5px 0;
        text-align: center;
        border-left: 4px solid #3498db;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .actor-card:hover {
        background-color: #d4edda;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        border-left: 4px solid #28a745;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown(
        "<h1 style='text-align: center; color: #1f77b4;'>"
        "🎬 Movies and Their Actors"
        "</h1>",
        unsafe_allow_html=True
    )

    # Load data from etl
    df = get_best_selling_movies_with_actors()
    if (
        df is None
        or df.empty
    ):
        st.error("No data available")
        return

    # Get unique movies sorted by revenue
    movies_df = df.groupby('title')['total_revenue'].first().sort_values(ascending=False).reset_index()

    # Movie selection with custom styling
    st.markdown("<h3 style='color: #ff6b6b;'>🎯 Select a Movie</h3>", unsafe_allow_html=True)
    selected_movie = st.selectbox(
        "Choose from our top-grossing films:",
        movies_df['title'].tolist(),
        index=0
    )

    # Show selected movie info and actors
    if selected_movie:
        movie_data = df[
            df['title'] == selected_movie
        ]
        movie_revenue = movie_data['total_revenue'].iloc[0]

        # Movie info card
        st.markdown(
            (
                f"<div style='background-color: #f0f2f6; padding: 20px; "
                f"border-radius: 10px; margin: 20px 0;'>"
                f"<h2 style='color: #4ecdc4; margin: 0;'>🎭 {selected_movie}</h2>"
                f"<p style='font-size: 18px; color: #2c3e50; margin: 10px 0 0 0;'>"
                f"💰 Revenue: <strong>${movie_revenue:,.2f}</strong></p>"
                f"</div>"
            ),
            unsafe_allow_html=True
        )

        # Display actors in styled cards
        actors_df = movie_data[['first_name', 'last_name']].drop_duplicates()
        actors_df['full_name'] = actors_df['first_name'] + ' ' + actors_df['last_name']

        st.markdown("<h3 style='color: #9b59b6;'>⭐ Cast Members</h3>", unsafe_allow_html=True)

        # Create columns for actor cards
        cols = st.columns(3)
        for i, actor in enumerate(actors_df['full_name']):
            with cols[i % 3]:
                st.markdown(
                    f"<div class='actor-card'>"
                    f"<p style='margin: 0; font-weight: bold; color: #2c3e50;'>"
                    f"🎭 {actor}</p></div>",
                    unsafe_allow_html=True
                )
