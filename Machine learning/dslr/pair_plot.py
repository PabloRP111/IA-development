import matplotlib.pyplot as plt
import sys
import aux

def pair_plot(data):
    n = len(aux.subjects)

    # Create matrix
    fig, axes = plt.subplots(n, n, figsize=(20, 20))

    for i in range(n):
        for j in range(n):
            ax = axes[i][j]

            if i != j:
                subject_x = aux.subjects[j]
                subject_y = aux.subjects[i]

                gryffindor_x = []
                gryffindor_y = []
                hufflepuff_x = []
                hufflepuff_y = []
                ravenclaw_x = []
                ravenclaw_y = []
                slytherin_x = []
                slytherin_y = []

                for row in data:
                    if row[subject_x] == "" or row[subject_y] == "":
                        continue

                    x = float(row[subject_x])
                    y = float(row[subject_y])

                    house = row["Hogwarts House"]

                    if house == "Gryffindor":
                        gryffindor_x.append(x)
                        gryffindor_y.append(y)
                    elif house == "Hufflepuff":
                        hufflepuff_x.append(x)
                        hufflepuff_y.append(y)
                    elif house == "Ravenclaw":
                        ravenclaw_x.append(x)
                        ravenclaw_y.append(y)
                    elif house == "Slytherin":
                        slytherin_x.append(x)
                        slytherin_y.append(y)

                ax.scatter(gryffindor_x, gryffindor_y)
                ax.scatter(hufflepuff_x, hufflepuff_y)
                ax.scatter(ravenclaw_x, ravenclaw_y)
                ax.scatter(slytherin_x, slytherin_y)

            else: # DIAGONAL
                subject = aux.subjects[i]

                gryffindor = []
                hufflepuff = []
                ravenclaw = []
                slytherin = []

                for row in data:
                    if row[subject] == "":
                        continue

                    score = float(row[subject])
                    house = row["Hogwarts House"]
                    if house == "Gryffindor":
                        gryffindor.append(score)
                    elif house == "Hufflepuff":
                        hufflepuff.append(score)
                    elif house == "Ravenclaw":
                        ravenclaw.append(score)
                    elif house == "Slytherin":
                        slytherin.append(score)

                ax.hist(gryffindor)
                ax.hist(hufflepuff)
                ax.hist(ravenclaw)
                ax.hist(slytherin)

            # LABELS
            if i == n - 1:
                ax.set_xlabel(aux.subjects[j], rotation=45)
            if j == 0:
                ax.set_ylabel(
                    aux.subjects[i],
                    rotation=0,
                    labelpad=60,
                    va="center"
                )

    plt.tight_layout()
    plt.subplots_adjust(left=0.1, bottom=0.1)
    plt.savefig("pair_plot.png")
    plt.show()
    plt.close()

def main():
    if len(sys.argv) != 2:
        print("Usage: python pair_plot.py dataset.csv")
        sys.exit(1)

    dataset = sys.argv[1]

    if not dataset.lower().endswith(".csv"):
        print("Error: file must be a CSV")
        sys.exit(1)

    data = aux.load_csv(dataset)

    pair_plot(data)


if __name__ == "__main__":
    main()
