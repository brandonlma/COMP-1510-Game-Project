import unittest
import battle
import io
from unittest.mock import patch

class MyTestCase(unittest.TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_fight_villain_three_attributes(self, mock_output):
        self.maxDiff = None
        enemy = ["Ronald McDonald", 8, "chicken nuggets"]
        enemy_name = enemy[0]
        enemy_health = enemy[1]
        attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}, {3: {"chomp": 4}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 3, 'Waist': 55, 'Floor': 1, 'Attributes': attributes}
        battle.fight_villain_story(player, enemy_name, enemy_health)
        actual = mock_output.getvalue()
        expected = """+--------------------------------+
| Ronald McDonald HP: 8          |
+--------------------------------+
| Waist Size: 55                 |
+--------------------------------+
| Attack Attributes:             |
| 1: lick = +/- 1 DMG            |
| 2: bite = +/- 2 DMG            |
| 3: chomp = +/- 4 DMG           |
+--------------------------------+
"""
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_fight_villain_one_attribute(self, mock_output):
        self.maxDiff = None
        enemy = ["Ronald McDonald", 8, "chicken nuggets"]
        enemy_name = enemy[0]
        enemy_health = enemy[1]
        attributes = [{1: {"lick": 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Waist': 55, 'Floor': 1, 'Attributes': attributes}
        battle.fight_villain_story(player, enemy_name, enemy_health)
        actual = mock_output.getvalue()
        expected = """+--------------------------------+
| Ronald McDonald HP: 8          |
+--------------------------------+
| Waist Size: 55                 |
+--------------------------------+
| Attack Attributes:             |
| 1: lick = +/- 1 DMG            |
+--------------------------------+
"""
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_fight_villain_two_attributes(self, mock_output):
        self.maxDiff = None
        enemy = ["Ronald McDonald", 8, "chicken nuggets"]
        enemy_name = enemy[0]
        enemy_health = enemy[1]
        attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 2, 'Waist': 55, 'Floor': 1, 'Attributes': attributes}
        battle.fight_villain_story(player, enemy_name, enemy_health)
        actual = mock_output.getvalue()
        expected = """+--------------------------------+
| Ronald McDonald HP: 8          |
+--------------------------------+
| Waist Size: 55                 |
+--------------------------------+
| Attack Attributes:             |
| 1: lick = +/- 1 DMG            |
| 2: bite = +/- 2 DMG            |
+--------------------------------+
"""
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
