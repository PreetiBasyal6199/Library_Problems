'''
The shape of an array is the number of elements in each dimension.
'''

import numpy as np

arr1 = np.array([1,2,3])

arr2 = np.array([[1,2,3], [4,5,6]])

arr3 = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]], [[13,14,15], [16,17,18]]])

print(arr1.shape)    # (3,)

print(arr2.shape)      # (2,3)

print(arr3.shape)     # (3,2,3)