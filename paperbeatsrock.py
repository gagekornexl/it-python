import random
from banner import banner

banner("Rock,Paper,Scissors","Gage")
print ("We are going to play Rock, Paper, Scissors. The first to win two out of three rounds is the winner.")

def choose():
    print ("1. Rock")
    print ("2. Paper")
    print ("3. Scissors")
    player_choice = int(input("What is your choice?"))
    return player_choice


player_score = 0
computer_score = 0

while player_score < 2 and computer_score < 2:
    player_choice = int(choose())
    comp_choice = random.randint(1,3)

    if player_choice == 1:
        if comp_choice == 1:
            print ("You chose rock the computer chose rock its a tie")
        if comp_choice == 2:
            print ("You chose rock the computer chose paper computer wins")
            computer_score = computer_score + 1
        if comp_choice == 3:
            print ("You chose rock the computer chose scissors you win")
    if player_choice == 2:
        if comp_choice == 1:
            print ("You chose paper the computer chose paper its a tie")
        if comp_choice == 2:
            print ("You chose paper the computer chose sissors computer wins")
        if comp_choice == 3:
            print ("You chose paper the computer chose rock you win")
    if player_choice == 3:
        if comp_choice == 1:
            print ("You chose scissors the computer chose scissors its a tie")
        if comp_choice == 2:
            print ("You chose scissors the computer chose rock computer wins")
        if comp_choice == 3:
            print ("You chose scissors the computer chose paper you win")


