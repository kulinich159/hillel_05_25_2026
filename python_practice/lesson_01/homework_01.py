# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = storona_1 + storona_2 + storona_3 + storona_4
print("Периметр фігури з task 05 =", perimeter)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2

all_trees_in_garden = apple_trees + pear_trees + plum_trees

print("В саду посадили", all_trees_in_garden, "дерев")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temperature_before_dinner = 5
temperature_after_dinner = temperature_before_dinner - 10
temperature_late_evening = temperature_after_dinner + 4

print("Температура надвечір становить: ", temperature_late_evening, "°C", sep="")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""

all_boys_in_theater_group = 24
all_girls_in_theater_group = all_boys_in_theater_group / 2
absent_boys = 1
absent_girls = 2

today_present_kids = ((all_boys_in_theater_group - absent_boys) + (all_girls_in_theater_group - absent_girls))

print("Сьогодні на театральному гуртку було", int(today_present_kids), "дітей")


# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""

first_book_price = 8
second_book_price = first_book_price + 2
third_book_price = (first_book_price + second_book_price) / 2

print("Вартість 3 примірників книг буде дорівнювати", first_book_price + second_book_price + third_book_price, "грн")