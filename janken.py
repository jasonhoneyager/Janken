#Janken Ver 2.0#

def Player1Choice():  
    P1Turn = True
    while P1Turn:
        print("Player 1")
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

def Player1MoveName():
    if P1Value == 0: P1Play = "Rock"
    elif P1Value == 1: P1Play = "Spock"
    elif P1Value == 2: P1Play = "Paper"
    elif P1Value == 3: P1Play = "Lizard"
    elif P1Value == 4: P1Play = "Scissors"
    return P1Play

def Player2Choice():  
    P2Turn = True
    while P2Turn:
        print("Player 2")
        P2Hand = input("Rock, Paper, Scissors, Lizard, Spock: ")
        if P2Hand == "Rock":
            P2Value = 0
            P2Turn = False
        elif P2Hand == "Spock":
            P2Value = 1
            P2Turn = False
        elif P2Hand == "Paper":
            P2Value = 2
            P2Turn = False
        elif P2Hand == "Lizard":
            P2Value = 3
            P2Turn = False
        elif P2Hand == "Scissors":
            P2Value = 4
            P2Turn = False
        else: print("Please choose a hand:")
    return P2Value

def Player2MoveName():
    if P2Value == 0: P2Play = "Rock"
    elif P2Value == 1: P2Play = "Spock"
    elif P2Value == 2: P2Play = "Paper"
    elif P2Value == 3: P2Play = "Lizard"
    elif P2Value == 4: P2Play = "Scissors"
    return P2Play

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
        
def Showdown():
    print("Player 1 chose",P1Play)
    print("Player 2 chose",P2Play)
    Outcome = (P1Value - P2Value) % 5
    if Outcome == 0:
        print("Stalemate!")
    elif Outcome <= 2:
        print("Player 1 wins!",P1Play,"beats",P2Play)
    else:
        print("Player 2 wins!",P2Play,"beats",P1Play)
    
def Setup():
    print("Championship Janken Tournament Edition")
    Players = int(input("How many players? 1-2 "))
    if Players == 1:
        Multi = False
    elif Players == 2:
        Multi = True
    return Multi

def Retry():
    Continue = input("Play Again? Y/N: ")
    if Continue in ("N", "n", "No", "no", "NO", "nO"):
        Game = False
        return Game
#################################################################
import random
        
Multi = Setup()        
        
while Multi == False:
    P1Value = Player1Choice() 
    P1Play = Player1MoveName()      
    ThrowDown()
    Game = Retry()
    if Game == False:
        break
    
while Multi == True:
    P1Value = Player1Choice() 
    P1Play = Player1MoveName()
    P2Value = Player2Choice() 
    P2Play = Player2MoveName()
    Showdown()
    Game = Retry()
    if Game == False:
        break