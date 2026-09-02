import pandas as pd
import numpy as np

def add_column(df: pd.DataFrame) -> pd.DataFrame:

    df["month"] = pd.to_datetime ( df["date"] ).dt.month_name ()
    df["sales"] = (df["price"] * df["quantity"]).round(2)

    return df

def summary_analytics(df: pd.DataFrame, output_path: str = "data/sales_summary.csv") -> pd.DataFrame:
    summary = (
        df.groupby("category")
        .agg (
            total_revenue=("sales", "sum"),
            items_sold=("quantity", "sum"),
            avg_rating=("customer_rating", "mean"),
        )
        .reset_index ()
        .round ( 2 )
    )
    summary.to_csv ( output_path, index=False )

    return summary
def run_analytics_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    df = add_column(df)
    summary_analytics(df)
    return df