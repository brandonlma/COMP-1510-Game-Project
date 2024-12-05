import output_display

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
        print("+------------------+\n"
              "| Move Options:    |\n"
              "+------------------+\n"
              "| W: North/Up      |\n"
              "| A: West/Left     |\n"
              "| S: South/Down    |\n"
              "| D: East/Right    |\n"
              "| E: View profile  |\n"
              "| R: View Rules    |\n"
              "+------------------+")
        move = input("Please enter your desired move: ").upper()
        if move in ["W", "A", "S", "D", "E", "R"]:
            valid_response = False
        else:
            print("Please enter a valid direction")

    return move


def validate_move(board, player, direction):
    """
    Verify validity of user's move.

    A function that determines if the inputted move causes character
    to step out of the boundaries of the board.

    :param board: a dictionary with all coordinates of the grid
    :param player: a key:value pair containing character's coordinates and health
    :param direction: a string with user's desired direction
    :precondition: board is a dictionary with all coordinates of the grid
    :precondition: character's current coordinates are valid
    :precondition: direction is a valid string from user's inputted direction
    :postcondition: correct result of whether new position is valid or not
    :return: a boolean

    >>> board = {(0,0), (0, 1), (1, 0), (1, 1)}
    >>> player = {"Y-coordinate": 0, "X-coordinate": 0, "Current HP": 5}
    >>> direction = 1
    >>> validate_move(board, player, direction)
    True
    >>> board = {(0,0), (0, 1), (1, 0), (1, 1)}
    >>> player = {"Y-coordinate": 0, "X-coordinate": 0, "Current HP": 5}
    >>> direction = 2
    >>> validate_move(board, player, direction)
    True
    >>> board = {(0,0), (0, 1), (1, 0), (1, 1)}
    >>> player = {"Y-coordinate": 0, "X-coordinate": 0, "Current HP": 5}
    >>> direction = 3
    >>> validate_move(board, player, direction)
    False
    """

    x = int(player['X-Coordinate'])
    y = int(player['Y-Coordinate'])

    if direction == "W":
        y -= 1
    elif direction == "D":
        x += 1
    elif direction == "S":
        y += 1
    elif direction == "A":
        x -= 1

    if (y, x) in board:
        return True
    else:
        if direction == "E" or direction == "R":
            return True
        else:
            return False


def move_character(player, direction):
    """
    Shifts character's coordinates.

    A function that moves the character in direction based on user's choice.

    :param player: a dictionary containing character's coordinates
    :param direction: an integer correlated to a specific direction
    :precondition: character's current coordinates are valid
    :postcondition: accurately move character
    :return: a dictionary

    >>> player = {"Y-coordinate": 0, "X-coordinate": 0, "Current HP": 5}
    >>> direction = 1
    >>> move_character(player, direction)
    {'Y-coordinate': 1, 'X-coordinate': 0, 'Current HP': 5}
    >>> player = {"Y-coordinate": 0, "X-coordinate": 0, "Current HP": 5}
    >>> direction = 2
    >>> move_character(player, direction)
    {'Y-coordinate': 0, 'X-coordinate': 1, 'Current HP': 5}
    >>> player = {"Y-coordinate": 4, "X-coordinate": 3, "Current HP": 5}
    >>> direction = 2
    >>> move_character(player, direction)
    {'Y-coordinate': 4, 'X-coordinate': 4, 'Current HP': 5}
    """
    x = int(player['X-Coordinate'])
    y = int(player['Y-Coordinate'])

    if direction == "W":
        y -= 1
    elif direction == "A":
        x -= 1
    elif direction == "S":
        y += 1
    else:
        x += 1

    player['X-Coordinate'] = x
    player['Y-Coordinate'] = y

    return player['Y-Coordinate'], player['X-Coordinate']

def check_if_floor_attained(rows, columns, player):
    """
    Determine if character has reached goal.

    A function that checks if a character's current coordinates is a possible

    :param rows: an integer for the number of rows
    :param columns: an integer for the number of columns
    :param player: a key:value pair containing character's current coordinates and health
    :precondition: board is a dictionary with all coordinates of the grid
    :postcondition: correctly checks if character has reached goal
    :return: a boolean

    >>> rows = 5
    >>> columns = 5
    >>> player = {"Y-coordinate": 4, "X-coordinate": 4, "Current HP": 5}
    >>> check_if_floor_attained((rows, columns, player)
    True
    >>> rows = 5
    >>> columns = 5
    >>> player = {"Y-coordinate": 1, "X-coordinate": 0, "Current HP": 5}
    >>> check_if_floor_attained(rows, columns, player)
    False
    >>> rows = 5
    >>> columns = 5
    >>> player = {"Y-coordinate": 0, "X-coordinate": 4, "Current HP": 5}
    >>> check_if_floor_attained(rows, columns, player)
    False
    """
    x = player['X-Coordinate']
    y = player['Y-Coordinate']

    if (x, y) == (columns - 1, rows - 1):
        return True
    else:
        return False


def reset_coordinates(player):
    player['X-Coordinate'] = 0
    player['Y-Coordinate'] = 0

def increase_floor(player):
    player['Floor'] += 1

def main():
    # attributes = {"lick": 1}
    # player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Waist': 55, 'HP': 5, 'Attributes': attributes}
    # direction = "W"
    # board = {(0,0), (0, 1), (1, 0), (1, 1)}
    # print(validate_move(board, player, direction))
    pass

if __name__ == '__main__':
    main()
