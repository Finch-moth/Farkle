#Code by Finch Stanger
# This is the game of Farkle. Farkle is a dice game. Roll to get points, most points win. Final round is when one player gets to 10,000 points. 

import random
from collections import Counter # yay!

#global variables for the game
score_1 = 0 # player score
score_2 = 0 # player score
pot = 0 # if someone piggybacks, this is how we will keep track
p_turn = 1 # player turn
prev_p_turn = 0 # helps with loops, might take out
cup = [1, 2, 3, 4, 5, 6] # how many dice are we rolling?
hold = [False, False, False, False, False, False]
exit = False

#for the game of farkle, we need several different functions

# this is how we will be able to play the game repeatedly
def run_code():
    global score_1, score_2, pot, p_turn, prev_p_turn, cup, hold, exit
    # print the rules (once)
    print("\n\n\n\nThis is the game of FARKLE. Roll the dice to get points. Ones are 100 points, Fives are 50 points. With each roll, you must get more points or you FARKLE. You must meld at least 500 points before you start scoring. If a player gets to 10,000 points or more, each other player gets one more turn. The player with the most points wins!!")
    print("Here are the special points: 3 Ones = 1,000; 3 Twos = 200; 3 Threes = 300; 3 Fours = 400; 3 Fives = 500; 3 Sixes = 600")
    print("Four of any number is 1,000; Five of any number is 2,000; Six of any number is 3,000")
    print("Three Pairs is 1,500; Two Triples is 2,500; 1-6 Straight is 1,500\n\n")
    while not exit:
        play_game()
        response = input("Would you like to play again? Type 'Yes'")
        if response == 'Yes':
            #reset all the variables
            score_1 = 0 
            score_2 = 0 
            pot = 0 
            p_turn = 1
            prev_p_turn = 0 
            cup = [1, 2, 3, 4, 5, 6] 
            hold = [False, False, False, False, False, False]
        else:
            exit = True



#during this function, we want the entirety of the game to be played. We also want to be able to play the game again once the game is over
def play_game():
    global score_1, score_2, pot, p_turn, prev_p_turn, cup, hold # declaring global variables as part of this function
    print("\n\n\n\t\t\tNEW GAME\n\n")
    while not game_has_winner(score_1, score_2):
        prev_p_turn = p_turn
        print(f"Player one's score: {score_1}. \t Player two's score: {score_2}.")
        print(f"\n\n\t\t\t\t\tIt\'s PLAYER {p_turn}\'S TURN.")
        #cup = [{die_1}, {die_2}, {die_3}, {die_4}, {die_5}, {die_6}]
        if pot > 0: # if the previous player left points behind
            opt = prompt_opponent() # this player can choose to piggyback or start fresh. only asks at beg of turn once
            if opt == "p" or opt == "P":
                pass
            elif opt == "r" or opt == "R":
                pot = 0
                hold = reset_hold() # use all dice
        roll(cup, hold) # rolls and searches for points?
        while prev_p_turn == p_turn:
            # should i put all of the below into a different function called player turn or something?
            choice = prompt_player()#call the prompt player function
            if choice == "r" or choice == "R":
                roll(cup, hold)
            elif choice == "k" or choice == "K":
                keep_points(pot, p_turn)#calls the keep function
    final_round()
    #end of game--print the winner
    print(get_winner(score_1, score_2))

def final_round():
    print("\n\n\n\t\t\tFINAL ROUND!!!!\n\n\n")
    global score_1, score_2, pot, p_turn, prev_p_turn, hold
    prev_p_turn = p_turn
    print(f"Player one's score: {score_1}. \t Player two's score: {score_2}.")
    print(f"\n\n\t\t\t\t\tIt\'s PLAYER {p_turn}\'S TURN.")
    opt = prompt_opponent()
    if opt == "p" or opt == "P":
        pass
    elif opt == "r" or opt == "R":
        pot = 0
        hold = reset_hold() # use all dice
    roll(cup, hold) # rolls and searches for points?
    while prev_p_turn == p_turn:
        choice = prompt_player()#call the prompt player function
        if choice == "r" or choice == "R":
            roll(cup, hold)
        elif choice == "k" or choice == "K":
            print(f"\n\t Player {p_turn}: You're keeping the points! Your turn is OVER!\n")
            if p_turn == 1:
                score_1 += pot
            else:
                score_2 += pot
            pass_turn()
    

