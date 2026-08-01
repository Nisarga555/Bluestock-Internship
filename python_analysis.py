import pandas as pd

# ==========================================
# STEP 1: Load the raw dataset
# ==========================================
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("=" * 70)
print("ORIGINAL DATASET")
print("=" * 70)

print("Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# ==========================================
# STEP 2: Data Cleaning
# ==========================================

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# ==========================================
# STEP 3: Save cleaned dataset
# ==========================================

output_path = "data/processed/cleaned_scheme_performance.csv"

df.to_csv(output_path, index=False)

# ==========================================
# STEP 4: Verify saved file
# ==========================================

cleaned_df = pd.read_csv(output_path)

print("\n" + "=" * 70)
print("CLEANED DATASET")
print("=" * 70)

print("Shape:", cleaned_df.shape)

print("\nFirst 5 Rows:")
print(cleaned_df.head())

print("\nColumns:")
print(cleaned_df.columns.tolist())

print("\n✅ Cleaned dataset recreated successfully!")
print(f"📁 Saved at: {output_path}")