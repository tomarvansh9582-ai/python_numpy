#dtype stands for datatypeof elements of array ex -int64 float64 etc
import numpy as np
arr= np.eye(3)
print(arr)
print(arr.shape)
print(arr.size)
print(arr.ndim)
print(arr.dtype)
#same as for
arr=np.array([['1','2'],['4','5'],['7','8']])
print(arr)
print(arr.shape)
print(arr.size)
print(arr.ndim)
print(arr.dtype)

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