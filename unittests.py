import unittest
from unittest.mock import patch
import pyirl


class TestBooleanInput(unittest.TestCase):

    @patch('builtins.input', return_value='y')
    def test_boolean_input_returns_true_for_y(self, mock_input):
        result = pyirl.boolean_input("Enter 'y': ")
        self.assertTrue(result)

    @patch('builtins.input', return_value='n')
    def test_boolean_input_returns_false_for_n(self, mock_input):
        result = pyirl.boolean_input("Enter 'n': ")
        self.assertFalse(result)

    @patch('builtins.input', return_value='')
    def test_boolean_input_returns_default_value(self, mock_input):
        result = pyirl.boolean_input("Enter nothing: ", default=True)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
