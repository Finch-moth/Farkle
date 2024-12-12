#PIGS
#project by finch stanger
#this is the dice game pig, a two-player game

#add a meld

import random

#global variables for the game
die_1 = 0
die_2 = 0
score_1 = 0
score_2 = 0
pot = 0
p_turn = 1

#now we will define the FUNCTIONS we will use

#this is our main function
def play_game():
    global die_1, die_2, score_1, score_2, pot, p_turn # declaring global variables as part of this function
    #start a loop for the gameplay
    while not game_has_winner(score_1, score_2):
        #print scores, the pot, and whose turn it is before each roll -- until the game has a winner
        print(f"Player one's score: {score_1}. \t Player two's score: {score_2}.")
        print(f"\n\n\t\t\t\t\tIt\'s PLAYER {p_turn}\'S TURN. \nThe pot has {pot} points.\n")
        # store a local variable; get whether current player wants to roll or pass
        choice = prompt_player()#call the prompt player function
        if choice == "r" or choice == "R":
            roll() #calls roll function
            check_dice(die_1, die_2) #calls check dice function
        elif choice == "k" or choice == "K":
            keep(pot, p_turn)#calls the keep function
            pass_dice()#
    #end of game--print the winner
    print(get_winner(score_1, score_2))



#this prompts the player to either roll or keep the pot
def prompt_player():
    print("----------------")
    return input("Do you want to roll or keep the pot and pass the dice? r/k: ")

def pass_dice():
    # we need to change the player turn and reset the pot
    global pot, p_turn
    pot = 0
    if p_turn == 1:
        p_turn = 2
    else:
        p_turn = 1

def roll():
    global die_1, die_2
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)
    display_dice(die_1, die_2)

def keep(points, turn):
    # we need to figure out whose turn it is and then give them the points
    print("\n\tYou're keeping the pot! Your turn is OVER!\n")
    global score_1, score_2
    if turn == 1:
        score_1 += points
    else:
        score_2 += points

def check_dice(d1,d2):
    global pot
    #use if statements to check values of dice & calculate points
    #options: doubles 
    if d1 == d2:
        if d1 == 1:
            pot += 30
            print("You got double ones, that\'s 30 points!")
        else:
            points = (d1 + d2) * 2 # could also say d1 * 4
            pot += points
            print(f"You got doubles! You get {points} added to the pot.")
    elif d1 == 1 or d2 == 1:
        print("\n\n\t\t\t\t\tYou rolled pig! TURN OVER: The dice are passed.\n\n")
        pass_dice()
    else:
        points = d1 + d2
        pot += points
        print(f"You get {points} added to the pot.")

def display_dice(d1, d2):
    print("---------\t---------")
    print("|       |\t|       |")
    print(f"|   {d1}   |\t|   {d2}   |")
    print("|       |\t|       |")
    print("---------\t---------")
    
def game_has_winner(p1, p2):
    if p1 >= 100 or p2 >= 100:
        return True
    else:
        return False

def get_winner(p1, p2):
    if p1 >= 100:
        return f"\n\n\nThe winner is Player 1 with {p1} points!\n\n\n"
    else:
        return f"\n\n\nThe winner is Player 2 with {p2} points!\n\n\n"

#this is our start function
play_game()
#------------------------------------------------------------------------------------------------------------------------------------------------------------
# Grocery


# You will need to modify possibly the save and load functions of your program.

#To submit this, commit your changes to your Python Grocery List Assignment with the description of Grocery Item Added

#code by Finch Stanger

import pickle 

from grocery_item import grocery_item

#this function will allow us to add an item

def add_item(my_list):
    des = input("What is the item to add? ")
    quan = int(input("How much do you need? "))
    my_list.append(grocery_item(d= des, q= quan))

def delete_item(my_list):
    placement = int(input("What is the placement of the item to delete: "))
    #check to make sure the placement is in the list
    if placement >= 1 and placement <= len(my_list):
        print(f"You deleted: {my_list.pop(placement - 1)}")
    
def print_list(my_list):
    print("Your grocery list:\n------------------")
    for i, b in enumerate(my_list):
        print(f"{i+1}- {b}")
    print("----------------")

def sort_list(my_list):
    my_list.sort(key=lambda item: item.get_description())
    print("The grocery list is now sorted alphabetically.")
    
def print_menu():
    print("----------------")
    print("1) Add an item")
    print("2) Delete an item")
    print("3) Print the grocery list")
    print("4) Sort the items")
    print("5) Exit the program")
    print("6) Clear the list")
    print("-------------------")

