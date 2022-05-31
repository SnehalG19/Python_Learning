print("enter num1")
num1 = input()
print("enter num2")
num2 = input()
try:
    print(int(num1)+int(num2))   #if error occurs it will ignore it
except Exception as e:
    print(e)

print("very important")