<<<<<<< HEAD
import random
import time
from operator import truediv


def make_board(rows, columns, floors):
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
    guessing_game(enemy)


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

def guessing_game(enemy):


    if enemy == "yourself":
        number = random.randInt(1, 2)
        guess = int(input("You are at a roulette table. Red or black?"))
    elif enemy == "Ronald McDonald" || enemy == "Colonel Sanders" || enemy == "Mid 2000s Jared Fogle":
        number = random.randInt(1, 4)
        guess = int(input("You are at a roulette table. Red or black, even or odd?"))
    else:
        number = random.randInt(1, 6)
        guess = int(input("You are at a roulette table. Red or black, 1-12, 13-24, or 25-36?"))

    if number:
        return True
    else:
        return False


def game():
    character = create_character()

=======
def start_story(user_name):

    return (f'Hi {user_name}, welcome to the game of life! Lets begin!\n '
            f'you are 25 years old, fresh out of college hot shot. You just got a job'
            f'at some big law firm making qauter million dollars a year. \n'
            f'A year goes by and now your making over 300k a year now, and you\'ve just \n'
            f'started a relationship with your smoking hot partner. 4 years go by, now your making\n'
            f'close to a MILLION dollars a year, you\'ve just got married to your partner, '
            f'and you just bought a new home in a gated community with a massive backyard pool. \n'
            f'Life \n Is\n Great\n 25 years have gone by now. You have 3 kids, gone through a nasty divorce\n'
            f'your spouse has cheated on you with the bartender at your local olivegarden, you\'ve \n'
            f'gambled your money away through an gambling addiction you got through')

def make_character():

    return {'X-Coordinates': 0, 'Y-Coordinates': 0, 'Floor': 1, 'Waist': 55}

def make_floors(rows, columns):

    board = {}
    for row in range(rows):
        for col in range(columns):
            board[(row, col)] = 'Empty room'
    return board

def level_up(character,rows,columns): # = level
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
    user_name = input("Please Enter Your Name")
    start_game = start_story(user_name)
    print(start_game)
    row = 6
    column = 6
    character = make_character()
    level = level_up(character)
>>>>>>> 26e33fde2cc8c218efde27948d38b70c28add3ad


def main():
    game()

<<<<<<< HEAD


if __name__ == "__main__":
=======
if __name__ == '__main__':
>>>>>>> 26e33fde2cc8c218efde27948d38b70c28add3ad
    main()