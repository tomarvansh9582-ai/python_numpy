#JUST LIKE ZER0S CREATE ARRAY OF ZEROS ONES CREATE OF 1.0
#IN THIS WE WILL CREATE AN ARRAY OF 0ES
#WITH THE USE OF ones(shape)
#shape is dimention magnitud of array whether 
#it is 1d,2d,3d etc


#importing numpy
import numpy as np
#ones(shape) 1d
arr=np.ones(3)
print(arr)
#OUTPUT
#[1. 1. 1.]



#ones(shape) 2d
arr=np.ones((3,2))
print(arr)
#OUTPUT
#[[0. 0.]
#[0. 0.]
#[0. 0.]]



#ones(shape) 3d OR MULTI
arr=np.ones((3,2,5))
print(arr)
#OUTPUT
"""[[[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]

 [[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]

 [[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]]"""