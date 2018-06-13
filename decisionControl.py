#Q1
#y%4==0 and y%400==0 or y%100!=0

y=int(input("enter year"))
if(y%4==0):
    print("leap year")
else:
    print("not a leap year")


#Q2
l=int(input("enter length"))
b=int(input("enter breadth"))
if(l==b):
    print("it is a square")
else:
    print("it is rectangle")




#Q3
a=int(input("enter age of person a : "))
b=int(input("enter age of person b :"))
c=int(input("enter age of person c :"))
if(a>b and a>c):
    print("a is oldest")
elif(b>a and b>c):
    print("b is oldest")
elif(c>a and c>b):
    print("c is oldest")
else:
    print("ages of all persons are equal")
if(a<b and a<c):
    print("a is younger")
elif(b<a and b<c):
    print("b is younger")
elif(c<a and c<b):
    print("c is younger")


#Q4
p=int(input("enter number of points scored :"))
if (1<=p<=50):
    print("sorry! no prize this time ")
elif(51<=p<=150):
    print("congratulations! you won a wooden dog")
elif(151<=p<=180):
    print("congratulations! you won a book")
elif(181<=p<=200):
    print("congratulations! you won choclates ")
else:
    print("points can only be upto 200")


#Q5
q=int(input("enter quantity to be purchased : "))
if(q*100>1000):
    p=q*100-(0.10*q*100)
    print("cost is %s" %p)
else:
    print("price is %s"%q*100)
