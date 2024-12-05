def valid_name(user_name):
    """
    Determines if the name is valid.

    :param user_name: a string
    :precondition: user_name is a string less than 30 characters
    :postcondition: correctly determine if user_name is less than 30 characters
    :return: a Boolean
    >>> name = "Peter"
    >>> valid_name(name)
    True
    >>> name = ""
    >>> valid_name(name)
    True
    >>> name = "Sir Charles The Third Coming From the Wastelands of South Sudan"
    >>> valid_name(name)
    False
    """
    if len(user_name) < 30:
        return True
    else:
        return False


def attributes_upgrade(player, attributes):
    """
    Upgrades player's attributes when reaching a new level.

    :param player: a dictionary
    :param attributes: a list of dictionaries
    :precondition: player contains all required key:value pairs
    :precondition: attributes contains individual dictionaries for each ability
    :postcondition: adds correct dictionary to list
    :return: None
    >>> player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'floor': 1, 'Waist': 55, 'Level': 2, 'Attributes': attributes}
    >>> attributes = [{1: {"lick": 1}}]
    >>> attributes_upgrade(player, attributes)
    "You've gained the ability to bite!"
    >>> player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'floor': 1, 'Waist': 55, 'Level': 3, 'Attributes': attributes}
    >>> attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}]
    >>> attributes_upgrade(player, attributes)
    "You've gained the ability to chomp!"
    >>> player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'floor': 1, 'Waist': 55, 'Level': 6, 'Attributes': attributes}
    >>> attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}, {3: {"chomp": 4}}, {4: {"devour": 6}}, {5: {"FEAST": 10}}]
    >>> attributes_upgrade(player, attributes)
    ""
    """
    if player['Level'] == 2:
        attributes.append({2: {"bite": 2}})
        return "You've gained the ability to bite!"
    if player['Level'] == 3:
        attributes.append({3: {"chomp": 4}})
        return "You've gained the ability to chomp!"
    if player['Level'] == 4:
        attributes.append({4: {"devour": 6}})
        return "You've gained the ability to devour!"
    if player['Level'] == 5:
        attributes.append({5: {"FEAST": 10}})
        return "You've gained the ability to FEAST!"



def is_alive(player):
    """
    Determines if player is alive.

    :param player: a dictionary
    :precondition: player contains all required key:value pairs
    :precondition: accurately determines if player is alive
    :return: a Boolean
    """
    if 30 <= player['Waist'] <= 100:
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
    if player['Level'] <= 5:
        waist_reduction_remover = 12 - (player['Level'] * 2)
        player['Waist'] -= waist_reduction_remover
        print("\nYou've successfully levelled up! -" + str(waist_reduction_remover) + " Waist size!")
    else:
        print("\n You've successfully levelled up!")
    player['Level'] += 1


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