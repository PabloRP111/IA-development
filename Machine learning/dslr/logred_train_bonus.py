import sys
import pandas as pd
import aux
import numpy as np

# Calc the average error
def cost(y_binary, predictions):
    m = len(y_binary)

    predictions = np.clip(predictions, 1e-15, 1 - 1e-15) #Avoid limits 0 and 1

    cost = -np.sum(
        y_binary * np.log(predictions)
        + (1 - y_binary) * np.log(1 - predictions)
    ) / m

    return cost

# Adjust the weights using all students
def batch_gradient_descent(x, y_binary, learning_rate, epochs, house):
	weights = np.zeros(x.shape[1])

	for _ in range(epochs):
		z = x @ weights
		predictions = aux.sigmoid(z)

		c = cost(y_binary, predictions)
		if _ % 100 == 0:
			print(f"Model of {house} with BGD, iteration {_}: cost = {c}")

		gradient = (x.T @ (predictions - y_binary)) / len(y_binary) # Look how much add all feature for the average error
		weights -= learning_rate * gradient

	return weights

# Adjust the weights using one student at a time
def stochastic_gradient_descent(x, y_binary, learning_rate, epochs, house):
    weights = np.zeros(x.shape[1])

    for epoch in range(epochs):
        indexes = np.random.permutation(len(y_binary))

        for i in indexes:
            xi = x[i]
            yi = y_binary[i]

            z = xi @ weights
            prediction = aux.sigmoid(z)

            gradient = xi * (prediction - yi) # Look the error for student
            weights -= learning_rate * gradient

        if epoch % 10 == 0:
            predictions = aux.sigmoid(x @ weights)
            c = cost(y_binary, predictions)
            print(f"Model of {house} with SGD, epoch {epoch}: cost = {c}")

    return weights

# Adjust the weights using a small batch of samples
def mini_batch_gradient_descent(x, y_binary, learning_rate, epochs, batch_size,house):
    weights = np.zeros(x.shape[1])

    for epoch in range(epochs):
        indexes = np.random.permutation(len(y_binary))

        x_shuffled = x[indexes]
        y_shuffled = y_binary[indexes]

        for start in range(0, len(y_binary), batch_size):
            end = start + batch_size

            x_batch = x_shuffled[start:end]
            y_batch = y_shuffled[start:end]

            z = x_batch @ weights
            predictions = aux.sigmoid(z)

            gradient = (
                x_batch.T @ (predictions - y_batch)
            ) / len(y_batch)

            weights -= learning_rate * gradient

        # Calculate cost using the complete dataset
        if epoch % 10 == 0:
            predictions = aux.sigmoid(x @ weights)
            c = cost(y_binary, predictions)

            print(
                f"Model of {house} with Mini-batch GD, "
                f"epoch {epoch}: cost = {c}"
            )

    return weights

def train(data, algorithm):
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

		if algorithm == 'BGD':
			weights = batch_gradient_descent(
				x,
				y_binary,
				learning_rate=0.1,
				epochs=1000,
				house=house
			)
		elif algorithm == 'SGD':
			weights = stochastic_gradient_descent(
				x,
				y_binary,
				learning_rate=0.01,
				epochs=50,
				house=house
			)
		else:
			weights = mini_batch_gradient_descent(
				x,
				y_binary,
				learning_rate=0.05,
				epochs=100,
				batch_size=16,
				house=house
			)
		print("")
		models[house] = weights

	return models, x_mean, x_std

def getData(file_n):
	try:
		df = pd.read_csv(file_n)
		clean_data = df.dropna(subset=aux.subjects + ['Hogwarts House']) #Clean n/a
		print(clean_data["Hogwarts House"].value_counts(), "\n")
		return clean_data
	except FileNotFoundError:
			print("Error: .csv not found")
			sys.exit(1)
	except PermissionError:
		print("Error: no permission to read .csv")
		sys.exit(1)

def main():
	if len(sys.argv) != 3 or (sys.argv[2] not in ['SGD', 'BGD', 'MBGD']):
		print("Error: Usage: python logreg_predict.py <dataset.csv> algorithm_name(SGD, BGD, MBGD)")
		sys.exit(1)

	data = getData(sys.argv[1])

	models, x_mean, x_std = train(data, sys.argv[2])

	# Save weights of the models. Also save x_mean and x_std for desnormalize
	np.savez( 
        "weights.npz",
        gryffindor=models["Gryffindor"],
        hufflepuff=models["Hufflepuff"],
        ravenclaw=models["Ravenclaw"],
        slytherin=models["Slytherin"],
        mean=x_mean.to_numpy(),
        std=x_std.to_numpy()
    )
	print("Models saved")

if __name__ == '__main__':
    main()
