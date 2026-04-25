import pandas as pd

# Load the combined datase
df = pd.read_csv("ieso_data/combined_2020_2025.csv")

# Convert Date column to datetime type to extract parts from it
df['Date'] = pd.to_datetime(df['Date'])

# Extract time-based features
df['day_of_week'] = df['Date'].dt.dayofweek   # 0=Monday, 6=Sunday
df['month'] = df['Date'].dt.month             # 1-12
df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)  # 1 if weekend, 0 if weekday

# Lag features - price from 24 hours ago and 48 hours ago
df['price_lag_24'] = df['HOEP'].shift(24)
df['price_lag_48'] = df['HOEP'].shift(48)

# Demand lag
df['demand_lag_24'] = df['Ontario Demand'].shift(24)

print(df.head(30))
print()
print("Columns:", df.columns.tolist())
print("Shape:", df.shape)

# Drop rows where lag features are NaN
df = df.dropna()
print("Shape after dropping NaN rows:", df.shape)

# Save the feature dataset
df.to_csv("ieso_data/features_2020_2025.csv", index=False)
print("Saved feature dataset")