def attributes_upgrade(player, attributes):
    if player['Level'] == 2:
        attributes.append({2: {"bite": 2}})
    if player['Level'] == 3:
        attributes.append({2: {"chomp": 4}})
    if player['Level'] == 4:
        attributes.append({3: {"devour": 6}})
    if player['Level'] == 5:
        attributes.append({3: {"FEAST": 10}})



def is_alive(player):
    if player['Waist'] < 100:
        return True
    else:
        return False

def level_upgrade(player):
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