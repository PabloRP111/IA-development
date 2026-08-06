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

def scatter_plot(data):
    best_corr = 0
    best_pair = (subjects[0], subjects[1])

    best_by_house = {
        "Gryffindor": ([], []),
        "Hufflepuff": ([], []),
        "Ravenclaw": ([], []),
        "Slytherin": ([], [])
    }

    for i in range(len(subjects)):
        for j in range(i + 1, len(subjects)):
            x = []
            y = []

            for row in data:
                house = row["Hogwarts House"]
                if house == "":
                    continue

                if row[subjects[i]] != "" and row[subjects[j]] != "":
                    x.append(float(row[subjects[i]]))
                    y.append(float(row[subjects[j]]))

            if len(x) < 2:
                continue

            corr = np.corrcoef(x, y)[0, 1]
            if abs(corr) > best_corr:
                best_corr = abs(corr)
                best_pair = (subjects[i], subjects[j])

                # reset
                best_by_house = {
                    "Gryffindor": ([], []),
                    "Hufflepuff": ([], []),
                    "Ravenclaw": ([], []),
                    "Slytherin": ([], [])
                }

                # rebuild grouped data
                for row in data:
                    house = row["Hogwarts House"]
                    if house == "":
                        continue
                    if row[subjects[i]] != "" and row[subjects[j]] != "":
                        best_by_house[house][0].append(float(row[subjects[i]]))
                        best_by_house[house][1].append(float(row[subjects[j]]))

    print("Mejor par:", best_pair)
    print("Correlación:", best_corr)

    for house in best_by_house:
        x, y = best_by_house[house]
        plt.scatter(x, y, label=house, alpha=0.3, s=20)

    plt.xlabel(best_pair[0])
    plt.ylabel(best_pair[1])
    plt.title(f"{best_pair[0]} vs {best_pair[1]}")
    plt.legend()
    plt.show()

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
        print("Usage: python sctter_plot.py dataset.csv")
        sys.exit(1)

    dataset = sys.argv[1]

    if not dataset.lower().endswith(".csv"):
        print("Error: file must be a CSV")
        sys.exit(1)

    data = load_csv(dataset)
    scatter_plot(data)

if __name__ == "__main__":
    main()
