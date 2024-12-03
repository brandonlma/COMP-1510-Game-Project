import random
import time
import user_information
from sys import excepthook


def random_enemy(player):
    value = random.randint(1,3)
    if player['Floor'] == 1:
        if value == 1:
            return ["Cookie Monster", 1, "cookies"]
        elif value == 2:
            return ["Chester the Cheetah", 2, "cheetos"]
        else:
            return ["Pillsbury Doughboy", 3, "raw dough"]
    elif player['Floor'] == 2:
        if value == 1:
            return ["Ronald McDonald", 2, "chicken nuggets"]
        elif value == 2:
            return ["Colonel Sanders", 4, "fried chicken"]
        else:
            return ["Burger King", 6, "Whoppers"]
    else:
        if value == 1:
            return ["Queen Elizabeth II", 3, "crumpets"]
        elif value == 2:
            return ["Mid 2000s Jared Fogle", 6, "Subway Sandwiches"]
        else:
            return ["Yourself", 9, "self-doubt"]


def fight_final_boss(player, user_name):
    player['HP'] = 2
    while player['HP'] > 0:
        input_one = input(f"Tell me {user_name}, what did you eat for breakfast this morning? Lying is acceptable,"
                          f"just make sure I don't catch you.\n")
        input_two = int(input(f'Now tell me, is what you ate for breakfast True or False\n'
                          f'Enter "1" for True or "0" for False:\n'))
        random_num = random.randint(1,3)
        print("Hmmmmm, I'm gonna take a guess and say\n...........")
        time.sleep(2)
        if random_num == 1:
            print("TRUE")
        else:
            print("FALSE")

        if random_num == input_two:
            player['hp'] -= 1
            if random == 1:
                print("HAHAHAHAHAHAHA I KNEW YOU WERE TELLING THE TRUTH FATTY")
            else:
                print("HAHAHAHAHA I KNEW YOU WERE LYING FATTY")

        else:
            print("Wow fatty, you fooled me, I guess you can have Lipo")
            return True
    return False


def check_for_villain(player):

    if player['Level'] == 1:
        random_num = random.randint(1,4)
    elif player['Level'] == 2:
        random_num = random.randint(1,3)
    else:
        random_num = random.randint(1,2)

    print(random_num)

    if random_num == 1:
        return True
    else:
        return False


def fight_villain(player, enemy):
    enemy_name = enemy[0]
    enemy_health = enemy[1]
    enemy_food = enemy[2]

    attributes = player['Attributes']
    print(f"\nYou have encountered " + enemy_name + " who wants to feed you " + enemy_food + ".\n"
           "Avoid the temptation!")

    while enemy_health > 0 and user_information.is_alive(player):
        print("+--------------------------------+")
        enemy_string = "| " + enemy_name + " HP: " + str(enemy_health)
        while len(enemy_string) < 33:
            enemy_string += " "
        enemy_string += "|"
        print(enemy_string)
        print("+--------------------------------+")
        waist_size = player["Waist"]
        waist_size_to_string = str(waist_size)
        waist_string = "| Waist Size: " + waist_size_to_string
        while len(waist_string) < 33:
            waist_string += " "
        waist_string += "|"
        print(waist_string)
        print("+--------------------------------+")


        attribute_is_valid = False
        while not attribute_is_valid:
            for keys, values in attributes.items():
                damage = str(attributes[keys])
                print(keys + " = +/- " + damage + " DMG")
            fight_input = input("Enter your desired attack: ")
            attribute_is_valid = fight_attribute_is_valid(player, fight_input)
            if not attribute_is_valid:
                print('Not a valid attack. Please enter a valid attribute.\n')
            time.sleep(1)
        value = random.randint(0, 100)
        if player['Floor'] == 1:
            waist_size_gained = 1 * player["Attributes"][fight_input]
            if value >= 80:
                player["Waist"] += waist_size_gained
                print(r"You've failed to resist temptation! +" + str(waist_size_gained) + " Waist Size")
            else:
                enemy_health -= waist_size_gained
                print(r"Nice! You've damaged " + enemy_name + " for " + str(waist_size_gained))
        elif player['Floor'] == 2:
            waist_size_gained = 2 * player["Attributes"][fight_input]
            if value >= 66:
                player["Waist"] += waist_size_gained
                print(r"You've failed to resist temptation! +" + str(waist_size_gained) + " Waist Size")
            else:
                enemy_health -= waist_size_gained
                print(r"Nice! You've damaged " + enemy_name + " for " + str(waist_size_gained))
        else:
            waist_size_gained = 3 * player["Attributes"][fight_input]
            if value >= 50:
                player["Waist"] += waist_size_gained
                print(r"You've failed to resist temptation! +" + str(waist_size_gained) + " Waist Size")
            else:
                enemy_health -= waist_size_gained
                print(r"Nice! You've damaged " + enemy_name + " for " + str(waist_size_gained))
        time.sleep(2)

    if enemy_health <= 0:
        print(r"You've successfully defeated " + enemy_name + "!")
        player['Kills'] += 1
        time.sleep(2)


def fight_attribute_is_valid(player, fight_input):
    if fight_input in player['Attributes']:
        return True
    else:
        return False


def main():
    # attributes = {"lick": 1, "bite": 2}
    # enemy = ["Ronald McDonald", 8, "chicken nuggets"]
    # player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Waist': 55, 'Floor': 1, 'Attributes': attributes}
    # fight_villain(player, enemy)
    pass

if __name__ == '__main__':
    main()