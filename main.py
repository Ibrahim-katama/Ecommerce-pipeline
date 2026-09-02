
import pandas as pd
from src.cleaner import clean_sales_pipeline
from src.analytics import run_analytics_pipeline


def main():
    #create a new csv to store cleaned data
    cleaned_file_path = "data/cleaned_sales.csv"
    cleaned_df = clean_sales_pipeline("data/raw_sales.csv")
    enriched_df = run_analytics_pipeline(cleaned_df)
    enriched_df.to_csv(cleaned_file_path, index=False)

    pd.set_option ( "display.float_format", lambda x: "%.2f" % x )

    df = pd.read_csv("data/sales_summary.csv")
    print(df)

if __name__ == "__main__":
    main ()