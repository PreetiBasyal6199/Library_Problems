import numpy as np

'''
Concatenating two arrays into one array
'''
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

arr3 = np.concatenate((arr1,arr2))

print(arr3)                     #       [1 2 3 4 5 6 7 8]


'''
Concatenate 2-D arrays into one array
'''

arr4 = np.array([[1, 2], [3, 4]])

arr5 = np.array([[5, 6], [7, 8]])

arr6 = np.concatenate((arr4,arr5), axis=1)              #[[1 2 5 6] [3 4 7 8]]
arr7 = np.concatenate((arr4,arr5), axis=0)              #[[1 2][3 4][5 6][7 8]]
arr8 = np.stack((arr4,arr5), axis=1)              #[[1 2 5 6] [3 4 7 8]]

print((arr6))
print((arr7))
print(arr8)
