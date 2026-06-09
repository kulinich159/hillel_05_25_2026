from operator import ifloordiv
from xml.sax.handler import property_lexical_handler

name = "Alex"
print(id(name))

name = name + "Kulinich"
print(id(name))

# mutable types - list, dict, set, bytearray
my_list_names = ["alex", "Den"]
print(id(my_list_names))
print(my_list_names)

my_list_names.append("ivan")
print(id(my_list_names))
print(my_list_names)


print("-------------tuple-------------")

my_tuple = ('Alex', "Den", "Ivan")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])

for i in my_tuple:
    print(i)

print("-------------tuple unpack-------------")

my_name, den_name, vik_name = ("Alex", "Den", "Viktor")
my_names = ("Alex", "Den", "Viktor")

print(den_name)
print(my_names)
print(*my_names)

# Добавляем декілька значень в not_my_name
my_name, *not_my_name  = ("Alex", "Den", "Viktor", "chichik")

print(my_name)
print(*not_my_name)
print(not_my_name)

some_text = "some_text"

tuple_text = tuple(some_text)
print(tuple_text)

tuple_with_one_element = (42,)
not_tuple = (42)

print(type(tuple_with_one_element))
print(type(not_tuple))

print("-------------List-------------")
# list це мютебл і ітерабельний елемент

my_new_list_names = ["Alex", "Den", "Viktor", "chichik", "Viktor"]

# append
my_list_names.append("Gora")

additional_list = [1,2,3]

# extend
my_new_list_names.extend(additional_list)
print(my_new_list_names)

# insert
my_new_list_names.insert(1, "Sofa")
print(my_new_list_names)

# pop
poped_element = my_new_list_names.pop(-1)
print(poped_element)
print(my_new_list_names)

element_to_delete = "Viktor"
list_of_viktor = []

for element in my_new_list_names:
    if element == element_to_delete:
        list_of_viktor.append(element)

print(list_of_viktor)

for element in list_of_viktor:
    my_new_list_names.remove(element)

print(my_new_list_names)

my_list_ages = [1, 23,56,23,76, 5, 34]
some_list_of_names = ["Alex", "Den", "Viktor", "chichik", "Viktor"]
viktor_name_count = some_list_of_names.count("Viktor")

print(some_list_of_names)
print(viktor_name_count)

while viktor_name_count > 0:
    some_list_of_names.remove(element_to_delete)
    viktor_name_count -= 1

print(some_list_of_names)

print("-------------------lambda sorted------------------")
def my_fn(word):
    word_lenght = len(word)
    return word_lenght

sorted_names_custom = sorted(some_list_of_names)
sorted_names_custom_lambda = sorted(some_list_of_names, key=lambda x: len(x))
# sorted_names_custom = sorted(my_list_ages, key=my_fn)
print(sorted_names_custom)
print(sorted_names_custom_lambda)

print("-------------------List comprehensive------------------")

string_example = "some text here"
list_strig = list(string_example)

print(list_strig)

my_numbers = [1, 2, 3, 4, 5, 6, 7]

list_comprehensive = [i ** 2 for i in my_numbers if i % 2 == 0 ]

sq_list = []

for i in my_numbers:
    if i % 2 == 0:
        sq_list.append(i**2)

print(sq_list)

print(list_comprehensive)

print("-------------------Dictionaries------------------")
# pare key = value
# ключі унікальні i хешабельні

my_dict = {"name": "Elena", "age": 29, "has_job": True}
print(my_dict)

my_dict["new_key"] = "new_value"
print(my_dict)

my_dict["new_key"] = "new_value_new"
print(my_dict)

new_dict_update = {"some_new_key": "some_new_value"}
my_dict.update(new_dict_update)
print(my_dict)

# словник в словнику
my_dict["new_dict_key"] = new_dict_update
print(my_dict)

# get
print(my_dict["age"])
print(my_dict.get("new_key"))

# не видає кей ерор
print(my_dict.get("new_key1"))

print("-------------------Dictionaries iteration------------------")

print(list(my_dict.keys()))
for i in my_dict.keys():
    print(i)

for i in my_dict.values():
    print(i)

for i in my_dict.items():
    print(i)

for key, value in  my_dict.items():
    print("ky-ky", key, value)
