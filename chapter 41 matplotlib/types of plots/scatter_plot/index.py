import numpy as np
import matplotlib.pyplot as plt


x_values = np.random.random(50) * 100
y_values = np.random.random(50) * 100

plt.scatter(x_values, y_values, c="aqua", s=50, marker="*", alpha=0.8)
plt.show()


