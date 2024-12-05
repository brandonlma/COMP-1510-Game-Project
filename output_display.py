def intro_image():
    """
    Print chocolate bar image to start game.
    """
    print(r"  ___  ___  ___  ___  ___.---------------.     ", "\n"
          r".'\__\'\__\'\__\'\__\'\__,`   .  ____ ___ \    ", "\n"
          r"|\/ __\/ __\/ __\/ __\/ _:\   |`.  \  \___ \   ", "\n"
          r" \\'\__\'\__\'\__\'\__\'\_`.__|```. \  \___ \  ", "\n"
          r"  \\/ __\/ __\/ __\/ __\/ __:                \ ", "\n"
          r"   \\'\__\'\__\'\__\ \__\'\_;-----------------`", "\n"
          r"    \\/   \/   \/   \/   \/ :                 |", "\n"
          r"     \|______________________;________________|", "\n")


def display_user_stats(player, user_name):
    """
    Display user stats and attributes in a dynamic box.

    :param player: a dictionary
    :param user_name: a string
    :precondition: player is a dictionary containing all required key value pairs
    :postcondition: displays correct user stats and attributes
    :return: None
    >>> attributes = [{1: {"lick": 1}}]
    >>> player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Floor': 1, 'Waist': 55, 'Kills': 0, 'Level': 1, 'Attributes': attributes}
    >>> user_name = "Brandon"
    >>> display_user_stats(player, user_name)
    +--------------------------------------------+
    | Brandon's INFORMATION:                     |
    +----------------------+---------------------+
    | Current Coordinates: | 0 , 0               |
    | Floor:               | 1                   |
    | Level:               | 1                   |
    | Kills:               | 0                   |
    | Waist Size:          | 55                  |
    +----------------------+---------------------+
    | Attack Abilities:    | lick       = 1 DMG  |
    +----------------------+---------------------+
    >>> attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}]
    >>> player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Floor': 1, 'Waist': 55, 'Kills': 0, 'Level': 2, 'Attributes': attributes}
    >>> user_name = "Brandon"
    >>> display_user_stats(player, user_name)
    +--------------------------------------------+
    | Brandon's INFORMATION:                     |
    +----------------------+---------------------+
    | Current Coordinates: | 0 , 0               |
    | Floor:               | 1                   |
    | Level:               | 2                   |
    | Kills:               | 0                   |
    | Waist Size:          | 55                  |
    +----------------------+---------------------+
    | Attack Abilities:    | lick       = 1 DMG  |
    |                      | bite       = 2 DMG  |
    +----------------------+---------------------+
    """
    number = 0;
    print("+--------------------------------------------+")

    name_string = "| " + user_name + "'s INFORMATION:"
    while len(name_string) < 45:
        name_string = name_string + " "
    name_string += "|"
    print(name_string)
    print("+----------------------+---------------------+\n"
          "| Current Coordinates: |", player["X-Coordinate"], ",", player["Y-Coordinate"], "              |\n"
          "| Floor:               |", player["Floor"], "                  |")
    level = player["Level"]
    level_to_string = str(level)
    level_string = "| Level:               | " + level_to_string
    while len(level_string) < 45:
        level_string += " "
    level_string += "|"
    print(level_string)
    kills = player["Kills"]
    kills_to_string = str(kills)
    kills_string = "| Kills:               | " + kills_to_string
    while len(kills_string) < 45:
        kills_string += " "
    kills_string += "|"
    print(kills_string)
    waist_size = player["Waist"]
    waist_size_to_string = str(waist_size)
    waist_string = "| Waist Size:          | " + waist_size_to_string
    while len(waist_string) < 45:
        waist_string += " "
    waist_string += "|"
    print(waist_string)
    print("+----------------------+---------------------+")
    list_of_attributes = player["Attributes"]
    for attributes in list_of_attributes:
        for integer, attribute in attributes.items():
            for ability, damage in attribute.items():
                temporary_string = ""
                if number == 0:
                    temporary_string += "| Attack Abilities:    | "
                    number += 1
                else:
                    temporary_string += "|                      | "
                damage = str(attribute[ability])
                temporary_string += ability
                while len(temporary_string) < 35:
                    temporary_string += " "
                temporary_string += " = " + damage + " DMG"
                while len(temporary_string) < 45:
                    temporary_string += " "
                temporary_string += "|"
                print(temporary_string)
    print("+----------------------+---------------------+")


