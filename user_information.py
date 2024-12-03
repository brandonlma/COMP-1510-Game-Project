def attributes_upgrade(character, attributes):
    if character['level'] == 2:
        attributes['bite'] = 2
    if character['level'] == 3:
        attributes['chomp'] = 4
    if character['level'] == 4:
        attributes['devour'] == 10
    # else:
    #     attribute['level'] = choice

def is_alive(player):
    if player['Waist'] < 100:
        return True
    else:
        return False


def main():
    # attributes = {"lick": 1}
    # player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'level': 1, 'Waist': 55, 'HP': 5, 'Attributes': attributes}
    pass


if __name__ == '__main__':
    main()