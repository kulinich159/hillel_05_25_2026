alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don\'t much care where ——" said Alice.
"Then it doesn\'t matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'''

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
square_of_black_see = 436402
square_of_azov_see = 37800

print(f"Площа Чорного та Азовського морів: {square_of_black_see + square_of_azov_see} км2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
all_goods_in_storages = 375291
first_storage = all_goods_in_storages - 222950
third_storage = all_goods_in_storages - 250449
second_storage = all_goods_in_storages - first_storage - third_storage

print(f"На 1 складі розміщено: {first_storage} товар, на 2 складі: {second_storage} товарів, "
      f"на 3 складі: {third_storage} товари")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
month_payment = 1179
count_of_month_payments = 18

print(f"Загальна вартість комп’ютера складає: {month_payment * count_of_month_payments} грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print(f"Остача від ділення чисел a): {8019 % 8}")
print(f"Остача від ділення чисел b): {9907 % 9}")
print(f"Остача від ділення чисел c): {2789 % 5}")
print(f"Остача від ділення чисел d): {7248 % 6}")
print(f"Остача від ділення чисел e): {7128 % 5}")
print(f"Остача від ділення чисел f): {19224 % 9}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza_price = 274
count_big_pizza = 4
medium_pizza_price = 218
count_medium_pizza = 2
juice_price = 35
count_juice = 4
cake_price = 350
count_cake = 1
water_price = 21
count_water = 3

cost_of_all_foods = (big_pizza_price * count_big_pizza) + (medium_pizza_price * count_medium_pizza) + (
            juice_price * count_juice) + (cake_price * count_cake) + (water_price * count_water)

print(f"Для оформлення замовлення знадобиться {cost_of_all_foods} грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
count_of_all_foto = 232
count_of_foto_in_one_page = 8

print(f"Щоб вклеїти всі фото потрібно буде щонайменше {count_of_all_foto / count_of_foto_in_one_page} сторінок альбому")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
fuel_consumption_every_hundred_km = 9
distance_for_liter_fuel = 100 / fuel_consumption_every_hundred_km
fuel_tank_in_auto = 48

liter_of_fuel_that_need_to_trip = distance / distance_for_liter_fuel
count_of_gasoline_fill_up = liter_of_fuel_that_need_to_trip / fuel_tank_in_auto

print(f"1). Для такої подорожі знадобиться {liter_of_fuel_that_need_to_trip} літрів бензину")
print(f"2). Родині необхідно заїхати на заправку щонайменше {int(count_of_gasoline_fill_up)} рази")
