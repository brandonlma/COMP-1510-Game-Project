from unittest import TestCase

import user_information


class TestIsAlive(TestCase):
    def test_is_alive_thirty(self):
        player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Waist': 30}
        actual = user_information.is_alive(player)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_alive_fifty_five(self):
        player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Waist': 55}
        actual = user_information.is_alive(player)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_alive_sixty(self):
        player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Waist': 60}
        actual = user_information.is_alive(player)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_alive_ninety(self):
        player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Waist': 90}
        actual = user_information.is_alive(player)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_alive_ninety_nine(self):
        player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Waist': 99}
        actual = user_information.is_alive(player)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_alive_one_hundred(self):
        player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Waist': 100}
        actual = user_information.is_alive(player)
        expected = False
        self.assertEqual(actual, expected)
