import numpy as np

# Slicing in 1 dimensional array

arr1=np.array([1,2,3,4,5,6])

# array_name[start:end]
print(arr1[1:5])                            #[2,3,4,5]
print(arr1[4:])                             # [5 6]
print(arr1[1:5:2])                          # [2,4]
print(arr1[-3:-1])                          #[4,5]
print(arr1[::2])                            #[1,3,5]


# Slicing in 2 dimensional array
arr2= np.array([[1,2,3,4],[5,6,7,8]])

#From the second element, slice elements from index 1 to index 4 (not included):

print(arr2[1, 1:3])                                         #[6,7]            


#From both elements, return index 2:

print(arr2[0:2, 2])                     #[3,7]


#From first element , return index 1

print(arr2[0:1, 1])                     # [2]


#  From both elements, slice index 1 to index 3 (not included), this will return a 2-D array:

print(arr2[0:2, 1:3])               #[[2,3], [6,7]]
