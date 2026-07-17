''' Створіть клас Book.
Поля:
title
author
pages
is_available

Методи
borrow()
Видає книгу.
Якщо книга вже видана → ValueError.

return_book()
Повертає книгу.
Якщо книга вже знаходиться у бібліотеці → ValueError.

reading_time(speed)
Повертає час читання.
pages / speed
де
speed — сторінок за годину.
speed > 0 '''


class Book:
    def __init__(self, title, author, pages, is_available=None):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_available = is_available

    def borrow(self):
        if self.is_available is True:
            self.is_available = False
            print(self.is_available)
            return f"Книгу видано"
        else:
            raise ValueError("Книга вже видана")

    def return_book(self):
        if self.is_available is False:
            self.is_available = True
            return f"Книгу повернуто"
        else:
            raise ValueError("Вже знаходиться у бібліотеці")

    def reading_time(self, speed):
        if speed <= 0:
            raise ValueError("Швидкість повинна бути більше 0")
        else:
            return self.pages / speed


book = Book("title", "author" , 244)
book.is_available = True

print(book.borrow())
print(book.is_available)

''' Дано список:
 logs = [
     "LoginTest,PASSED,1.24",
     "PaymentTest,FAILED,2.81",
     "CartTest,PASSED,0.93",
     "SearchTest,FAILED,1.78",
     "LogoutTest,PASSED,0.65",
 ]
 Потрібно реалізувати функції.
 parse_logs(logs)
 Повертає список словників
 [
     {
         "name": "LoginTest",
         "status": "PASSED",
         "duration": 1.24
     },
     ...
 ]

 count_passed(logs)
 Повертає кількість успішних тестів.

 count_failed(logs)
 Повертає кількість невдалих тестів.

 get_failed_tests(logs)
 Повертає список назв тестів, що впали.

 get_average_duration(logs)
 Повертає середню тривалість виконання.

 sort_by_duration(logs)
 Повертає список тестів, відсортований за часом виконання (від більшого до меншого). '''

logs = [
     "LoginTest,PASSED,1.24",
     "PaymentTest,FAILED,2.81",
     "CartTest,PASSED,0.93",
     "SearchTest,FAILED,1.78",
     "LogoutTest,PASSED,0.65",
 ]

keys = ["name","status","duration"]

print(len(logs))
def parse_logs(some_list):
    for element in logs:
        new_dict = dict(zip(keys, element))
    print(new_dict)


parse_logs(logs)
