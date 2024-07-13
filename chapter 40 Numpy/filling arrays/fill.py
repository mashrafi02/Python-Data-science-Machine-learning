import numpy as np

# full function --> give the shape of your desired array and the thing you want to fill with

array1 = np.full((5,2,3), "smash")
print(array1)

# zeroes function --> just give the shape of the array and the array will be filled with zeroes

array2 = np.zeros((5,2,3))
print(array2)

# ones function --> just give the shape of the array and the array will be filled with ones

array3 = np.ones((5,2,3))
print(array3)

# empty function --> just give the shape of the array and the array will be filled with memory spaces instead of values

array4 = np.empty((5,1,2))
print(array4)

# if you want to create some x or y values use arange  function

x_values = np.arange(0,1000,5) # here 0 is starting value, 1000 is stopping value, 5 is step argument
print(x_values)

# Or you can use linspace function

y_values = np.linspace(0,1000,50) # here 0 is starting value, 1000 is stopping value, 50 is how many values you want
print(y_values)

# Nan --> Not a number and inf --> infinity

print(np.nan)
print(np.inf)

print(np.sqrt(-1))
print(np.array([10]) / 0)

print(np.isnan(np.nan))
print(np.isinf(np.inf))

print(np.isnan(np.sqrt(-1)))
print(np.isinf(np.array([10]) / 0))