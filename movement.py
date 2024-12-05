import output_display

def get_user_choice():
    """
    Determine desired direction of movement.

    A function that asks for input of user's choice of direction.

    :return: a value of desired direction inputted from the user

    >>> get_user_choice() # doctest: +SKIP
    +------------------+
    | Move Options:    |
    +------------------+
    | W: North/Up      |
    | A: West/Left     |
    | S: South/Down    |
    | D: East/Right    |
    | E: View profile  |
    | R: View Rules    |
    +------------------+
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
    >>> player = {"Y-Coordinate": 0, "X-Coordinate": 0, "Current HP": 5}
    >>> direction = "S"
    >>> validate_move(board, player, direction)
    True
    >>> board = {(0,0), (0, 1), (1, 0), (1, 1)}
    >>> player = {"Y-Coordinate": 0, "X-Coordinate": 0, "Current HP": 5}
    >>> direction = "D"
    >>> validate_move(board, player, direction)
    True
    >>> board = {(0,0), (0, 1), (1, 0), (1, 1)}
    >>> player = {"Y-Coordinate": 0, "X-Coordinate": 0, "Current HP": 5}
    >>> direction = "W"
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
    Shift character's coordinates.

    A function that moves the character in direction based on user's choice.

    :param player: a dictionary containing character's coordinates
    :param direction: an integer correlated to a specific direction
    :precondition: character's current coordinates are valid
    :postcondition: accurately move character
    :return: a dictionary

    >>> player = {"Y-Coordinate": 0, "X-Coordinate": 0}
    >>> direction = "S"
    >>> move_character(player, direction)
    (1, 0)
    >>> player = {"Y-Coordinate": 0, "X-Coordinate": 0}
    >>> direction = "D"
    >>> move_character(player, direction)
    (0, 1)
    >>> player = {"Y-Coordinate": 4, "X-Coordinate": 3}
    >>> direction = "D"
    >>> move_character(player, direction)
    (4, 4)
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
    >>> player = {"Y-Coordinate": 4, "X-Coordinate": 4}
    >>> check_if_floor_attained(rows, columns, player)
    True
    >>> rows = 5
    >>> columns = 5
    >>> player = {"Y-Coordinate": 1, "X-Coordinate": 0}
    >>> check_if_floor_attained(rows, columns, player)
    False
    >>> rows = 5
    >>> columns = 5
    >>> player = {"Y-Coordinate": 0, "X-Coordinate": 4}
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
    """
    Reset coordinates of character to (0, 0).

    :param player: a dictionary
    :precondition: player is a dictionary with X and Y coordinates
    :postcondition: coordinates are set to (0, 0)
    :return: None
    >>> player = {"Y-Coordinate": 5, "X-Coordinate": 5}
    >>> reset_coordinates(player)
    {'Y-Coordinate': 0, 'X-Coordinate': 0}
    >>> player = {"Y-Coordinate": 0, "X-Coordinate": 0}
    >>> reset_coordinates(player)
    {'Y-Coordinate': 0, 'X-Coordinate': 0}
    >>> player = {"Y-Coordinate": 100, "X-Coordinate": 21}
    >>> reset_coordinates(player)
    {'Y-Coordinate': 0, 'X-Coordinate': 0}
    """
    player['X-Coordinate'] = 0
    player['Y-Coordinate'] = 0

    return player


def increase_floor(player):
    """
    Increase player floor by one.

    :param player: a dictionary
    :precondition: player is a dictionary with 'Floor' key.
    :postcondition: player's floor is increased by 1
    :return: a dictionary
    >>> player = {'Y-Coordinate': 0, 'X-Coordinate': 0, 'Floor': 1}
    >>> increase_floor(player)
    {'Y-Coordinate': 0, 'X-Coordinate': 0, 'Floor': 2}
    >>> player = {'Y-Coordinate': 0, 'X-Coordinate': 0, 'Floor': 2}
    >>> increase_floor(player)
    {'Y-Coordinate': 0, 'X-Coordinate': 0, 'Floor': 3}
    >>> player = {'Y-Coordinate': 0, 'X-Coordinate': 0, 'Floor': 3}
    >>> increase_floor(player)
    {'Y-Coordinate': 0, 'X-Coordinate': 0, 'Floor': 4}
    """
    player['Floor'] += 1

    return player


def main():
    """
    Drive the program.
    """
    # attributes = {"lick": 1}
    # player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Waist': 55, 'HP': 5, 'Attributes': attributes}
    # direction = "W"
    # board = {(0,0), (0, 1), (1, 0), (1, 1)}
    # print(validate_move(board, player, direction))
    pass

if __name__ == '__main__':
    main()
