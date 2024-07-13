import numpy as np

array1 = np.array([[1,2,3],
                   [4,5,6]]) #it's a 2 dimentional array
print(array1)

array2 = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]]) #it's a 3 dimentional array
print(array2,"\n")

array3 = np.array([[[1,2,3], 
                    [4,5,6],
                    [7,8,9]],
                   [[1,3,5],
                    [2,4,6],
                    [1,2,7]]]) #it's a2 times deep 3 dimentional array
print(array3)



# calling elements from multidimention arrays

print(array1[1,2])
print(array2[0,1])
print(array3[1,2,2])

# u can also call like this

print(array1[0][2])
print(array3[1][2][0])


# ######################################################## array attirbutes ################################################

# shape

print(array1.shape)
print(array2.shape)
print(array3.shape)

# size

print(array1.size)
print(array2.size)
print(array3.size)

# dimention

print(array1.ndim)
print(array2.ndim)
print(array3.ndim)

# types

print(array1.dtype)
print(array2.dtype)
print(array3.dtype)