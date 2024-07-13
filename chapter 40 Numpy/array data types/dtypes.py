import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [1,3,6,9]])

print(type(array))
print(array.dtype)

array1 = np.array([[1,2,3],
                  [5,"hello",7],
                  [1,3,6]])

print(type(array1))

print(array1.dtype) # now it's consider the array elements as a character which is less than or equal to 11

print(array1[0,1].dtype)

print(type(array1[0,1])) # it's a numpy string not a numpy int32

# because we have included a string in the array, the other elements also becomes a numpy string
# but we can schnge the dtype if we write the a number in int form instead of letter form


array2 = np.array([[1,2,3],
                  [5,"5",7],
                  [1,3,6]], dtype="int32")

print(array2.dtype)

print(array2[0,1].dtype)
print(array2[0][1].dtype)

print(type(array2[0,1]))

# you can change the dtype in any data type as long as all the elements are numerically same

# float type

array3 = np.array([[1,2,3],
                  [5,"5",7],
                  [1,3,6]], dtype="float32")

print(array3.dtype)

print(array3[0,1].dtype)
print(array3[0][1].dtype)

print(type(array3[0,1]))


# string type

array4 = np.array([[1,2,3],
                  [5,"5",7],
                  [1,3,6]], dtype="<U7")

print(array4.dtype)

print(array4[0,1].dtype)
print(array4[0][1].dtype)

print(type(array4[0,1]))


# if you inlcude a data that is not premitive like dictionary the array will turn into a object and this time dtype attribute won't 
# work. and every number elements will be considerd as an int data type not a int32


d = {"1":"A"}

array5 = np.array([[1,2,3],
                  [5,d,7],
                  [1,3,6]])

print(array5.dtype)

print(type(array5[0,1]))
print(type(array5[0][1]))




