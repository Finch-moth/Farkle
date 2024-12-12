#Code by Finch Stanger
# This is the game of Farkle. Farkle is a dice game. Roll to get points, most points win. Final round is when one player gets to 10,000 points. 

#import random library
import random

#global variables for the game
die_1 = 0
die_2 = 0
die_3 = 0
die_4 = 0
die_5 = 0
die_6 = 0
score_1 = 0 # player score
score_2 = 0 # player score
pot = 0 # if someone piggybacks, this is how we will keep track
p_turn = 1 # player turn
prev_p_turn = 0 # helps with loops, might take out

#for the game of farkle, we need several different functions

# this is how we will be able to play the game repeatedly

def run_code():
    # print the rules (once)
    print("This is the game of FARKLE. Roll the dice to get points. Ones are 100 points, Fives are 50 points. With each roll, you must get more points or you FARKLE. You must meld at least 500 points before you start scoring. If a player gets to 10,000 points or more, each other player gets one more turn. The player with the most points wins!!")
    print("Here are the special points: 3 Ones = 1,000; 3 Twos = 200; 3 Threes = 300; 3 Fours = 400; 3 Fives = 500; 3 Sixes = 600")
    print("Four of any number is 1,000; Five of any number is 2,000; Six of any number is 3,000")
    print("Three Pairs is 1,500; Two Triples is 2,500; 1-6 Straight is 1,500")

# This will be the hardest function to get
def search_points(d1, d2, d3, d4, d5, d6):
    global pot
    if d1 == 1 or d2 == 1 or d3 == 1 or d4 == 1 or d5 == 1 or d6 == 1:
        pot += 100
        print(f"Points:{pot}")
    else:
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 or d5 == 5 or d6 == 5:
            pot += 50
            print(f"Points:{pot}")
        else:
                print("Farkle! No points this round")
                pot = 0
                pass_turn()
    
    #this function is from pigs. rewrite for this game!!
    #use if statements to check values of dice & calculate points
    #options: doubles 
    #if d1 == d2:
    #    if d1 == 1:
    #        pot += 30
    #        print("You got double ones, that\'s 30 points!")
    #    else:
    #        points = (d1 + d2) * 2 # could also say d1 * 4
    #        pot += points
    #        print(f"You got doubles! You get {points} added to the pot.")
    #elif d1 == 1 or d2 == 1:
    #    print("\n\n\t\t\t\t\tYou rolled pig! TURN OVER: The dice are passed.\n\n")
    #    pass_turn()
    #else:
    #    points = d1 + d2
    #    pot += points
    #    print(f"You get {points} added to the pot.")

    # this is how the game will check if they rolled any points, or if they "Farkled"
    # check for ones, fives, and special rolls. 
    # if they farkle, reset pot to zero!!!


def prompt_select_dice():
    pass

def play_game():
    global die_1, die_2, die_3, die_4, die_5, die_6, score_1, score_2, pot, p_turn, prev_p_turn # declaring global variables as part of this function
    while not game_has_winner(score_1, score_2):
        prev_p_turn = p_turn
        print(f"Player one's score: {score_1}. \t Player two's score: {score_2}.")
        print(f"\n\n\t\t\t\t\tIt\'s PLAYER {p_turn}\'S TURN.")
        roll() # rolls and searches for points?
        while prev_p_turn == p_turn:
            # should i put all of the below into a different function called player turn or something?
            choice = prompt_player()#call the prompt player function
            if choice == "r" or choice == "R":
                roll()
            elif choice == "k" or choice == "K":
                keep_points(pot, p_turn)#calls the keep function
                pass_turn()

    #during this funciton, we want the entirety of the game to be played. We also want to be able to play the game again once the game is over
    
    #end of game--print the winner
    print(get_winner(score_1, score_2))



# idk
    #during this function, we want everything in a players turn to occur
    # print the scores


# this is how we will roll the dice, no matter how many dice there are
def roll():
    global die_1, die_2, die_3, die_4, die_5, die_6
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)
    die_3 = random.randint(1,6)
    die_4 = random.randint(1,6)
    die_5 = random.randint(1,6)
    die_6 = random.randint(1,6)
    display_dice(die_1, die_2, die_3, die_4, die_5, die_6)
    search_points(die_1, die_2, die_3, die_4, die_5, die_6)

def display_dice(d1, d2, d3, d4, d5, d6):
    print("---------\t---------\t---------\t---------\t---------\t---------")
    print("|       |\t|       |\t|       |\t|       |\t|       |\t|       |")
    print(f"|   {d1}   |\t|   {d2}   |\t|   {d3}   |\t|   {d4}   |\t|   {d5}   |\t|   {d6}   |")
    print("|       |\t|       |\t|       |\t|       |\t|       |\t|       |")
    print("---------\t---------\t---------\t---------\t---------\t---------")    

def prompt_player():
    print("----------------")
    return input("Do you want to roll again or keep the points and pass the dice? r/k: ")
    # If they rolled anything!! This is how we will ask the player if they want to keep the points or continue rolling

def keep_points(points, turn):
    # we need to figure out whose turn it is and then give them the points
    print(f"\n\t Player {p_turn}: You're keeping the points! Your turn is OVER!\n")
    global score_1, score_2, pot
    if turn == 1:
        score_1 += points
    else:
        score_2 += points
    # if the player keeps the points, we add the points to their current score
    # print the scores
    # Meld
    # see if there is a winner
    opt = prompt_opponent()
    if opt == "p" or opt == "P":
        pass
    elif opt == "r" or opt == "R":
        pot = 0 

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
    print(f"\n\n\t\t\t\t\t\nThe pot has {pot} points.\n")
    print("----------------")
    return input(f"Player {p_turn}: Do you want to piggyback or roll all 6 dice? p/r: ")

def game_has_winner(p1, p2):
    if p1 >= 10000 or p2 >= 10000:
        return True
    else:
        return False
    # this function will determine if a player has reached/gone over 10,000 points

def get_winner(p1, p2):
    if p1 >= 10000:
        return f"\n\n\nThe winner is Player 1 with {p1} points!\n\n\n"
    else:
        return f"\n\n\nThe winner is Player 2 with {p2} points!\n\n\n"



play_game()
#this is how you play the game! we will change this eventually to "run code" function instead