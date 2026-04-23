import pandas as pd

# Load one year of demand data
demand = pd.read_csv("ieso_data/Hourly_Demand_Report_2020-2025/PUB_Demand_2020.csv",
                     skiprows=3)

print(demand.head(10))
print()
print("Shape:", demand.shape)
print("Columns:", demand.columns.tolist())

# Load one year of price data
price = pd.read_csv("ieso_data/HOEP_2020-2025/PUB_PriceHOEPPredispOR_2020.csv", skiprows=3)

print(price.head(10))
print()
print("Shape:", price.shape)
print("Columns:", price.columns.tolist())

# Look at just the price column
print("Price stats:")
print(price['HOEP'].describe())

import matplotlib.pyplot as plt

# Plot one week of prices to see the pattern
week = price.head(168)  # 24 hours x 7 days
plt.figure(figsize=(12, 4))
plt.plot(week['HOEP'])
plt.title('Ontario Electricity Price - First Week of 2020')
plt.xlabel('Hour')
plt.ylabel('Price ($/MWh)')
plt.savefig('first_plot.png')
print("Plot saved as first_plot.png")