'''#index of string starts from 0
str='My School'
print(len(str))# wil, print length
print(str[0:3])# will write0,1,2th letters
print(str[0:3:2])#print alternative letters 
print(str[0:3:2])#print by leaving alternative 2 letters
print(str[0:])#will write whole string
print(str[:5])#will write only upto that index
print(str[-1:-5:]) #index will count from end but negativ index starts from 1 
print(str[::-1])#will make string end to start'''

str='My School'
print(str.isalnum())
print(str.isalpha())
print(str.endswith("School"))
print(str.count("o"))
print(str.capitalize())
print(str.find("oo"))
print(str.lower())
print(str.upper())
print(str.replace("oo", "rr"))