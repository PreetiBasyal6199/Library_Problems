import matplotlib.pyplot as plt
import numpy as np

'''
Plotting with 2-D array 
'''
x_points=np.array([2,150])
y_points=np.array([4,100])

# plt.plot(x_points,y_points)
# plt.show()


'''
Plotting with 1-D array with additional paramenter marker
The keyword argument marker is to emphasize each point with a specified marker:
'''

y_point2=np.array([2,50,4,150])
# plt.plot(y_point2, marker='o')
# plt.show()

'''
You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:
  Other linestyle are "solid', 'dashed', 'dashdot', 'dotted'"
'''
# plt.plot(y_point2,marker='o',linestyle='dashed')
# plt.show()

'''
Note :      The line style can be written in a shorter syntax:

            linestyle can be written as ls.

            dotted can be written as :.

            dashed can be written as --.
'''


'''
You can use the keyword argument color or the shorter c to set the color of the line:
'''
# plt.plot(y_point2,marker='o',color='r')
# plt.show()

'''
You can use the keyword argument linewidth or the shorter lw to change the width of the line.
'''
plt.plot(y_point2,marker='o',linewidth=20)
plt.show()