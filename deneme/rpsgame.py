
import random


def winner(player1, pleyer2):

    if (player1 == "r" and pleyer2 == "s") or (player1 == "p" and pleyer2 == "r") or (player1 == "s" and pleyer2 == "p"):
        print("You won !!")
    elif player1 ==pleyer2:
        print("You lost !!") 
    else:
        print("It's tie.")

def rps():
    
    l = ["r" , "p", "s"]
    comp = random.choice(l)
    print(comp)

    human = ""

    while not human in l:
        human = input("Rock (r), scissors(s) or paper(p) ??: ").lower()

        if not human in l:
            print("Invalid move. Try again.")

    winner(human,comp)


rps()








    

