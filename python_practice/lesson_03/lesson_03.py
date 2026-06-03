first_string = "String example #1 n \'n"
second_string = 'String example #2'
# lorem_ipsum_text = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam pulvinar augue lacus, \n'
#                     'ut cursus orci scelerisque quis. Nulla et pretium orci, quis vehicula mi. Duis sapien odio, mollis\n'
#                     '\tsed odio lobortis, euismod efficitur \"enim\". Integer tempus tortor at nibh efficitur vehicula. \n'
#                     '\tClass aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. \n'
#                     '\\Suspendisse sit amet luctus sapien. Fusce id posuere est. Quisque vulputate egestas turpis. \n'
#                     'Morbi nec ornare lectus. Proin rutrum libero elementum, imperdiet diam quis, condimentum neque. \n'
#                     'Nullam quis hendrerit turpis. Aenean non diam magna. Nulla maximus sodales eros, placerat convallis \n'
#                     'lorem mollis volutpat. Donec nec turpis mattis, eleifend tellus non, ullamcorper lorem. Aliquam \n'
#                     'viverra, nisl vel mattis pulvinar, enim massa pulvinar tortor, a tristique nunc turpis id odio.')
#
# lorem_ipsum_triple = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam pulvinar augue lacus,
# ut cursus orci scelerisque quis. Nulla et pretium orci, quis vehicula mi. Duis sapien odio, mollis sed odio lobortis,
# euismod efficitur enim. Integer tempus tortor at nibh ef o.'''

print(first_string)
print(second_string)
# print(lorem_ipsum_text)
# print(lorem_ipsum_triple)

print(5**2)
print(2**10)

print(7/2)
print(10/3)
print(4%2)


# 5 -> 0101 -> 0010
print(5>>1)

name = 'Alex'
age = 36

# 1 - True
# 0 - False
if name == "Alex" and age == 36:
    print("Hello Alex")
#  &  теж саме що and
if (name == "Alex") & (age == 36):
    print("Hello Alex")

print(5 + 5 == 10)
true_number = 0.2 + 0.1
true_number_no = round(true_number, 2)
print("--------")
print(true_number_no)
print(true_number_no == 0.3)

print("--------")
print(0.1 + 0.2 == 0.3)
print(0.1 + 0.2)

# name = input("What is you name:")
# age = int(input("What is you age:"))

print("My name is", name, "I am", age, "years old")
final_string = f"My name is {name},I am {age} years old"

print(final_string)

print("---------------------------------Sequences------------------------")

string_seq = 'Hello World'
list_seq = [0,2,3,4,6]
tuple_seq = {1,2,3}
dict_seq = {"name":"AAA", "age":"BBB", "pass":"CCC"}

print(string_seq)
print(list_seq)
print(tuple_seq)
print(dict_seq)
print(string_seq[6])
print(string_seq[len(string_seq)-1])


print(string_seq[1])
print(list_seq[1])
# Неможливо отримати індекс елементу в таплу і словнику якшо не укащаний кей як індекс
# print(tuple_seq[1])
# print(dict_seq[1])
print(string_seq[1:len(string_seq)-1])

# Піднесення до степеня
print(pow(5, 2))

print(max([1, 2, 3, 4]))
print(min([1, 2, 3, 4]))


