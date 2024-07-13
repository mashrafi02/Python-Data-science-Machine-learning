import numpy as np
import matplotlib.pyplot as plt

x = np.arange(100)

fig, axis = plt.subplots(2,2)


fig.suptitle("Four plots")


axis[0,0].plot(x, np.sin(x))
axis[0,0].set_title("Sine wave")
axis[0,0].set_xlabel("values of x")
axis[0,0].set_ylabel("values of sin(x)")


axis[0,1].plot(x, np.cos(x))
axis[0,1].set_title("Cosine wave")
axis[0,1].set_xlabel("values of x")
axis[0,1].set_ylabel("values of cos(x)")


axis[1,0].plot(x, np.random.random(100))
axis[1,0].set_title("Random Function")
axis[1,0].set_xlabel("values of x")
axis[1,0].set_ylabel("values of y")


axis[1,1].plot(x, np.log(x))
axis[1,1].set_title("Log wave")
axis[1,1].set_xlabel("values of x")
axis[1,1].set_ylabel("values of log(x)")

plt.tight_layout()   # for avoiding overlapping texts
plt.show()