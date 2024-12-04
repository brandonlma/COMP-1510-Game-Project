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
    attributes = [{1: {'lick': 1}}]
    user_name = output_display.intro_image()
    # initialize.start_story(user_name)
    player = initialize.make_character(attributes)
    output_display.display_user_stats(player, user_name)
    time.sleep(2)
    while user_information.is_alive(player) and player['Floor'] <= 3:
        output_display.describe_current_location(row, column, player)
        direction = movement.get_user_choice()
        if movement.validate_move(board, player, direction):
            movement.validate_move(board, player, direction)
            if direction == "E":
                output_display.display_user_stats(player, user_name)
                time.sleep(5)
            elif direction == "R":
                initialize.objective()
                time.sleep(5)
            else:
                movement.move_character(player, direction)
                villain = battle.check_for_villain(player)
                if villain:
                    enemy = battle.random_enemy(player)
                    battle.fight_villain(player, enemy)
                    if player['Kills'] % 3 == 0 and player['Kills'] != 0:
                        user_information.level_upgrade(player)
                        time.sleep(2)
                        if player['Level'] <= 3:
                            user_information.attributes_upgrade(player, attributes)
                            time.sleep(2)
                if movement.check_if_floor_attained(row, column, player):
                    movement.increase_floor(player)
                    movement.reset_coordinates(player)
        else:
            print("That move would make you go off the board. Try again.")
            time.sleep(1)
    if user_information.is_alive(player):
        final_game = battle.fight_final_boss(player, user_name)
        if final_game:
            print("Congratulations! You won LIPOSUCTION!!")
        else:
            print("You lost. Have fun love handles")
    else:
        print("You lost. Have fun love handles")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()