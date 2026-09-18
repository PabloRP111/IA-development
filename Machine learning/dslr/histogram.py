import sys
import aux
import matplotlib.pyplot as plt
import numpy as np

def histogram(houses):
    fig, axes = plt.subplots(4, 4, figsize=(16, 12))
    axes = axes.flatten()

    for i, subject in enumerate(aux.subjects):
        ax = axes[i]

        for house in houses:
            ax.hist(
                houses[house].get(subject, []), #if this house hasn´t values for this subject, .get return a empty list
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

def score_homogeneity(houses):
    scores = {}
    for subject in aux.subjects:
        means = [aux.mean(houses[house].get(subject, [np.nan])) for house in houses]
        stds = [np.std(houses[house].get(subject, [np.nan])) for house in houses]
        # normalizamos por la dispersión general para comparar asignaturas distintas
        scores[subject] = np.std(means) / aux.mean(stds)

    sorted_scores = sorted(scores.items(), key=lambda x: x[1])
    print(f"Subject | Homogeneity Score")

    for subject, score in sorted_scores: 
        print(f"{subject}: {score}")

    print(f"\nThe course with more homogeneity is {sorted_scores[0][0]} "
          f"with a score of {sorted_scores[0][1]:.4f}")

def preprocesing(data):
    houses = {
        "Gryffindor": {},
        "Hufflepuff": {},
        "Ravenclaw": {},
        "Slytherin": {}}
    
    for row in data:
        house = row["Hogwarts House"]
        for subject in aux.subjects:
            value = row[subject]

            if value == "":
                continue
            if subject not in houses[house]:
                houses[house][subject] = []
            
            houses[house][subject].append(float(value))
    return houses

def main():
    if len(sys.argv) != 2:
        print("Usage: python hstogram.py dataset.csv")
        sys.exit(1)

    dataset = sys.argv[1]
    if not dataset.lower().endswith(".csv"):
        print("Error: file must be a CSV")
        sys.exit(1)

    data = aux.load_csv(dataset)
    houses = preprocesing(data)
    score_homogeneity(houses)
    histogram(houses)

if __name__ == "__main__":
    main()
