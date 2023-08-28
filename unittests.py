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
class TestInputWithDefault(unittest.TestCase):

    def test_input_with_default(self):
        # Testing when user provides input
        with patch('builtins.input', return_value='Hello'):
            self.assertEqual(pyirl.input_with_default("Enter a message: "), 'Hello')

        # Testing when user does not provide input but default value is provided
        with patch('builtins.input', return_value=''):
            self.assertEqual(pyirl.input_with_default("Enter a message: ", default="Default"), 'Default')

        # Testing when user does not provide input and default value is not provided
        with patch('builtins.input', return_value=''):
            self.assertEqual(pyirl.input_with_default("Enter a message: "), '')

if __name__ == '__main__':
    unittest.main()
