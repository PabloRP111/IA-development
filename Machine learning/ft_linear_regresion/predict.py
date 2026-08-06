import json
import sys

# Load model
try:
    with open("model.json", mode="r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: model.json not found")
    sys.exit(1)
except json.JSONDecodeError:
    print("Error: model.json is corrupted")
    sys.exit(1)

# Validate model keys
required_keys = [
    "theta0",
    "theta1",
    "max_km",
    "max_price",
]

for key in required_keys:
    if key not in data:
        print(f"Error: missing key '{key}' in model")
        sys.exit(1)

theta0 = data["theta0"]
theta1 = data["theta1"]
max_km = data["max_km"]
max_price = data["max_price"]

# Validate normalization
if max_km == 0:
    print("Error: max_km cannot be 0")
    sys.exit(1)

# User input
try:
    km = float(input("Enter mileage: "))

    if km < 0:
        print("Mileage cannot be negative")
        sys.exit(1)
except ValueError:
    print("Invalid mileage")
    sys.exit(1)

# Prediction
km_norm = km / max_km

pred = theta0 + theta1 * km_norm

real_price = pred * max_price

print(f"Estimated price: {real_price:.2f}")
