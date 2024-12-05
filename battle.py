import random
import time
import user_information


def random_enemy(player):
    """
    Determine if the enemy to be faced.

    :param player: a dictionary
    :precondition: player is a dictionary that contains a 'Floor' key
    :postcondition: accurately determines which enemy is to be faced
    :return: a list containing a name, health, and it's favourite food
    """
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
            return ["Anxiety", 9, "self-doubt"]


def final_boss_story(user_name):
    """
    Output the final boss storyline.


    """
    print("You've successfully reached Floor 4!\n")
    time.sleep(2)
    print("You must now have a consultation with Dr.Fat to get approved liposuction surgery.\n")
    time.sleep(3)
    print("stomp~ stomp~ the ground shakes beneath you\n")
    time.sleep(3)
    print("stomp~ stomp~ he's getting closer\n")
    time.sleep(3)
    print("~BOOM~ the door aggressively swings open\n")
    time.sleep(3)
    print("""                                                                                           
                                              ░░░░░░                                                
                                             ░▓▓▓▓▓▓▓▒░                                             
                                             ░░▒░▒▒░▓▓▓                                             
                                             ░░░░░░░▒▒▒                                             
                                            ░▒▒░░░░▓▓▓░░                                            
                                             ░▓▓▓▓▓▓▒░░▒▒▒▒▒░░                                      
                                       ░░░▒░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░                                  
                                      ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░                                 
                                    ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░░░░░░░                                
                                   ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░                                
                                  ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░                                
                                 ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░                                
                                ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░                                
                                ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░                                 
                                ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░                                  
                                 ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▒░░                                  
                                  ▒▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒░░▒▓▓░                                   
                                  ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░                                   
                                  ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░                                    
                                   ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░                                     
                                    ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░                                     
                                    ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░                                      
                                     ▒▓▓▓▓▓▓▓▓▓░░▒▓▓▓▓▓▓▓▓▓▓▓░                                      
                                     ░▓▓▓▓▓▓▓▓▒░  ░▒▓▓▓▓▓▓▓▓▓░                                      
                                      ▒▓▓▓▓▓▓▓░     ░▓▓▓▓▓▓▓░░                                      
                                      ░▓▓▓▓▓▓░       ▒▓▓▓▓▓▓                                        
                               ░░░░░░▓██████▓░░░░░░▓▓██████▓░░░░░░░░""")
    print(f"Dr.Fat: 'Hello {user_name}. I'm going to check whether you've been good or bad on your diet.'\n")
    time.sleep(3)


def fight_final_boss():
    """
    Run the fighting action against the final boss.

    :return:
    """
    HP = 2
    while HP > 0:
        input_one = input(f"Tell me, what did you eat for breakfast this morning? Lying is acceptable,"
                          f"just make sure I don't catch you.\n")
        input_two = int(input(f'Now tell me, is what you ate for breakfast True or False?\n'
                          f'(Enter "1" for True or "0" for False)\n'))
        random_num = random.randint(1,3)
        print("Hmm, I'm gonna take a guess and say\n...........")
        time.sleep(2)
        if random_num == 1:
            print("TRUE")
        else:
            print("FALSE")

        if random_num == input_two:
            HP -= 1
            if random == 1:
                print("HAHAHAHAHAHAHA I KNEW YOU WERE TELLING THE TRUTH FATTY!")
            else:
                print("HAHAHAHAHAHAHA I KNEW YOU WERE LYING FATTY!")

        else:
            print("Wow fatty, you fooled me. I guess you can have Lipo. :(")
            return True
    return False


def check_for_villain(player):
    """
    Check whether there is a villain.

    :param player: a dictionary
    :precondition: player is a dictionary that contains a 'Floor' key with a value
    :postcondition: randomly determines if there is an enemy based on a random number
    :return: a Boolean
    """
    random_num = random.randint(1, 10)
    if player['Floor'] == 1:
        if random_num <= 40:
            return True
        else:
            return False
    elif player['Floor'] == 2:
        if random_num <= 50:
            return True
        else:
            return False
    else:
        if random_num <= 60:
            return True
        else:
            return False


def fight_villain_story(player, enemy_name, enemy_health):
    """
    Print attack block to display information.

    :param player: a dictionary
    :param enemy_name: a string
    :param enemy_health: an integer
    :return: None
    """

    list_of_attributes = player['Attributes']
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
    print("| Attack Attributes:             |")
    for attributes in list_of_attributes:
        for integer, attribute in attributes.items():
            for ability, damage in attribute.items():
                number = str(integer)
                damage = str(attribute[ability])
                attribute_string = "| " + number + ": "
                attribute_string += ability + " = +/- " + damage + " DMG"
                while len(attribute_string) < 33:
                    attribute_string += " "
                attribute_string += "|"
                print(attribute_string)
    print("+--------------------------------+")


