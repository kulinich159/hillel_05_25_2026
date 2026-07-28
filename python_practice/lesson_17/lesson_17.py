# iter()
# next()
import time

list_of_numbers = [11, 12, 32, 23, 34, 65]
list_of_numbers2 = [111, 112, 1212, 123, 134, 165]

iter_object = iter(list_of_numbers)
iter_object2 = iter(list_of_numbers2)

# print(type(iter_object))
#
# print(next(iter_object))
# print(next(iter_object))
# print(next(iter_object2))
# print(next(iter_object))
# print(next(iter_object2))
# print(next(iter_object))
# print(next(iter_object))
# print(next(iter_object2))

try:
    while True:
        print(next(iter_object))
except StopIteration:
    pass

print("-Simple_Iterator-"*10)

class SimpleRangeIterator:
    def __init__(self, max_number):
        self.__current = -1
        self.max_number = max_number

    def __next__(self):
        self.__current = self.__current + 1
        if self.__current == self.max_number:
            raise StopIteration
        return  self.__current

    def __iter__(self):
        return self

for el in SimpleRangeIterator(10):
    print(el)

print("-Simple_Numbers_Iterator-"*10)

class SimpleNumbersIterator:
    def __init__(self, quantity_simple_numbers):
        self.quantity_simple_numbers = quantity_simple_numbers
        self.__current_num = 2
        self.__quantity_returned = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__quantity_returned == self.quantity_simple_numbers:
            raise StopIteration
        self.__quantity_returned = self.__quantity_returned + 1
        self.__get_simple_number()
        return self.__current_num

    def __get_simple_number(self):
        while True:
            self.__current_num += 1
            if self.__is_prime(self.__current_num):
                return self.__current_num

    def __is_prime(self, number):
        for k in range(2, number - 1):
            if number % k == 0:
                return False
        return True

for el in SimpleNumbersIterator(5):
    print(el)

print("-generator_example-" * 10)

#yield

def get_names():
    return ["Alex", "Den", "Ivan"]

def get_names_gen():
    print("return Alex")
    yield "Alex"
    print("return Den")
    yield "Den"
    print("return Ivan")
    yield "Ivan"

print(get_names())
for name in get_names_gen():
    print(name)

print("-generator_timer-" * 10)
# def do_something(counter):
#     for _ in range(counter):
#         print("Sending requests to server...")
#         time.sleep(2)
#         print("end of sending")
#         yield "requests was successfully"
#
# for _ in do_something(5):
#     pass

def greeting(first_name):
    print(f"Hi {first_name}")

def good_morning(fn, first_name):
    print(f"Good morning!")
    fn(first_name)



my_new_func = greeting
my_new_func("Den")

good_morning(greeting, "Artem")

print("-decorator_timer-" * 10)

def greeting_decorator(function):
    def wrapper(*args, **kwargs):
        print("Good morning")
        return function(*args, **kwargs)
    return wrapper

@greeting_decorator
def greeting_second(first_name):
    print(f"Hi {first_name}")


greeting_second("Al6owa")
