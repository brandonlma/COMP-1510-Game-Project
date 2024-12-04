def attributes_upgrade(player, attributes):
    """
    Upgrades player's attributes when reaching a new level.

    :param player: a dictionary
    :param attributes: a list of dictionaries
    :precondition: player contains all required key:value pairs
    :precondition: attributes contains individual dictionaries for each ability
    :postcondition: adds correct dictionary to list
    :return: None
    """
    if player['Level'] == 2:
        attributes.append({2: {"bite": 2}})
    if player['Level'] == 3:
        attributes.append({2: {"chomp": 4}})
    if player['Level'] == 4:
        attributes.append({3: {"devour": 6}})
    if player['Level'] == 5:
        attributes.append({3: {"FEAST": 10}})



def is_alive(player):
    """
    Determines if player is alive.

    :param player: a dictionary
    :precondition: player contains all required key:value pairs
    :precondition: accurately determines if player is alive
    :return: a Boolean
    """
    if player['Waist'] < 100:
        return True
    else:
        return False

def level_upgrade(player):
    """
    Upgrades player's level.

    :param player: a dictionary
    :precondition: player contains all required key:value pairs
    :precondition: accurately increases player's level by 1 and lowers waist size by 10
    :return: None
    """
    if player['Level'] < 5:
        print("\nYou've successfully levelled up! -10 Waist size!")
        player['Level'] += 1
        player['Waist'] -= 10


def main():
    attributes = [{1: {"lick": 1}}]
    player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'floor': 1, 'Waist': 55, 'Level': 2, 'Attributes': attributes}
    attributes_upgrade(player, attributes)
    print(player)
    player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'floor': 1, 'Waist': 55, 'Level': 3, 'Attributes': attributes}
    attributes_upgrade(player, attributes)
    print(player)
    player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'floor': 1, 'Waist': 55, 'Level': 4, 'Attributes': attributes}
    attributes_upgrade(player, attributes)
    print(player)
    player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'floor': 1, 'Waist': 55, 'Level': 5, 'Attributes': attributes}
    attributes_upgrade(player, attributes)
    print(player)


if __name__ == '__main__':
    main()