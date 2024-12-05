from unittest import TestCase

import initialize
import movement

class Test(TestCase):
    def test_move_north_valid(self):
        board = initialize.make_board(6, 6)
        player = {'X-Coordinate': 3, 'Y-Coordinate': 3}
        direction = "W"
        actual = movement.validate_move(board, player, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_move_north_invalid(self):
        board = initialize.make_board(6, 6)
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0}
        direction = "W"
        actual = movement.validate_move(board, player, direction)
        expected = False
        self.assertEqual(actual, expected)

    def test_move_east_valid(self):
        board = initialize.make_board(6, 6)
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0}
        direction = "D"
        actual = movement.validate_move(board, player, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_move_east_invalid(self):
        board = initialize.make_board(6, 6)
        player = {'X-Coordinate': 5, 'Y-Coordinate': 5}
        direction = "D"
        actual = movement.validate_move(board, player, direction)
        expected = False
        self.assertEqual(actual, expected)

    def test_move_south_valid(self):
        board = initialize.make_board(6, 6)
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0}
        direction = "S"
        actual = movement.validate_move(board, player, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_move_south_invalid(self):
        board = initialize.make_board(6, 6)
        player = {'X-Coordinate': 5, 'Y-Coordinate': 5}
        direction = "S"
        actual = movement.validate_move(board, player, direction)
        expected = False
        self.assertEqual(actual, expected)

    def test_move_west_valid(self):
        board = initialize.make_board(6, 6)
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0}
        direction = "A"
        actual = movement.validate_move(board, player, direction)
        expected = False
        self.assertEqual(actual, expected)

    def test_move_west_invalid(self):
        board = initialize.make_board(6, 6)
        player = {'X-Coordinate': 5, 'Y-Coordinate': 5}
        direction = "A"
        actual = movement.validate_move(board, player, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_move_E(self):
        board = initialize.make_board(6, 6)
        player = {'X-Coordinate': 5, 'Y-Coordinate': 5}
        direction = "E"
        actual = movement.validate_move(board, player, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_move_R(self):
        board = initialize.make_board(6, 6)
        player = {'X-Coordinate': 5, 'Y-Coordinate': 5}
        direction = "R"
        actual = movement.validate_move(board, player, direction)
        expected = True
        self.assertEqual(actual, expected)


