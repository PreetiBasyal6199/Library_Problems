import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([2,50,100])
y_points = np.array([5,75,40])


plt.plot(x_points,y_points)

#you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.
plt.xlabel("Age")
plt.ylabel("Weight")

# You can use the title() function to set a title for the plot.
plt.title("Age-Weight Comparision data")

# you can use the grid() function to add grid lines to the plot.
plt.grid()

# You can use the axis parameter in the grid() function to specify which grid lines to display.
plt.grid(axis="x")

# You can also set the line properties of the grid, like this: grid(color = 'color', linestyle = 'linestyle', linewidth = number).
plt.grid(color='red', linestyle='dotted')
plt.show()