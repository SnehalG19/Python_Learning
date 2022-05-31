#f = open("harry.txt",'w')
#a = f.write("snehal is a girl\n")
#f.write("snehal is intelligent\n")
#print(a)
#f.close()


#f = open("harry.txt",'a')
#a = f.write("snehal is a girl\n")
#f.write("snehal is intelligent\n")
#print(a)
#f.close()


#handle read and write and both
f = open ("harry.txt",'r+')
print(f.read())
f.write("bye")