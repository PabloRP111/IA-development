import sys
import matplotlib.pyplot as plt
import aux
import math

def get_corr_pearson(x, y):
    mean_x = aux.mean(x)
    mean_y = aux.mean(y)

    numerator = 0
    for i in range(len(x)):
        dx = x[i] - mean_x
        dy = y[i] - mean_y

        numerator += dx * dy

    sum_x = 0
    for i in range(len(x)):
        dx = x[i] - mean_x
        sum_x += dx ** 2

    sum_y = 0
    for i in range(len(y)):
        dy = y[i] - mean_y
        sum_y += dy ** 2

    denominator = math.sqrt(sum_x * sum_y)
    return numerator / denominator

def scatter_plot(data):
    best_corr = 0
    best_pair = (aux.subjects[0], aux.subjects[1])

    best_by_house = {
        "Gryffindor": ([], []),
        "Hufflepuff": ([], []),
        "Ravenclaw": ([], []),
        "Slytherin": ([], [])
    }

    for i in range(len(aux.subjects)):
        for j in range(i + 1, len(aux.subjects)):
            x = []
            y = []

            # Save all the scores for two courses
            for row in data:
                house = row["Hogwarts House"]
                if house == "":
                    continue

                if row[aux.subjects[i]] != "" and row[aux.subjects[j]] != "":
                    x.append(float(row[aux.subjects[i]]))
                    y.append(float(row[aux.subjects[j]]))

            if len(x) < 2:
                continue

            corr = get_corr_pearson(x, y) # Calc the correlation coeficient for two courses
            if abs(corr) > best_corr:
                best_corr = abs(corr)
                best_pair = (aux.subjects[i], aux.subjects[j])

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
                    if row[aux.subjects[i]] != "" and row[aux.subjects[j]] != "":
                        best_by_house[house][0].append(float(row[aux.subjects[i]]))
                        best_by_house[house][1].append(float(row[aux.subjects[j]]))

    print("Best pair:", best_pair)
    print("Correlation:", best_corr)

    for house in best_by_house:
        x, y = best_by_house[house]
        plt.scatter(x, y, label=house, alpha=0.3, s=20)

    plt.xlabel(best_pair[0])
    plt.ylabel(best_pair[1])
    plt.title(f"{best_pair[0]} vs {best_pair[1]}")
    plt.legend()
    plt.show()

def main():
    if len(sys.argv) != 2:
        print("Usage: python sctter_plot.py dataset.csv")
        sys.exit(1)

    dataset = sys.argv[1]
    if not dataset.lower().endswith(".csv"):
        print("Error: file must be a CSV")
        sys.exit(1)

    data = aux.load_csv(dataset)
    scatter_plot(data)

if __name__ == "__main__":
    main()
