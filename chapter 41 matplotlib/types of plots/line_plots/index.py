import numpy as np
import matplotlib.pyplot as plt


years = [2001 + x for x in range(24)]
rolls = [0,0,0,0,0,21,1,13,1,1,67,6,2,3,19,1,161,161,54,54,54,54,54,54]

# print(len(years), len(rolls))

plt.plot(years, rolls, "b--", lw=2)
plt.show()




