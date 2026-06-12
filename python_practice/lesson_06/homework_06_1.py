# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

user_string = input("Enter text there: ")

unique_chars = len(set(user_string))

more_than_ten_elements = True
less_than_ten_elements = False

if unique_chars > 10:
    print(more_than_ten_elements)
else:
    print(less_than_ten_elements)

