import random
import time


# def fight_temptation():
#     enemy = random_enemy()
#     int(input(print("You stumble across " + enemy + ". They prepare to attack you! What do you choose to counter?")))
#     # guessing_game(enemy)


# def random_enemy(character):
#     value = random.randInt(1,3)
#     if character['Floor'] == 1:
#         if value == 1:
#             return "Pillsbury Doughboy"
#         elif value == 2:
#             return "Cookie Monster"
#         else:
#             return "Chester the Cheetah"
#     elif character['Floor'] == 2:
#         if value == 1:
#             return "Ronald McDonald"
#         elif value == 2:
#             return "Colonel Sanders"
#         else:
#             return "Mid 2000s Jared Fogle"
#     else:
#         return "yourself"


def start_story(user_name):
    """
    Prints out initial story of the game.

    :param user_name: a string
    :precondition: user_name is a string of the user's desired name
    :postcondtion: accurately prints out the story with user's name.
    :return: None
    """

    print('\nHi '+ user_name + ', welcome to the game of life! Lets begin!\n')
    time.sleep(3)
    print('You are 25 years old, fresh out of college hot shot. You just got a job\n'
        'at some big law firm making qauter million dollars a year. \n')
    time.sleep(5)
    print('A year goes by and now your making over 300k a year now, and you\'ve just \n'
        'started a relationship with your smoking hot partner.\n')
    time.sleep(5)
    print('4 years go by, now your making close to a MILLION dollars a year.\n'
          'You\'ve just got married to the love of your life,\n'
          'and you just bought a new home in a gated community with a massive backyard pool. \n')
    time.sleep(5)
    print('LIFE\n')
    time.sleep(1)
    print('IS\n')
    time.sleep(1)
    print('GREAT\n')
    time.sleep(1)
    print('.....\n')
    time.sleep(0.5)
    print('.....\n')
    time.sleep(0.5)
    print('.....\n')
    time.sleep(0.5)
    print('.....\n')
    time.sleep(0.5)
    print('.....\n')
    time.sleep(0.5)
    print('.....\n')
    time.sleep(0.5)
    print('.....\n')
    time.sleep(1)
    print('25 years have gone by now.\n') 
    time.sleep(4)
    print('You lost custody of all 3 of your kids after going through a nasty divorce.')
    time.sleep(2)
    print('Your spouse has cheated on you with the bartender at your local Olive Garden.')
    time.sleep(2)
    print('You\'ve gambled your money away through a gambling addiction.')
    time.sleep(2)
    print('And most importantly, you\'ve eaten your sadness away and gained 300lbs.')
    time.sleep(2)
    print('Your waist size is now 55 and none of your pants fit you anymore.\n')
    time.sleep(2)
    print('Your objective is to lose enough weight to be approved a surgical gastric bypass procedure.\n'
          'Drop your waist size to 40 before Father Time catches up to you.')
    time.sleep(2)
    print("")


def print_map(rows, columns, character):
    """
    Prints the board map.

    Displays the board map including special characters to represent locations of character and
    special items.

    :param rows: an integer
    :param columns: an integer
    :param character: a dictionary
    :precondition: rows and columns are positive integers greater than 0
    :precondition: character contains coordinates of current location
    :postcondition: accurately displays board map and location of character and special items
    :return: None
    """
    print("\nCurrent Floor:", character["Floor"], "Current HP:", character["Waist"])
    for y in range(rows):
        temporary_row = ""
        for num in range(columns):
            temporary_row += "-----"
        print(temporary_row)
        temp = ""
        for x in range(columns):
            temp += "| "
            if character["X-Coordinate"] == x and character["Y-Coordinate"] == y:
                temp += "O"
            else:
                temp += " "
            temp += " |"
        print(temp)
        print(temporary_row)


