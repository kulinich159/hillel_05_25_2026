import csv

unique_rows = set()
result_rows = []

def add_unique_rows(filename):
    with open(filename, 'r') as file:
        reader = list(csv.reader(file))

        for row in reader:
            row_to_tuple = tuple(row)
        if row_to_tuple not in unique_rows:
           unique_rows.add(row_to_tuple)
           result_rows.append(row)

    return result_rows

print(add_unique_rows('random.csv'))




# with open('random.csv', 'r') as csvfile1, open('random-michaels.csv', 'r') as csvfile2:
#     reader1 = list(csv.reader(csvfile1))
#     reader2 = list(csv.reader(csvfile2))
#
#     for row in reader1:
#         row_to_tuple = tuple(row)
#
#     for row in reader2:
#         row_to_tuple2 = tuple(row)
#
#     if row_to_tuple not in unique_rows:
#         unique_rows.add(row_to_tuple)
#         result_rows.append(row)


    #     for row2 in reader2:
    #         print(row2)
    #         if row1 == row2:
    #             dif_reader.append(row1)
    # print(dif_reader)


#
# def open_file_as_set(filename):
#
#     with open(filename, 'r') as file:
#         dif_set = set()
#         reader = csv.reader(file)
#         for row in reader:
#             dif_set.add(row)
#     return dif_set


#
# set1 = open_file_as_set("random.csv")
# set2 = open_file_as_set("random-michaels.csv")
#
#
# print(set1)
# set_difference = set1 - set2
#
# print(set_difference)