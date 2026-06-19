# Написати програму, яка розраховує оподаткування на основі річного доходу користувача.
#
# Отримайте річний дохід користувача.
# Ми припускаємо, що користувач ЗАВЖДИ буде вводити нормальне число (≥0)
# На основі введеного доходу розрахуйте податок за такими умовами:
# Якщо дохід менше ніж 10 000 грн, податок складає 10% від доходу.
# Якщо дохід від 10 000 до 50 000 грн, податок складає 15% від доходу.
# Якщо дохід більше ніж 50 000 грн, податок складає 20% від доходу.
# Запишіть результат у змінну tax_amount.

def calculate_tax(user_income):

    tax_amount = 0

    if user_income < 10000:
        tax_amount += user_income * 0.1
    elif 10000 < user_income < 50000:
        tax_amount += user_income * 0.15
    elif user_income >= 50000:
        tax_amount += user_income * 0.2
    else:
        print("Unexpected condition")

    return tax_amount

print(calculate_tax(50000))



# Ваша задача - написати функцію, яка визначає, чи є введене користувачем число простим чи складеним.
# Зазначте, що користувач завжди буде вводити цілі числа.
#
# Простим вважаємо число, яке має 2 дільники - одиницю і саме це число
#
# Ваш код повинен використовувати цикл та умови для визначення простоти числа.
#
# Запишіть результат в змінну result.

def is_prime_number(number):
    result = 0
    if number % number == 1:
        result += True
    else:
        result += number

    return result


print('---------------------------def------------------ ')

def function_name(params):
    print("Hello World")
    return params

print(function_name("hello"))
print(len([1,2,3]), "asd", sep= " ")


print('---------------------------any  all------------------ ')
print(all([True, True, True]))
print(all([True, False, True]))

def is_even(number):
    return number % 2 == 0

print(is_even(5))
print(is_even(10))

result = [is_even(num) for num in [1,2,3,45,67]]
print(result)
print(any(result))

print("-"*80)
print(all([1,2,3]))

print("-"*80)
print(any([1, False, "Hello"]))

print('---------------------------Enumerate------------------ ')

for k in enumerate(["den", "alex"]):
    print(k)

print(type(enumerate(["den", "alex"])))

for index, name in enumerate(["den", "alex"]):
    print(f"Name {name}, index {index} ")

print('---------------------------Filter------------------------')

print([num for num in range(20) if is_even(num)])
print(list(filter(is_even, range(20))))

my_description = "My      name     is    Alex".split(" ")
print(my_description)

res = []
for i in my_description:
    if len(i):
        res.append(i)

print(res)
print(list(filter(len, my_description)))
print([k for k in my_description if len(k)])

print("---------------------------MAP\ZIP------------------------")

print(list(filter(len, my_description)))

print(list(map(len, my_description)))
print(pow(2, 5))
base_number = [2, 4, 6, 8, 10, 100]
powers = [1, 2, 3, 4, 5, 6]

result_of_map = list(map(pow, base_number, powers))
print(result_of_map)

print(list(zip(my_description, range(20))))

print('---------------------------TYPE\IS_INSTANCE------------------------')

print(isinstance("name", str)) # -> True
print(isinstance("name", int)) # -> False

print(type("name"))

print(type("name") == str) # -> True
print(type("name") == int) # -> False

print(isinstance(False, bool))
print(isinstance(False, int))
print(isinstance(False, object))
print(isinstance("False", object))
print("---------------------------Self Function ------------------------")

def greeting(first_name, second_name):
    print(f"Hell {first_name}, {second_name}")

for full_name in [("alex", "kul"), ("Svet", "Guz")]:
    greeting(first_name=full_name[0], second_name=full_name[1])


def greeting_new_def(first_name: str, second_name: str) -> str:
    """
    :param first_name:
    :param second_name:
    :return:
    """
    print(f"Hell {first_name}, {second_name}")

print("---------------------------args kwargs ------------------------")

def sum_af_all_elements(list_elements):
    return sum(list_elements)

print(sum_af_all_elements([1,2,3]))

def sum_af_all_elements_num(number1, number2, number3):
    return sum([number1, number2, number3])

print(sum_af_all_elements_num(1,2, 3))

def sum_af_all_elements_args(*numbers):
    return sum(numbers)

print(sum_af_all_elements_args(1,2,3,4,5,6,7, * [41, 3, 5]))

def sum_af_all_elements_few_args(double_arg, *args, ignore_arg):
    print("double arg: ", double_arg)
    print("Numbers: ", args)
    print("Ignore number: ", ignore_arg)

    numbers = [g for g in args if g != ignore_arg]

    return sum(numbers) +  double_arg * 2

print(sum_af_all_elements_few_args(1,2,3,4,5,6,7, * [41, 3, 5], ignore_arg=5))