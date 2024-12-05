from unittest import TestCase
import unittest.mock
import io

import battle


class Test(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_final_boss(self, mock_stdout):
        user_name = "Chris"
        battle.final_boss_story(user_name)
        actual = mock_stdout.getvalue()
        # actual = battle.final_boss_story(user_name)
        expected = ("You've successfully reached Floor 4!\n"
                    
                    "You must now have a consultation with Dr.Fat to get approved liposuction surgery.\n"
                    
                    "stomp~ stomp~ the ground shakes beneath you\n"
                    
                    "stomp~ stomp~ he's getting closer\n"\
                    
                    "~BOOM~ the door aggressively swings open\n"
                    
                    """                                                                                           
                                                  ░░░░░░                                                
                                                 ░▓▓▓▓▓▓▓▒░                                             
                                                 ░░▒░▒▒░▓▓▓                                             
                                                 ░░░░░░░▒▒▒                                             
                                                ░▒▒░░░░▓▓▓░░                                            
                                                 ░▓▓▓▓▓▓▒░░▒▒▒▒▒░░                                      
                                           ░░░▒░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░                                  
                                          ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░                                 
                                        ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░░░░░░░                                
                                       ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░                                
                                      ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░                                
                                     ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░                                
                                    ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░                                
                                    ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░                                 
                                    ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░                                  
                                     ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▒░░                                  
                                      ▒▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒░░▒▓▓░                                   
                                      ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░                                   
                                      ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░                                    
                                       ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░                                     
                                        ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░                                     
                                        ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░                                      
                                         ▒▓▓▓▓▓▓▓▓▓░░▒▓▓▓▓▓▓▓▓▓▓▓░                                      
                                         ░▓▓▓▓▓▓▓▓▒░  ░▒▓▓▓▓▓▓▓▓▓░                                      
                                          ▒▓▓▓▓▓▓▓░     ░▓▓▓▓▓▓▓░░                                      
                                          ░▓▓▓▓▓▓░       ▒▓▓▓▓▓▓                                        
                                   ░░░░░░▓██████▓░░░░░░▓▓██████▓░░░░░░░░"""
                    f"Dr.Fat: 'Hello {user_name}. I'm going to check whether you've been good or bad on your diet.'\n"
                    f"")
        self.assertEqual(expected, actual)
