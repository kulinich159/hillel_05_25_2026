import unittest
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))

from python_practice.lesson_12.functions  import sum_of_chars_in_string
from python_practice.lesson_12.functions  import Quadrature
from python_practice.lesson_12.functions  import count_sum_of_even_numbers

class CheckSumOfCharsInString(unittest.TestCase):

     def test_countable_chars_in_list_element(self):
         actual_result = sum_of_chars_in_string(["1,2,3,4"])
         expected_result = 10
         self.assertEqual(actual_result, expected_result)

     def test_uncountable_chars_in_list_element(self):
         with self.assertRaises(ValueError):
             sum_of_chars_in_string(["1,2", "qwerty"])

     def test_empty_string_element_in_list(self):
         with self.assertRaises(ValueError):
            sum_of_chars_in_string([""])

     def test_incorrect_element_type_in_list(self):
         with self.assertRaises(AttributeError):
             sum_of_chars_in_string([5])

     def test_incorrect_type_of_data(self):
         with self.assertRaises(TypeError):
             sum_of_chars_in_string(4)

     def test_empty_data(self):
        with self.assertRaises(TypeError):
            sum_of_chars_in_string()


class CheckCountingOfQuadrature(unittest.TestCase):

    def test_check_int_side_perimeter(self):
        quadrature = Quadrature(3)
        actual_result = quadrature.perimeter()
        expected_result = 12
        self.assertEqual(actual_result, expected_result)

    def test_check_int_side_square(self):
        quadrature = Quadrature(3)
        actual_result = quadrature.square()
        expected_result = 9
        self.assertEqual(actual_result, expected_result)

    def test_check_zero_side_perimeter(self):
        quadrature = Quadrature(0)
        actual_result = quadrature.perimeter()
        expected_result = 0
        self.assertEqual(actual_result, expected_result)

    def test_check_zero_side_square(self):
        quadrature = Quadrature(0)
        actual_result = quadrature.square()
        expected_result = 0
        self.assertEqual(actual_result, expected_result)

    def test_check_float_side_perimeter(self):
        quadrature = Quadrature(2.5)
        actual_result = quadrature.perimeter()
        expected_result = 10.0
        self.assertEqual(actual_result, expected_result)

    def test_check_float_side_square(self):
        quadrature = Quadrature(2.5)
        actual_result = quadrature.square()
        expected_result = 6.25
        self.assertEqual(actual_result, expected_result)

class TestCountSumOfEvenNumbers(unittest.TestCase):

    def test_sum_of_even_numbers(self):
        actual_result = count_sum_of_even_numbers([1, 2, 3, 4, 5, 6])
        expected_result = 12
        self.assertEqual(actual_result, expected_result)

    def test_empty_list(self):
        actual_result = count_sum_of_even_numbers([])
        expected_result = 0
        self.assertEqual(actual_result, expected_result)

    def test_negative_numbers(self):
        actual_result = count_sum_of_even_numbers([-2, -4, 1, 3])
        expected_result = -6
        self.assertEqual(actual_result, expected_result)

    def test_incorrect_type_of_element(self):
        with self.assertRaises(TypeError):
            count_sum_of_even_numbers(["4", True, [], 3])

if __name__ == "__main__":
    unittest.main(verbosity=2)