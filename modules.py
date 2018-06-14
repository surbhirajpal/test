#Q1
'''
TIME TUPLE-
We represent time in a way that’s easy for us to understand. However, Python stores it in tuples.
These python tuples are made of nine numbers.
Index	 Field	            Domain of Values
0	     Year (4 digits)	Ex.- 1995
1	     Month	            1 to 12
2	     Day	            1 to 31
3	     Hour	            0 to 23
4	     Minute	            0 to 59
5	     Second	            0 to 61 
6	     Day of Week	    0 to 6 (Monday to Sunday)
7	     Day of Year	    1 to 366
8	     DST	            -1,0,1
'''

import datetime
import time
from datetime import date
#Q2
print("local time is")
print(time.asctime(time.localtime()))


#Q3
d=datetime.date.today()
print("current month is %s"%d.month)

#Q4
t=time.gmtime()
w=(t.tm_wday)
if(w==0):
    print(" day is monday")
if(w==1):
    print("day is tuesday")
if(w==2):
    print("day is wednesday")
if(w==3):
    print("day is thursday")
if(w==4):
    print("day is friday")
if(w==5):
    print("day is saturday")
if(w==6):
    print("day is sunday")


#Q5
t='2018/01/20'
d=(datetime.datetime.strptime(t,"%Y/%m/%d"))
print("date is %s"%d.day)

#Q6
t=time.localtime()
print(time.asctime(time.localtime()))
print(t.tm_hour ,t.tm_min ,t.tm_sec)

#Q7
import math
a=int(input("enter a number "))
print(math.factorial(a))

#Q8
a=int(input("enter first number "))
b=int(input("enter second number "))
print(math.gcd(a,b))






