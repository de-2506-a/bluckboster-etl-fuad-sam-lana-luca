import pandas as pd
import numpy as np
from src.utils.data_cleaning import DataCleaner


def test_data_cleaner():
    # Create a sample DataFrame with duplicates,
    # missing values, and mixed date formats
    df = pd.DataFrame(
        {
            "Name": ["Alice", "Alice", "Bob", "Luke"],
            "Age": [25, 25, 30, None],
            "Join Date": ["2021-01-05", "2021-01-05", "05 Feb 2023", "2024/02/08"],
        }
    )

    # Run cleaning
    cleaned_df = (
        DataCleaner(df)
        .standardise_date_column("Join Date")
        .clean_values(fill_value=34)
        .get_df()
    )

    # Tests duplicate removal
    assert cleaned_df.shape[0] == 3

    # Test missing value filling
    assert cleaned_df["Age"].isna().sum() == 0

    # All dates should be in dd/mm/yyyy format
    date_values = cleaned_df["Join Date"]
    for d in date_values:
        # Ensures format is dd/mm/yyyy by checking indexes of slashes
        assert len(d) == 10 and d[2] == "/" and d[5] == "/"

    # Test that the function is not in place, and cleans duplicates
    assert (
        np.count_nonzero(df["Name"] == "Alice") == 2
    )  # Original remains unchanged
    assert (
        np.count_nonzero(cleaned_df["Name"] == "Alice") == 1
    )  # Cleaned one has duplicates removed
