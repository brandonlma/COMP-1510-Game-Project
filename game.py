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


def main():
    game()

if __name__ == '__main__':
    main()