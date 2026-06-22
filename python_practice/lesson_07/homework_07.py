# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result >= 25:
            # Enter the action to take if the result is greater than 25
            break
        print(f"{number} x {multiplier} = {result}")

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_of_two_numbers(number_one,number_two):
    print(f"Сума чисел = {sum([number_one, number_two])}")

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def arithmetic_mean(*args):
    print(f"Середнє арифметичне списку чисел {args} = {sum([*args])/len([*args])}")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(user_str):
    print(f"Рядок {user_str} у зворотному порядку:")
    return user_str[::-1]

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word_in_list(list_of_words):
    longest_word = list_of_words[0]
    for word in list_of_words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
def count_of_unique_chars(user_str):
    """
    Checks if the string contains more than 10 unique characters.

    :param user_str: String to check.
    :return: True if the number of unique characters is greater than 10,and False in other case.
    """
    return len(set(user_str)) > 10

print(count_of_unique_chars(input("Введіть текст: ")))


# task 8
def find_word_with_h_letter_inside():
    """
    Repeatedly asks the user to enter a word containing the letter 'h' or 'H'.
    Function checks the entered word regardless of letter case and stopes if the word contains the letter 'h'

    :return: User word that contain letter 'h' or 'H'.
    """
    while True:
        user_word = input("Введіть слово з літерою \'h\': ")

        if "h" in user_word.lower():
            return user_word

        print("У слові немає літери \'h\'. Спробуйте ще раз.")

word_with_h_letter = find_word_with_h_letter_inside()
print(f"Знайдено слово з літерою \'h\' - {word_with_h_letter}")

# task 9
def find_string_values_in_list(user_list):
    """
    Function that filtered input list and returns only string values.

    :param user_list: List with elements of any data type.
    :return: List containing only string elements from user_list.
    """
    lst2 = []

    for value in user_list:
        if type(value) == str:
            lst2.append(value)
    return lst2

print(find_string_values_in_list(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']))

# task 10
import random

def count_sum_of_even_numbers(user_list):
    """
    Function that find even number from user_list with numbers and count sum of this even numbers

    :param user_list: List with users numbers.
    :return: Sum of even numbers from user_list
    """
    sum_of_element = 0
    for element in user_list:
        if element % 2 == 0:
            sum_of_element += element
    return sum_of_element

print(f"Сумма парних елементів із списка = {count_sum_of_even_numbers([random.randint(1, 100) for item in range(20)])}")

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""