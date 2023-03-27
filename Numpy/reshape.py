import numpy as np


arr1 = np.array([1,2,3,4,5,6])
copy_arr = arr1.copy()

'''
Converting 1 dimensional array into two dimensional array
'''

arr2 = copy_arr.reshape(2,3)

print(np.ndim(arr2))                # 2

'''
Converting 1 dimsional array into three dimensional array
'''

arr3 = arr1.reshape(3,2,1)

print(np.ndim(arr3))


'''
Convert the following 1-D array with 12 elements into a 3-D array.
'''
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

arr4 =  arr.reshape(3, 2,2)

print(np.ndim(arr4))


'''
Convert the following 1-D array with 9 elements into a 2-D array.
'''

arr5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

newarr = arr5.reshape(3, 3)

print(np.ndim(newarr))       #2

