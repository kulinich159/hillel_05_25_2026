import unittest
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))

from python_practice.lesson_13.homework_10 import log_event

class CheckLogEvent(unittest.TestCase):

    def test_logging_level_of_success_event(self):
        log_event("Alex", "success")
        with open("login_system.log") as file:
            log_content = file.read().splitlines()
            self.assertTrue(log_content[-1].endswith("INFO"))


    def test_logging_level_of_expired_event(self):
        log_event("Alex", "expired")
        with open("login_system.log") as file:
            log_content = file.read().splitlines()
            self.assertTrue(log_content[-1].endswith("WARNING"))


    def test_logging_level_of_failed_event(self):
        log_event("Alex", "failed")
        with open("login_system.log") as file:
            log_content = file.read().splitlines()
            self.assertTrue(log_content[-1].endswith("ERROR"))

    def test_logging_adding_new_record(self):
        with open("login_system.log") as file:
            log_content_len_before_new_event = len(file.read().splitlines())

        log_event("Alex", "expired")

        with open("login_system.log") as file:
            log_content_len_after_new_event = len(file.read().splitlines())
            self.assertEqual(log_content_len_after_new_event, log_content_len_before_new_event + 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)