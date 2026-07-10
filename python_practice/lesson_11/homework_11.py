test_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def sum_of_chars_in_string(user_list):
    for element in user_list:
        try:
            chars_sum = sum(int(x) for x in element.split(","))
            print(chars_sum)
        except ValueError:
            print(f"Не можу це зробити!")

sum_of_chars_in_string(test_list)