import random
import time
from sys import excepthook


# def random_enemy(character):
#     value = random.randInt(1,3)
#     if character['Floor'] == 1:
#         if value == 1:
#             return "Pillsbury Doughboy"
#         elif value == 2:
#             return "Cookie Monster"
#         else:
#             return "Chester the Cheetah"
#     elif character['Floor'] == 2:
#         if value == 1:
#             return "Ronald McDonald"
#         elif value == 2:
#             return "Colonel Sanders"
#         else:
#             return "Mid 2000s Jared Fogle"
#     else:
#         return "yourself"


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

    if player['level'] == 1:
        random_num = random.randint(0,4)
    elif player['level'] == 2:
        random_num = random.randint(0,3)
    else:
        random_num = random.randint(0,2)

    print(random_num)

    if random_num == 1:
        return True
    else:
        return False

def attributes_upgrade(player, attribute):

    if player['level'] == 1:
        attribute['punch'] = 2
    elif player['level'] == 2:
        attribute['lick'] = 3
    else:
        attribute['level'] = 6 #choice



def fight_villain(player):

    attribute_is_valid = False
    attributes = player['Attributes']
    while not attribute_is_valid:
        print(f"You have encountered a villain. Choose from your available attributes to fight back.")
        string_of_attributes = ""
        for keys, values in attributes.items():
            damage = str(attributes[keys])
            print(keys + " = +/-" + damage + " DMG")
        fight_input = input("Enter your desired attack: ")
        attribute_is_valid = fight_attribute_is_valid(player, fight_input)
        if not attribute_is_valid:
            print('Wrong value. Please enter a valid attribute.')
            time.sleep(1)


    value = random.randint(0,100)
    if player['level'] == 1:
        if value >= 80:
            waist_size_gained = 1 * player["Attributes"][fight_input]
            player["Waist"] += waist_size_gained
            print(r"You've lost! +" + str(waist_size_gained) + "Waist Size")
        else:
            print("Nice! You defeated the ")
    elif player['level'] == 2:
        if value >= 70:
            waist_size_gained = 2 * player["Attributes"][fight_input]
            player["Waist"] += waist_size_gained
            print(r"You've lost! +" + str(waist_size_gained) + "Waist Size")
        else:
            print("Nice! You defeated the ")
    else:
        if value >= 60:
            waist_size_gained = 3 * player["Attributes"][fight_input]
            player["Waist"] += waist_size_gained
            print(r"You've lost! +" + str(waist_size_gained) + "Waist Size")
        else:
            print("Nice! You defeated the ")

    time.sleep(2)


    # while True:
    #     fight_input = input(f"You have encountered a villain. Choose your available attributes to fight back "
    #                          f"\n{player['Attributes']} \nEnter attack name to choose: ")
    #     try: fight_input in player['Attributes']
    #     except fight_input not in player['Attributes']:
    #         print('Wrong Value, Please enter a valid attribute')
    #     else:
    #         return True
    #

def fight_attribute_is_valid(player, fight_input):
    if fight_input in player['Attributes']:
        return True
    else:
        return False


def main():
    # attributes = {"lick": 1, "bite": 2}
    # player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'level': 2, 'Waist': 55, 'HP': 5, 'Attributes': attributes}
    pass

if __name__ == '__main__':
    main()