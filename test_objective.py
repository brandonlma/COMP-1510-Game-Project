from unittest import TestCase

import initialize

class Test(TestCase):
    def test_objective(self):
        actual = initialize.objective()
        expected = ('+-------------------------------------------------------+\n'
                  '| YOUR OBJECTIVE:                                       |\n'
                  '+-------------------------------------------------------+\n'
                  '| 1. Reach the 4th level of the hospital without        |\n'
                  '|    getting too fat.                                   |\n'
                  '|    STAY BELOW WAIST SIZE 100 OR YOU LOSE              |\n'
                  '| 2. Resist the temptation of junk food by              |\n'
                  '|    defeating monsters.                                |\n'
                  '| 3. Defeat monsters to level up and achieve better     |\n'
                  '|    attack abilities.                                  |\n'
                  '| 4. Failed attacks makes you gain waist size!          |\n'
                  '| 5. WIN AUTOMATICALLY IF YOU REACH WAIST SIZE 30!      |\n'
                  '+-------------------------------------------------------+\n'
                  '| TIP: Level up to lower your waist size!               |\n'
                  '|      Level 2: -10 Waist Size                          |\n'
                  '|      Level 3:  -8 Waist Size                          |\n'
                  '|      Level 4:  -6 Waist Size                          |\n'
                  '|      Level 5:  -4 Waist Size                          |\n'       
                  '+-------------------------------------------------------+')
        self.assertEqual(expected, actual)
