import pandas as pd
import sys
from pathlib import Path
from utils.db_engine import db_engine

sys.path.append(str(Path(__file__).parent.parent))
# Pathing is used to manage file paths relatively and regardless of execution directory


def get_highest_selling(amount: int = 25) -> pd.DataFrame | None:
    """
    Fetch the highest selling movies

    Returns:
        pd.DataFrame | None: A DataFrame containing the highest selling movies
    """
    try:
        engine = db_engine()
        # Get the correct path to the SQL file
        current_dir = Path(__file__).parent
        sql_file_path = current_dir.parent / "sql" / "highest_selling.sql"

        if not sql_file_path.exists():
            print(f"Error: SQL file not found at {sql_file_path}")
            return None
        with open(sql_file_path, "r") as query_file:
            query = query_file.read()
        df = pd.read_sql_query(query, engine).head(amount) # If something doesn't work it's this

        if df.empty:
            print("Warning: Query returned no results")
            return df
        return df

    except FileNotFoundError as e:
        print(f"Error: SQL file not found - {e}")
        return None
    except Exception as e:
        print(f"Error executing query: {e}")
        return None


if __name__ == "__main__":
    result = get_highest_selling()
    if result is not None:
        print(result.head())
    else:
        print("Failed to retrieve data")
