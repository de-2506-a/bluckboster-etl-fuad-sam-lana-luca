import pandas as pd
from typing import Self


class DataCleaner:
    """
    Usage:
    df = pd.DataFrame({
        "Name": [" Alice ", "Bob", "Alice "],
        "Age": [25, 30, None],
        "Join Date": ["2021-01-05", "05 Feb 2021", "2021/01/05"]
    })

    dc = DataCleaner(df)
    cleaned_df = (
        dc.standardise_dates("Join Date")
        .clean_values(fill_value="ZERO")
        .get_df()
    )

    print(cleaned_df)
    """
    def __init__(self, df: pd.DataFrame):
        # Create a copy as an attribute
        self.df = df.copy()

    def clean_values(self, fill_value: any = None, by_column=None) -> Self:
        """
        Generically cleans a Pandas DataFrame:
        - Removes duplicated rows
        - Handles missing/null values in a custom way

        Parameters
        ----------
        df : pd.DataFrame
        - The input DataFrame
        fill_value : Any, optional
        - Value to use to fill missing values, defaults to None
        by_column : str, optional
        - If set to None, it dont work
        """
        # 1. Remove duplicates
        self.df = self.df.drop_duplicates(keep="first")

        # 2. Handle missing values
        if by_column is not None and fill_value is not None:
            self.df[by_column] = self.df[by_column].fillna(fill_value)
        elif fill_value is not None:
            self.df = self.df.fillna(fill_value)

        return self

    @staticmethod
    def _standardise_datestring(date_str: str) -> pd.Timestamp:
        """Tries parsing a date string into a pandas Timestamp."""
        if pd.isna(date_str) or date_str == "":
            return pd.NaT

        formats = [
            "%Y/%m/%d",
            "%Y-%m-%d",
            "%d %b %Y",
            "%b %d, %Y",
            "%d %B %Y",
            "%d-%m-%Y",
            "%d/%m/%Y",
            "%m/%d/%Y",
        ]
        for fmt in formats:
            try:
                return pd.to_datetime(date_str, format=fmt)
            except ValueError:
                continue

        return pd.NaT

    def standardise_date_column(self, column_name: str) -> Self:
        """
        Converts a date column into dd/mm/yyyy format
        using _standardise_datestring.
        """
        self.df[column_name] = self.df[column_name].apply(self._standardise_datestring)
        self.df[column_name] = self.df[column_name].dt.strftime("%d/%m/%Y")
        return self

    def convert_column_to_numeric(self, column_name: str) -> Self:
        # Convert column to numeric
        self.df[column_name] = pd.to_numeric(self.df[column_name], errors="coerce")
        return self

    def get_df(self) -> pd.DataFrame:
        """Return the cleaned DataFrame. Call when finished processing."""
        return self.df
