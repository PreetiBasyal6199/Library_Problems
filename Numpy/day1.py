import numpy as np

# OPERATION FOR CREATING AN ARRAY


array_1 = np.array([1,2,3,4])               # creating a normal  array
array_2 = np.zeros(2)                       # creating an array of size 2 with its elements 0
array_3 = np.ones(2)                         # creating an array of size 2 with its elements 1
array_4 = np.empty(2)                           # initializing an empty array with andom values of size 2
array_5 = np.arange(4)                          #Create an array with a range of elements
array_6 = np.arange(2,9,2)                   #an array that contains a range of evenly spaced intervals. To do this, you will specify the first number, last number, and the step size.
array_7 = np.linspace(0,10,num=5)               #   array([ 0. ,  2.5,  5. ,  7.5, 10. ])
array_8 = np.empty(3,dtype=np.int64)
print(array_1[1])                           # accessing the ith index element of array




# Adding, removing, and sorting elements IN array

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
new_arr = np.sort(arr)
print(new_arr)                          #[1 2 3 4 5 6 7 8]


a= np.array([1,2,3,4])
b= np.array([2,2,2,2])
c=np.concatenate((a,b), axis=0)
print(c)                                        #[1 2 3 4 2 2 2 2]
