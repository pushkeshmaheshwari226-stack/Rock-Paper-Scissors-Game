# making rock paper and scissor 

import random


computer=random.choice([-1,0,1])

print("'R' for Rock or 'P' for Paper or 'S' for Scissor")
humanstr=input("Enter Your Choice:- ").upper()
humandict={"R":-1,"P":0,"S":1}
reversedict={-1:"Rock",0:"Paper",1:"Scissor"}

if humanstr in humandict:
    human=humandict [humanstr]

    print(f"Your choice is:- {reversedict[human]} \n Computer choice is:- {reversedict[computer]}")

    if(computer == human):
        print("IT'S A DRAW !")
    
    elif(human ==-1 and computer==1 or human ==0 and computer==-1 or human ==1 and computer==0 ):
        print("YAAAAA!,YOU WIN !")
    
    else:
        print("OPPS,YOU LOSE !")

else:
    print("Invalid input , Please enter 'R','P' OR 'S' ")