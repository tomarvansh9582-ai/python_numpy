#in indexing we got to know how to access element within the array 
#same as string in array can be indexed both +tve and -ve way
#[1,2,3,4,5] where i=0 to i=4 and -ve -4 to -1
import numpy as np
arr=np.array([1,2,3,4,5,6])
#to access 3
print(arr[2])#OUTPUT:-3
#to access 5
print(arr[4])#OUTPUT:-5


#same as for negative indexing
#to access last element of array
print(arr[-1])
#to access 2nd last element of array
print(arr[-3])

# for 2 d array 
#array[row,column]