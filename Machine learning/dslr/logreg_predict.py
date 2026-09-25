import sys
import numpy as np
import pandas as pd
import aux

def getData(file_n):
	try:
		df = pd.read_csv(file_n)
		clean_data = df.dropna(subset=aux.subjects) #Clean n/a
		weigths = np.load("weights.npz")

		return clean_data, weigths
	except FileNotFoundError:
			print("Error: .csv not found")
			sys.exit(1)
	except PermissionError:
		print("Error: no permission to read .csv")
		sys.exit(1)

def prepare_data(data, weights):
	x = data[aux.subjects].astype(float)
	x_mean = weights["mean"]
	x_std = weights["std"]

	x = (x - x_mean) / x_std
	x = x.to_numpy()
	x = np.c_[np.ones(x.shape[0]), x]

	return x

def predict(x, weights):
    z = x @ weights
    return aux.sigmoid(z)

def main():
	if len(sys.argv) != 2:
		print("Error: Usage: python logreg_predict.py <dataset.csv>")
		sys.exit(1)

	data, weights = getData(sys.argv[1])
	x = prepare_data(data, weights)

	probabilities = np.column_stack([
        predict(x, weights["gryffindor"]),
        predict(x, weights["hufflepuff"]),
        predict(x, weights["ravenclaw"]),
        predict(x, weights["slytherin"])
    ])

	houses = np.array([
    "Gryffindor",
    "Hufflepuff",
    "Ravenclaw",
    "Slytherin"
	])

	predict_indexes = np.argmax(probabilities, axis=1)
	predictions = houses[predict_indexes]
	print(predictions)

	result = pd.DataFrame({
		"Index": data["Index"],
		"Hogwarts House": predictions
	})
	result.to_csv("houses.csv", index=False)

if __name__ == '__main__':
	main()
