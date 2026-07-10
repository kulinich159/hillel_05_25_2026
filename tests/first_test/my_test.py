import unittest
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
# print(sys.path)
# print(pathlib.Path(__file__).parent.parent.parent)
from  function import some_function

def sum_two_numbers(a, b):
    return a + b

class MyTest(unittest.TestCase):

    def test_example(self):
        actual_result = some_function(2, 3)
        expected_result = 5
        self.assertEqual(expected_result, actual_result)

    def test_example_second(self):
        actual_result = sum_two_numbers(2, 3)
        expected_result = 4
        self.assertEqual(actual_result, expected_result)

    # def test_example_third(self):
    #     actual_result = [
    #         {"Name": "Alex", "Age": "30", "Position":"AQA"},
    #         {"Name": "Den", "Age": "23", "Position": "QA"},
    #         {"Name": "Ivan", "Age": "56", "Position": "Developer"},
    #         ]
    #     expected_result =  [
    #         {"Name": "Alex", "Age": "``30``", "Position":"23"},
    #         {"Name": "Den", "Age": "232", "Position": "QA"},
    #         {"Name": "Ivan", "Age": "56", "Position": "Developer"},
    #         ]
    #     self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":  # спеціальна конструкція яка дає можливість запуску із консолі
    unittest.main(verbosity=2)


