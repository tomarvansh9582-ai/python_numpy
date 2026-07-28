#this propersty ofarray shows total no of items in data set
import numpy as np
arr= np.eye(3)
print(arr)
print(arr.shape)
print(arr.size)

#same as for
arr=np.array([[1,2],[4,5],[7,8]])
print(arr)
print(arr.shape)
print(arr.size)
"""[[1 2]
 [4 5]
 [7 8]]
(3, 2)
"""
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

"""[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
(3, 3)
9
[[1 2]
 [4 5]
 [7 8]]
(3, 2)
6
[[[0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]]

 [[0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]]

 [[0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]]]
(3, 2, 5)
30"""