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



def main():
    game()



if __name__ == "__main__":
    main()