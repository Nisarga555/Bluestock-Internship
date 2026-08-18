import requests
import csv

# --------------------------------------------------
# 1. API endpoint
# --------------------------------------------------

url = "https://api.frankfurter.app/latest?from=USD"

# --------------------------------------------------
# 2. Send GET request
# --------------------------------------------------

response = requests.get(url, timeout=10)

print("=" * 60)
print("REST API DATA EXTRACTION")
print("=" * 60)

print("API URL:", url)
print("Status Code:", response.status_code)

# --------------------------------------------------
# 3. Check response
# --------------------------------------------------

if response.status_code != 200:
    print("❌ API request failed")
    print(response.text)
    raise SystemExit()

# --------------------------------------------------
# 4. Convert JSON response
# --------------------------------------------------

data = response.json()

print("\nJSON RESPONSE:")
print(data)

# --------------------------------------------------
# 5. Extract required fields
# --------------------------------------------------

base_currency = data["base"]
date = data["date"]
rates = data["rates"]

print("\nBase Currency:", base_currency)
print("Date:", date)

print("\nExchange Rates:")
for currency, rate in rates.items():
    print(currency, "=", rate)

# --------------------------------------------------
# 6. Convert JSON → CSV
# --------------------------------------------------

csv_file = "exchange_rates.csv"

with open(csv_file, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "base",
        "date",
        "currency",
        "rate"
    ])

    for currency, rate in rates.items():

        writer.writerow([
            base_currency,
            date,
            currency,
            rate
        ])

print("\n✅ JSON successfully converted to CSV")
print("CSV file created:", csv_file)

# --------------------------------------------------
# 7. Display completion message
# --------------------------------------------------

print("=" * 60)
print("API ASSIGNMENT COMPLETED")
print("=" * 60)