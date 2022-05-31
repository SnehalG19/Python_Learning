#exercise
'''create a dictionary and take input from the user and return the meaning of the 
word from the dictionary'''
dict={"Append":"add to the end ofdocument",
"Remove":"take (something) away",
"list":"number of connected items",
"tuple":"data structure consisting multiple parts"}

print("enter your word")
d1=input()

print("meaning of",d1,"is",dict[d1])