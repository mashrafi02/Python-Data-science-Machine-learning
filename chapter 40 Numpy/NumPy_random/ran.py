import numpy as np

numbers = np.random.random(30) * 100
print(numbers, end="\n\n")

numbers1 = np.random.randint(20, 50, size=(2,4,5))
print(numbers1, end="\n\n")

numbers2 = np.random.binomial(6, p=0.5, size=(2,4,5))
print(numbers2, end="\n\n")

numbers3 = np.random.normal(loc=175, scale=15, size=(5,10))
print(numbers3, np.max(numbers3), end="\n\n")

numbers4 = np.random.choice([10,20,53,46,64,67,1,3,6,161,54], size=(10,5))
print(numbers4, end="\n\n")