def save_file(my_list):
    my_file = open("grocery_list.dat", "wb")
    pickle.dump(my_list, my_file)
    my_file.close()


def read_file(my_list):
    read_it = open("grocery_list.dat", "rb")
    try:
        my_list = pickle.load(read_it)
    except:
        my_list = []
    read_it.close()
    print("File loaded")
    print_list(my_list)
    return my_list
      

#main part of the program to create a list and call the functions
items = read_file("grocery_list.dat")
quit = False
while not quit:
    print_menu()
    try:
        response = int(input("Your choice: "))
    except:
        continue
    if response == 1:
        add_item(items)
    elif response == 2:
        delete_item(items)
    elif response == 3:
        print_list(items)
    elif response == 4:
        sort_list(items)
    elif response == 5:
        #save file before exiting 
        save_file(items)
        quit = True
        # open the file in write mode
        # save the grocery list to it
        # close the file
    elif response == 6:
        items.clear()
        save_file(items)
    





#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Repeating guessing

#code by Finch
# we will create a repeating guessing game that allows a user to guess a number until they get it right
# we will also tell the user how many guesses it took them to find the right number
import random 

guess = 0
previous_guesses = []
count = 0
my_number = 0
max = 10
done = False
while guess == 0:
    # this is where they can play it again if they want
    while not done:
        start = random.randint(0,79)
        end = random.randint(start,100)
        my_number = random.randint(start,end)
        while guess!=my_number:
            guess = int(input(f"Guess a number between {start} and {end}: \n\n"))
            count += 1
            if guess == my_number:
                print(f"Congrats! You got it:) It took you {count} guess(es).")
                break
            elif guess < my_number:
                #if outside the metric
                if guess < start:
                    print("You have guessed lower than the metric")
                else:
                    print(f"Close! You're too low.")
            else:
                # if they guess outside the metrics
                if guess > end:
                    print("You have guessed higher than the metric")
                else:
                    print(f"Close! You're too high.")
            # this is where they lose if they hit the max guesses
            if count >= max:
                print(f"You reached the max number of guesses. The number was {my_number}.")
                break
            # # this is where we would remind player the previous guesses
            previous_guesses.append(guess)
            print(f"Guesses so far: {', '.join (map(str,previous_guesses))}")
            # this gives the user another guess
        choice = input("\n\nDo you want to play again (y/n): ")
        if choice == 'y' or choice == 'Y':
            my_number = 0
            count = 0
            previous_guesses = []
            print("\n\n-------------------New Game!----------------------\n\n")
        else:
            done = True
print("Thanks for playing!")


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Personality

#Overview

#Create an interactive Python-based personality quiz that categorizes users into different personality types based on their responses to a series of questions. The quiz should be fun, engaging, and provide meaningful feedback at the end.

    #Questionnaire Design:
        #Create a list of at least 5 questions. Each question should have multiple-choice answers (at least 3-4 options per question).
        #The questions should aim to reveal the user's preferences, habits, or traits (e.g., "How do you handle stressful situations?" or "What's your favorite way to spend a weekend?").

    #Personality Types:
        ##Define 3 to 5 different personality types (e.g., "The Adventurer", "The Thinker", "The Social Butterfly", etc.).
        #Map responses to specific personality types by assigning points or weights to each answer. At the end of the quiz, the user’s answers should determine which personality type they match.

    #Interactive Input:
        #The quiz should be fully interactive, taking input from the user and presenting them with questions one at a time.

   # Quiz Results:
        #After the quiz, display a summary of the user's personality type with a brief description (3-4 sentences) that explains their result.

# code created by Finch Stanger
# purpose: code will send user through a personality test to assess their personality

#variables used
Type_1 = 0 # personality one
Type_2 = 0 # personality two
Type_3 = 0 # personality three
Type_4 = 0 # personality four
Type_5 = 0 # personality five

answer = 0
win = "none"

#Tell the user what this program is
print("Welcome to Finch's Personality Test!")
#Print first question
print("\nQ. 1/5 ~ When someone first meets you, you want them to think you are \n1 - confusing \n2 - useful \n3 - orderly \n4 - scary \n5 - fun + cute")
#take their response
answer = int(input("Answer (1/2/3/4/5): "))
print(f"Answer = {answer}")
# add 1 pt to whichever personality that answer aligns with
if answer == 1:
    Type_1 += 1
if answer == 2:
    Type_2 += 1
