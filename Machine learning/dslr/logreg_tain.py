import sys
import pandas as pd
import aux
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z)) # returns an array result of e^-z[x] for each position 

def cost(y_binary, predictions):
    m = len(y_binary)

    predictions = np.clip(predictions, 1e-15, 1 - 1e-15)

    cost = -np.sum(
        y_binary * np.log(predictions)
        + (1 - y_binary) * np.log(1 - predictions)
    ) / m

    return cost

def gradient_descent(x, y_binary, learning_rate, iterations):
	weights = np.zeros(x.shape[1])

	for _ in range(iterations):
		z = x @ weights
		predictions = sigmoid(z)

		c = cost(y_binary, predictions)
		if _ % 100 == 0:
			print(f"Iteration {_}: cost = {cost}")

		gradient = (x.T @ (predictions - y_binary)) / len(y_binary)

		weights -= learning_rate * gradient

	return weights

def train(data):
	x = data[aux.subjects]		# Features
	y = data["Hogwarts House"]	# Target

	x = x.astype(float) #castToFLoat
	
	#Normalize
	x_mean = x.mean()
	x_std = x.std()
	x = (x - x_mean) / x_std 

	# Convert to NumPy
	x = x.to_numpy()
	y = y.to_numpy()

	#Add a first colum as a bias with value 1
	x = np.c_[np.ones(x.shape[0]), x] 

	models = {}
	for house in aux.houses:
		y_binary = (y == house).astype(int)

		weights = gradient_descent(
			x,
			y_binary,
			learning_rate=0.1,
			iterations=1000
		)
		models[house] = weights

	return models

def getData(file_n):
	try:
		df = pd.read_csv(file_n)
		clean_data = df.dropna(subset=aux.subjects + ['Hogwarts House']) #Clean n/a
		print(clean_data["Hogwarts House"].value_counts())
		return clean_data
	except FileNotFoundError:
			print("Error: .csv not found")
			sys.exit(1)
	except PermissionError:
		print("Error: no permission to read .csv")
		sys.exit(1)

def main():
	if len(sys.argv) != 2:
		print("Error: Usage: python logreg_train.py <dataset.csv>")
		sys.exit(1)
	data = getData(sys.argv[1])
	models = train(data)

if __name__ == '__main__':
    main()
