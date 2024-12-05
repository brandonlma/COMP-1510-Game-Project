from unittest import TestCase

from battle


class Test(TestCase):
    def test_increase_floor_1(self):
        player = {'Floor': 1}
        actual = battle.(player)
        expected = {'Floor': 2}
        self.assertEqual(expected, actual)