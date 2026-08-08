#np.delete(): Deletes an element from an array at a specific index, returning a new array.
import numpy as np
array=np.array([1,2,3,4,5,6,7])
print(array)
array=np.delete(array,3)    
print(array)