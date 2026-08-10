import pandas as pd

df = pd.read_csv("data/raw/10_benchmark_indices.csv")

print("=" * 70)
print("BENCHMARK DATASET")
print("=" * 70)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 10 Rows:")
print(df.head(10))

print("\nData Types:")
print(df.dtypes)

print("\nUnique Index Names:")
for col in df.columns:
    if df[col].dtype == "object" or str(df[col].dtype).startswith("str"):
        print(f"\n{col}:")
        print(df[col].unique())