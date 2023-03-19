# Creating numpy array of different dimensions

import numpy as np

# Numpy array of 0 dimension
dim0=np.array(20)
print(dim0.ndim)

#Numpy array of 1 dimension
dim1=np.array([1,2,3,4])
print(dim1.ndim)

#Numpy array of 2 dimension
dim2= np.array([[1,2,3], [4,5,6]])
print(dim2.ndim)

#Numpy array of 3 dimension
dim3 = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]], [[13,14,15], [16,17,18]]])
print(dim3[2,1,0])                  #7
print(dim3.ndim)

