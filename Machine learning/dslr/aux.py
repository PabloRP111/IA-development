import math
import sys
import csv

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

houses = [
    "Gryffindor",
    "Hufflepuff",
    "Ravenclaw",
    "Slytherin"
]

def is_number(value):
    try:
        float(value) # If is numb is casteable
        return True
    except:
        return False

def mean(values):
    total = 0
    count = 0

    for v in values:
        total += v
        count += 1
    return total / count

def minimum(values):
    min_value = values[0]

    for v in values:
        if v < min_value:
            min_value = v

    return min_value

def maximum(values):
    max_value = values[0]

    for v in values:
        if v > max_value:
            max_value = v
    
    return max_value

def std_deviation(values, avg):
    total = 0
    count = 0

    for v in values:
        total += (v - avg) ** 2
        count += 1
    
    variance = total / count

    return math.sqrt(variance)

def percentile(values, percent):
    sorted_values = sorted(values)

    k = (len(sorted_values) - 1) * percent
    f = math.floor(k)
    c = math.ceil(k)

    if f == c:
        return sorted_values[int(k)] # Easy case, the numb is integer

    # Complex case, lineal interpolation
    d0 = sorted_values[f] * (c -k)
    d1 = sorted_values[c] * (k - f)

    return d0 + d1

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
