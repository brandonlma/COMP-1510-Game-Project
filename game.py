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
    initialize.make_board(row, column)
    user_name = input("Please Enter Your Name: ")
    # start_story(user_name)
    player = initialize.make_character()
    while character.is_alive and player['level'] <= 3:
        output_display.describe_current_location(row, column, player)
        direction = movement.get_user_choice()
        if movement.validate_move(board, player, direction):
            movement.move_character(player, direction)
            villain = battle.check_for_villain(player)
            if villain:
                # fight_villain()
                character.is_alive(player)
            movement.check_if_level_attained(row, column, player)
            if movement.check_if_level_attained(row, column, player):
                movement.increase_floor(player)
                movement.reset_coordinates(player)
                character.attributes_upgrade(player, player)
        else:
            print("You can't go past the board")
    if character.is_alive(player):
        battle.fight_final_boss(player, user_name)
        if battle.fight_final_boss(player, user_name):
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