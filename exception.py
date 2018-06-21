#Q1
#exception is zero division error
a=3
try:
    if (a<4):
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("cannot divide by 0")


#Q2
#exception is index error
l=(1,2,3)
try:
    print(l[3])
except IndexError:
    print("value out of range ")


#Q3
#An exception

#Q4
'''
-5
a/b result in 0
'''

#Q5
#1. import error
try:
    #import os
    import surbhi
except ImportError:
    print("there is an import error")

#2. value error
try:
    a=int(input("enter no."))
    print(a)
except ValueError:
    print("please enter only integer")

#3. index error
try:
    a=[1,2,3]
    print(a[8])
except IndexError:
    print("number out of range")


#Q6
class AgeTooSmallError(Exception):
    pass
try:
     age=int(input("enter age"))
     print(age)
     if(age<18):
         raise AgeTooSmallError
except AgeTooSmallError:
    print("entered age is less than 18")
