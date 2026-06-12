# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

user_string = str(input("Enter text there: "))

list_of_chars = list(user_string)
unique_set_of_chars = set(user_string)

more_than_ten_elements = True
less_than_ten_elements = False

for element_in_set in unique_set_of_chars:
    count_of_unique_element = 0
    for element_in_list in list_of_chars:
        if element_in_list == element_in_set:
            count_of_unique_element += 1
    if count_of_unique_element > 10:
        # До True/False додав вивід самого символа і його к-ть в строці
        print(f"Count of char \'{element_in_set}\' = {count_of_unique_element} {more_than_ten_elements}")
    else:
        print(f"Count of char \'{element_in_set}\' = {count_of_unique_element} {less_than_ten_elements}")
