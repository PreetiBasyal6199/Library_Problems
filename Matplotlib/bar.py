import matplotlib.pyplot as plt
import numpy as np



a=np.array([2,4,6,8,10])
b=np.array([4,8,12,16,20])

# You can use the bar() function to draw bar graphs:
plt.bar(a,b)

# use the barh() function for horizontal bars
plt.barh(a,b)

# The bar() and barh() take the keyword argument color to set the color of the bars:
plt.barh(a,b,color="red")

# Specifying the width of the bar
plt.bar(a,b,width=1)

# The barh() takes the keyword argument height to set the height of the bars:
plt.barh(a,b,height=1)


plt.show()