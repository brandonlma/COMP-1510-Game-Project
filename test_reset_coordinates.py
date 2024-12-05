import unittest

import movement

class MyTestCase(unittest.TestCase):
    def test_reset_coordinates_five_five(self):
        player = {"Y-Coordinate": 5, "X-Coordinate": 5}
        actual = movement.reset_coordinates(player)
        expected = {'Y-Coordinate': 0, 'X-Coordinate': 0}
        self.assertEqual(expected, actual)

    def test_reset_coordinates_zero_zero(self):
        player = {"Y-Coordinate": 0, "X-Coordinate": 0}
        actual = movement.reset_coordinates(player)
        expected = {'Y-Coordinate': 0, 'X-Coordinate': 0}
        self.assertEqual(expected, actual)

    def test_reset_coordinates_one_thousand_one_thousand(self):
        player = {"Y-Coordinate": 1000, "X-Coordinate": 1000}
        actual = movement.reset_coordinates(player)
        expected = {'Y-Coordinate': 0, 'X-Coordinate': 0}
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
