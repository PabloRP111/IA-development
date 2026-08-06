import csv
import json
import math
import sys
import matplotlib.pyplot as plt

km = []
price = []

# DATA PREPROCESING
#-------------------
# Open file and Read
try:
    with open("data.csv", mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        next(reader)  # skip header
        print("Dataset:\n Km | Price")

        for row in reader:
            try:
                x = int(row[0]) # Km
                y = int(row[1]) # Price
                # Validate values
                if x < 0 or y < 0:
                    print(f"Skipping negative values: {row}")
                    continue
                
                print(x, " ", y)
                km.append(x)
                price.append(y)
            except ValueError as e:
                print(f"Skipping non numeric row: {row}")
except FileNotFoundError:
    print("Error: data.csv not found")
    sys.exit(1)
except PermissionError:
    print("Error: no permission to read data.csv")
    sys.exit(1)

# Validate data
if len(km) == 0 or len(price) == 0:
    print("Error: dataset is empty")
    sys.exit(1)

# Normalize
max_km = max(km)
max_price = max(price)

if max_km == 0:
    print("Error: max_km cannot be 0")
    sys.exit(1)

if max_price == 0:
    print("Error: max_price cannot be 0")
    sys.exit(1)

km_norm = []
price_norm = []

for x in km:
	km_norm.append(x / max_km)
for y in price:
    price_norm.append(y / max_price)

# TRAINING
#----------
theta0 = 0
theta1 = 0

m = len(km_norm) # Number of data
lr = 0.01 # Learning rate
iterations = 1000 # Numbers of adjustments for the straight line

for i in range(iterations):
    sum_error_y = 0
    sum_error_x = 0
    
    for j in range(m):
         x = km_norm[j]
         y = price_norm[j]
         
         pred = theta0 + theta1 * x
         error = pred - y
         sum_error_y += error
         sum_error_x += error * x
    
    tmp_theta0 = lr * (sum_error_y / m)
    tmp_theta1 = lr * (sum_error_x / m)

    theta0 -= tmp_theta0
    theta1 -= tmp_theta1

# Validate model
if (math.isnan(theta0) or math.isnan(theta1)
    or math.isinf(theta0) or math.isinf(theta1)):
    print("Error: invalid theta values")
    sys.exit(1)


# MAE (Mean Absolute Error) y MSE (Mean Square Error)
#---------------
total_absolute_error = 0
total_square_error = 0
for i in range(m):
    pred_norm = theta0 + theta1 * km_norm[i]
    pred = pred_norm * max_price
    error = price[i] - pred
    total_square_error += error ** 2
    total_absolute_error += abs(error)

mae = total_absolute_error / m
mse = total_square_error / m
print(f"\nMAE: {mae:.2f}\nMSE: {mse:.2f}")

# CREATE GRAPHIC
#----------------
print("\nDisplaying graph ...")
plt.scatter(km, price, color='blue', label='Datos')

# Calculate x
min_km = min(km)
min_km_norm = min_km / max_km

# Calculates y normalize
pred_price_min_norm = theta0 + (theta1 * min_km_norm)
pred_price_max_norm = theta0 + (theta1 * 1.0) # max_km / max_km its always 1.0

# Desnormalize
pred_price_min = pred_price_min_norm * max_price;
pred_price_max = pred_price_max_norm * max_price;

x_recta = [min_km, max_km]
y_recta = [pred_price_min, pred_price_max]

# Draw points
plt.plot(x_recta, y_recta, color='red', linestyle='--', linewidth=2, label='Tendencia')

plt.title("Dots Graphic of a Price Car Prediction")
plt.xlabel("Km")
plt.ylabel("Price")
plt.grid(True)
plt.legend()
plt.show()

# SAVE MODEL
#------------
model = {
    "theta0": theta0,
    "theta1": theta1,
    "max_km": max_km,
    "max_price": max_price
}

try:
    with open("model.json", "w") as f:
        #Save .json
        json.dump(model, f, indent=4)
        print("\nTheta0: ", theta0)
        print("Theta1: ", theta1, "\n")
        print("Model saved successfully")
except PermissionError:
    print("Error: no permission to save model.json")
except OSError as e:
    print(f"Error saving model: {e}")
