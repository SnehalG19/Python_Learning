#exercise 3


print("Welcome to the guess the number game", "You will be provided with only 9 guesses")
print("guess the number from 1 to 100")
n=45
g= 1
while (g<=9):
    print("guess the number ")
    i=int(input())
    if (i<n):
        print("You entered the smaller number, please enter the greater number. ")
    elif (i>n):
        print("you entered the greater number, please enter the smaller number. ")
    else:
        print("Congrats! You have guessed the number correct")
        print(g,"no. of guesses you took to finish.")
        break
    print(9-g,"no. of guesses are left.")
    g= g+1
if (g>9):
    print("Hard luck! Game over")