def make_character():
    """
    Initializes character's position, stats, and attributes.

    :return: a dictionary containing keys and initialized values
    """
    return {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Floor': 1, 'Waist': 55, 'Attributes': {}}


def make_board(rows, columns):
    """
    Builds a board with desired length and width.

    :param rows: an integer
    :param columns: in integer
    :precondition: rows and columns must be positive integers greater than 0
    :postcondition: creates a dictionary of all coordinates keys attached to description values
    :return: a dictionary
    """
    board = {}
    for row in range(rows):
        for col in range(columns):
            board[(row, col)] = 'Empty room'
    return board


def get_user_choice():
    """
    Determine desired direction of movement.

    A function that asks for input of user's choice of direction.

    :return: a value of desired direction inputted from the user

    >>> get_user_choice() # doctest: +SKIP
    1: South/Down
    2: East/Right
    3: North/Up
    4: West/Left
    Please enter your desired direction (1, 2, 3, or 4):
    """
    valid_response = True

    while valid_response:
        print("W: North/Up\n"
             "A: West/Left\n"
             "S: South/Down\n"
             "D: East/Right")
        direction = input("Please enter your desired direction (W, A, S, or D): \n").upper()
        if direction in ["W", "A", "S", "D"]:
            valid_response = False
        else:
            print("Please enter a valid direction")

    return direction


def validate_move(board, character, direction):
    """
    Verify validity of user's move.

    A function that determines if the inputted move causes character
    to step out of the boundaries of the board.

    :param board: a dictionary with all coordinates of the grid
    :param character: a key:value pair containing character's coordinates and health
    :param direction: a string with user's desired direction
    :precondition: board is a dictionary with all coordinates of the grid
    :precondition: character's current coordinates are valid
    :precondition: direction is a valid string from user's inputted direction
    :postcondition: correct result of whether new position is valid or not
    :return: a boolean

    >>> board = {(0,0), (0, 1), (1, 0), (1, 1)}
    >>> character = {"Y-coordinate": 0, "X-coordinate": 0, "Current HP": 5}
    >>> direction = 1
    >>> validate_move(board, character, direction)
    True
    >>> board = {(0,0), (0, 1), (1, 0), (1, 1)}
    >>> character = {"Y-coordinate": 0, "X-coordinate": 0, "Current HP": 5}
    >>> direction = 2
    >>> validate_move(board, character, direction)
    True
    >>> board = {(0,0), (0, 1), (1, 0), (1, 1)}
    >>> character = {"Y-coordinate": 0, "X-coordinate": 0, "Current HP": 5}
    >>> direction = 3
    >>> validate_move(board, character, direction)
    False
    """
    x = int(character['X-Coordinate'])
    y = int(character['Y-Coordinate'])

    if direction == "W":
        y -= 1
    elif direction == "A":
        x -= 1
    elif direction == "S":
        y += 1
    else:
        x += 1

    if (y, x) in board:
        return True
    else:
        return False
    

def move_character(character, direction):
    """
    Shifts character's coordinates.

    A function that moves the character in direction based on user's choice.

    :param character: a dictionary containing character's coordinates
    :param direction: an integer correlated to a specific direction
    :precondition: character's current coordinates are valid
    :postcondition: accurately move character
    :return: a dictionary

    >>> character = {"Y-coordinate": 0, "X-coordinate": 0, "Current HP": 5}
    >>> direction = 1
    >>> move_character(character, direction)
    {'Y-coordinate': 1, 'X-coordinate': 0, 'Current HP': 5}
    >>> character = {"Y-coordinate": 0, "X-coordinate": 0, "Current HP": 5}
    >>> direction = 2
    >>> move_character(character, direction)
    {'Y-coordinate': 0, 'X-coordinate': 1, 'Current HP': 5}
    >>> character = {"Y-coordinate": 4, "X-coordinate": 3, "Current HP": 5}
    >>> direction = 2
    >>> move_character(character, direction)
    {'Y-coordinate': 4, 'X-coordinate': 4, 'Current HP': 5}
    """
    x = int(character['X-Coordinate'])
    y = int(character['Y-Coordinate'])

    if direction == "W":
        y -= 1
    elif direction == "A":
        x -= 1
    elif direction == "S":
        y += 1
    else:
        x += 1

    character['X-Coordinate'] = x
    character['Y-Coordinate'] = y

    return character


def check_if_goal_attained(rows, columns, character):
    """
    Determine if character has reached goal.

    A function that checks if a character's current coordinates is a possible

    :param rows: an integer for the number of rows
    :param columns: an integer for the number of columns
    :param character: a key:value pair containing character's current coordinates and health
    :precondition: board is a dictionary with all coordinates of the grid
    :postcondition: correctly checks if character has reached goal
    :return: a boolean

    >>> rows = 5
    >>> columns = 5
    >>> character = {"Y-coordinate": 4, "X-coordinate": 4, "Current HP": 5}
    >>> check_if_goal_attained(rows, columns, character)
    True
    >>> rows = 5
    >>> columns = 5
    >>> character = {"Y-coordinate": 1, "X-coordinate": 0, "Current HP": 5}
    >>> check_if_goal_attained(rows, columns, character)
    False
    >>> rows = 5
    >>> columns = 5
    >>> character = {"Y-coordinate": 0, "X-coordinate": 4, "Current HP": 5}
    >>> check_if_goal_attained(rows, columns, character)
    False
    """
    x = character['X-Coordinate']
    y = character['Y-Coordinate']

    if (x, y) == (columns - 1, rows - 1):
        return True
    else:
        return False


def next_level_reset(character):
    """
    Resets character's coordinates when reaching a new level/floor.

    :param character: a dictionary containing character's coordinates
    :precondition: character's coordinates are (5, 5)
    :postcondition: character's coordinates are reset to (0,0)
    :return: a dictionary
    """
    character["Floor"] += 1
    character['X-Coordinate'] = 0
    character['Y-Coordinate'] = 0

    return character


def game():
    """
    Drive the game.
    """
    row = 6
    column = 6
    board = make_board(row, column)
    user_name = input("Please Enter Your Name: ")
    start_story(user_name)
    character = make_character()
    game_not_ended = True
    while game_not_ended:
        reached_next_level = check_if_goal_attained(board, character, character)
        if reached_next_level:
            next_level_reset(character)
        else:
            direction = get_user_choice()
            move_allowed = validate_move(board, character, direction)
            if move_allowed:
                move_character(character, direction)
                print_map(row, column, character)
            else:
                print("Move is not valid. Try Again.")
            # print(character)
            # level = level_up(character)


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()