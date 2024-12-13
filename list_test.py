
import random

def roll(dice_pool, holding):
    input("Press ENTER to roll")
    for i in range(6):
        if not holding[i]:
            dice_pool[i] = random.randint(1,6)
    return dice_pool

def hold_item(my_list):
    placements = map(int, input("Which die/dice would you like to hold? If multiple, leave a space between ").split(' '))
    #check to make sure the placement is in the list
    for placement in placements:
        if placement >= 1 and placement <= len(my_list):
            my_list[placement-1]= True

def reset_hold():
    my_list = [False, False, False, False, False, False]
    return my_list

def delete_item(my_list):
    placement = int(input("What is the placement of the item to delete: "))
    #check to make sure the placement is in the list
    if placement >= 1 and placement <= len(my_list):
        print(f"You deleted: {my_list.pop(placement - 1)}")

def print_list(my_list):
    print("Your list:\n------------------")
    for i, b in enumerate(my_list):
        print(f"{i+1}- {b}")

    print("----------------")

def print_menu():
    print("----------------")
    print("1) Hold a Die")
    print("2) Delete an item")
    print("3) Print the list")
    print("4) Roll Dice")
    print("5) Exit the program")
    print("6) Clear the list")
    print("7) Reset (the hold)")
    print("-------------------")




pool = [False, False, False, False, False, False]

#main part of the program to create a list and call the functions
items = [1, 2, 3, 4, 5, 6]
quit = False
while not quit:
    print_menu()
    try:
        response = int(input("Your choice: "))
    except:
        continue
    if response ==1:
        hold_item(pool)
    elif response == 2:
        delete_item(items)
    elif response == 3:
        print_list(items)
    elif response == 4:
        roll(items, pool)
    elif response == 5:
        quit = True
    elif response == 6:
        items.clear()
    elif response == 7:
        pool = reset_hold()

