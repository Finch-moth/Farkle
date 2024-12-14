# Code by Finch Stanger
# This is the game of Farkle. Can be played with any number of players, can play the game multiple times

import random
from class_function import Farkle

#global variables for the game
n_players = 0
scores = [0]
pot = 0 
p_turn = 1 # player turn
exit = False
game_count = 1
remaining_dice = 6
score_evaluator = Farkle()
player_end = 0

#functions below-----------------------------------------------------------------------------------------------------------

# this is how we will be able to play the game repeatedly
def run_code():
    global pot, p_turn, exit, game_count, remaining_dice, n_players, scores
    # print the rules (once)
    print("\n\n\n\nThis is the game of FARKLE. \nRULES: Roll the dice to get points. With each roll, you must get more points or you FARKLE. You must meld at least 500 points before you start scoring. If a player gets to 10,000 points or more, each other player gets one more turn. The player with the most points wins!!")
    print("SCORING: Ones are 100 points, Fives are 50 points. \nHere are the special points: 3 Ones = 7000; 3 Twos = 200; 3 Threes = 300; 3 Fours = 400; 3 Fives = 500; 3 Sixes = 600")
    print("Four of any number is 1,000; Five of any number is 2,000; Six of any number is 3,000")
    print("Three Pairs is 1,500; Two Triples is 2,500; 1-6 Straight is 1,500\n\n")
    n_players = int(input("How many players are there? Number = "))
    #could input names here, EXTRA
    scores = [0]*n_players
    while not exit:
        play_game()
        # print the winners here. make an empty string and add to it every time?? EXTRA
        response = input("Would you like to play again? Type 'Yes' ") 
        if response == 'Yes': #We want to be able to play the game again 
            #reset all the variables
            scores = [0]*n_players
            pot = 0 
            p_turn = 1 
            game_count += 1
            remaining_dice = 6
        else:
            exit = True

#during this function, we want the entirety of the game to be played
def play_game(): 
    global scores, p_turn  # declaring global variables as part of this function
    print(f"\n\n\n\t\t\tN E W    G A M E :     G A M E   {game_count}\n\n\n")
    while not game_has_winner():
        turn()
    final_round()
    show_all_scores()
    #end of game--print the winner
    print(get_winner())

#consolidate from play_game and final_round -- created a function for player turn
def turn():
    global remaining_dice, pot, p_turn, n_players, scores
    prev_p_turn = p_turn
    show_all_scores()
    print(f"\n\n\t\t\t\t\tIt\'s PLAYER {p_turn}\'S TURN.")
    if pot > 0: # if the previous player left points behind
        if check_meld():  #now it is just checking if the current player has melded
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
        if check_meld() or pot >= 500:
            choice = prompt_player()#call the prompt player function
            if choice == "r" or choice == "R":
                roll()
            elif choice == "k" or choice == "K":
                keep_points()
        else:
            print("Roll again!")
            roll()

#this function allows all players (except for the trigger player) to have one more turn, once last chance to increase their score and take the win!
def final_round(): 
    print("\n\n------------------------------------------------------------------------\n\t\t\tFINAL ROUND!!!!\n------------------------------------------------------------------------\n\n")
    global p_turn, player_end
    while p_turn != player_end:
        turn()

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
        print("\n\n\t\tFarkle!!!\n\n")
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
        for i, component in enumerate(components):
            if i+1 not in placements:
                remaining_dice += len(component)
        if remaining_dice == 0:
            remaining_dice = 6
        print(f"Current Dice Pool: {remaining_dice}\tPoints: {pot}")

#this function displays dice, whether all 6 or less than that.
def display_dice(dice):
    global remaining_dice
    print("---------\t"*remaining_dice)
    print("|       |\t"*remaining_dice)
    print("".join([f"|   {dice[i]}   |\t" for i in range(remaining_dice)]))
    print("|       |\t"*remaining_dice)
    print("---------\t"*remaining_dice)    

# create a function that evaluates if the current player has melded or not. It should return a "True" or "False" statement.
def check_meld():
    global scores, p_turn
    return scores[p_turn-1] >= 500

# If they rolled anything!! This is how we will ask the player if they want to keep the points or continue rolling
def prompt_player():
    print("----------------")
    return input("Roll again or keep points and pass dice? r/k: ")
    
# if the player keeps the points, we add the points to their current score
def keep_points():
    global p_turn, pot, scores
    print(f"\n\t Player {p_turn}: You're keeping the points! Your turn is OVER!\n")
    scores[p_turn-1] += pot 
    pass_turn()

# from roll function or keep points, pass the turn to other player
def pass_turn():
    global p_turn, n_players
    p_turn += 1
    if p_turn > n_players:
        p_turn = 1

def show_all_scores():
    for i, score in enumerate(scores):
        print(f"Player {i+1} score: {score}.")

# if player keeps points, ask opponent if they would like to "steal" or "pigyback"
def prompt_opponent():    
    global remaining_dice
    print(f"\nThere are {remaining_dice} dice\t\tThe pot has {pot} points.\n")
    print("----------------")
    return input(f"Player {p_turn}: Do you want to piggyback or roll all 6 dice? p/r: ")

# this function will determine if a player has reached/gone over 10,000 points
def game_has_winner():
    global player_end, scores 
    for i, score in enumerate(scores):
        if score >= 10000: #testing in 1000, CHANGE TO 10,000 for game!!
            player_end = i+1
            return True
    return False

def get_winner():
    global n_players, scores
    winning_score = max(scores)
    for i, score in enumerate(scores):
        if score == winning_score:
            return f"\n\n\n THE WINNER IS: Player {i+1} with {winning_score} points!!\n\n\n"

run_code()
#this is how you play the game!