import numpy as np
import sys

list_one = [1,2,3,4]
list_two = [1,2,3,4]

print list_one+list_two

arr1 = np.array(list_one)
arr2 = np.array(list_two)

print(arr1+arr2)

####Memory space#############

l = range(1000)

print (sys.getsizeof(5)*len(l))

arr = np.arange(1000)

print(arr.size*arr.itemsize)

##Fast and convient
SIZE = 1000000
list_one = range(SIZE)
list_two = range(SIZE)

import time
start = time.time()

result = [(x+y) for x,y in zip(list_one,list_two)]

print("pyhton list took :",(time.time()-start)*1000)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

start = time.time()
res = a1+a2

print("pyhton list took :",(time.time()-start)*1000)