def describe_current_location(player):
    """
    Print player's current floor and waist size.

    :param player: a dictionary
    :precondition: player is a dictionary containing all required key value pairs
    :return: None
    >>> attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}]
    >>> player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Floor': 1, 'Waist': 55, 'Kills': 0, 'Level': 1, 'Attributes': attributes}
    >>> describe_current_location(player)
    Current Floor: 1 Waist Size: 55
    >>> attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}]
    >>> player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Floor': 3, 'Waist': 80, 'Kills': 0, 'Level': 1, 'Attributes': attributes}
    >>> describe_current_location(player)
    Current Floor: 3 Waist Size: 80
    >>> attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}]
    >>> player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Floor': 5, 'Waist': 99, 'Kills': 0, 'Level': 1, 'Attributes': attributes}
    >>> describe_current_location(player)
    Current Floor: 5 Waist Size: 99
    """
    print("Current Floor:", player["Floor"], "Waist Size:", player["Waist"])


def print_map_location(rows, columns, player):
    """
    Print the board map.

    Displays the board map including special characters to represent locations of character and
    special items.

    :param rows: an integer
    :param columns: an integer
    :param player: a dictionary
    :precondition: rows and columns are positive integers greater than 0
    :precondition: player contains coordinates of current location
    :postcondition: accurately displays board map and location of character and special items
    :return: None
    >>> rows = 6
    >>> columns = 6
    >>> attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}]
    >>> player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Floor': 1, 'Waist': 55, 'Kills': 0, 'Level': 1, 'Attributes': attributes}
    >>> print_map_location(rows, columns, player)
    ==============================
    | O ||   ||   ||   ||   ||   |
    ==============================
    |   ||   ||   ||   ||   ||   |
    ==============================
    |   ||   ||   ||   ||   ||   |
    ==============================
    |   ||   ||   ||   ||   ||   |
    ==============================
    |   ||   ||   ||   ||   ||   |
    ==============================
    |   ||   ||   ||   ||   || ! |
    ==============================
    'O': Your location '!': Stairs to reach next floor
    >>> rows = 6
    >>> columns = 6
    >>> attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}]
    >>> player = {'X-Coordinate': 5, 'Y-Coordinate': 5, 'Floor': 1, 'Waist': 55, 'Kills': 0, 'Level': 1, 'Attributes': attributes}
    >>> print_map_location(rows, columns, player)
    ==============================
    |   ||   ||   ||   ||   ||   |
    ==============================
    |   ||   ||   ||   ||   ||   |
    ==============================
    |   ||   ||   ||   ||   ||   |
    ==============================
    |   ||   ||   ||   ||   ||   |
    ==============================
    |   ||   ||   ||   ||   ||   |
    ==============================
    |   ||   ||   ||   ||   || O |
    ==============================
    'O': Your location '!': Stairs to reach next floor
    """
    for y in range(rows):
        temporary_row = ""
        for num in range(columns):
            temporary_row += "====="
        print(temporary_row)
        temp = ""
        for x in range(columns):
            temp += "| "
            if player["X-Coordinate"] == x and player["Y-Coordinate"] == y:
                temp += "O"
            elif x == columns - 1 and y == rows - 1:
                temp += "!"
            else:
                temp += " "
            temp += " |"
        print(temp)
    end_row = ""
    for num in range(columns):
        end_row += "====="
    print(end_row)
    print("'O': Your location '!': Stairs to reach next floor")



def main():
    """
    Drive the program.
    """
    # user_name = "Bob"
    # attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}]
    # player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Floor': 1, 'Waist': 55, 'Kills': 0, 'Level': 1, 'Attributes': attributes}
    #
    # display_user_stats(player, user_name)
    pass


if __name__ == '__main__':
    main()