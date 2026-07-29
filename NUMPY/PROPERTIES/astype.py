#this property of array is used to convert the datatype of elements of the array
#from 1-> datatype to another-> datatype
import numpy as np
arr=np.array([1,2,3,4,5,6])
print("BEFORE")
print(arr)
print(arr.dtype)
print("AFTER")
arr=arr.astype(float)
print(arr)
print(arr.dtype)
#OUTPUT
"""BEFORE
[1 2 3 4 5 6]
int64
AFTER
[1. 2. 3. 4. 5. 6.]
float64"""