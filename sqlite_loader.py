import pandas as pd
from sqlalchemy import create_engine
import os

print("=" * 70)
print("LOADING CLEANED DATASETS INTO SQLITE")
print("=" * 70)

# Create database folder
os.makedirs("database", exist_ok=True)

# Create SQLite database
engine = create_engine("sqlite:///database/bluestock_mf.db")

datasets = {
    "cleaned_nav_history":
        "data/processed/cleaned_nav_history.csv",

    "cleaned_investor_transactions":
        "data/processed/cleaned_investor_transactions.csv",

    "cleaned_scheme_performance":
        "data/processed/cleaned_scheme_performance.csv"
}

for table_name, file_path in datasets.items():

    print(f"\nLoading {table_name}...")

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Rows Loaded : {len(df)}")

print("\n" + "=" * 70)
print("ALL DATASETS LOADED SUCCESSFULLY")
print("=" * 70)