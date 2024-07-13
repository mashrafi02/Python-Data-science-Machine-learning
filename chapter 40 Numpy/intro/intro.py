import numpy as np

# basic numpy array are like python lists
# it's written in C in behind the scenes

arra1 = np.array([1,2,3,4,5])
print(arra1) #arrays are seperated by spaces insted of commas like in lists
print(type(arra1))

# you can do basic operations like indexing, slicing, change values with indexing like python lists

print(arra1[3])
print(arra1[2:4])
print(arra1[:-2])
print(arra1[::-1])

arra1[2] = 7
print(arra1)




