class Quadrature:
    """
    Represents a quadrature with a given side length.
    """
    def __init__(self, side_length):
        self.__side_length = side_length

    def perimeter(self):
        return 4 * self.__side_length

    def square(self):
        return self.__side_length**2

def sum_of_chars_in_string(user_list):
    """
    Calculates the sum of comma-separated numbers from the last string in the list.

    :param user_list: A list of strings containing comma-separated chars.
    :return: The sum of numbers from element in the list
    """
    for element in user_list:
        chars_sum = sum(int(x) for x in element.split(","))
    return chars_sum

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




