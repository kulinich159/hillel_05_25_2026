import csv

def add_rows_from_file_to_set(*files):
    unique_rows_from_file = set()
    for filename in files:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                unique_rows_from_file.add(tuple(row))
    return unique_rows_from_file

with open('result_Kulinich.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(add_rows_from_file_to_set("random-michaels.csv", "random.csv"))



