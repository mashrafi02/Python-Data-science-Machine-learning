import numpy as np

array1 = np.array([[1,2,3,4,5],
                   [6,7,8,9,10],
                   [11,12,13,14,15],
                   [16,17,18,19,20]])

# print(array1.shape)

# reshape method --> whatever the argument number is , the multiplication should be equal to the number of elements
print(array1.reshape((5,4)))
print(array1.reshape((10,2)))
print(array1.reshape((20)))
print(array1.reshape((20,1)))
print(array1.reshape((2,5,2)))
print(array1.reshape((2,10,1)))
print(array1.reshape((5,2,2)))


# but reshape method won't change the actual array unless you assign it to the previous array
# if you don't want assign but want to change it directly you can use the resize method and the argument rules are the same as the reshape method

array1.resize((5,4))
print(array1)

# flatten method --> it will give us a 1D copy of the actual array and if we made any change to the copy the actual array won't be affected
print(array1.flatten())

var1 = array1.flatten()
var1[2] = 100
print(var1)
print(array1)

# ravel method --> it will give us a 1D view of the actual array and if we made any change to the view copy the actual array would be affected
print(array1.ravel())

var2 = array1.ravel()
var2[2] = 100
print(var2)
print(array1)

# flat method --> you can make a list with this

print(array1.flat) # it's an object which can be iterate through

var = [v for v in array1.flat]
print(var)
print(type(var))

# tranpose or T method

print(array1.transpose())
print(array1.T)

# swapaxis method --> this is used to do transpose kind of work for higher dimentional arrays

print(array1.swapaxes(0,1))