import numpy as np

# a1 = np.array([[1,2,3,4,5],
#                [6,7,8,9,10],
#                [11,12,13,14,15],
#                [16,17,18,19,20]])

# np.save("my_array.npy", a1)
# np.savetxt("my_array.csv", a1, delimiter=",")

a = np.load("my_array.npy")
b = np.loadtxt("my_array.csv", delimiter=",")

print(a,b)