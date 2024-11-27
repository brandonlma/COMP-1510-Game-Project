import random
import time
from operator import truediv


def make_board(rows, columns):
    row = 0
    board = {}

    while row < rows:
        column = 0
        while column < columns:
            coordinate = (row, column)
            board.update({coordinate: "Empty Room"})
            column += 1
        row += 1
    return board


def create_character():
    name = input("What is your name? ")
    character = {"Name": name, "Waist Size": 55, "Dedication to lose weight": 50}
    print("Hello " + name + "! Welcome to The Central Hospital for Gastric Bypass Surgeries. I see you want to apply for a Gastric Bypass surgery.")
    print("However, you must have a consultation with Dr.Now before getting approved. Please follow me this way. ")
    return character


def fight_temptation():
    enemy = random_enemy()
    int(input(print("You stumble across " + enemy + ". They prepare to attack you! What do you choose to counter?")))
    # guessing_game(enemy)


def random_enemy(character):
    value = random.randInt(1,3)
    if character['Floor'] == 1:
        if value == 1:
            return "Pillsbury Doughboy"
        elif value == 2:
            return "Cookie Monster"
        else:
            return "Chester the Cheetah"
    elif character['Floor'] == 2:
        if value == 1:
            return "Ronald McDonald"
        elif value == 2:
            return "Colonel Sanders"
        else:
            return "Mid 2000s Jared Fogle"
    else:
        return "yourself"


def start_story(user_name):

    print('\nHi '+ user_name + ', welcome to the game of life! Lets begin!\n')
    time.sleep(3)
    print('You are 25 years old, fresh out of college hot shot. You just got a job\n'
        'at some big law firm making qauter million dollars a year. \n')
    time.sleep(5)
    print('A year goes by and now your making over 300k a year now, and you\'ve just \n'
        'started a relationship with your smoking hot partner.\n')
    time.sleep(5)
    print('4 years go by, now your making close to a MILLION dollars a year.\n'
          'You\'ve just got married to the love of your life,\n'
          'and you just bought a new home in a gated community with a massive backyard pool. \n')
    time.sleep(5)
    print('LIFE\n')
    time.sleep(1)
    print('IS\n')
    time.sleep(1)
    print('GREAT\n')
    time.sleep(1)
    print('.....\n')
    time.sleep(4)
    print('25 years have gone by now.\n') 
    time.sleep(4)
    print('You have 3 kids, gone through a nasty divorce.')
    time.sleep(2)
    print('Your spouse has cheated on you with the bartender at your local Olive Garden.')
    time.sleep(2)
    print('You\'ve gambled your money away through a gambling addiction.')
    time.sleep(2)
    print('And most importantly, you\'ve eaten your sadness away and gained 300lbs.')
    time.sleep(2)
    print('Your waist size is now 55 and none of your pants fit you anymore.\n')
    time.sleep(2)
    print('Your objective is to lose enough weight to be approved a surgical gastric bypass procedure.\n'
          'Drop your waist size to 40 before Father Time catches up to you.')



def make_character():

    return {'X-Coordinates': 0, 'Y-Coordinates': 0, 'Floor': 1, 'Waist': 55}


def make_floors(rows, columns):

    board = {}
    for row in range(rows):
        for col in range(columns):
            board[(row, col)] = 'Empty room'
    return board


def level_up(character): # = level
    if character['Waist'] == 50:
        character['Floor'] = 2
        make_floors(rows,columns)
    elif character['Waist'] == 45:
        character['Floor'] = 3
        make_floors(rows, columns)
    elif character['Waist'] == 40:
        print("Game over")
        # character['Floor'] = 'WINNER'


def game():
    row = 6
    column = 6
    make_board(row, column)
    user_name = input("Please Enter Your Name: ")
    start_game = start_story(user_name)
    print(start_game)
    row = 6
    column = 6
    character = make_character()
    level = level_up(character)


def main():
    game()



if __name__ == "__main__":
    main()