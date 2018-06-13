
#Q1
def area(a):
    a=3.14*a*a
    return a
x=int(input("enter radius : "))
print("area of circle is %s "%area(x))


#Q2

def perfect(i):
    sum=0
    for n in range(1,i):
        if(i%n==0):
            sum=sum+n
        n=n+1
    if(sum==i):
        return True

for i in range(1,1001):
    if(perfect(i)==True):
        print("perfect number is %s"%i)
    i=i+1



#Q3
i=1
def table(x,i):
    print(x*i)
    i=i+1
    if(i<=10):
        table(x,i)
table(12,i)


#Q4
n=int(input("enter base "))
p=int(input("enter power raised "))
def power(n,p):
    if(p!=0):
        return(n*power(n,p-1))
    else:
        return 1
print("result is %s"%power(n,p))


#Q5
x=int(input("enter number "))
def factorial(x):
    if(x==1):
        return 1
    else:
        return (x*factorial(x-1))
d={}
d={x:factorial(x)}
print(d)

