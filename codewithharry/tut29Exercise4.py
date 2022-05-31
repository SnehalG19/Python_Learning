#pattern writing
'''input = integer n
boolean = True or False
True n =4
*
**
***
****
4

False n =4
****
***
**
*
'''
print("enter the number")
n=int(input())
print("Type 1 or 0")
b=int(input())
new=bool(b)
if new==True:
    for i in range(0,n+1):
        for j in range(1,i+1):
            print('*',end=" ")
        print()
elif new==False :
    for i in range(n+1,1,-1):
        for j in range(1,i+1):
            print('*',end=" ")
        print()