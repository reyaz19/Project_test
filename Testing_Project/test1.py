import numpy as np

# Creating a rank 1 Array
arr = np.array([1, 2, 3])
print("Array with Rank 1: ", arr)

arr_1 = np.array([])
print(arr_1)

# Creating a rank 2 Array
list_1 = [1, 2, 3]
print(list_1)
list_2 = [4, 5,6]
print(list_2)
arr = np.array([list_1, list_2])
print("Array with Rank 2: \n", arr)

# Creating an array from tuple
arr = np.array((1, 3, 2))
print("\nArray created using passed tuple:\n", arr)
