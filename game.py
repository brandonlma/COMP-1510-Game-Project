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


def describe_current_location(rows, columns, character):
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
    print("\nCurrent Floor:", character["level"], "Current HP:", character["Waist"])
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
        print("------------------------------", character["X-Coordinate"], character["Y-Coordinate"])


        




def make_character():
    """
    Initializes character's position, stats, and attributes.

    :return: a dictionary containing keys and initialized values
    """
    return {'X-Coordinate': 0, 'Y-Coordinate': 0, 'level': 1, 'Waist': 55, 'Attributes': {}}


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
        move = input("Please enter your desired direction (W, A, S, or D): \n").upper()
        if move in ["W", "A", "S", "D"]:
            valid_response = False
        else:
            print("Please enter a valid direction")

    return move


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
        y += 1
    elif direction == "D":
        x += 1
    elif direction == "S":
        y -= 1
    else:
        x -= 1

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
        x -= 1

    character['X-Coordinate'] = x
    character['Y-Coordinate'] = y

    return character


def check_if_level_attained(rows, columns, character):
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
    >>> check_if_level_attained(rows, columns, character)
    True
    >>> rows = 5
    >>> columns = 5
    >>> character = {"Y-coordinate": 1, "X-coordinate": 0, "Current HP": 5}
    >>> check_if_level_attained(rows, columns, character)
    False
    >>> rows = 5
    >>> columns = 5
    >>> character = {"Y-coordinate": 0, "X-coordinate": 4, "Current HP": 5}
    >>> check_if_level_attained(rows, columns, character)
    False
    """
    x = character['X-Coordinate']
    y = character['Y-Coordinate']

    if (x, y) == (columns - 1, rows - 1):
        return True
    else:
        return False


def reset_coordinates(character):
    character['X-coordinate'] = 0
    character['Y-coordinate'] = 0

def fight_final_boss(character, user_name):
    character['hp'] = 2
    while character['hp'] > 0:
        input_one = input(f"Tell me {user_name}, what did you eat for breakfast this morning? Lying is acceptable,"
                          f"just make sure I don't catch you.\n")
        input_two = int(input(f'Now tell me, is what you ate for breakfast True or False\n '
                          f'Enter "1" for True or "0" for False'))
        random_num = random.randint(1,3)
        print("Hmmmmm, I'm gonna take a guess and say\n...........")
        time.sleep(2)
        if random_num == 1:
            print("TRUE")
        else:
            print("FALSE")

        if random_num == input_two:
            character['hp'] -= 1
            if random == 1:
                print("HAHAHAHAHAHAHA I KNEW YOU WERE TELLING THE TRUTH FATTY")
            else:
                print("HAHAHAHAHA I KNEW YOU WERE LYING FATTY")

        else:
            print("Wow fatty, you fooled me, I guess you can have Lipo")
            return True
    return False


def check_for_villain(character):

    if character['level'] == 1:
        random_num = random.randint(1,4)
    elif character['level'] == 2:
        random_num = random.randint(1,3)
    else:
        random_num = random.randint(1,2)

    print(random_num)

    if random_num == 1:
        return True
    else:
        return False


def attributes_upgrade(character, attribute):

    if character['level'] == 1:
        attribute['punch'] = 2
    elif character['level'] == 2:
        attribute['lick'] = 3
    # else:
    #     attribute['level'] = choice

def is_alive(character):
    if character['hp'] > 0:
        return True
    else:
        return False

def increase_floor(character):
    character['level'] += 1
    return character['level']

def fight_villain():
    pass


def game():
    """
    Drive the game.
    """
    row = 6
    column = 6
    board = make_board(row, column)
    direction = get_user_choice
    make_board(row, column)
    user_name = input("Please Enter Your Name: ")
    # start_story(user_name)
    character = make_character()
    while is_alive and character['level'] <= 3:
        describe_current_location(row, column, character)
        direction = get_user_choice()
        if validate_move(board, character, direction):
            move_character(character, direction)
            villain = check_for_villain(character)
            if villain:
                # fight_villain()
                is_alive(character)
            check_if_level_attained(row, column, character)
            if check_if_level_attained(row, column, character):
                increase_floor(character)
                reset_coordinates(character)
                attributes_upgrade(character, character)
        else:
            print("You can't go past the board")
    if is_alive(character):
        fight_final_boss(character, user_name)
        if fight_final_boss(character, user_name):
            print("Congratulations! You won LIPOSUCTION!!")
        else:
            print("You lost. Have fun love handles")
    else:
        print("You lost. Have fun love handles")

    # level = level_up(character)


def main():
    """
    Drive the program.
    """
    game()



if __name__ == "__main__":
    main()