import time

def make_character(attributes):
    """
    Initialize character's position, stats, and attributes.

    :param attributes: a list
    :precondition: attributes contains a list of attribute dictionaries
    :postcondition: correctly initializes player's information in a dictionary
    :return: a dictionary
    >>> attributes = [{1: {'lick': 1}}]
    >>> make_character(attributes)
    {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': [{1: {'lick': 1}}]}
    >>> attributes = [{1: {'lick': 1}}, {2: {'bite': 2}}]
    >>> make_character(attributes)
    {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': [{1: {'lick': 1}}, {2: {'bite': 2}}]}
    >>> attributes = [{1: {'lick': 1}}, {2: {'bite': 2}}, {3: {'chomp': 4}}]
    >>> make_character(attributes)
    {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': [{1: {'lick': 1}}, {2: {'bite': 2}}, {3: {'chomp': 4}}]}

    """
    return {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': attributes}


def make_board(rows, columns):
    """
    Build a board with desired length and width.

    :param rows: an integer
    :param columns: in integer
    :precondition: rows and columns must be positive integers greater than 0
    :postcondition: creates a dictionary of all coordinates keys attached to description values
    :return: a dictionary
    >>> rows = 1
    >>> columns = 1
    >>> make_board(rows, columns)
    {(0, 0): 'Empty room'}
    >>> rows = 2
    >>> columns = 2
    >>> make_board(rows, columns)
    {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
    >>> rows = 0
    >>> columns = 0
    >>> make_board(rows, columns)
    {}
    """
    board = {}
    for row in range(rows):
        for col in range(columns):
            board[(row, col)] = 'Empty room'
    return board

def start_story(user_name):
    """
    Print out initial story of the game.

    :param user_name: a string
    :precondition: user_name is a string of the user's desired name
    :postcondtion: accurately prints out the story with user's name.
    :return: None
    """

    print('\nHi '+ user_name + "! Welcome to the game of life! Let's begin!\n")
    time.sleep(3)
    print('You are 25 years old, fresh out of college hot shot. You just got a job\n'
        'at some big law firm making a quarter million dollars a year. \n')
    time.sleep(5)
    print('A year goes by and now your making over 300k a year now, and you\'ve just \n'
        'started a relationship with your smoking hot partner.\n')
    time.sleep(5)
    print('4 years go by, now your making close to a MILLION dollars a year.\n'
          'You\'ve just got married to the love of your life,\n'
          'and you just bought a new home in a gated community with a massive backyard pool. \n')
    time.sleep(7)
    print('LIFE\n')
    time.sleep(1)
    print('IS\n')
    time.sleep(1)
    print('GREAT\n')
    time.sleep(2)
    print('.....\n')
    time.sleep(2)
    print('.....\n')
    time.sleep(2)
    print('.....\n')
    time.sleep(2)
    print('25 years have gone by now.\n')
    time.sleep(4)
    print('You\'ve lost custody of all 3 of your kids after going through a nasty divorce.')
    time.sleep(3)
    print('Your spouse has cheated on you with the bartender at your local Olive Garden.')
    time.sleep(3)
    print('You\'ve gambled your money away through a gambling addiction.')
    time.sleep(3)
    print('And most importantly, you\'ve eaten your sadness away and gained 300lbs.')
    time.sleep(3)
    print('Your waist size is now 55 and none of your pants fit you anymore.\n')
    time.sleep(3)
    print('.....\n')
    time.sleep(2)
    print('.....\n')
    time.sleep(2)
    print('Which is why you are now at the World Famous Hospital for Liposuction.\n')
    time.sleep(5)
    print(objective())
    time.sleep(15)
    print('Good luck!')


def objective():
    """
    Return the objectives of game as a string.

    :return: a string
    """
    return('+-------------------------------------------------------+\n'
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


def main():
    """
    Drive the program.
    """
    pass

if __name__ == '__main__':
    main()