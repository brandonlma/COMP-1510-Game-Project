from unittest import TestCase
from unittest.mock import patch

import battle


class Test(TestCase):
    @patch('random.randint', side_effect=[99])
    def test_attack_result_floor_one_80(self, _):
        player = {'Floor': 1}
        actual = battle.attack_result(player)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[99])
    def test_attack_result_floor_two_80(self, _):
        player = {'Floor': 2}
        actual = battle.attack_result(player)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[99])
    def test_attack_result_floor_three_99(self, _):
        player = {'Floor': 3}
        actual = battle.attack_result(player)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1])
    def test_attack_result_floor_one_1(self, _):
        player = {'Floor': 1}
        actual = battle.attack_result(player)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1])
    def test_attack_result_floor_two_1(self, _):
        player = {'Floor': 1}
        actual = battle.attack_result(player)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1])
    def test_attack_result_floor_three_1(self, _):
        player = {'Floor': 1}
        actual = battle.attack_result(player)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[65])
    def test_attack_result_floor_one_65(self, _):
        player = {'Floor': 1}
        actual = battle.attack_result(player)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[60])
    def test_attack_result_floor_two_60(self, _):
        player = {'Floor': 2}
        actual = battle.attack_result(player)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[55])
    def test_attack_result_floor_three_55(self, _):
        player = {'Floor': 3}
        actual = battle.attack_result(player)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[60])
    def test_attack_result_floor_one_60(self, _):
        player = {'Floor': 1}
        actual = battle.attack_result(player)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[60])
    def test_attack_result_floor_three_60(self, _):
        player = {'Floor': 3}
        actual = battle.attack_result(player)
        expected = True
        self.assertEqual(expected, actual)



