import requests
import pandas as pd
import os

# Create folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# Scheme names and AMFI codes
schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)
    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    file_name = f"data/raw/{name}_NAV.csv"
    nav_df.to_csv(file_name, index=False)

    print(f"{name} - Downloaded Successfully")