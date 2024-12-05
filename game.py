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
    output_display.intro_image()
    user_name = input("Hello! Welcome to Lose Your Weight!\n"
                 "To start the game, please enter your name: ")
    valid_name = False
    while not valid_name:
        valid_name = user_information.valid_name(user_name)
        if not valid_name:
            user_name = input("\nName is too long. Please input a name less than 30 characters: ")
    # initialize.start_story(user_name)
    player = initialize.make_character(attributes)
    print("")
    output_display.display_user_stats(player, user_name)
    time.sleep(2)
    while user_information.is_alive(player) and player['Floor'] <= 3:
        print("")
        output_display.describe_current_location(player)
        output_display.print_map_location(row, column, player)
        direction = movement.get_user_choice()
        if movement.validate_move(board, player, direction):
            movement.validate_move(board, player, direction)
            if direction == "E":
                print("")
                output_display.display_user_stats(player, user_name)
                time.sleep(3)
            elif direction == "R":
                print(initialize.objective())
                time.sleep(5)
            else:
                movement.move_character(player, direction)
                villain = battle.check_for_villain(player)
                if villain:
                    enemy = battle.random_enemy(player)
                    battle.fight_villain(player, enemy)
                    if player['Kills'] % 3 == 0 and player['Kills'] != 0:
                        print("")
                        print(user_information.level_upgrade(player))
                        if player['Level'] <= 5:
                            print(user_information.attributes_upgrade(player, attributes))
                        time.sleep(2)
                if movement.check_if_floor_attained(row, column, player):
                    movement.increase_floor(player)
                    movement.reset_coordinates(player)
        else:
            print("That move would make you go off the board. Try again.")
            time.sleep(1)
    if user_information.is_alive(player):
        battle.final_boss_story(user_name)
        final_game = battle.fight_final_boss(player)
        if final_game:
            time.sleep(1)
            print("Congratulations! You won LIPOSUCTION!!")
        else:
            time.sleep(1)
            print("You lost. You don't deserve the liposuction.\n")
            time.sleep(2)
            print("Surgical procedure DENIED!")
    else:
        if player['Waist'] >= 100:
            time.sleep(1)
            print("You lost. You got way too fat.\n")
            time.sleep(2)
            print("Rest in peace.")
        else:
            time.sleep(1)
            print("WHAT??? YOU WON WITHOUT REACHING THE END GOAL?\n")
            time.sleep(2)
            print("You're too skinny now! You don't need liposuction anymore!\n")
            time.sleep(2)
            print("Congrats... I guess we can't get money from your surgery now.")



def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()