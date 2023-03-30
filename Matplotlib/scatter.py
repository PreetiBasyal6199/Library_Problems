import matplotlib.pyplot as plt
import numpy as np


a= np.array([2,4,6,8,10])
b= np.array([4,8,12,16,20])

plt.scatter(a,b)

# You can set your own color for each scatter plot with the color or the c argument:
plt.scatter(a,b,c="pink")

# You can even set a specific color for each dot by using an array of colors as value for the c argument:
colors = np.array(["red","green","blue","yellow","pink"])
plt.scatter(a,b,c=colors)

# You can include the colormap in the drawing by including the plt.colorbar() statement:
plt.colorbar()

# You can change the size of the dots with the s argument.
plt.scatter(a,b,s=5)

# You can adjust the transparency of the dots with the alpha argument.
plt.scatter(a,b,alpha=0.3)

plt.show()