from unittest import TestCase
import unittest.mock
import io

import output_display



class Test(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_user_stats(self, mock_stdout):
        player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1,
                  'Waist': 55, 'Attributes': [{1: {'lick': 1}}]}
        user_name = "Chris"
        output_display.display_user_stats(player, user_name)
        actual = mock_stdout.getvalue()
        expected = (
            "+--------------------------------------------+\n"
            "| Chris's INFORMATION:                       |\n"
            "+----------------------+---------------------+\n"
            "| Current Coordinates: | 0 , 0               |\n"
            "| Floor:               | 1                   |\n"
            "| Level:               | 1                   |\n"
            "| Kills:               | 0                   |\n"
            "| Waist Size:          | 55                  |\n"
            "+----------------------+---------------------+\n"
            "| Attack Abilities:    | lick       = 1 DMG  |\n"
            "+----------------------+---------------------+\n")
        self.assertEqual(expected.strip(), actual.strip())
