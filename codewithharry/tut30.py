f=open("harry.txt")
print(f.seek(10))
print(f.tell())
print(f.readline())
print(f.readline())
#print(f.tell())
f.close()




"""
tell will tell at what index line is starting
seek can print the line from the index we want

"""