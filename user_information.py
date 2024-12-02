def attributes_upgrade(character, attributes):
    if character['level'] == 2:
        attributes['bite'] = 2
    if character['level'] == 3:
        attributes['chomp'] = 4
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