import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, root_mean_squared_error

# Load feature dataset
df = pd.read_csv("ieso_data/features_2020_2025.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Define feature and target
features = ['Hour', 'day_of_week', 'month', 'is_weekend', 'Ontario Demand', 'price_lag_24', 'price_lag_48', 'demand_lag_24']
target = 'HOEP'

# Train/test split by time - train on 2020-2023, test on 2024+
train = df[df['Date'] < '2024-01-01']
test = df[df['Date'] >= '2024-01-01']

X_train = train[features]
y_train = train[target]
X_test = test[features]
y_test = test[target]

print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Model trained")

# Make predictions
predictions = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, predictions)
rmse = root_mean_squared_error(y_test, predictions)
print(f"MAE: {mae:.2f} $/MWh")
print(f"RMSE: {rmse:.2f} $/MWh")
