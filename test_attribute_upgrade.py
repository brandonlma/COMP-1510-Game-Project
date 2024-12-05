import unittest

import user_information

class MyTestCase(unittest.TestCase):
    def test_attribute_upgrade_level_two(self):
        attributes = [{1: {"lick": 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'floor': 1, 'Waist': 55, 'Level': 2, 'Attributes': attributes}
        actual = user_information.attributes_upgrade(player, attributes)
        expected = "You've gained the ability to bite!"
        self.assertEqual(actual, expected)

    def test_attribute_upgrade_level_three(self):
        attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'floor': 1, 'Waist': 55, 'Level': 3, 'Attributes': attributes}
        actual = user_information.attributes_upgrade(player, attributes)
        expected = "You've gained the ability to chomp!"
        self.assertEqual(actual, expected)

    def test_attribute_upgrade_level_four(self):
        attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}, {3: {"chomp": 4}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'floor': 1, 'Waist': 55, 'Level': 4, 'Attributes': attributes}
        actual = user_information.attributes_upgrade(player, attributes)
        expected = "You've gained the ability to devour!"
        self.assertEqual(actual, expected)

    def test_attribute_upgrade_level_five(self):
        attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}, {3: {"chomp": 4}}, {4: {"devour": 6}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'floor': 1, 'Waist': 55, 'Level': 5, 'Attributes': attributes}
        actual = user_information.attributes_upgrade(player, attributes)
        expected = "You've gained the ability to FEAST!"
        self.assertEqual(actual, expected)

    def test_attribute_upgrade_level_six(self):
        attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}, {3: {"chomp": 4}}, {4: {"devour": 6}}, {5: {"FEAST": 10}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'floor': 1, 'Waist': 55, 'Level': 6, 'Attributes': attributes}
        actual = user_information.attributes_upgrade(player, attributes)
        expected = None
        self.assertEqual(actual, expected)

    def test_attribute_upgrade_level_any_greater_than_five(self):
        attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}, {3: {"chomp": 4}}, {4: {"devour": 6}}, {5: {"FEAST": 10}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'floor': 1, 'Waist': 55, 'Level': 10, 'Attributes': attributes}
        actual = user_information.attributes_upgrade(player, attributes)
        expected = None
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
