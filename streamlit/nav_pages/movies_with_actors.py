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
    st.header("🎬 Movies and Their Actors")

    # Load data from etl
    df = get_best_selling_movies_with_actors()
    if df is None or df.empty:
        st.error("No data available")
        return

    # Get unique movies sorted by revenue
    movies_df = df.groupby('title')['total_revenue'].first().sort_values(ascending=False).reset_index()
    
    # Movie selection
    selected_movie = st.selectbox(
        "Select a movie to see its actors:",
        movies_df['title'].tolist(),
        index=0
    )
    
    # Show selected movie info and actors
    if selected_movie:
        movie_data = df[df['title'] == selected_movie]
        movie_revenue = movie_data['total_revenue'].iloc[0]
        
        st.subheader(f"🎭 Actors in '{selected_movie}'")
        st.info(f"Movie Revenue: ${movie_revenue:,.2f}")
        
        # Display actors
        actors_df = movie_data[['first_name', 'last_name']].drop_duplicates()
        actors_df['full_name'] = actors_df['first_name'] + ' ' + actors_df['last_name']
        
        for actor in actors_df['full_name']:
            st.write(f"• {actor}")