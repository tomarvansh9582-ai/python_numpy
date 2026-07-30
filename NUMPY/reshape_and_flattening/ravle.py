#Flattening: Converting a multi-dimensional array back into a 1D array.

#array.ravel(): Returns a "view" of the original array, meaning changes to the new array will affect the original.


import numpy as np
arr=np.array([[1,2,],[3,4],[5,6]])
print(arr)
print(arr.ravel())