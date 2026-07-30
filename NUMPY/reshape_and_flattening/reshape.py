#Reshaping: Changing the dimensions of an array without changing its data.

#array.reshape(rows, columns): Reshapes a 1D array into a 2D array, for example. The total number of elements must remain the same.
import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr.reshape(3,2))
arr2=arr.reshape(3,2)
print(arr2)
"""[[1 2]
 [3 4]
 [5 6]]"""
#array.flatten(): Returns a "copy," so the original array remains unchanged.
arr2=arr.flatten()
print(arr2)