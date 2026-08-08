#import numpy
import numpy as np
array=np.array([1,2,3,4,5,6,7])
#now using import function
array=np.insert(array,4,values=20,axis=0)
print(array)
array2=np.array([[1,2,3],[4,6,8]])
array2=np.insert(array2,1,[6,7,8],axis=0)
print(array2)