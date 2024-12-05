from unittest import TestCase
from unittest.mock import patch

import battle

class Test(TestCase):
    @patch('random.randint', side_effect= [1])
    def test_random_enemy_floor_1_enemy_1(self, mock_randint):
        player = {'Floor': 1}
        actual = battle.random_enemy(player)
        expected = ["Cookie Monster", 1, "cookies"]
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[2])
    def test_random_enemy_floor_1_enemy_2(self, mock_randint):
        player = {'Floor': 1}
        actual = battle.random_enemy(player)
        expected = ["Chester the Cheetah", 2, "cheetos"]
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[3])
    def test_random_enemy_floor_1_enemy_3(self, mock_randint):
        player = {'Floor': 1}
        actual = battle.random_enemy(player)
        expected = ["Pillsbury Doughboy", 3, "raw dough"]
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[1])
    def test_random_enemy_floor_2_enemy_1(self, mock_randint):
        player = {'Floor': 2}
        actual = battle.random_enemy(player)
        expected = ["Ronald McDonald", 2, "chicken nuggets"]
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[2])
    def test_random_enemy_floor_2_enemy_2(self, mock_randint):
        player = {'Floor': 2}
        actual = battle.random_enemy(player)
        expected = ["Colonel Sanders", 4, "fried chicken"]
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[3])
    def test_random_enemy_floor_2_enemy_3(self, mock_randint):
        player = {'Floor': 2}
        actual = battle.random_enemy(player)
        expected = ["Burger King", 6, "Whoppers"]
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[1])
    def test_random_enemy_floor_3_enemy_1(self, mock_randint):
        player = {'Floor': 3}
        actual = battle.random_enemy(player)
        expected = ["Queen Elizabeth II", 3, "crumpets"]
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[2])
    def test_random_enemy_floor_3_enemy_2(self, mock_randint):
        player = {'Floor': 3}
        actual = battle.random_enemy(player)
        expected = ["Mid 2000s Jared Fogle", 6, "Subway Sandwiches"]
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[3])
    def test_random_enemy_floor_3_enemy_3(self, mock_randint):
        player = {'Floor': 3}
        actual = battle.random_enemy(player)
        expected = ["Anxiety", 9, "self-doubt"]
        self.assertEqual(actual, expected)








