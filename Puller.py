import random
from data import *
import time

total_pulls = 0

# We will total_pulls to keep track of the total number of pulls to implement pity system which works as follows:
# If you havent pulled a Legendary or Mythic in 40 pulls, you are guaranteed to pull one on the 41th pull.
def pull(banner_type, num_pulls):
    global total_pulls
    total_pulls += num_pulls
    results = []
    total_weight = 0
    for i in range(num_pulls):
        if banner_type == "Regular":
            weights = regular_weights
        elif banner_type == "Ember Banner":
            weights = Ember_weights
        elif banner_type == "Nyla Banner":
            weights = Nyla_weights
        elif banner_type == "Elysia Banner":
            weights = Elysia_weights
        elif banner_type == "Azure Banner":
            weights = Azure_weights
        elif banner_type == "Aphrodite Banner":
            weights = aphrodite_weights
        elif banner_type == "Hades Banner":
            weights = hades_weights
        elif banner_type == "Weapon":
            weights = weapon_weights
        # pity system
    for key in weights:
        total_weight += weights[key]
    random_num = random.randint(0, total_weight - 1)
    for key in weights:
        random_num -= weights[key]
        if random_num < 0:
            return key
    return "Error"

#run the simulation
def run_simulation(banner_type, num_pulls):
    results = []
    for i in range(num_pulls):
        results.append(pull(banner_type, num_pulls))

    characters = {}
    items = {}
    for result in results:
        if "Sword" not in result and "Bow" not in result and "Staff" not in result and "Shield" not in result and "Knives" not in result and "Wand" not in result:
            if result in characters:
                characters[result] += 1
            else:
                characters[result] = 1
        if "Sword" in result or "Bow" in result or "Staff" in result or "Shield" in result or "Knives" in result or "Wand" in result:
            if result in items:
                items[result] += 1
            else:
                items[result] = 1

    result_list = []
    # combine keys from both dictionaries into one list
    for key in characters:
        result_list.append(key)
    for key in items:
        result_list.append(key)
    
    return result_list

#ask for input
while True:
    banner_type = input("What banner type? ")
    num_pulls = int(input("How many pulls? "))
    
    print(run_simulation(banner_type, num_pulls))
    print("Total pulls: " + str(total_pulls//10))
            

