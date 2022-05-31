#Health management system
# 3 clients - harry,rohan and hammad
# total6 Files 
# write a function that when executed takes as input client name
# def getdate():
#     import datetime
#     return datetime.datetime.now()
# client = ["Harry","Rohan","Hammad"]
# f1 = open("Harry1.txt","w")
# a=f1.write(input())
# f2 = open("Harry2.txt","w")
# f3 = open("Rohan1.txt","w")
# f4 = open("Rohan2.txt","w")
# f5 = open("Hammad1.txt","w")
# f6 = open("Hammad2.txt","w")
import datetime
def getdate():
    return datetime.datetime.now()

def take(k):
    if k==1:
        c= int(input("enter 1 for exercise and 2 for food\n"))
        if c==1:
            value=input("Type here\n")
            with open("Harry1.txt",'a') as f1:
                f1.write(str([str(getdate())])+":"+value+"\n")
        if c==2:
            value=input("Type here\n")
            with open("Harry2.txt",'a') as f1:
                f1.write(str([str(getdate())])+":"+value+"\n")
        print("succesfully written")
    elif k==2:
        c= int(input("enter 1 for exercise and 2 for food\n"))
        if c==1:
            value=input("Type here\n")
            with open("Rohan1.txt",'a') as f1:
                f1.write(str([str(getdate())])+":"+value+"\n")
        if c==2:
            value=input("Type here\n")
            with open("Rohan2.txt",'a') as f1:
                f1.write(str([str(getdate())])+":"+value+"\n")
        print("succesfully written")
    elif k==3:
        c= int(input("enter 1 for exercise and 2 for food\n"))
        if c==1:
            value=input("Type here\n")
            with open("Hammad1.txt",'a') as f1:
                f1.write(str([str(getdate())])+":"+value+"\n")
        if c==2:
            value=input("Type here\n")
            with open("Hammad2.txt",'a') as f1:
                f1.write(str([str(getdate())])+":"+value+"\n")
        print("succesfully written")
    else:
        print("please enter valid inputs")
print("Health Management system: ")
a=int(input("press 1 for lock the value and 2 for retrieve the value\n"))
if a==1:
    b = int(input("press 1 for Harry,2 for Rohan,3 for Hammad\n"))
    take(b)
else:
    b = int(input("press 1 for Harry,2 for Rohan,3 for Hammad\n"))
    retrieve(b)

