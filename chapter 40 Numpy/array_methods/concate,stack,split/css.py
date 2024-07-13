import numpy as np

array1 = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

array2 = np.array([[11,12,13,14,15],
                   [16,17,18,19,20]])

# concatinate
array = np.concatenate((array1, array2), axis=0) # axis 0 means it'll concatinate row wise
print(array)

aray = np.concatenate((array1, array2), axis=1)
print(aray)


# stack
a1 = np.stack((array1,array2))
print(a1)

# vstack --> does same work as axis = 0
a2 = np.vstack((array1,array2))
print(a2)

# hstack --. does same work as axis = 1
a3 = np.hstack((array1,array2))
print(a3)


# split
print(np.split(array, 2, axis=0))
print(np.split(array, 4, axis=0))

print(np.split(array, 5, axis=1))
