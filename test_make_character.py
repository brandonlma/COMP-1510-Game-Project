import unittest

import initialize


class MyTestCase(unittest.TestCase):
    def test_make_character_original_one_attribute(self):
        attributes = [{1: {'lick': 1}}]
        actual = initialize.make_character(attributes)
        expected = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': [{1: {'lick': 1}}]}
        self.assertEqual(actual, expected)

    def test_make_character_two_attributes(self):
        attributes = [{1: {'lick': 1}}, {2: {'bite': 2}}]
        actual = initialize.make_character(attributes)
        expected = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': [{1: {'lick': 1}}, {2: {'bite': 2}}]}
        self.assertEqual(actual, expected)

    def test_make_character_three_attributes(self):
        attributes = [{1: {'lick': 1}}, {2: {'bite': 2}}, {3: {'chomp': 4}}]
        actual = initialize.make_character(attributes)
        expected = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': [{1: {'lick': 1}}, {2: {'bite': 2}}, {3: {'chomp': 4}}]}
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
