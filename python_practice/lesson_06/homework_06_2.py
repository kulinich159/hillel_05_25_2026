# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

while True:

    user_string = str(input("Enter you word there: ")).lower()

    if "h" in user_string:
        print("Word with letter \'h\' - was found")
        break
