# import numpy
import numpy as np
import random

# create a list with random numbers
my_list = [random.randint(0, 1000) for _ in range(10)]

# convert the list to an array
my_array = np.array(my_list)

# print the array
print('Array:', my_array)
