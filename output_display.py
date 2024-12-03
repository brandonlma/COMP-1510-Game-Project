def intro_image():
    """
    Prints image to start game.
    """
    print(r"  ___  ___  ___  ___  ___.---------------.     ", "\n"
          r".'\__\'\__\'\__\'\__\'\__,`   .  ____ ___ \    ", "\n"
          r"|\/ __\/ __\/ __\/ __\/ _:\   |`.  \  \___ \   ", "\n"
          r" \\'\__\'\__\'\__\'\__\'\_`.__|```. \  \___ \  ", "\n"
          r"  \\/ __\/ __\/ __\/ __\/ __:                \ ", "\n"
          r"   \\'\__\'\__\'\__\ \__\'\_;-----------------`", "\n"
          r"    \\/   \/   \/   \/   \/ :                 |", "\n"
          r"     \|______________________;________________|", "\n")

    return input("Hello! Welcome to Lose Your Weight!\n"
                "To start the game, please enter your name: ")



def display_user_stats(player, user_name):
    """

    :return:
    """
    number = 0;
    print("\n+--------------------------------------------+")

    name_string = "| " + user_name + "'s INFORMATION:"
    while len(name_string) < 45:
        name_string = name_string + " "
    name_string += "|"
    print(name_string)
    print("+----------------------+---------------------+\n"
          "| Current Coordinates: |", player["X-Coordinate"], ",", player["Y-Coordinate"], "              |\n"
          "| Floor:               |", player["Floor"], "                  |\n"
          "| Level:               |", player["Level"], "                  |")
    waist_size = player["Waist"]
    waist_size_to_string = str(waist_size)
    waist_string = "| Waist Size:          | " + waist_size_to_string
    while len(waist_string) < 45:
        waist_string += " "
    waist_string += "|"
    print(waist_string)
    print("+----------------------+---------------------+")
    attributes = player["Attributes"]
    for keys, values in player["Attributes"].items():
        temporary_string = ""
        if number == 0:
            temporary_string += "| Attack Abilities:    | "
            number += 1
        else:
            temporary_string += "|                      | "
        damage = str(attributes[keys])
        temporary_string += keys
        while len(temporary_string) < 35:
            temporary_string += " "
        temporary_string += " = " + damage + " DMG"
        while len(temporary_string) < 45:
            temporary_string += " "
        temporary_string += "|"
        print(temporary_string)
    print("+----------------------+---------------------+")






def describe_current_location(rows, columns, player):
    """
    Prints the board map.

    Displays the board map including special characters to represent locations of character and
    special items.

    :param rows: an integer
    :param columns: an integer
    :param player: a dictionary
    :precondition: rows and columns are positive integers greater than 0
    :precondition: player contains coordinates of current location
    :postcondition: accurately displays board map and location of character and special items
    :return: None
    """
    print("\nCurrent Floor:", player["Level"], "Waist Size:", player["Waist"])
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
            else:
                temp += " "
            temp += " |"
        print(temp)
    end_row = ""
    for num in range(columns):
        end_row += "====="
    print(end_row)



def main():
    user_name = "Bob"
    attributes = {"lick": 1}
    player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Floor': 1, 'Waist': 55, 'Level': 1, 'Attributes': attributes}

    display_user_stats(player, user_name)


if __name__ == '__main__':
    main()