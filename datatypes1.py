l=[]
a=input("enter no")
l.append(a)
print(l)

#q2
l.append("google")
l.append("apple")
l.append("facebook")
l.append("microsoft")
l.append("tesla")
print(l)

#q3
print(l.count("apple"))

#q4
a=[2,5,7,8,4,2,4,6,8,9]
a.sort()
print(a)

#q5
a=[1,5,3,4,2]
a.sort()
b=[9,6,7,8]
b.sort()
c=[]
c=a+b
c.sort()
print(c)

#q6
c.append(10)
print(c)
c.pop()
print(c)

#q7
even=0
odd=0
for i in range(10):
    if i/2==0:
        even = even+1
    else:
        odd = odd+1
print(even)
print (odd)

