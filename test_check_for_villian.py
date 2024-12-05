from unittest import TestCase

from unittest.mock import patch

from battle import check_for_villain


class Test(TestCase):
    @patch('random.randint', side_effect=[20])
    def test_check_for_villain_under_forty(self, mock_choice):
        attributes = [{1: {"lick": 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55,
                       'Attributes': attributes}
        actual = check_for_villain(player)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[40])
    def test_check_for_villain_forty(self, mock_choice):
        attributes = [{1: {"lick": 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55,
                       'Attributes': attributes}
        actual = check_for_villain(player)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[60])
    def test_check_for_villain_over_forty(self, mock_choice):
        attributes = [{1: {"lick": 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55,
                       'Attributes': attributes}
        actual = check_for_villain(player)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[30])
    def test_check_for_villain_under_fifty(self, mock_choice):
        attributes = [{1: {"lick": 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 2, 'Kills': 0, 'Floor': 2, 'Waist': 55,
                       'Attributes': attributes}
        actual = check_for_villain(player)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[50])
    def test_check_for_villain_fifty(self, mock_choice):
        attributes = [{1: {"lick": 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 2, 'Waist': 55,
                       'Attributes': attributes}
        actual = check_for_villain(player)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[70])
    def test_check_for_villain_over_fifty(self, mock_choice):
        attributes = [{1: {"lick": 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 2, 'Waist': 55,
                       'Attributes': attributes}
        actual = check_for_villain(player)
        expected = False
        self.assertEqual(expected, actual)


    @patch('random.randint', side_effect=[35])
    def test_check_for_villain_under_sixty(self, mock_choice):
        attributes = [{1: {"lick": 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 3, 'Waist': 55,
                       'Attributes': attributes}
        actual = check_for_villain(player)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[60])
    def test_check_for_villain_sixty(self, mock_choice):
        attributes = [{1: {"lick": 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 3, 'Waist': 55,
                       'Attributes': attributes}
        actual = check_for_villain(player)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[80])
    def test_check_for_villain_over_sixty(self, mock_choice):
        attributes = [{1: {"lick": 1}}]
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 3, 'Waist': 55,
                       'Attributes': attributes}
        actual = check_for_villain(player)
        expected = False
        self.assertEqual(expected, actual)



