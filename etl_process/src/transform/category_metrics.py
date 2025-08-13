import pandas as pd
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from utils.db_engine import db_engine

def get_top_and_bottom_categories() -> pd.DataFrame | None:
    """
    Fetch top 5 and bottom 5 film categories by average rental price.

    Returns:
        pd.DataFrame | None: Combined DataFrame of top and bottom categories,
                             or None if query fails.
    """
    try:
        engine = db_engine()

        # Locate SQL files
        current_dir = Path(__file__).parent
        sql_dir = current_dir.parent / "sql"
        top_path = sql_dir / "top_categories_query.sql"
        bottom_path = sql_dir / "bottom_categories_query.sql"

        if not top_path.exists() or not bottom_path.exists():
            print(f"Error: SQL file(s) not found at {top_path} or {bottom_path}")
            return None

        # Read queries
        top_query = top_path.read_text()
        bottom_query = bottom_path.read_text()

        # Execute queries
        top_df = pd.read_sql_query(top_query, engine)
        bottom_df = pd.read_sql_query(bottom_query, engine)

        if top_df.empty and bottom_df.empty:
            print("Warning: Both queries returned no results.")
            return None

        # Label and combine
        top_df["Group"] = "Top 5"
        bottom_df["Group"] = "Bottom 5"
        combined = pd.concat([top_df, bottom_df], ignore_index=True)

        return combined

    except Exception as e:
        print(f"Error executing category queries: {e}")
        return None

if __name__ == "__main__":
    result = get_top_and_bottom_categories()
    if result is not None:
        print(result.head(10))
    else:
        print("Failed to retrieve category data")
