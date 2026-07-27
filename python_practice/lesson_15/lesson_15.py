import pathlib
import os
import csv
import json

file_path = "file_for_read_write.txt"
from constantas import BASE_PROJECT_PATCH
# mode="?"  ?-- options
# r - reading, читання файлу
# w - write, запис.перетворення файлу
# a - append, доповнення файлу, якшо файлу нема - він створиться
# r+ - read + write, файл маэ бути присутній
# w+ - read + write, файл може не бути
# a+ - read + append, файлу може не бути

# with open(file_path, mode="w") as f:
#     f.write("line1\n")
#     f.write("line2\n")

with open(file_path, mode="w") as f:
    f.write("line3\n")
    f.write("line4\n")
    f.write(r"line5\n")
    f.write(" lin\'e4\\\n")
    f.write(file_path)
    f.writelines(["\nwritelines1\n", "writelines2\n", "writelines3\n"])
    f.write("ERROR")

with open(file_path, mode="r") as f:
    data = f.read()
    print(data)

with open(file_path, mode="r") as f:
    data = f.readlines()
    print(data)

with open(file_path, mode="r") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())

with open(file_path, mode="r") as f:

    while True:
        line = f.readline()
        if "ERROR" in line:
            print(line)
            break

print("--"*80)

current_dir = pathlib.Path().absolute()

print(type(current_dir))
print(current_dir)
print(current_dir.name)
print(current_dir.parent)
print("--"*80)
parents = current_dir.parents

for par in parents:
    print(par.name)

for path_ in current_dir.iterdir():
    if path_.is_file():
        print(path_.name)



lesson_04_full_path = os.path.join(str(current_dir.parent), "lesson04")
print(lesson_04_full_path)

for path_ in pathlib.Path(lesson_04_full_path).iterdir():
    if path_.is_file():
        print(path_.name)
print("--"*80)

for path_ in pathlib.Path(lesson_04_full_path).iterdir():
    if path_.is_dir():
        print(path_.name)

file_to_find = "lesson_04.py"

for current_path, folders, files in os.walk(BASE_PROJECT_PATCH):
    if file_to_find in files:
        print(os.path.join(current_path, file_to_find))

print("CSV--"*40)

# Дані для запису у CSV-файл
data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Alice', 25, 'Los Angeles'],
    ['Bob', 35, 'Chicago']
]

# Відкриття CSV-файлу для запису
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

with open('output.csv', 'r') as csvfile:
    reader = list(csv.reader(csvfile))
    header = reader[0]
    rows = reader[1:]
    print("Header", header)
    for row in reader:
        print(row)

print("JSON--"*40)


# Дані для запису у JSON-файл
user_data = [
    {"name": "John","age": 30,"city": "New York", "is_active": True},
    {"name": "Alex","age": 45,"city": "New York1", "is_active": False},
    {"name": "Ivan","age": 67,"city": "New York2", "has_friends": None}
]

user_data_json = json.dumps(user_data)
print(user_data_json)

# Запис JSON-даних у файл
with open('user_data.json', 'w') as file:
    json.dump(user_data, file, indent=4)

# with open('user_data.json') as file:  # для txt файлів
#     data = json.loads(file.read())
with open('user_data.json') as file:
    data2 = json.load(file)


print(data)
print(data2)