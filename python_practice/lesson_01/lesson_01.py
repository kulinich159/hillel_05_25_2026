print("hi, rebyatishki")

my_int = 10
another_int = my_int
my_float = 10.1
my_string = "string"
my_list = [1, 2, 3, True, [1, 0], None]
my_tuple = (1, 2, None)
my_set = {1, 3, 4, 5, 6, 7, 5, 4}
my_dictionary = {"key": "value", "key1": {"sub_key": "sub_value"}}

my_bool = True
my_none = None

my_var = None
print(my_var)
my_var = my_int + my_float
print(my_var)
print(my_dictionary)

# snake_case  - naming for Variables
# CamelCase - naming for Classes
# UPPER_SNAKE - naming for Constants

_ = 'Trash variable'
# ctr + alt + l - auto formating

sum_ = 5 + 10
diff = 15 - 20
mult = 5 * 12
div = 50 / 5

print(sum_)
print(diff)
print(mult)
print(div)

if sum_ == 45:
    print("sum_ is equal to 45")
else:
    print("sum_ is NOT equal to 45")


my_name = "Alex"
print("My name", my_name, sep=" ", end="")
print("My name", my_name)

print("Hello", my_name, "My age is", sum_+20)

print(id(my_int))
print(id(another_int))


for letter in "Hello world!":
    print(letter)