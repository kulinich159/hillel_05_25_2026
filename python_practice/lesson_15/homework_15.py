import csv

unique_rows = set()
result_rows = []

def add_unique_rows(filename):
    with open(filename, 'r') as file:
        reader = list(csv.reader(file))


    return result_rows

print(add_unique_rows('random.csv'))
