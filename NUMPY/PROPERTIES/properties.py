import numpy as np
arr=np.array([1,2,3,4,5,6])
arr2=np.full((3,3),7)
print(arr, "\n",arr2)
#operations
print("\n\n for arr")
print(arr+1)#[2 3 4 5 6 7]
print(arr/2)#[0.5 1.  1.5 2.  2.5 3. ]
print(arr%10)#[1 2 3 4 5 6]
print(arr**2)#[ 1  4  9 16 25 36]
print(arr*2)#[ 2  4  6  8 10 12]
print("\n\n\n for arr2")
print(arr2+1)#
print(arr2/2)#
print(arr2%10)#
print(arr2**2)#
print(arr2*2)#
"""[[8 8 8]
 [8 8 8]
 [8 8 8]]
[[3.5 3.5 3.5]
 [3.5 3.5 3.5]
 [3.5 3.5 3.5]]
[[7 7 7]
 [7 7 7]
 [7 7 7]]
[[49 49 49]
 [49 49 49]
 [49 49 49]]
[[14 14 14]
 [14 14 14]
 [14 14 14]]"""