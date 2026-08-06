import csv
import sys
import matplotlib.pyplot as plt
import numpy as np

subjects = [
        "Arithmancy",
        "Astronomy",
        "Herbology",
        "Defense Against the Dark Arts",
        "Divination",
        "Muggle Studies",
        "Ancient Runes",
        "History of Magic",
        "Transfiguration",
        "Potions",
        "Care of Magical Creatures",
        "Charms",
        "Flying"]

def compute_homogeneity(houses):
    scores = {}

    for subject in subjects:

        means = []

        for house in houses:
            values = houses[house][subject]
            means.append(sum(values) / len(values))

        scores[subject] = np.std(means)

    return scores

def histogram(houses):
    fig, axes = plt.subplots(4, 4, figsize=(16, 12))
    axes = axes.flatten()

    for i, subject in enumerate(subjects):
        ax = axes[i]

        for house in houses:
            ax.hist(
                houses[house][subject],
                bins=20,
                alpha=0.5,
                density=True,
                label=house
            )

        ax.set_title(subject)

    fig.legend(
        ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"],
        loc="upper right"
    )
    plt.tight_layout()
    plt.show()

def preprocesing(data):
    houses = {
        "Gryffindor": {},
        "Hufflepuff": {},
        "Ravenclaw": {},
        "Slytherin": {}}
    
    for row in data:
        house = row["Hogwarts House"]
        for subject in subjects:
            value = row[subject]

            if value == "":
                continue
            if subject not in houses[house]:
                houses[house][subject] = []
            
            houses[house][subject].append(float(value))

    return houses

def load_csv(filename):
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file) # Save all row as dictionary
            return list(reader)
    except FileNotFoundError:
        print("Error: data.csv not found")
        sys.exit(1)
    except PermissionError:
        print("Error: no permission to read data.csv")
        sys.exit(1)

    return data

def main():
    if len(sys.argv) != 2:
        print("Usage: python hstogram.py dataset.csv")
        sys.exit(1)

    dataset = sys.argv[1]

    if not dataset.lower().endswith(".csv"):
        print("Error: file must be a CSV")
        sys.exit(1)

    data = load_csv(dataset)
    houses = preprocesing(data)
    histogram(houses)

if __name__ == "__main__":
    main()
