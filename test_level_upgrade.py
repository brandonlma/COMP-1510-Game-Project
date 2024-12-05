from unittest import TestCase

import user_information

class Test(TestCase):
    def test_level_upgrade_level_1(self):
        attributes = [{1: {'lick': 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'floor': 1, 'Waist': 55, 'Level': 1, 'Attributes': attributes}
        actual = user_information.level_upgrade(player)
        expected = "You've successfully levelled up! -10 Waist size!"
        self.assertEqual(expected, actual)

    def test_level_upgrade_level_2(self):
        attributes = [{1: {'lick': 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'floor': 1, 'Waist': 55, 'Level': 2, 'Attributes': attributes}
        actual = user_information.level_upgrade(player)
        expected = "You've successfully levelled up! -8 Waist size!"
        self.assertEqual(expected, actual)

    def test_level_upgrade_level_3(self):
        attributes = [{1: {'lick': 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'floor': 1, 'Waist': 55, 'Level': 3, 'Attributes': attributes}
        actual = user_information.level_upgrade(player)
        expected = "You've successfully levelled up! -6 Waist size!"
        self.assertEqual(expected, actual)

    def test_level_upgrade_level_4(self):
        attributes = [{1: {'lick': 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'floor': 1, 'Waist': 55, 'Level': 4, 'Attributes': attributes}
        actual = user_information.level_upgrade(player)
        expected = "You've successfully levelled up! -4 Waist size!"
        self.assertEqual(expected, actual)