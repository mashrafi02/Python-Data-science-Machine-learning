import numpy as np
import matplotlib.pyplot as plt


ax = plt.axes(projection="3d")

x = np.arange(-5,5, 0.1)
y = np.arange(-5,5, 0.1)

X, Y = np.meshgrid(x,y)
Z = np.sin(X) * np.cos(Y)

ax.plot_surface(X,Y,Z, cmap="Spectral", )
ax.set_title("3D line Plot")
ax.set_xlabel("Test")
ax.view_init(azim=0, elev=90)


plt.show()
