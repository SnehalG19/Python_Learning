#function and docstring

'''a=9
b=4
c= sum((a,b))  #built in function'''

def function1 (a,b):
    print("You are in function 1",a+b)

def function2 (a,b):
    """This is a function which will calculate average of two numbers"""
    average=(a+b)/2
    #print(average)
    return average

#
print(function2.__doc__)
