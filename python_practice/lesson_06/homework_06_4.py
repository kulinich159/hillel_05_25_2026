# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

import random

list_of_elements = [random.randint(1, 100) for item in range(20)]
sum_of_element = 0

for element in list_of_elements:
    if element % 2 == 0:
        sum_of_element += element

print(f"Сумма парних елементів із списка = {sum_of_element}")
