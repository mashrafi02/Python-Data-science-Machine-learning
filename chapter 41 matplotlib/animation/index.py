import numpy as np
import matplotlib.pyplot as plt
import random

head_tails = [0,0]

for _ in range(1000000):
    head_tails[random.randint(0,1)] += 1
    plt.bar(["Head", "Tails"], head_tails, color=["red", "aqua"])
    plt.pause(0.000001)

plt.show()