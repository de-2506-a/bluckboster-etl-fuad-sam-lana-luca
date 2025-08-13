import pandas as pd
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
# Pathing is used to manage file paths relatively and regardless of execution directory
from utils.db_engine import db_engine


def get_customer_by_city_and_country() -> pd.DataFrame | None:
    """
    Fetch the total customers by city and country.

    Returns:
        pd.DataFrame | None: A DataFrame containing the number of total customers by city and country in descending order of total customers,
                            or None if an error occurs.
    """
    try:
        engine = db_engine()
        # Get the correct path to the SQL file
        current_dir = Path(__file__).parent
        sql_file_path = current_dir.parent / "sql" / "customer_location_query.sql"

        if not sql_file_path.exists():
            print(f"Error: SQL file not found at {sql_file_path}")
            return None
        with open(sql_file_path, "r") as query_file:
            query = query_file.read()
        df = pd.read_sql_query(query, engine)

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
    result = get_customer_by_city_and_country()
    if result is not None:
        print(result.head())
    else:
        print("Failed to retrieve data")