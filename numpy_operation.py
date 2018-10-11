import numpy as np
#a=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
a=np.arange(15).reshape(3,5)
#b=np.arange(30)
#print(b)
print(a)
print(a.ndim)#it will show the dimension of array
print(a.shape)#it will show the r*c(row*column) of your array
print(a.dtype.name)
print(a.itemsize)
