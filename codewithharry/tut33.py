#Global variable


# l=10 #Global variable - it can use many function as it want
# def funct1(n):
#     #l=5  #local variable
#     m=8 #local variable- Can be used only inside the function, if it 
#     #is called outside of the function it'll throw an error
#     global l
#     l=l+45
#     print(l)
#     print(n,"I have printed")

# funct1("Good job")
# print(l)    

x=48
def snehal():
    x=45
    def sam():
        global x
        x=12
    print("before calling x", x)
    sam()
    print("after calling x", x)
#print(x)  if print before function it'll give global value from outside function
snehal()
#print(x)  if print before function it'll give global value from inside function
