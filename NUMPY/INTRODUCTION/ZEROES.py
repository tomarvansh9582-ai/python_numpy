#IN THIS WE WILL CREATE AN ARRAY OF 0ES
#WITH THE USE OF zeroes(shape)
#shape is dimention magnitud of array whether 
#it is 1d,2d,3d etc


#importing numpy
import numpy as np
#zeros(shape) 1d
arr=np.zeros(3)
print(arr)
#OUTPUT
#[0. 0. 0.]



#zeros(shape) 2d
arr=np.zeros((3,2))
print(arr)
#OUTPUT
#[[0. 0.]
#[0. 0.]
#[0. 0.]]



#zeros(shape) 3d OR MULTI
arr=np.zeros((3,2,5))
print(arr)
#OUTPUT
"""[[[0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]]

 [[0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]]

 [[0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]]]"""