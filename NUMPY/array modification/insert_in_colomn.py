import numpy as np
array=np.array([[1,2,3],[4,5,6]])
#now using import function
new_array=np.insert(array,1,[7,8],axis=1)
print("new array")
print(new_array)