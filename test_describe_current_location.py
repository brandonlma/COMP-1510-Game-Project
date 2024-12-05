from unittest import TestCase
import unittest.mock
import io

import output_display

class Test(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_almost_dead(self, mock_stdout):
        player = {'Floor': 1, 'Waist': 99}
        output_display.describe_current_location(player)
        actual = mock_stdout.getvalue()
        expected = f"Current Floor: {player["Floor"]}, Waist Size: {player["Waist"]}\n"
        self.assertEqual(expected, actual)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_dead(self, mock_stdout):
        player = {'Floor': 1, 'Waist': 100}
        output_display.describe_current_location(player)
        actual = mock_stdout.getvalue()
        expected = f"Current Floor: {player["Floor"]}, Waist Size: {player["Waist"]}\n"
        self.assertEqual(expected, actual)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_lowest_possible_waist(self, mock_stdout):
        player = {'Floor': 1, 'Waist': 35}
        output_display.describe_current_location(player)
        actual = mock_stdout.getvalue()
        expected = f"Current Floor: {player["Floor"]}, Waist Size: {player["Waist"]}\n"
        self.assertEqual(expected, actual)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_first_level(self, mock_stdout):
        player = {'Floor': 1, 'Waist': 55}
        output_display.describe_current_location(player)
        actual = mock_stdout.getvalue()
        expected = f"Current Floor: {player["Floor"]}, Waist Size: {player["Waist"]}\n"
        self.assertEqual(expected, actual)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_second_level(self, mock_stdout):
        player = {'Floor': 2, 'Waist': 55}
        output_display.describe_current_location(player)
        actual = mock_stdout.getvalue()
        expected = f"Current Floor: {player["Floor"]}, Waist Size: {player["Waist"]}\n"
        self.assertEqual(expected, actual)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_last_level(self, mock_stdout):
        player = {'Floor': 3, 'Waist': 35}
        output_display.describe_current_location(player)
        actual = mock_stdout.getvalue()
        expected = f"Current Floor: {player["Floor"]}, Waist Size: {player["Waist"]}\n"
        self.assertEqual(expected, actual)