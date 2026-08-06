import csv
import sys
import aux

def describe(data):
    stats = {}

    for column_name, values in data.items():

        if len(values) == 0:
            continue

        avg = aux.mean(values)

        stats[column_name] = {
            "Count": len(values),
            "Mean": avg,
            "Std": aux.std_deviation(values, avg),
            "Min": aux.minimum(values),
            "25%": aux.percentile(values, 0.25),
            "50%": aux.percentile(values, 0.50),
            "75%": aux.percentile(values, 0.75),
            "Max": aux.maximum(values)
        }

    return stats

def print_stats(stats):
    MAX_COLS = 12
    headers = list(stats.keys())[:MAX_COLS]
    rows = ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]

    # 1. Calc the dinamic width
    col_widths = {}
    for h in headers:
        # Search the longest value in this colum (.6f ocupa bastantes caracteres)
        max_value_len = max(len(f"{stats[h][row]:.6f}") for row in rows)
        # The width will be the maximum between the name of assignature and it´s largest value, plus an margin of 2 spaces
        col_widths[h] = max(len(h), max_value_len) + 2

    # 2. Print header
    # To leave 8 spaces for each label in the row (Count, Mean, etc.)
    print(f"{'':8}", end="")
    for h in headers:
        print(f"{h:<{col_widths[h]}}", end="")
    print()

    # 3. Print body
    for row in rows:
        print(f"{row:8}", end="")
        for h in headers:
            value = stats[h][row]
            print(f"{value:<{col_widths[h]}.6f}", end="")
        print()

def load_csv(filename):
    try:
        with open(filename, newline='', encoding='utf-8') as file:

            reader = csv.DictReader(file) # Save all row as dictionary

            data = {}

            for row in reader:
                for key, value in row.items():

                    if key not in data:
                        data[key] = []

                    if value != "" and aux.is_number(value):
                        data[key].append(float(value))
    except FileNotFoundError:
        print("Error: data.csv not found")
        sys.exit(1)
    except PermissionError:
        print("Error: no permission to read data.csv")
        sys.exit(1)

    return data

def main():

    if len(sys.argv) != 2:
        print("Usage: python describe.py dataset.csv")
        sys.exit(1)

    dataset = sys.argv[1]

    if not dataset.lower().endswith(".csv"):
        print("Error: file must be a CSV")
        sys.exit(1)

    data = load_csv(dataset)

    stats = describe(data)

    print_stats(stats)


if __name__ == "__main__":
    main()
