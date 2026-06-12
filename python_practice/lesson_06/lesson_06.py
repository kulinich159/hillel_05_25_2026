dct_cmp = {number: number**2 for number in range(10)}
print(dct_cmp)

# names = ["Alex", "Den", "Ivan", "Sofa", "Viktor"]
# dict_with_names =

print("-------------set-------------")

my_set = {1,3, "", 5, 67, 8, 3, 56, 4, 3}

# will be error
# my_set = {1, {1,2}}
print(my_set)

my_set.add(99)
my_set.add(991)
print(my_set)

some_variable = my_set.pop()
print(some_variable)
print(my_set)

my_set.remove(991)
print(my_set)


my_set_34 = [1001, 1002, 1003, 1004, 1005]

len_list = len(my_set_34)
len_set = len(set(my_set_34))

print(len_list)
print(len_set)

print(len_list==len_set)

print("-------------for-------------")
ages = [10, 20, 30, 40]

for _ in range(10):
    print("Hello")

response = [
    {"id": 1, "name": "Read_1", "description": "descr_1"},
    {"id": 1, "name": "Read_2", "description": "descr_2"},
    {"id": 3, "name": "Read_3", "description": "descr_3"},
    {"id": 4, "name": "Read_4", "description": "descr_4"},
    {"id": None, "name": "Read_None", "description": None}
]

for permission in response:
    if permission.get("id") is None:
        print(f"Alarm no id for permission {permission}")

uniq_ids = []
for perm in response:
    if perm.get("id") in uniq_ids:
        print(f"Id's are not uniq, id = {perm.get('id')}")
    else:
        uniq_ids.append(perm.get('id'))