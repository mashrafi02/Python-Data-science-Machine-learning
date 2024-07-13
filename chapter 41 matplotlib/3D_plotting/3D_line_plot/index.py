import numpy as np
import matplotlib.pyplot as plt


ax = plt.axes(projection="3d")

x = np.arange(0,50, 0.1)
y = np.sin(x)
z = np.cos(x)

ax.plot(x,y,z)
ax.set_title("3D line Plot")
ax.set_xlabel("Test")


plt.show()
