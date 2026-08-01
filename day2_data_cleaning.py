import pandas as pd

print("=" * 70)
print("SCHEME PERFORMANCE DATASET")
print("=" * 70)

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())