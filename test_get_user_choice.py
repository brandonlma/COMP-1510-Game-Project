from unittest import TestCase
from unittest.mock import patch

import movement

class Test(TestCase):
    @patch('builtins.input', side_effect='W')
    def test_get_user_choice_up(self,_):
        actual = movement.get_user_choice()
        expected = 'W'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect='S')
    def test_get_user_choice_down(self,_):
        actual = movement.get_user_choice()
        expected = 'S'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect='D')
    def test_get_user_choice_right(self,_):
        actual = movement.get_user_choice()
        expected = 'D'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect='A')
    def test_get_user_choice_left(self,_):
        actual = movement.get_user_choice()
        expected = 'A'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1','W'])
    def test_get_user_choice_wrong_value_int(self,_):
        actual = movement.get_user_choice()
        expected = 'W'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Q','A'])
    def test_get_user_choice_wrong_value_string(self,_):
        actual = movement.get_user_choice()
        expected = 'A'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['6.5','W'])
    def test_get_user_choice_wrong_value_float(self,_):
        actual = movement.get_user_choice()
        expected = 'W'
        self.assertEqual(expected, actual)
