import unittest

import movement

class MyTestCase(unittest.TestCase):
    def test_check_if_floor_attained_valid_achieved(self):
        rows = 6
        columns = 6
        player = {"Y-Coordinate": 5, "X-Coordinate": 5}
        actual = movement.check_if_floor_attained(rows, columns, player)
        expected = True
        self.assertEqual(actual, expected)

    def test_check_if_floor_attained_valid_not_achieved(self):
        rows = 6
        columns = 6
        player = {"Y-Coordinate": 0, "X-Coordinate": 0}
        actual = movement.check_if_floor_attained(rows, columns, player)
        expected = False
        self.assertEqual(actual, expected)

    def test_check_if_floor_attained_invalid_not_achieved(self):
        rows = 6
        columns = 6
        player = {"Y-Coordinate": 7, "X-Coordinate": 0}
        actual = movement.check_if_floor_attained(rows, columns, player)
        expected = False
        self.assertEqual(actual, expected)

    def test_check_if_floor_attained_valid_middle_of_board(self):
        rows = 6
        columns = 6
        player = {"Y-Coordinate": 3, "X-Coordinate": 3}
        actual = movement.check_if_floor_attained(rows, columns, player)
        expected = False
        self.assertEqual(actual, expected)




if __name__ == '__main__':
    unittest.main()
