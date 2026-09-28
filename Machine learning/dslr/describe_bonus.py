import sys
import aux
import csv

def describe(data, missing):
    stats = {}

    for column_name, values in data.items():

        if len(values) == 0:
            continue

        avg = aux.mean(values)
        variance = aux.variance(values, avg)
        std = aux.std_deviation(variance)
        minimum = aux.minimum(values)
        maximum = aux.maximum(values)
        q25 = aux.percentile(values, 0.25)
        q75 = aux.percentile(values, 0.75)

        stats[column_name] = {
            "Count": len(values),
            "Mean": avg,
            "Variance": variance,
            "Std": std,
            "Missing values": missing[column_name],
            "Min": minimum,
            "Max": maximum,
            "Range": maximum - minimum,
            "25%": q25,
            "50%": aux.percentile(values, 0.50),
            "75%": q75,
            "IQR": q75 - q25,
            "Skewness": aux.skewness(values, avg, std)
        }
    return stats

def print_stats(stats):
    MAX_COLS = 12
    headers = list(stats.keys())[:MAX_COLS]
    rows = ["Count", "Mean", "Variance", "Std", "Min", "Max", "Range", "Missing values", "25%", "50%", "75%", "IQR", "Skewness"]
    integer_rows = ["Count", "Missing values"]

    # 1. Calc the dinamic width
    col_widths = {}
    for h in headers:
        # Search the longest value in this colum (.6f)
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
        print(f"{row:15}", end="")

        for h in headers:
            value = stats[h][row]

            if row in integer_rows:
                print(f"{int(value):<{col_widths[h]}}", end="")
            else:
                print(f"{value:<{col_widths[h]}.6f}", end="")

        print()

def load_csv(filename):
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            data = {}
            missing = {}

            for row in reader:
                for key, value in row.items():

                    if key not in data:
                        data[key] = []
                        missing[key] = 0

                    if value != "" and aux.is_number(value):
                        data[key].append(float(value))
                    else:
                        missing[key] += 1

            return data, missing

    except FileNotFoundError:
        print("Error: data.csv not found")
        sys.exit(1)

    except PermissionError:
        print("Error: no permission to read data.csv")
        sys.exit(1)

def main():

    if len(sys.argv) != 2:
        print("Usage: python describe.py dataset.csv")
        sys.exit(1)

    dataset = sys.argv[1]

    if not dataset.lower().endswith(".csv"):
        print("Error: file must be a CSV")
        sys.exit(1)

    data, missing = load_csv(dataset)

    stats = describe(data, missing)

    print_stats(stats)

if __name__ == "__main__":
    main()
