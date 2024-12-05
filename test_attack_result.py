from unittest import TestCase
from unittest.mock import patch

import battle


class Test(TestCase):
    @patch('random.randint', side_effect=[99])
    def test_attack_result_floor_one_ninety_nine(self, _):
        player = {'Floor': 1}
        actual = battle.attack_result(player)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[99])
    def test_attack_result_floor_two_ninety_nine(self, _):
        player = {'Floor': 2}
        actual = battle.attack_result(player)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[99])
    def test_attack_result_floor_three_ninety_nine(self, _):
        player = {'Floor': 3}
        actual = battle.attack_result(player)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1])
    def test_attack_result_floor_one_one(self, _):
        player = {'Floor': 1}
        actual = battle.attack_result(player)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1])
    def test_attack_result_floor_two_one(self, _):
        player = {'Floor': 1}
        actual = battle.attack_result(player)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1])
    def test_attack_result_floor_three_one(self, _):
        player = {'Floor': 1}
        actual = battle.attack_result(player)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[65])
    def test_attack_result_floor_one_sixty_five(self, _):
        player = {'Floor': 1}
        actual = battle.attack_result(player)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[60])
    def test_attack_result_floor_two_sixty(self, _):
        player = {'Floor': 2}
        actual = battle.attack_result(player)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[55])
    def test_attack_result_floor_three_fifty_five(self, _):
        player = {'Floor': 3}
        actual = battle.attack_result(player)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[60])
    def test_attack_result_floor_one_sixty(self, _):
        player = {'Floor': 1}
        actual = battle.attack_result(player)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[60])
    def test_attack_result_floor_three_sixty(self, _):
        player = {'Floor': 3}
        actual = battle.attack_result(player)
        expected = True
        self.assertEqual(expected, actual)



