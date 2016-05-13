#Janken Ver 1.0#

import random

def Player1Choice():  
    P1Turn = True
    while P1Turn:
        P1Hand = input("Rock, Paper, Scissors, Lizard, Spock: ")
        if P1Hand == "Rock":
            P1Value = 0
            P1Turn = False
        elif P1Hand == "Spock":
            P1Value = 1
            P1Turn = False
        elif P1Hand == "Paper":
            P1Value = 2
            P1Turn = False
        elif P1Hand == "Lizard":
            P1Value = 3
            P1Turn = False
        elif P1Hand == "Scissors":
            P1Value = 4
            P1Turn = False
        else: print("Please choose a hand:")
    return P1Value

def PlayerMoveName():
    if P1Value == 0: P1Play = "Rock"
    elif P1Value == 1: P1Play = "Spock"
    elif P1Value == 2: P1Play = "Paper"
    elif P1Value == 3: P1Play = "Lizard"
    elif P1Value == 4: P1Play = "Scissors"
    return P1Play

def ThrowDown():
    DeepBlue = random.randrange(0,4)
    if DeepBlue == 0: CPUPlay = "Rock"
    elif DeepBlue == 1: CPUPlay = "Spock"
    elif DeepBlue == 2: CPUPlay = "Paper"
    elif DeepBlue == 3: CPUPlay = "Lizard"
    elif DeepBlue == 4: CPUPlay = "Scissors"
    print("You chose",P1Play)
    print("DeepBlue chose",CPUPlay)
    Outcome = (P1Value - DeepBlue) % 5
    if Outcome == 0:
        print("Stalemate!")
    elif Outcome <= 2:
        print("You win!",P1Play,"beats",CPUPlay)
    else:
        print("You Lose!",CPUPlay,"beats",P1Play)
        
P1Value = Player1Choice() 
P1Play = PlayerMoveName()      
ThrowDown()