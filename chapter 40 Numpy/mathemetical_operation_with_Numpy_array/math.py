import numpy as np

a = np.array([1,2,3])
b = np.array((4,5,6))


print(a+b)
print(a-b)
print(a*b)
print(a/b)

a1 = np.array([1,2,3])
b1 = np.array([[1],
               [2]])

print(a1+b1)
print(a1-b1)
print(a1*b1)
print(a1/b1)

# ummm you cannot do any mathemetical operations with different shapes of array

# a2 = np.array([[1,2,3],
#               [4,5,6],
#               [7,8,9]])
# b2 = np.array([[1,2],
#                [2,3]])

# print(a2+b2)
# print(a2-b2)
# print(a2*b2)
# print(a2/b2)


# then we have a lot of mathemetical functions that comes with numpy like sin, cos, tan. arctan, log, log2, log10, sqrt etc
# just see the documentation in the website

print(np.sqrt(a))

