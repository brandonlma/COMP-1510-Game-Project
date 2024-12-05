from unittest import TestCase

import initialize


class Test_make_boardoard(TestCase):
    def test_make_board_smallest(self):
        actual = initialize.make_board(1, 1)
        expected = {(0, 0): 'Empty room'}
        self.assertEqual(actual, expected)

    def test_make_board_small(self):
        actual = initialize.make_board(2, 2)
        expected = {
            (0, 0): 'Empty room', (0, 1): 'Empty room',
            (1, 0): 'Empty room', (1, 1): 'Empty room'
        }
        self.assertEqual(actual, expected)

    def test_make_board_medium(self):
        actual = initialize.make_board(5, 5)
        expected = {
            (0, 0): 'Empty room', (0, 1): 'Empty room', (0, 2): 'Empty room', (0, 3): 'Empty room',
            (0, 4): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room',
            (1, 2): 'Empty room', (1, 3): 'Empty room', (1, 4): 'Empty room', (2, 0): 'Empty room',
            (2, 1): 'Empty room', (2, 2): 'Empty room', (2, 3): 'Empty room',
            (2, 4): 'Empty room', (3, 0): 'Empty room', (3, 1): 'Empty room',
            (3, 2): 'Empty room', (3, 3): 'Empty room', (3, 4): 'Empty room',(4, 0): 'Empty room',
            (4, 1): 'Empty room', (4, 2): 'Empty room', (4, 3): 'Empty room',
            (4, 4): 'Empty room'
        }
        self.assertEqual(actual, expected)

    def test_make_board_actual_board_size(self):
        actual = initialize.make_board(6, 6)
        expected = {
            (0, 0): 'Empty room', (0, 1): 'Empty room', (0, 2): 'Empty room', (0, 3): 'Empty room',
            (0, 4): 'Empty room', (0, 5): 'Empty room',
            (1, 0): 'Empty room', (1, 1): 'Empty room', (1, 2): 'Empty room', (1, 3): 'Empty room',
            (1, 4): 'Empty room', (1, 5): 'Empty room',
            (2, 0): 'Empty room', (2, 1): 'Empty room', (2, 2): 'Empty room', (2, 3): 'Empty room',
            (2, 4): 'Empty room', (2, 5): 'Empty room', (3, 0): 'Empty room', (3, 1): 'Empty room',
            (3, 2): 'Empty room', (3, 3): 'Empty room', (3, 4): 'Empty room', (3, 5): 'Empty room',
            (4, 0): 'Empty room', (4, 1): 'Empty room', (4, 2): 'Empty room', (4, 3): 'Empty room',
            (4, 4): 'Empty room', (4, 5): 'Empty room', (5, 0): 'Empty room', (5, 1): 'Empty room',
            (5, 2): 'Empty room', (5, 3): 'Empty room', (5, 4): 'Empty room', (5, 5): 'Empty room',
        }
        self.assertEqual(actual, expected)

    def test_make_board_large(self):
        actual = initialize.make_board(9, 9)
        expected = {
            (0, 0): 'Empty room', (0, 1): 'Empty room', (0, 2): 'Empty room', (0, 3): 'Empty room',
            (0, 4): 'Empty room', (0, 5): 'Empty room', (0, 6): 'Empty room', (0, 7): 'Empty room',
            (0, 8): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room',
            (1, 2): 'Empty room', (1, 3): 'Empty room', (1, 4): 'Empty room', (1, 5): 'Empty room',
            (1, 6): 'Empty room', (1, 7): 'Empty room', (1, 8): 'Empty room',
            (2, 0): 'Empty room', (2, 1): 'Empty room', (2, 2): 'Empty room', (2, 3): 'Empty room',
            (2, 4): 'Empty room', (2, 5): 'Empty room', (2, 6): 'Empty room', (2, 7): 'Empty room',
            (2, 8): 'Empty room', (3, 0): 'Empty room', (3, 1): 'Empty room',
            (3, 2): 'Empty room', (3, 3): 'Empty room', (3, 4): 'Empty room', (3, 5): 'Empty room',
            (3, 6): 'Empty room', (3, 7): 'Empty room', (3, 8): 'Empty room',
            (4, 0): 'Empty room', (4, 1): 'Empty room', (4, 2): 'Empty room', (4, 3): 'Empty room',
            (4, 4): 'Empty room', (4, 5): 'Empty room', (4, 6): 'Empty room', (4, 7): 'Empty room',
            (4, 8): 'Empty room', (5, 0): 'Empty room', (5, 1): 'Empty room',
            (5, 2): 'Empty room', (5, 3): 'Empty room', (5, 4): 'Empty room', (5, 5): 'Empty room',
            (5, 6): 'Empty room', (5, 7): 'Empty room', (5, 8): 'Empty room',
            (6, 0): 'Empty room', (6, 1): 'Empty room', (6, 2): 'Empty room', (6, 3): 'Empty room',
            (6, 4): 'Empty room', (6, 5): 'Empty room', (6, 6): 'Empty room', (6, 7): 'Empty room',
            (6, 8): 'Empty room', (7, 0): 'Empty room', (7, 1): 'Empty room',
            (7, 2): 'Empty room', (7, 3): 'Empty room', (7, 4): 'Empty room', (7, 5): 'Empty room',
            (7, 6): 'Empty room', (7, 7): 'Empty room', (7, 8): 'Empty room',
            (8, 0): 'Empty room', (8, 1): 'Empty room', (8, 2): 'Empty room', (8, 3): 'Empty room',
            (8, 4): 'Empty room', (8, 5): 'Empty room', (8, 6): 'Empty room', (8, 7): 'Empty room',
            (8, 8): 'Empty room'
        }
        self.assertEqual(actual, expected)

    def test_make_board_largest(self):
        actual = initialize.make_board(10, 10)
        expected = {
            (0, 0): 'Empty room', (0, 1): 'Empty room', (0, 2): 'Empty room', (0, 3): 'Empty room',
            (0, 4): 'Empty room', (0, 5): 'Empty room', (0, 6): 'Empty room', (0, 7): 'Empty room',
            (0, 8): 'Empty room', (0, 9): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room',
            (1, 2): 'Empty room', (1, 3): 'Empty room', (1, 4): 'Empty room', (1, 5): 'Empty room',
            (1, 6): 'Empty room', (1, 7): 'Empty room', (1, 8): 'Empty room', (1, 9): 'Empty room',
            (2, 0): 'Empty room', (2, 1): 'Empty room', (2, 2): 'Empty room', (2, 3): 'Empty room',
            (2, 4): 'Empty room', (2, 5): 'Empty room', (2, 6): 'Empty room', (2, 7): 'Empty room',
            (2, 8): 'Empty room', (2, 9): 'Empty room', (3, 0): 'Empty room', (3, 1): 'Empty room',
            (3, 2): 'Empty room', (3, 3): 'Empty room', (3, 4): 'Empty room', (3, 5): 'Empty room',
            (3, 6): 'Empty room', (3, 7): 'Empty room', (3, 8): 'Empty room', (3, 9): 'Empty room',
            (4, 0): 'Empty room', (4, 1): 'Empty room', (4, 2): 'Empty room', (4, 3): 'Empty room',
            (4, 4): 'Empty room', (4, 5): 'Empty room', (4, 6): 'Empty room', (4, 7): 'Empty room',
            (4, 8): 'Empty room', (4, 9): 'Empty room', (5, 0): 'Empty room', (5, 1): 'Empty room',
            (5, 2): 'Empty room', (5, 3): 'Empty room', (5, 4): 'Empty room', (5, 5): 'Empty room',
            (5, 6): 'Empty room', (5, 7): 'Empty room', (5, 8): 'Empty room', (5, 9): 'Empty room',
            (6, 0): 'Empty room', (6, 1): 'Empty room', (6, 2): 'Empty room', (6, 3): 'Empty room',
            (6, 4): 'Empty room', (6, 5): 'Empty room', (6, 6): 'Empty room', (6, 7): 'Empty room',
            (6, 8): 'Empty room', (6, 9): 'Empty room', (7, 0): 'Empty room', (7, 1): 'Empty room',
            (7, 2): 'Empty room', (7, 3): 'Empty room', (7, 4): 'Empty room', (7, 5): 'Empty room',
            (7, 6): 'Empty room', (7, 7): 'Empty room', (7, 8): 'Empty room', (7, 9): 'Empty room',
            (8, 0): 'Empty room', (8, 1): 'Empty room', (8, 2): 'Empty room', (8, 3): 'Empty room',
            (8, 4): 'Empty room', (8, 5): 'Empty room', (8, 6): 'Empty room', (8, 7): 'Empty room',
            (8, 8): 'Empty room', (8, 9): 'Empty room', (9, 0): 'Empty room', (9, 1): 'Empty room',
            (9, 2): 'Empty room', (9, 3): 'Empty room', (9, 4): 'Empty room', (9, 5): 'Empty room',
            (9, 6): 'Empty room', (9, 7): 'Empty room', (9, 8): 'Empty room', (9, 9): 'Empty room'
        }
        self.assertEqual(actual, expected)