import unittest
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
from python_practice.lesson_14.control_work import Book

class CheckBookFunctions(unittest.TestCase):
    def test_if_book_available(self):
        book = Book("title", "author", 244)
        book.is_available = True
        actual_result = book.borrow()
        expected_result = "Книгу видано"
        self.assertEqual(actual_result, expected_result)

    def test_if_book_not_available(self):
        book = Book("title", "author", 244)
        book.is_available = False
        with self.assertRaises(ValueError):
            book.borrow()

    def test_if_book_can_be_return(self):
        book = Book("title", "author", 244)
        book.is_available = False
        actual_result = book.return_book()
        expected_result = "Книгу повернуто"
        self.assertEqual(actual_result, expected_result)

    def test_if_book_can_not_be_return(self):
        book = Book("title", "author", 244)
        book.is_available = True
        with self.assertRaises(ValueError):
            book.return_book()

    def test_if_book_can_be_return(self):
        book = Book("title", "author", 144)
        actual_result = book.reading_time(12)
        expected_result = 12
        self.assertEqual(actual_result, expected_result)

    def test_reading_time_less_then_zero(self):
        book = Book("title", "author", 244)
        with self.assertRaises(ValueError):
            book.reading_time(-5)