if answer == 3:
    Type_3 += 1
if answer == 4:
    Type_4 += 1
if answer == 5:
    Type_5 += 1
# reset the variable just in case
answer = 0
#Print second Question
print("\nQ. 2/5 ~ Your favorite part of the forest is: \n1 - finding funky creatures \n2 - stomping and bush-wacking \n3 - you don't feel like you belong here \n4 - spooking unsuspecting hikers \n5 - making friends and finding pet rocks")
#take their response
answer = int(input("Answer (1/2/3/4/5): "))
print(f"Answer = {answer}")
# add 1 pt to whichever personality that answer aligns with
if answer == 1:
    Type_1 += 1
if answer == 2:
    Type_2 += 1
if answer == 3:
    Type_3 += 1
if answer == 4:
    Type_4 += 1
if answer == 5:
    Type_5 += 1
# reset the variable just in case
answer = 0
#print third question
print("\nQ. 3/5 ~ Your perfect vacation looks like: \n1 - i don't care as long as there isn't anyone else around \n2 - going down a rabit-hole about a special interest \n3 - catching up on projects \n4 - Somewhere bright and sunny, like the beach \n5 - Hanging out with friends, watching movies")
#take their response
answer = int(input("Answer (1/2/3/4/5): "))
print(f"Answer = {answer}")
# add 1 pt to whichever personality that answer aligns with
if answer == 1:
    Type_1 += 1
if answer == 2:
    Type_2 += 1
if answer == 3:
    Type_3 += 1
if answer == 4:
    Type_4 += 1
if answer == 5:
    Type_5 += 1
# reset the variable just in case
answer = 0
# print fourth question
print("\nQ. 4/5 ~ What's your favorite thing to collect: \n1 - bones ( I found them in the woods ) \n2 - Lint and flammables \n3 - Shiny things, silver and jewelry \n4 - feathers and lightbulbs \n5 - friends!")
#take their response
answer = int(input("Answer (1/2/3/4/5): "))
print(f"Answer = {answer}")
# add 1 pt to whichever personality that answer aligns with
if answer == 1:
    Type_1 += 1
if answer == 2:
    Type_2 += 1
if answer == 3:
    Type_3 += 1
if answer == 4:
    Type_4 += 1
if answer == 5:
    Type_5 += 1
# reset the variable just in case
answer = 0
# print fifth question
print("\nQ. 5/5 ~ What your friends might say about you: \n1 - Lonely \n2 - Reliable \n3 - Tidy & clean \n4 - Protective \n5 - Outgoing")
#take their response
answer = int(input("Answer (1/2/3/4/5): "))
print(f"Answer = {answer}")
# add 1 pt to whichever personality that answer aligns with
if answer == 1:
    Type_1 += 1
if answer == 2:
    Type_2 += 1
if answer == 3:
    Type_3 += 1
if answer == 4:
    Type_4 += 1
if answer == 5:
    Type_5 += 1
# reset the variable just in case
answer = 0
print(f"1 = {Type_1} 2 = {Type_2} 3 = {Type_3} 4 = {Type_4} 5 = {Type_5}")
# decide which personality wins
if Type_1 >= 3:
    win = "The Cryptid \nYou are mysterious, unique, and funky. You tend to be a lone wolf, but you have an eye for safe people that value you for who you are. Don't get lost in the story or you'll forget you're the main character."
    print("waiting")
elif Type_2 >= 3:
    win = "The Left Boot \nYou are efficient, thoughtful, and straight-forward. You don't tend to party, but you have a close circle of friends you are loyal to. Don't forget to have some fun: you are more than your strength."
    print("patience")
elif Type_3 >= 3:
    win = "The Salad Fork \nYou are reliable, organized, and observant. You are usually the \'mom friend\' or designated driver, but don't always feel wanted. Don't lose yourself to please others; you will be loved as you love yourself."
    print("loading")
elif Type_4 >= 3:
    win = "The Biblically-acurate Angel \nYou are intimidating, outgoing, and intelligent. You like leaving an impression, but once people get to know you they see you as their safe space. Don't forget to protect your own heart, too."
    print("working")
elif Type_5 >= 3:
    win = "The Hoard of Squishmallows \nYou are fun, loud, and genuine. You tend to have a lot of friends, and can usually spot someone who needs a hug. Don't forget to take time to take care of yourself; your needs are valid."
    print("almost there")
# put code here if i figure out ties
# code if nothing above works (they answer different for e/a question)
else:
    print("Congrats! You're an amalgamation. Or trying to cheat. To get a real personality, try again.\n\n\n")
