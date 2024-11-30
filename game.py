import random
import time
from operator import truediv


# def create_character():
#     name = input("What is your name? ")
#     character = {"Name": name, "Waist Size": 55, "Dedication to lose weight": 50}
#     print("Hello " + name + "! Welcome to The Central Hospital for Gastric Bypass Surgeries. I see you want to apply for a Gastric Bypass surgery.")
#     print("However, you must have a consultation with Dr.Now before getting approved. Please follow me this way. ")
#     return character


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

    return {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Floor': 1, 'Waist': 55} 


def make_board(rows, columns):

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
    :return: a key:value pair containing character's new coordinates

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
    character["Floor"] += 1
    character['X-Coordinate'] = 0
    character['Y-Coordinate'] = 0


def game():
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
    game()



if __name__ == "__main__":
    main()