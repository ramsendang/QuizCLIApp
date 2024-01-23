import unittest
from unittest.mock import patch
from io import StringIO
import sys
import time
from colorama import Fore, Style, init
init()
from spinner import spinner
from menu import menu
from userInput import *

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.original_time_sleep = time.sleep
        self.original_time_time = time.time

    def tearDown(self):
        time.sleep = self.original_time_sleep
        time.time = self.original_time_time

    # testing spinner 
    def test_spinner(self):
        # Redirect stdout for capturing printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Mock time.sleep to avoid actual waiting during the test
        with patch('time.sleep') as mock_sleep:
            # Configure mock_sleep to do nothing (return None)
            mock_sleep.return_value = None

            # Mock time.time to control the time during the test
            with patch('time.time') as mock_time:
                # Configure mock_time to return specified values in sequence
                mock_time.side_effect = [0, 0.1, 0.2, 0.3, 0.4, 0.5]

                # Call the spinner function
                spinner(duration=0.3)

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Check the captured output against the expected spinner frames pattern
        expected_output_pattern = r'\r[-/\\|\\ ]*'  # Allow for spaces and variations
        self.assertRegex(captured_output.getvalue(), expected_output_pattern)

    # testting showMenu function 
    def test_show_menu(self):
        # Arrange
        instance = menu()
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        # Act
        instance.showMenu()

        # Assert
        captured_output = sys.stdout.getvalue()
        expected_output = (
            "\x1b[32m Available Options are :) \n"
            "\x1b[33m 1) Start a Quiz\n"
            "\x1b[33m 2) View your score history\n"
            "\x1b[33m 3) View Top Players\n"
            "\x1b[33m 4) Quite Quiz app \n"
        )
        self.assertIn(expected_output, captured_output)

        sys.stdout = saved_stdout

    @patch('builtins.input', return_value='2')  # Mocking user input with '2'
    def test_get_menu_options(self, mock_input):
        # Arrange
        expected_output = "You have selected option 2\n"
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        # Act
        result = getMenuOptions()

        # Assert
        self.assertEqual(result, '2')  # Ensure the function returns the user input
        self.assertEqual(sys.stdout.getvalue(), expected_output)

        sys.stdout = saved_stdout

    @patch('builtins.input', return_value='2')  # Mocking user input with '2'
    def test_get_user_answer(self, mock_input):
        # Arrange
        expected_output = "You have Selected answer 2\n"
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        # Act
        result = getUserAnswer()

        # Assert
        self.assertEqual(result, '2')  # Ensure the function returns the user input
        self.assertEqual(sys.stdout.getvalue(), expected_output)

        sys.stdout = saved_stdout
if __name__ == '__main__':
    unittest.main()