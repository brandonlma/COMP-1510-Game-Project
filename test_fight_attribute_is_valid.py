import unittest
from unittest import TestCase

import battle


class MyTestCase(unittest.TestCase):
    def test_attribute_is_valid_one_attribute(self):
        attributes = [{1: {"lick": 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': attributes}
        fight_input = '1'
        actual = battle.fight_attribute_is_valid(player, fight_input)
        expected = True
        self.assertEqual(expected, actual)

    def test_attribute_input_is_invalid_one_attribute(self):
        attributes = [{1: {"lick": 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': attributes}
        fight_input = '2'
        actual = battle.fight_attribute_is_valid(player, fight_input)
        expected = False
        self.assertEqual(expected, actual)

    def test_attribute_input_is_invalid_one_attribute_blank(self):
        attributes = [{1: {"lick": 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': attributes}
        fight_input = ' '
        actual = battle.fight_attribute_is_valid(player, fight_input)
        expected = False
        self.assertEqual(expected, actual)

    def test_attribute_input_is_invalid_one_attribute_character(self):
        attributes = [{1: {"lick": 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': attributes}
        fight_input = 'S'
        actual = battle.fight_attribute_is_valid(player, fight_input)
        expected = False
        self.assertEqual(expected, actual)

    def test_attribute_is_valid_two_attributes(self):
        attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': attributes}
        fight_input = '2'
        actual = battle.fight_attribute_is_valid(player, fight_input)
        expected = True
        self.assertEqual(expected, actual)

    def test_attribute_input_is_invalid_two_attributes_number(self):
        attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': attributes}
        fight_input = '3'
        actual = battle.fight_attribute_is_valid(player, fight_input)
        expected = False
        self.assertEqual(expected, actual)

    def test_attribute_input_is_invalid_two_attributes_blank(self):
        attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': attributes}
        fight_input = ' '
        actual = battle.fight_attribute_is_valid(player, fight_input)
        expected = False
        self.assertEqual(expected, actual)

    def test_attribute_input_is_invalid_two_attributes_character(self):
        attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': attributes}
        fight_input = 'S'
        actual = battle.fight_attribute_is_valid(player, fight_input)
        expected = False
        self.assertEqual(expected, actual)

    def test_attribute_is_valid_three_attributes(self):
        attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}, {3: {"chomp": 4}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': attributes}
        fight_input = '3'
        actual = battle.fight_attribute_is_valid(player, fight_input)
        expected = True
        self.assertEqual(expected, actual)

    def test_attribute_input_is_invalid_three_attributes_number(self):
        attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}, {3: {"chomp": 4}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': attributes}
        fight_input = '4'
        actual = battle.fight_attribute_is_valid(player, fight_input)
        expected = False
        self.assertEqual(expected, actual)

    def test_attribute_input_is_invalid_three_attributes_blank(self):
        attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}, {3: {"chomp": 4}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': attributes}
        fight_input = ' '
        actual = battle.fight_attribute_is_valid(player, fight_input)
        expected = False
        self.assertEqual(expected, actual)

    def test_attribute_input_is_invalid_three_attributes_character(self):
        attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}, {3: {"chomp": 4}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': attributes}
        fight_input = 'S'
        actual = battle.fight_attribute_is_valid(player, fight_input)
        expected = False
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
