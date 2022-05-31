import time
initial = time.time()

k=0
while(k<5):
    print("Snehal")
    time.sleep(3)
    k+=1
print("While loop ran in" ,time.time()-initial,"Seconds")
initial2=time.time()
for i in range(5):
    print("Snehal")
print("for loop ran in" ,time.time()-initial2,"Seconds")
# localtime=time.asctime(time.localtime(time.time()))
# localtime=time.localtime(time.time())
# print(localtime)