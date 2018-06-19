import threading
import time


#Q1
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        time.sleep(5)
        print(" sleep time is 5 seconds ")
thread=mythread(1)
thread.start()



#Q2
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        print("number is  ",self.h)
for i in range (1,11):
    thread=mythread(i)
    thread.start()
    time.sleep(1)




#Q3
class mythread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        n=2
        l=(1,2,3,4,5)
        for i in l:
            time.sleep(n)
            print("element is %d"%i)
            n=n+2


thread = mythread("")
thread.start()
thread.join()


#Q4
class mythread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        fact=1
        n=int(input("enter number : "))
        for i in range (1,n+1):
            fact=fact*i
        print("factorial of %d is %d"%(n,fact))
thread = mythread(1)
thread.start()




