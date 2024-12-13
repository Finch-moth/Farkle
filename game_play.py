#Code by Finch Stanger
# This is the game of Farkle. Farkle is a dice game. Roll to get points, most points win. Final round is when one player gets to 10,000 points. 

import random
from class_function import Farkle

#global variables for the game
score_1 = 0 #NEWWW player score
score_2 = 0 #NEWWW player score
pot = 0 
p_turn = 1 # player turn
prev_p_turn = 0 # helps with loops, might take out
exit = False
game_count = 1
remaining_dice = 6
score_evaluator = Farkle() #NEWWW 

#functions below-----------------------------------------------------------------------------------------------------------

# this is how we will be able to play the game repeatedly
def run_code():
    global score_1, score_2, pot, p_turn, prev_p_turn, exit, game_count, remaining_dice
    # print the rules (once)
    print("\n\n\n\nThis is the game of FARKLE. Roll the dice to get points. Ones are 100 points, Fives are 50 points. With each roll, you must get more points or you FARKLE. You must meld at least 500 points before you start scoring. If a player gets to 10,000 points or more, each other player gets one more turn. The player with the most points wins!!")
    print("Here are the special points: 3 Ones = 7000; 3 Twos = 200; 3 Threes = 300; 3 Fours = 400; 3 Fives = 500; 3 Sixes = 600")
    print("Four of any number is 1,000; Five of any number is 2,000; Six of any number is 3,000")
    print("Three Pairs is 1,500; Two Triples is 2,500; 1-6 Straight is 1,500\n\n")

    #NEWWW input number of players here?
    #NEWWW input player names here?

    while not exit:
        play_game()
        response = input("Would you like to play again? Type 'Yes' ") 
        if response == 'Yes': #We want to be able to play the game again 
            #reset all the variables
            score_1 = 0 #NEWWW  change this
            score_2 = 0 #NEWWW  change this
            pot = 0 
            p_turn = 1 #NEWWW  we will need to account for more than one player in the rest of the code
            prev_p_turn = 0 
            game_count += 1
            remaining_dice = 6
        else:
            exit = True


# create a function that evaluates if the current player has melded or not. It should return a "True" or "False" statement.
def check_meld(): #should we pass the function player turn or something else?
    pass

#during this function, we want the entirety of the game to be played
def play_game(): #NEWWW  change scores to incorporate different code
    global score_1, score_2, p_turn, prev_p_turn # declaring global variables as part of this function
    print(f"\n\n\n\t\t\tN E W    G A M E :     G A M E   {game_count}\n\n")
    while not game_has_winner(score_1, score_2): #NEWWW change these, but have to be global variables still!!
        turn()
    # print("\n\n\n\t\t\tFINAL ROUND!!!!\n\n\n") ??
    final_round()
    #end of game--print the winner
    print(get_winner(score_1, score_2)) #NEWWW  this will also change for allowing multiple players

def final_round(): #NEWWW incorporate for multiple players in a round, not just one player having a final turn
    print("\n\n\n\t\t\tFINAL ROUND!!!!\n\n\n")
    #NEWWW  we will remove/change the scoring
    global p_turn #NEWWW change to allow multiple people (do a while p_turn not get winner person)
    turn()

#consolidate from play_game and final_round -- created a function for player turn
def turn():
    global score_1, score_2, remaining_dice, pot, p_turn, prev_p_turn  # NEWWW need to change scores
    prev_p_turn = p_turn
    print(f"Player one's score: {score_1}. \t Player two's score: {score_2}.")
    print(f"\n\n\t\t\t\t\tIt\'s PLAYER {p_turn}\'S TURN.")
    if pot > 0: # if the previous player left points behind
        if score_1 >= 500 and score_2 >= 500: #NEWWW  this will change to account for more people
            opt = prompt_opponent() # this player can choose to piggyback or start fresh. only asks at beg of turn once
            if opt == "p" or opt == "P":
                pass
            elif opt == "r" or opt == "R":
                pot = 0
                remaining_dice = 6
        else:
            pot = 0
            remaining_dice = 6
    roll() # rolls and searches for points
    while prev_p_turn == p_turn:
        #NEWWW need to account for melding here
        if pot >= 500:
            choice = prompt_player()#call the prompt player function
            if choice == "r" or choice == "R":
                roll()
            elif choice == "k" or choice == "K":
                keep_points(p_turn) #NEWWW change what it gets passed to bc multiple people
        else:
            print("Roll again!")
            roll()
    

