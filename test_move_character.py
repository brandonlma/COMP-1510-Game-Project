from unittest import TestCase

import movement

class Test(TestCase):
    def test_move_character_down_top_left(self):
        actual = movement.move_character({'Y-Coordinate': 0, 'X-Coordinate': 0}, 'S')
        expected = 1, 0
        self.assertEqual(expected, actual)

    def test_move_character_down_top_right(self):
        actual = movement.move_character({'Y-Coordinate': 0, 'X-Coordinate': 6}, 'S')
        expected = 1, 6
        self.assertEqual(expected, actual)

    def test_move_character_right_top_left(self):
        actual = movement.move_character({'Y-Coordinate': 0, 'X-Coordinate': 0}, 'D')
        expected = 0, 1
        self.assertEqual(expected, actual)

    def test_move_character_left_top_right(self):
        actual = movement.move_character({'Y-Coordinate': 0, 'X-Coordinate': 5}, 'A')
        expected = 0, 4
        self.assertEqual(expected, actual)

    def test_move_character_up_bottom_left(self):
        actual = movement.move_character({'Y-Coordinate': 5, 'X-Coordinate': 0}, 'W')
        expected = 4, 0
        self.assertEqual(expected, actual)

    def test_move_character_up_bottom_right(self):
        actual = movement.move_character({'Y-Coordinate': 5, 'X-Coordinate': 5}, 'W')
        expected = 4, 5
        self.assertEqual(expected, actual)

    def test_move_character_right_bottom_left(self):
        actual = movement.move_character({'Y-Coordinate': 5, 'X-Coordinate': 0}, 'D')
        expected = 5, 1
        self.assertEqual(expected, actual)

    def test_move_character_left_bottom_right(self):
        actual = movement.move_character({'Y-Coordinate': 5, 'X-Coordinate': 5}, 'A')
        expected = 5, 4
        self.assertEqual(expected, actual)
