import numpy as np
import matplotlib.pyplot as plt

langs = ["python", "java", "c#", "go", "c++"]
votes = [50, 5, 10, 15, 23]

plt.pie(votes, labels=langs, autopct="%.2f%%", explode=[0,0.2,0,0,0], pctdistance=0.5, startangle=180)
plt.show()