def attributes_upgrade(character, attribute):

    if character['level'] == 1:
        attribute['punch'] = 2
    elif character['level'] == 2:
        attribute['lick'] = 3
    # else:
    #     attribute['level'] = choice

def is_alive(character):
    if character['HP'] > 0:
        return True
    else:
        return False


def main():
    pass


if __name__ == '__main__':
    main()