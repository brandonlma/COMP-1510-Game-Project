import random
import time
import movement
import battle
import initialize
import character
import output_display


def game():
    """
    Drive the game.
    """
    row = 6
    column = 6
    board = initialize.make_board(row, column)
    direction = movement.get_user_choice()
    initialize.make_board(row, column)
    user_name = input("Please Enter Your Name: ")
    # start_story(user_name)
    character = initialize.make_character()
    while character.is_alive and character['level'] <= 3:
        output_display.describe_current_location(row, column, character)
        direction = movement.get_user_choice()
        if movement.validate_move(board, character, direction):
            movement.move_character(character, direction)
            villain = battle.check_for_villain(character)
            if villain:
                # fight_villain()
                character.is_alive(character)
            movement.check_if_level_attained(row, column, character)
            if movement.check_if_level_attained(row, column, character):
                movement.increase_floor(character)
                movement.reset_coordinates(character)
                character.attributes_upgrade(character, character)
        else:
            print("You can't go past the board")
    if character.is_alive(character):
        battle.fight_final_boss(character, user_name)
        if battle.fight_final_boss(character, user_name):
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