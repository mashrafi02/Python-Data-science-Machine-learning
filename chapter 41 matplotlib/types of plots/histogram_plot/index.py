import matplotlib.pyplot as plt
import numpy as np

ages = np.random.normal(21, 2.5, 1000)
# print(ages)

plt.hist(ages, bins=20, cumulative=True)
# you can also define bins with list like bins = [15,18,21,24,28]
plt.show()

