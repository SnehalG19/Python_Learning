#file to basics
'''
"r" - open file for reading -default
"w" - open file for writing
"x" - creates file if not exists
"a" - Add more content to a file
"t" - text mode - default
"b" - binary mode
"+" - read and write

'''
'''qustion of the day
func1()
''' 

from tut23 import function1


def func1(a,b):
    """very important"""
    sum=a+b
    print(sum)

print(func1.__doc__)
