from operator import index

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

print(f"В текстсі літера \'h\' зустрічається {adwentures_of_tom_sawer.count("h")} разів.")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

count_of_word_from_upper_letter = 0

for element in adwentures_of_tom_sawer:
    if element.istitle():
        count_of_word_from_upper_letter += 1

print(f"В текстсі з великої літери починається {count_of_word_from_upper_letter} слів.")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

first_position_of_word_tom = adwentures_of_tom_sawer.find("Tom")

print(f"Вдруге слово \'Tom\' зустрічається на позиції - {adwentures_of_tom_sawer.find("Tom", first_position_of_word_tom + 1)}.")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print(adwentures_of_tom_sawer_sentences[4].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        print(f"Знайдено речення що починається зі слів \'By the time\'.")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

list_of_words_in_last_sentence = adwentures_of_tom_sawer_sentences[-1].split(" ")

print(f"Кількість слів в останньому реченні - {len(list_of_words_in_last_sentence)}.")

"""
Задача. Розділення логу 
Умова:

На вхід функції потрапляють строки лог-файлу виду:

```

2023-04-27 15:30:45 - TestCase: login_successful

2023-04-27 15:35:12 - TestCase: invalid_password

```

Після строки 'TestCase: ' іде назва тесту.

Зробити так, щоб функця виводила лише назву тесту.

Увага! Замість print у функії використовуйте return.
"""

def solution(test_string):
    find_test_case = test_string.find("TestCase:")
    separated_test_string = test_string.split(" - ")
    if find_test_case != -1:
        new_text = separated_test_string[1].replace("TestCase: ", "")
        return new_text
    else:
        return test_string



print(solution("2023-04-27 15:30:45 - TestCase: login_successful"))
print(solution("2023-04-27 15:35:12 - TestCase: invalid_password"))
print(solution("2023-04-27 15:30:45 - test PASS"))


def check_file_format(file_list: list, extention: str):
    new_list = []
    str_list = str(file_list)
    str_list_exist = str_list.replace("'","").lstrip("[").rstrip("]").split(", ")
    for element in str_list_exist:
        if str(element).find(str(extention)) != -1 :
            new_list.append(element)


    # for element in str_list:
    #     new_list.append(element)

    return new_list



print(check_file_format( ["a.txt", "b.txt", "c.log", "d.html", "e.log", ".diff"], ".txt"))
print(check_file_format(["a.txt", "b.txt", "c.log", "d.html", "e.log", ".diff"],".log"))
print(check_file_format(["a.txt", "b.txt", "c.log", "d.html", "e.log", ".diff"], ".json"))


def change_params(old_value:str, new_value:str):
    filetext = """\
    screen_size = 800x600
    paralel_processes = 10
    db_conection = localhost:5432"""

    filetext = filetext.replace(old_value, new_value)

    return filetext



print(change_params("screen_size = 800x600","screen_size = 1024x800"))
print(change_params("paralel_processes = 10","paralel_processes = 3"))
print(change_params("",""))