#print results unless they're all tied
if win != 'none':
    print(f"The result are in! Your personality type is: {win}")
    print("\nThanks for taking the quiz. Come again soon!\n\n\n")



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#GUESSING

#code created by Finch Stanger
#this will be a simple guessing game to guess a number between 1 and 10. You will tell the user if they were too high, too low, or if they guessed correctly.
#we will also use the random library to generate random numbers
import random

user_guess = 0
#can I store previous guesses? this creates an empty list
previous_guesses = []
while user_guess == 0:
    start = random.randint(0,99)
    end = random.randint(1, 100)
    if start < end:
        my_number = random.randint(start,end)

        #prompt for a guess
        user_guess = int(input(f"Guess a number between {start} and {end}: "))
        #tell the player if they were high, low, or correct
        # give guesser multiple tries until they correctly guess
        while user_guess != my_number:
            # if they guess too high
            if user_guess > my_number:
                # if they guess outside the metrics
                if user_guess > end:
                    print("You have guessed higher than the metric")
                else:
                    print(f"Close! You're too high.")
            else: # would be user_guess < my_number
                #if outside the metric
                if user_guess < start:
                    print("You have guessed lower than the metric")
                else:
                    print(f"Close! You're too low.")
            # this is where we would remind player the previous guesses
            previous_guesses.append(user_guess)
            print(f"Guesses so far: {', '.join (map(str,previous_guesses))}")
            # this gives the user another guess
            user_guess = int(input(f"Guess again! A number between {start} and {end}: \n\n"))
            # reward for correct guess
        if user_guess == my_number:
            print("Congrats! That was the number! \n\n")
        #game over

                
#----------------------------------------------------------------------------------------------------------------------------------------------------

#slots

#program by finch stanger
#this program simulates a slot machine

import random #color is weird rn? it says it is not accessed

# global variables for the game
slot_1 = 0
slot_2 = 0
slot_3 = 0
bank = 5.00 # The user starts with $5.00.
choice = 0
pot = 0




#now we will define the FUNCTIONS

#main function
def play_slots( ):
    global slot_1, slot_2, slot_3, bank, choice, pot
    # instructions for player:
    print("Welcome to the slot machine. Each pull costs you 50 cents. You will start with $5.00. If you get two numbers the same, you win your money back. If you get three numbers the same, you win the jackpot and add $100.00 to your money. If none of the numbers are the same, you will lose your 50 cents.")
    while not exit()==True: #  Use a loop
        # allow the user to either "pull" the lever or quit.  
        choice = prompt_user() #local variable, call the prompt user function
        if choice == "1":
            pull_lever()
            #If the user pulls the lever, repeat generating 3 random numbers and either adding or subtracting money to the user.  
            if slot_3 == slot_2 == slot_1:
                print(f"You win the jackpot!!! ${pot:.2f} and $100 added to your balance.")
                bank += 100.00 + pot
            elif slot_1 == slot_2 or slot_1 == slot_3 or slot_2 == slot_3:
                print("You got a match! You win your money back")
            else:
                print("Sorry you lost.")
                bank += -0.50
                # If the user loses all their money, quit automatically. 
                if bank <= 0.00:
                    print("You're out of money. Restart the game to try again.")
                    exit()
                pot += 0.50
                print(f"The pot has ${pot:.2f}.")     
        elif choice == "2":
            # display how much money they have/are getting
            print(f"You have a balance of ${bank: .2f} returned to you.")
            exit()
            #exit() # leave the function
    print("\n\n\tThanks for playing!")


#function to prompt the user to pull the lever again or quit
def prompt_user():
    return input(f"\nYou have ${bank: .2f}. Do you want to Pull (1) or Get your refund (2): ") #1

#function to change the slots 
def pull_lever():
    global slot_1, slot_2, slot_3
    # slots should be randomly chosen from digits 1 through 9    
    slot_1 = random.randint(1,9)
    slot_2 = random.randint(1,9)
    slot_3 = random.randint(1,9)
    display_slots(slot_1, slot_2, slot_3)

#function to print the slots
def display_slots(s1, s2, s3):
    print("\nSlot 1  Slot 2  Slot 3")
    print(f"  -{s1}-     -{s2}-     -{s3}-\n")

def exit():
    global bank, choice
    if choice == "2":
        return True
    if bank <= 0.00:
        return True
#this is our start function
play_slots()

#--------------------------------------------------------------------------------------------------------------