# this is how we will roll the dice, no matter how many dice there are
def roll(dice_pool, holding): #works with list
    input("Press ENTER to roll")
    for i in range(6):
        if not holding[i]:
            dice_pool[i] = random.randint(1,6)
    display_dice(dice_pool)
    search_points(dice_pool)
    return dice_pool

def display_dice(dice):
    print("---------\t---------\t---------\t---------\t---------\t---------")
    print("|       |\t|       |\t|       |\t|       |\t|       |\t|       |")
    print(f"|   {dice[0]}   |\t|   {dice[1]}   |\t|   {dice[2]}   |\t|   {dice[3]}   |\t|   {dice[4]}   |\t|   {dice[5]}   |")
    print("|       |\t|       |\t|       |\t|       |\t|       |\t|       |")
    print("---------\t---------\t---------\t---------\t---------\t---------")    

# this is how the game will check if they rolled any points, or if they "Farkled"
def search_points(cup): # working with list
    global pot
    temp_points = 0
    counts = Counter(cup)
    h_max = max(counts.values())
    h_min = min(counts.values())
    unused_dice = 6
    if h_max == 6:
        temp_points += 3000
        unused_dice = 0
    elif h_max == 5:
        temp_points += 2000
        unused_dice = 1
    elif h_max == 4: 
        if h_min == 2: #this is four of a kind plus a pair
            temp_points += 1500
            unused_dice = 0
        else:
            temp_points += 1000
            unused_dice = 2
    elif h_max == 3: 
        if h_min == 3: # this is two trips
            temp_points += 2500
            unused_dice = 0
        else:
            high_die = max(counts, key=counts.get)
            point_values = [300, 200, 300, 400, 500, 600]
            temp_points = point_values[high_die-1]
            unused_dice = 3
    elif h_max == 2: 
        if h_min == 2: # this is three pairs
            temp_points += 1500
            unused_dice = 0
    elif h_max == 1: # this is a straight
        temp_points += 1500
        unused_dice = 0
    one_count = counts.get(1)
    five_count = counts.get(5)
    if one_count is not None and one_count <= unused_dice:
        temp_points += 100*one_count
    if five_count is not None and five_count <= unused_dice:
        temp_points += 50*five_count
    if temp_points > 0:
        print(f"{temp_points} points were added to the pot")
        pot += temp_points
    else:
        print("\n\n\nFARKLE!\n No points this round\n\n")
        pot = 0     # if they farkle, reset pot to zero!!!
        pass_turn()
    print(f"points: {pot}")

def hold_dice(my_list): #which winning dice will you hold onto while the rest are rolled?
    placements = map(int, input("Which die/dice would you like to hold? If multiple, leave a space between ").split(' '))
    #check to make sure the placement is in the list
    for placement in placements:
        if placement >= 1 and placement <= len(my_list):
            my_list[placement-1]= True

def prompt_player():
    print("----------------")
    return input("Do you want to roll again or keep the points and pass the dice? r/k: ")
    # If they rolled anything!! This is how we will ask the player if they want to keep the points or continue rolling

def reset_hold(): # set "hold" equal to this 
    my_list = [False, False, False, False, False, False]
    return my_list

# if the player keeps the points, we add the points to their current score
def keep_points(points, turn):
    # ADD CODE FOR MELD
    print(f"\n\t Player {p_turn}: You're keeping the points! Your turn is OVER!\n")
    global score_1, score_2, pot, pool
    if turn == 1:     # we need to figure out whose turn it is and then give them the points
        score_1 += points
    else:
        score_2 += points
    pass_turn()

def pass_turn():
    # from search points or keep points, pass the turn to other player
    global p_turn
    if p_turn == 1:
        p_turn = 2
    else:
        p_turn = 1

def prompt_opponent():    
    # if player keeps points, ask opponent if they would like to "steal" or "pigyback"
    #first check to see if opponent has a meld
    print(f"\n\t\t\t\t\tThe pot has {pot} points.\n")
    print("----------------")
    return input(f"Player {p_turn}: Do you want to piggyback or roll all 6 dice? p/r: ")

def game_has_winner(p1, p2):
    if p1 >= 1000 or p2 >= 1000: #CHANGE BACK to 10,000
        return True
    else:
        return False
    # this function will determine if a player has reached/gone over 10,000 points

def get_winner(p1, p2):
    if p1 >= 1000: #CHANGE BACK to 10,000
        return f"\n\n\nThe winner is: Player 1 with {p1} points!\n\n\n"
    else:
        return f"\n\n\n\t\tTHE WINNER IS: Player 2 with {p2} points!\n\n\n"

run_code()
#this is how you play the game!