# this is how we will roll the dice, no matter how many dice there are
def roll(): 
    global pot, remaining_dice
    dice_pool = []
    input("Press ENTER to roll")
    for i in range(remaining_dice):
        dice_pool.append(random.randint(1,6))
    display_dice(dice_pool)
    components, scores = score_evaluator.evaluate_dice(dice_pool)
    if sum(scores) == 0:
        print("Farkle!!!")
        pass_turn()
        remaining_dice = 6
        pot = 0
    else:
        print(f"Patterns found: {components}, Respective Points: {scores}")
        placements = list(map(int, input("Which pattern would you like to keep? If multiple, leave a space between each ").strip().split(' ')))
        for placement in placements:
            pot += scores[placement-1]
        placements = set(placements)
        remaining_dice = 0
        print(f"{placements}")
        for i, component in enumerate(components):
            if i+1 not in placements:
                remaining_dice += len(component)
        if remaining_dice == 0:
            remaining_dice = 6
        print(f"Current Dice Pool: {remaining_dice}\tPoints: {pot}")




def display_dice(dice):
    global remaining_dice
    print("---------\t"*remaining_dice)
    print("|       |\t"*remaining_dice)
    print("".join([f"|   {dice[i]}   |\t" for i in range(remaining_dice)]))
    print("|       |\t"*remaining_dice)
    print("---------\t"*remaining_dice)    

# this is how the game will check if they rolled any points, or if they "Farkled"


def prompt_player():
    print("----------------")
    return input("Roll again or keep points and pass dice? r/k: ")
    # If they rolled anything!! This is how we will ask the player if they want to keep the points or continue rolling

# if the player keeps the points, we add the points to their current score
def keep_points(turn):
    print(f"\n\t Player {p_turn}: You're keeping the points! Your turn is OVER!\n")
    global score_1, score_2, pot
    #NEWWW  this will change to account for more people
    if turn == 1:     # we need to figure out whose turn it is and then give them the points
        score_1 += pot
    else:
        score_2 += pot
    pass_turn()

def pass_turn():
    # from search points or keep points, pass the turn to other player
    global p_turn
    #NEWWW  this will change to account for more people
    if p_turn == 1:
        p_turn = 2
    else:
        p_turn = 1

def prompt_opponent():    
    global remaining_dice
    # if player keeps points, ask opponent if they would like to "steal" or "pigyback"
    print(f"\nThere are {remaining_dice} dice\t\tThe pot has {pot} points.\n")
    print("----------------")
    return input(f"Player {p_turn}: Do you want to piggyback or roll all 6 dice? p/r: ")

def game_has_winner(p1, p2):
    #NEWWW  this will change to account for more people
    if p1 >= 1000 or p2 >= 1000: #CHANGE BACK to 10,000
        return True
    else:
        return False
    # this function will determine if a player has reached/gone over 10,000 points

def get_winner(p1, p2):
    #NEWWW this will change to account for more people
    if p1 > p2:
        return f"\n\n\n\t\tTHE WINNER IS: Player 1 with {p1} points!\n\n\n"
    elif p2 > p1:
        return f"\n\n\n\t\tTHE WINNER IS: Player 2 with {p2} points!\n\n\n"
    else:
        return "\n\n\n\t\tTied Game!! \nYOU SILLY GOOSE, you're created an impass. Play again to settle the score\n\n\n"

run_code()
#this is how you play the game!