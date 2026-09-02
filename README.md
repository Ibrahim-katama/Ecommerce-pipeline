# E-Commerce Sales Data Pipeline

A modular Python ETL pipeline for cleaning and standardizing messy e-commerce sales data using Pandas and NumPy.

## Project Status

Data Cleaning, Feature Engineering, and Category Analytics: Complete
## Features

* **Text Cleaning:** Normalizes whitespace and casing, and validates email formats.
* **Numeric Cleaning:** Converts contaminated values, handles outliers above $10,000, and imputes missing values.
* **Date Parsing:** Standardizes mixed date formats and handles missing dates.
* **Identifier Formatting:** Formats Order IDs as `ORD-XXXXX` and phone numbers as `(XXX) XXX-XXXX`.
* **Deduplication:** Removes duplicate records based on primary identifiers.
* **Feature Engineering:** Automatically calculates line-item revenue and extracts month names.
* **Summary Analytics:** Computes category-level metrics and exports aggregated reports.
## Roadmap

* [ ] Category-based aggregations
* [ ] Correlation matrix analysis

## Requirements

* Python 3.x , Pandas , Numpy

## Usage
Run the pipeline with:

```bash
python main.py
```
