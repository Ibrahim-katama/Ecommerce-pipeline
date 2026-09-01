from src.cleaner import clean_sales_pipeline


def main():
    file_path = "data/raw_sales.csv"
    df = clean_sales_pipeline (file_path)

    print (df.head(50))
    print(df.tail(50))


if __name__ == "__main__":
    main ()