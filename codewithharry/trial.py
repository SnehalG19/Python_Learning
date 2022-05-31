


def getdate():
    import datetime
    return datetime.datetime.now()




def take(k):
    if k==1:
        c=int(input("press 1 for exercise or 2 for food\n"))
        if (c==1):
            value=input("Type here\n")
            with open("Snehal.txt",'a') as f:
                f.write(str([str(getdate())])+":"+value+"\n")
        else:
            value=input("Type here\n")
            with open("Snehal1.txt",'a') as f:
                f.write(str([str(getdate())])+":"+value+"\n")
        print("Succesfully added")
    elif k==2:
        c=int(input("press 1 for exercise or 2 for food\n"))
        if (c==1):
            value=input("Type here\n")
            with open("Sandhya.txt",'a') as f:
                f.write(str([str(getdate())])+":"+value+"\n")
        else:
            value=input("Type here\n")
            with open("Sandhya1.txt",'a') as f:
                f.write(str([str(getdate())])+":"+value+"\n")
        print("Succesfully added")
    elif k==3:
        c=int(input("press 1 for exercise or 2 for food\n"))
        if (c==1):
            value=input("Type here\n")
            with open("Shreya.txt",'a') as f:
                f.write(str([str(getdate())])+":"+value+"\n")
        else:
            value=input("Type here\n")
            with open("Shreya1.txt",'a') as f:
                f.write(str([str(getdate())])+":"+value+"\n")
        print("Succesfully added")
    else:
        print("Only input about Snehal, Sandhya, Shreya")
    
def retrieve(k):
    if k==1:
        c=int(input("press 1 for exercise or 2 for food\n"))
        if (c==1):
            with open("Snehal.txt") as f:
                for i in f:
                    print(i,end="")
        else:
            with open("Snehal1.txt") as f:
                for i in f:
                    print(i,end="")
    elif k==2:
        c=int(input("press 1 for exercise or 2 for food\n"))
        if (c==1):
            with open("Sandhya.txt") as f:
                for i in f:
                    print(i,end="")
        else:
            with open("Sandhya1.txt") as f:
                for i in f:
                    print(i,end="")
    elif k==3:
        c=int(input("press 1 for exercise or 2 for food\n"))
        if (c==1):
            with open("Shraeya.txt") as f:
                for i in f:
                    print(i,end="")
        else:
            with open("Shraeya1.txt") as f:
                for i in f:
                    print(i,end="")
    else:
        print("Only input about Snehal, Sandhya, Shreya")

def again():
    print("Do you want to enter again(print 1 or 0)")
    x=int(input())
    if x==1:
        take(b)
    else:
        retrieve(b)


print("WELCOME TO THE HEALTH MANAGEMENT SYSTEM")
a=int(input("press 1 for lock and 2 for retrieve\n"))
if a==1:
    b=int(input("press 1 for Snehal, 2 for Sandhya and 3 for Shreya\n"))
    take(b)
    again()
else:
    b=int(input("press 1 for Snehal, 2 for Sandhya and 3 for Shreya\n"))
    retrieve(b)
    again()

    

    







