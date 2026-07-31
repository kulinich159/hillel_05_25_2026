import logging
logging.basicConfig(filename="decorator.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

'''
Генератори:
1. Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
'''
def even_generator(number):
    counter = 0
    while counter <= number:
        if counter % 2 == 0:
            yield counter
        counter += 1


even = even_generator(10)
for element in even:
    print(element)

'''
Генератори:  
2. Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
'''
def fibonacci_generator(number):
    a, b = 0, 1
    while a <= number:
        yield a
        a, b = b, a + b

fibonacci = fibonacci_generator(10)
for element in fibonacci:
    print(element)


'''
Ітератори:
1. Реалізуйте ітератор для зворотного виведення елементів списку.
'''
class ReversedList:
    def __init__(self, list_of_elements):
        self.list_of_elements = list_of_elements
        self.__current = len(list_of_elements)

    def __iter__(self):
        return self

    def __next__(self):
        self.__current = self.__current - 1
        if self.__current >= 0:
            return self.list_of_elements[self.__current]
        else:
            raise StopIteration


list_of_numbers = [11, 12, 32, 23, 34, 65, 98]
some_list = ReversedList(list_of_numbers)
for element in some_list:
    print(element)


'''
Ітератори:
2. Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
'''
class EvenNumbersInDiapason:
    def __init__(self, max_number):
        self.max_number = max_number
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.current += 1
            if self.current <= self.max_number:
                if self.current % 2 == 0:
                     return self.current
            else:
                raise StopIteration


some_list1 = EvenNumbersInDiapason(27)

for element in some_list1:
    print(element)

'''
Декоратори:
1. Напишіть декоратор, який логує аргументи та результати викликаної функції.
'''
def logs_arguments_and_result(function):
    def wrapper(*args, **kwargs):
        logging.info(f"Function '{function.__name__}' arguments: args={args}, kwargs={kwargs}")
        result = function(*args, **kwargs)
        logging.info(f"Function '{function.__name__}' result: {result}")
        return result
    return wrapper

list_of_numbers1 = []
@logs_arguments_and_result
def adding_to_new_list(list_of_some_elements):
    for e in list_of_some_elements:
        list_of_numbers1.append(e)
    return list_of_numbers1

adding_to_new_list(list_of_numbers)

'''
Декоратори:
2. Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції..
'''
def cath_exceptions(function):
    def wrapper(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except Exception as exception:
            logging.error(f"During running function '{function.__name__}' was exception: {exception}")
    return wrapper

