from unittest import TestCase

import movement


class Test(TestCase):
    def test_increase_floor_1(self):
        player = {'Floor': 1}
        actual = movement.increase_floor(player)
        expected = {'Floor': 2}
        self.assertEqual(expected, actual)

    def test_increase_floor_2(self):
        player = {'Floor': 1}
        actual = movement.increase_floor(player)
        expected = {'Floor': 2}
        self.assertEqual(expected, actual)

    def test_increase_floor_3(self):
        player = {'Floor': 1}
        actual = movement.increase_floor(player)
        expected = {'Floor': 2}
        self.assertEqual(expected, actual)
