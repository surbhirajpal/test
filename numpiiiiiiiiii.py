import numpy as np
import math

#Q1
a=np.random.random((10,1))
print (a)
m=a.mean()
print("mean is "+str(m))

#Q2
b=np.random.random((20,1))
print(b)
v=b.var()
print("variance is "+str(v))
s=b.std()
print("standard deviaation is "+str(s))

#Q3
a=np.random.random((10,20))
b=np.random.random((20,25))
#a.dtype=np.float64
#b.dtype=np.float64
#print(a*b)
c=np.matmul(a,b)
print(c)
d=np.sum(c)
print("sum of all elements of new matrix is "+str(d))

#Q4
a=np.random.random((10,1))
print(a)
b=[]
for i in range (0,10):
    x=1/(1+math.exp(-(a[i,0])))
    b.append(x)
print(b)









