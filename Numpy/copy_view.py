import numpy as np




arr1 = np.array([1,2,3,4])

# Creating copy of the array
arr2 = arr1.copy()

# Creating a copy of array using view
arr3 = arr1.view()

# Changing  the data of index 2 
arr1[2]=5
print(arr1)                         #[1 2 5 4]
print(arr2)                         #[1 2 3 4]
print(arr3)                         #[1 2 5 4]

'''
Here using the copy  function the array is copied to arr2. If we change the arr1 , the copied arr2 is not changed.
But in case of view the copied array is also changed, if the main array is changed.
'''



