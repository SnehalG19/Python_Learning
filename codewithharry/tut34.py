# def print2(str1):
#     # return  "This is " + str1
#     # print2(str1)
#     print("This is " + str1)

# print2("harry")

# def factorial_iterative(n):
#     fac=1
#     for i in range (n):
#         fac = fac * (i+1)
#     return fac
# n= int(input("Enter the number\n"))
# print("Factorial using factorial iterative is ",factorial_iterative(n))

# def factorial_recurssive(n):
#     if n ==1:
#         return 1
#     else:
#         return n * factorial_recurssive(n-1)
# n= int(input("Enter the number\n"))
# print("Factorial using factorial recursive is ",factorial_recurssive(n))

def fabinacci(n):
    if n==1:
        return 0
    elif n ==2:
        return 1
    else:
        return fabinacci(n-1) + fabinacci (n-2)
n = int(input())
print(fabinacci(n))