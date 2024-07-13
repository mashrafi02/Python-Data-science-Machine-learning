import numpy as np

# for all these methods every time you have to assign them in the previous array otherwise the change won't be permanent

a = np.array([[1,2,3],
              [4,5,6]])

# append method
a= np.append(a, [7,8,9])

print(a)

# insert method
a = np.insert(a, 5, [1,3,9])  # here a is the base array, 5 is the index number of element in a linear array and last part is the array you
                              # want to insert

print(a)

#delete method

print(np.delete(a, 5))
print(np.delete(a, 6))
print(np.delete(a, 7))

# here the number arguments are the index number of a linear array


# if you wnt to delete the entire row or column then do this

b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

# if you give 3rd argument 0 .. it will remove rows.. and the 2nd argument will be the index of rows
print(np.delete(b, 1, 0))
print(np.delete(b, 2, 0))

# if you give 3rd argument 1 .. it will remove columns.. and the 2nd argument will be the index of columns
print(np.delete(b, 0, 1))
print(np.delete(b, 1, 1))