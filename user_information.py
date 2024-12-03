def attributes_upgrade(character, attributes):
    if character['Level'] == 2:
        attributes['bite'] = 2
    if character['Level'] == 3:
        attributes['chomp'] = 4
    if character['Level'] == 4:
        attributes['devour'] == 10
    # else:
    #     attribute['level'] = choice


def is_alive(player):
    if player['Waist'] < 100:
        return True
    else:
        return False

def level_upgrade(player):
    print("\nYou've successfully levelled up! -10 Waist size!\n")
    player['Level'] += 1
    player['Waist'] -= 10


def main():
    # attributes = {"lick": 1}
    # player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'level': 1, 'Waist': 55, 'HP': 5, 'Attributes': attributes}
    pass


if __name__ == '__main__':
    main()