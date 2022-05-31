#*args and **kwargs

# def f(a,b):
#     print(a,b)

# f("sally","snehal")

def f(labs,*lab):
    print(labs)
    for items in lab:
        print(items)

har = ["sally","snehal","Sandhya","Shreya","Mayuri"]
labs="Hello Welcome"
f(labs,*har)