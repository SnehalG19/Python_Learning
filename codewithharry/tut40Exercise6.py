#stone paper and scizzor
#use random function
# 10
# use while

#using python external and build in modules
# import random

# random_n=random.randint(0,1)
# # print(random_n)
# rand=random.random()
# print(rand)

print("\t\t\t\tWelcome to the stone paper scizzor game")
import random
list={1:"stone",2:"paper",3:"scizzor"}
i=1
R=0
O=0
while i<=10:
    G=random.randint(1,3)
    print("Enter 1 for stone,2 for paper and 3 for scissor")
    U=input("Enter\n")
    print("Opponent entered\n",G)
    if G==1:
        if U==1:
            R=R+0
            O=O+0
            print("Draw")
        elif U==2:
            R=R+1
            O=O+0
            print("You won")
        elif U==3:
            R=R+0
            O=O+1
            print("You lost")
        else:
            print("INVALID ACTION")
    elif G==2:
        if U==1:
            R=R+0
            O=O+1
            print("You lost")
        elif U==2:
            R=R+0
            O=O+0
            print("Draw")
        elif U==3:
            R=R+1
            O=O+0
            print("You won")
        else:
            print("INVALID ACTION")
            continue
    elif G==3:
        if U==1:
            R=R+1
            O=O+0
            print("You won")
        elif U==2:
            R=R+0
            O=O+1
            print("You lost")
        elif U==3:
            R=R+0
            O=O+0
            print("Draw")
        else:
            print("INVALID ACTION")
    print("Your points are",R)
    print("Your oppononts points are",O)
    print("You have ",10-i,"turns left")
    i=i+1



if R>O:
    print("Congrats,You won the game")
elif R<O:
    print("Hard luck! You lost")
else:
    print("Good try!")

if i==10:
    print("Game over")

