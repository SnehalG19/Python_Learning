n=60
i=int(input("Enter the grade"))
if i<38:
    print("student has failed")
elif 38<i<100:
    i=i+5-(i%5)
    print("student is passed with",i)
else:
    print("grade is not valid")
