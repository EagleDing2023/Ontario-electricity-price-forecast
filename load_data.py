import pandas as pd
import os

# Define file paths
price_dir = "ieso_data/HOEP_2020-2025"
demand_dir = "ieso_data/Hourly_Demand_Report_2020-2025"
years = [2020, 2021, 2022, 2023, 2024, 2025]

# Load all price files
price_frames = []
for year in years:
    path = os.path.join(price_dir, f"PUB_PriceHOEPPredispOR_{year}.csv")
    df = pd.read_csv(path, skiprows = 3)
    df['Year'] = year
    price_frames.append(df)

price_all = pd.concat(price_frames, ignore_index = True)
print("Price data shape:", price_all.shape)

# Load all demand files
demand_frames = []
for year in years:
    path = os.path.join(demand_dir, f"PUB_Demand_{year}.csv")
    df = pd.read_csv(path, skiprows = 3)
    df['Year'] = year
    demand_frames.append(df)

demand_all = pd.concat(demand_frames, ignore_index = True)
print("Demand data shape:", demand_all.shape)

# Check date ranges
print("Price date range:", price_all['Date'].min(), "to", price_all['Date'].max())
print("Demand date range:", demand_all['Date'].min(), "to", demand_all['Date'].max())


# Merge price and demand on Date and Hour
combined = pd.merge(price_all[['Date', 'Hour', 'HOEP']],
                    demand_all[['Date', 'Hour', 'Ontario Demand']],
                    on=['Date', 'Hour'],
                    how='inner')

print("Combined shape:", combined.shape)
print(combined.head(10))

# Save combined dataset to a single CSV
combined.to_csv("ieso_data/combined_2020_2025.csv", index=False)
print("Saved combined dataset")