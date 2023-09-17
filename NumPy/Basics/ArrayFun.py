import numpy as np


ar=np.array([1,2,3,4,5,6])
print(ar)

print(ar.ndim)
#array access 1D array 
print(ar[4])
#array sliceing 
print(ar[2:])
print(ar[:4])
print(ar.dtype)
#it will retrun the shape of array
print(ar.shape)

#array reshapeing
nar=ar.reshape(3,2)
print(nar)

#array concatenate
ar2=np.array([10,9,7,12,13,18])

print(np.concatenate((ar,ar2)))

#horizontal printing like 1d array
print(np.hstack((ar,ar2)))

#vertical printing like 2d Array
print(np.vstack((ar,ar2))) 

#depth equals to hegiht
print(np.dstack((ar,ar2)))

#spliting array into number of division
print(np.array_split(ar,3))

#seraching the element using where 
print(np.where(ar==4))

#serachsort array firt sort and next serach
print(np.searchsorted(ar,4))

print("2D array\n")
ar=np.array([[1,2,3],[4,5,6]])
print(ar)
print(ar.ndim)
#array access 2D Array
print(ar[1,0])
#it will retrun the shape of array
print(ar.shape)





