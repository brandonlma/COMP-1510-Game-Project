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



def display_user_stats():
    """

    :return:
    """
    print("+------------------+\n"
          "|       YOU        |\n"
          "|       MAKE       |\n"
          "|        MY        |\n"
          "|      DREAMS      |\n"
          "|       COME       |\n"
          "|       TRUE       |\n"
          "|                  |\n"
          "|      I <3 U      |\n"
          "|      STEAK       |\n"
          "+------------------+\n")






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
        print("------------------------------")


def main():
    intro_image()


if __name__ == '__main__':
    main()