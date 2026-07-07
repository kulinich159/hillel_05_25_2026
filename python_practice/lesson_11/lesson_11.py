from python_practice.lesson_07.lesson_07 import result

try:
    print(1 / 0)
except ZeroDivisionError:
    print("You get zero division error")

print("------------------------------------------exception tree example-------------------------------------")
users = [

    {"name": "Alex", "math": 67, "philosophy": 5},
    {"name": "Den", "math": 50, "philosophy": 55},
    {"name": "Ivan", "math": 50, "philosophy": None},
    {"name": "Ivan", "math": 50}

]

users_new = [

    {"name": "Alex", "scores":{"math": 67, "philosophy": 5, "literature": 23}} ,
    {"name": "Den", "scores":{"math": 67, "philosophy": 5}},
    {"name": "Ira", "scores":{"math": 67, "philosophy": 5, "literature": None}},
    {"name": "Dora", "scores":{"math": 67, "philosophy": 0}},
    {"name": "Kira", "scores":{}}

]



def test_count_score(user_list):
    for k in user_list:
        # if  k["philosophy"] is None:   # Поганий варіант
        #     continue
        try:
            assert k["math"] + k["philosophy"] > 0
            print(k["name"], k["math"] + k["philosophy"])
            print("Test passed")
            print("-"*80)
        except TypeError as exception_instance:
            print(f"Can't get correct data {k}")
            print("Warning!!! Bad data")
            print(exception_instance)
            print("-"*80)
        except KeyError as key:
            print(f"No key {key} in file! It's a bug!")
            print("Test failed")
            print("-" * 80)
        except Exception as e:
            print("Unexpected error")
            print(e)



test_count_score(users)

print("------------------------------------------else example exception-------------------------------------")

def get_user_score(user):
    scores = user.get("scores")
    sum_ = 0
    for s in scores:
        try:
            sum_ += scores[s]
        except TypeError:
            print(f"set none for {s}")
    try:
        result = sum_ / len(scores)
    except ZeroDivisionError:
        print(f"No data for user {user['name']}")
        return 0
    else: # виконується якщо помилок не було
        print("We can see this only if no errors appeared")
    finally: # виконується у будь-якому випадку
        print(f"Finally: user has score: {sum_}")
    return result

for user in users_new:
    print(f"User name is {user['name']}")
    print(f"User name is {get_user_score(user)}")
    print("-"*80)

# Структура
# try
# many exception
# else
# finally
print("------------------------------------------raise example-------------------------------------")

def check_age(age):
    if age < 0:
        raise ValueError("Вік не може бути від'ємним")

try:
    user_age = int(input("Введіть ваш вік: "))
    check_age(user_age)
    print(f"Ваш вік: {user_age}")
except ValueError as ve:
    print(f"Помилка: {ve}")