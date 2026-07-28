import numpy as np
#just lies zeros() and ones() it creates a default array but with user defined or coder defind value
arr=np.full((3),7)
print(arr)
# 1d
#[7 7 7] :-output
arr=np.full((2,3),7)
print(arr)
"""[[7 7 7]
 [7 7 7]] :- output"""
arr=np.full((3,3,2),7)
print(arr)
"""[[[7 7]
  [7 7]
  [7 7]]

 [[7 7]
  [7 7]
  [7 7]]

 [[7 7]
  [7 7]
  [7 7]]]  :-output"""