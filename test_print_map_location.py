from unittest import TestCase
import unittest.mock
import io

import output_display


class Test(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_location(self, mock_stdout):
        output_display.print_map_location(6, 6, {'Y-Coordinate': 0, 'X-Coordinate': 0, 'Floor': 1, 'Waist': 32})
        actual = mock_stdout.getvalue()
        expected = ("==============================\n"
                "| O ||   ||   ||   ||   ||   |\n"
                "==============================\n"
                "|   ||   ||   ||   ||   ||   |\n"
                "==============================\n"
                "|   ||   ||   ||   ||   ||   |\n"
                "==============================\n"
                "|   ||   ||   ||   ||   ||   |\n"
                "==============================\n"
                "|   ||   ||   ||   ||   ||   |\n"
                "==============================\n"
                "|   ||   ||   ||   ||   || ! |\n"
                "==============================\n"
                "'O': Your location '!': Stairs to reach next floor\n")
        self.assertEqual(expected, actual)


