import numpy as np


arr1 = np.array([1,2,3,4])

# Creating copy of the array
arr2 = arr1.copy()

# Changing  the data of index 2 
arr1[2]=5
print(arr1)                         #[1 2 5 4]
print(arr2)                         #[1 2 3 4]

'''
Here using the copy  function the array is copied to arr2. If we change the arr1 , the copied arr2 is not changed.
'''

