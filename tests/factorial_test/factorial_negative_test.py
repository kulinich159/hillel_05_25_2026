import unittest
import sys
import pathlib
import logging
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))

from function import factorial
logger = logging.getLogger('root')

class FactorialNegativeTest(unittest.TestCase):
    def test_factorial_negative_number(self):
        expected_error_message = 'You have to use 0 or positive numbers. You put -5'
        logger.info(f"Some logger info message {expected_error_message}")
        with self.assertRaises(ValueError) as value_error:
            factorial(-5)
        exception = value_error.exception
        actual_error_message = exception.args[0]
        self.assertEqual(expected_error_message , actual_error_message, msg="Wrong Error appeared")

        pass

    def test_factorial_not_number(self):
        with self.assertRaises(TypeError):
            factorial("Hello")
