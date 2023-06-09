import numpy as np


'''
Iterating over a 1-D array
'''
arr1 = np.array([1,2,3,4])
for x in arr1:
    print(x)     # returna 1 2 3 4


'''
Iterating over a 2-D array
'''

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
for x in arr2:
    print(x)            # returns [1,2,3] [4,5,6] [7,8,9]


'''
Iterating over a 3-D array  ; returns a 2-D array in each iteration
'''
arr3 = np.array([[[1,2,3],[4,5,6]], [[7,7,9],[10,11,12]],[[13,14,15],[16,17,18]]])
for x in arr3:
    print(x)                # returns [[1,2,3],[4,5,6]]       [[7,7,9],[10,11,12]]   [[13,14,15],[16,17,18]]


'''
Iteration using nditer() function
'''

for y in np.nditer(arr3):
    print(y)

for z in np.nditer(arr2):
    print(z)                    # 1 2 3 4 5 6 7 8 9

'''
Iterationg over the arrays with index too
'''
for u,v in np.ndenumerate(arr2):
    print(u,v)                     # (0, 0) 1 (0, 1) 2 (0, 2) 3 .......................