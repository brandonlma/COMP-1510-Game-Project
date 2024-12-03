import movement
import battle
import initialize
import user_information
import output_display
import time

def game():
    """
    Drive the game.
    """
    row = 6
    column = 6
    board = initialize.make_board(row, column)
    initialize.make_board(row, column)
    attributes = {'lick': 1}
    user_name = output_display.intro_image()
    initialize.start_story(user_name)
    player = initialize.make_character(attributes)
    output_display.display_user_stats(player, user_name)
    time.sleep(3)
    output_display.describe_current_location(row, column, player)
    time.sleep(3)
    while user_information.is_alive(player) and player['Level'] <= 3:
        direction = movement.get_user_choice(player)
        if movement.validate_move(board, player, direction):
            if direction == "E":
                output_display.display_user_stats(player, user_name)
                time.sleep(5)
            else:
                movement.move_character(player, direction)
                villain = battle.check_for_villain(player)
                if villain:
                    battle.fight_villain(player)
                movement.check_if_level_attained(row, column, player)
                if movement.check_if_level_attained(row, column, player):
                    movement.increase_floor(player)
                    movement.reset_coordinates(player)
                    user_information.attributes_upgrade(player, attributes)
                output_display.describe_current_location(row, column, player)
        else:
            print("You can't go past the board")
    if user_information.is_alive(player):
        final_game = battle.fight_final_boss(player, user_name)
        if final_game:
            print("Congratulations! You won LIPOSUCTION!!")
        else:
            print("You lost. Have fun love handles")
            player['HP'] = 0
    else:
        print("You lost. Have fun love handles")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()