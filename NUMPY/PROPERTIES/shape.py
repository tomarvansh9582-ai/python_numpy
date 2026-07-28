"""WHEN WE ARE DEALING WITH THE 
MULTIDIMENTIONAL DATA 
TO CHECK WHAT ITS SHAPE IS 
.shape  is used"""
import numpy as np
arr= np.eye(3)
print(arr)
print(arr.shape)
"""[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
(3, 3) """

#same as for
arr=np.array([[1,2],[4,5],[7,8]])
print(arr)
print(arr.shape)
"""[[1 2]
 [4 5]
 [7 8]]
(3, 2)"""

#same as for
arr=np.array([[[0., 0., 0., 0., 0.],
  [0., 0., 0., 0., 0.]],

 [[0., 0., 0., 0., 0.],
  [0., 0., 0. ,0., 0.]],

 [[0., 0., 0., 0., 0.],
  [0., 0., 0., 0., 0.]]])
print(arr)
print(arr.shape)
#(3, 2, 5)