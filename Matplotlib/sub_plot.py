import matplotlib.pyplot as plt
import numpy as np

'''
The subplot() function takes three arguments that describes the layout of the figure.
'''

# Plot1
x= np.array([2,6,12,20])
y =np.array([4,9,6,18])

# plt.subplot(1,2,1)          
#the figure has 1 row, 2 columns, and this plot is the first plot.
plt.subplot(2,1,1)   
#the figure has 1 row, 2 columns, and this plot is the first plot.

plt.title("Figure1")      
plt.plot(x,y)

# Plot2
x= np.array([1,5,10])
y= np.array([10,5,1])

# plt.subplot(1,2,2)
#the figure has 1 row, 2 columns, and this plot is the second plot.
plt.subplot(2,1,2)
plt.title("Figure1")      
#the figure has 1 row, 2 columns, and this plot is the second plot.

plt.plot(x,y)
# You can add a title to the entire figure with the suptitle() function:
plt.suptitle("All Figures")
plt.show()