def fight_villain(player, enemy):
    """
    Run the fight action against the villain.

    :param player: a dictionary
    :param enemy: a list
    :precondition: player is a dictionary that contains all required keys and values
    :precondition: enemy is a list containing name, health, and favourite food
    :postcondition: accurately updates health of player and enemy throughout battle
    :return: None
    """
    enemy_name = enemy[0]
    enemy_health = enemy[1]
    enemy_food = enemy[2]
    list_of_attributes = player['Attributes']

    print(f"\nYou have encountered " + enemy_name + " who wants to feed you " + enemy_food + ".\n"
           "Avoid the temptation!")
    while enemy_health > 0 and user_information.is_alive(player):
        fight_villain_story(player, enemy_name, enemy_health)
        attribute_is_valid = False
        damage = 0
        fight_input = 0
        while not attribute_is_valid:
            # for attributes in list_of_attributes:
            #     for integer, attribute in attributes.items():
            #         for ability, damage in attribute.items():
            #             damage = str(attribute[ability])

            fight_input = input("Enter your desired attack (e.g. 1): ")
            attribute_is_valid = fight_attribute_is_valid(player, fight_input)
            if not attribute_is_valid:
                print('Not a valid attack. Please enter a valid attack.\n')
                time.sleep(1)
        attack_chosen = list_of_attributes[int(fight_input) - 1]
        for integer, attribute in attack_chosen.items():
            for key, value in attribute.items():
                damage += value

        if attack_result(player):
            player["Waist"] += damage
            print("\nYou've failed to resist temptation! +" + str(damage) + " Waist Size\n")
        else:
            enemy_health -= damage
            print("\nNice! You've damaged " + enemy_name + " for " + str(damage) + "\n")
        time.sleep(1)

    if enemy_health <= 0:
        print("You've successfully defeated " + enemy_name + "!")
        player['Kills'] += 1
        time.sleep(2)


def attack_result(player):
    """
    Determine if player has successfully attacked the enemy.

    :param player: a dictionary
    :precondition: player is a dictionary that contains all required keys and values
    :postcondition: determines randomly if attack was successful
    :return: a Boolean
    """
    value = random.randint(0, 100)
    if player['Floor'] == 1:
        if value >= 65:
            return True
        else:
            return False
    elif player['Floor'] == 2:
        if value >= 60:
            return True
        else:
            return False
    else:
        if value >= 55:
            return True
        else:
            return False


def fight_attribute_is_valid(player, fight_input):
    """
    Determine if the inputted attack value is valid.

    :param player: a dictionary
    :param fight_input: a string
    :precondition: player is a dictionary that contains a value that holds all possible attacks
    :postcondition: accurately determines if fight_input is in the allowed inputs
    :return: a boolean
    >>> attributes = [{1: {"lick": 1}}]
    >>> player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': attributes}
    >>> fight_input = '1'
    >>> fight_attribute_is_valid(player, fight_input)
    True
    >>> attributes = [{1: {"lick": 1}}]
    >>> player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': attributes}
    >>> fight_input = '2'
    >>> fight_attribute_is_valid(player, fight_input)
    False
    >>> attributes = [{1: {"lick": 1}}]
    >>> player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Kills': 0, 'Floor': 1, 'Waist': 55, 'Attributes': attributes}
    >>> fight_input = 'B'
    >>> fight_attribute_is_valid(player, fight_input)
    False
    """
    inputs = []
    for attributes in player['Attributes']:
        for integer, attribute in attributes.items():
            inputs.append(str(integer))
    if fight_input in inputs:
        return True
    else:
        return False


def main():
    """
    Drive the program.
    """
    attributes = [{1: {"lick": 1}}, {2: {"bite": 2}}, {3: {"chomp": 4}}]
    enemy = ["Ronald McDonald", 8, "chicken nuggets"]
    player = {'X-Coordinate': 0, 'Y-Coordinate': 0, 'Level': 1, 'Waist': 55, 'Floor': 1, 'Attributes': attributes}
    user_name = "Bob"
    fight_final_boss()

if __name__ == '__main__':
    main()