#this property detrmine their no of dimensions of arrays 
import numpy as np
arr= np.eye(3)
print(arr)
print(arr.shape)
print(arr.size)
print(arr.ndim)

#same as for
arr=np.array([[1,2],[4,5],[7,8]])
print(arr)
print(arr.shape)
print(arr.size)
print(arr.ndim)

#same as for
arr=np.array([[[0., 0., 0., 0., 0.],
  [0., 0., 0., 0., 0.]],

 [[0., 0., 0., 0., 0.],
  [0., 0., 0. ,0., 0.]],

 [[0., 0., 0., 0., 0.],
  [0., 0., 0., 0., 0.]]])
print(arr)
print(arr.shape)
print(arr.size)
print(arr.ndim)
"""[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
(3, 3)
9
2
[[1 2]
 [4 5]
 [7 8]]
(3, 2)
6
2
[[[0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]]

 [[0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]]

 [[0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]]]
(3, 2, 5)
30
3"""

#where 1--> 1 dimension
#      2--> 2 dimension and so on