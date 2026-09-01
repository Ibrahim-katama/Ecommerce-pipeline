import pandas as pd
import numpy as np

def _clean_text_fields(df: pd.DataFrame) -> pd.DataFrame:
    # Handle whitespace, case normalization and missing values
    df["customer_name"] = (
        df["customer_name"]
        .astype ( str )
        .str.replace (r"[^a-zA-Z\s]", "", regex=True)
        .str.strip ()
        .str.title ()
        .replace("X","Unkown Unkown" )
        .replace (["", "Nan", "None"], np.nan)
        .fillna ("Unkown Unkown")
    )
    valid_genders = ["Female","Male", "Others"]
    df["gender"]=(
        df["gender"]
        .str.strip()
        .str.title()
    )
    df["gender"] = np.where(df["gender"].isin (valid_genders), df["gender"], "-")


    df["email"] = (
        df["email"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    is_valid = df["email"].str.match ( email_pattern, na=False )
    df["email"] = np.where(is_valid, df["email"], "Invalid email")

    valid_category = ["Home", "Toys", "Grocery", "Beauty", "Clothing", "Electronics"]
    df["category"] = (
        df["category"]
        .astype(str)
        .str.strip()
        .str.title()
    )
    df["category"] = np.where(df["category"].isin(valid_category), df["category"], "Not Known")
    return df

def _clean_numeric_fields(df: pd.DataFrame) -> pd.DataFrame:
    # Handle data types and fill missing values
    df["price"] =  pd.to_numeric(df["price"] , errors="coerce").abs()
    df["price"] = df["price"].mask (df["price"] > 10000, np.nan)
    df["price"] = df["price"].fillna(df["price"].mean()).round(2)


    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["quantity"] = df["quantity"].fillna(1).clip(lower = 0).astype(int)

    df["customer_rating"] =pd.to_numeric(df["customer_rating"], errors="coerce")
    df["customer_rating"]= (
        df["customer_rating"]
        .fillna(df['customer_rating'].median())
        .clip(lower = 0)
        .round(2)
    )

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df['date'] =(
        df["date"]
        .fillna(pd.Timestamp("2026-05-05"))
        .dt.strftime("%m/%d/%Y")
    )

    df["order_id"] = df["order_id"].astype ( str ).str.strip ().str.upper ()
    digits = df["order_id"].str.extract ( r"(\d+)", expand=False ).str.zfill ( 5 )
    df["order_id"] = np.where ( digits.notna (), "ORD-" + digits, "ORD-00000" )
    df = df.drop_duplicates ( subset=["order_id"], keep="first" )

    digits = df["phone_number"].astype ( str ).str.replace ( r"\D", "", regex=True )
    formatted = digits.str.replace (
        r"^(\d{3})(\d{3})(\d{4})$", r"(\1) \2-\3", regex=True
    )
    is_valid = formatted.str.match ( r"^\(\d{3}\) \d{3}-\d{4}$", na=False )
    df["phone_number"] = np.where ( is_valid, formatted, "Unknown" )
    return df

def clean_sales_pipeline(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    pd.set_option('display.max_columns', None)
    pd.set_option ( 'display.width', None )
    df = _clean_text_fields(df)
    df = _clean_numeric_fields(df)
    return df