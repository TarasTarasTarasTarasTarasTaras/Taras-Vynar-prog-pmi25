import unittest
from Validation import *
from basedata_test import basedata_valid_attr


class TestValidation(unittest.TestCase):
    validation = Validation()


    def test_isstr_valid(self):
        test_valid = Validation.validate_is_str('key', 'filename.txt')
        self.assertTrue(test_valid)

    
    def test_isstr_invalid(self):
        try:
            Validation.validate_is_str('key', 11111111)
            self.fail() # if not exception - bad validate, test error
        except ValueError:
            return True


    def test_filename_isstr_valid(self):
        test_valid = self.validation.validate_file('key', 'filename.txt')
        self.assertTrue(test_valid)

    
    def test_filename_isstr_invalid(self):
        try:
            self.validation.validate_file('key', 11111111)
            self.fail() # if not exception - bad validate, test error
        except ValueError:
            return True


    def test_format_file_valid(self):
        test_valid = self.validation.validate_file('key', 'filename.txt')
        self.assertTrue(test_valid)


    def test_format_file_invalid(self):
        try:
            self.validation.validate_file('key', 'filename.json')
            self.fail() # if not exception - bad validate, test error
        except ValueError:
            return True



