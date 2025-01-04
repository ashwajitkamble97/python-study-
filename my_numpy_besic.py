"""numPy (numerical python) is a powerfull library for numerical computing in python.
it provide supports with arrays, matrics and a wide range of mathamatical functions.
to operate on these data structures efficiently."""
# ----------------------------------------------------------------------------
# 1. Creating NumPy Arrays
# NumPy provides several ways to create arrays.

# import numpy as np

# Create an array
# arr1 = np.array([1, 2, 3, 4, 5]) #1D arrays
# print(arr1)

# arr2 = np.array([[1,2,3],[4,5,6]]) #2D arrays
# print(arr2)

# #special arrays
# arr3 =np.zeros((10,10)) # arrays of zeros
# print(arr3) 

# arr4 = np.ones((10, 10)) # array od ones
# print(arr4)

# arr5 = np.eye(5) # identity matrix
# print(arr5)

# O/P
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]

# ----------------------------------------------------------------------------
# 2. Array Attributes
# Understanding array properties such as shape, size, and type.

# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)
# print(f"array sizes:-  {arr.size}") # size of an arrays elements 
# print(f"array shapes:-  {arr.shape}") #shape of arrays elements like (2 X 3)
# print(f"array data types:-  {arr.dtype}") # data type of array elemets

# ----------------------------------------------------------------------------
# 3. Array Indexing and Slicing
# Accessing elements in arrays.

# import numpy as np

# arr = np.array([10, 20, 30, 40, 50, 60])
# print(arr)

# print(arr[2]) # single element
# print(arr[1:4]) #slicing array 
# print(arr[::-1]) # reversing array

# ----------------------------------------------------------------------------
# 4. Array Operations
# Element-wise operations such as addition, subtraction, multiplication, and division.

# import numpy as np 

# arr1 = np.array([1,2,3,4,5])
# arr2 = np.array([10,9,8,7,6])
# print(arr1,arr2)

# print(arr1 + arr2) # Element-wise addition
# print(arr1 * arr2) # Element-wise multification
# print(arr1 ** 2) #squreing elemets 

# --------------------------------------------------------------------
# 5. Broadcasting
# Perform operations between arrays of different shapes.

# import numpy as num

# arr = num.array([1,2,3,4,5])
# print(arr)

# a = 2
# print(arr + a) # add 2 to every elemnts in array

# ---------------------------------------------------------------------------------------
# 6. Mathematical Functions
# Apply functions like sum, mean, std, etc.

# import numpy as nn

# arr = nn.array([1,2,3,4,5])
# print(arr)

# print(f"sum :- {nn.sum(arr)}") # sum of array elements
# print(f"mean :- {nn.mean(arr)}") #
# print(f"std :- {nn.std(arr)}") #

# ---------------------------------------------------------------------------------------------
# 7. Linear Algebra
# Perform matrix operations like dot product, transpose, inverse, etc.

# import numpy as np

# arr = np.array([[4,7,2], [3,6,1], [2,5,3]])
# print(arr)

# print(f" transpose :- {arr.T}") # transpose of matrix
# print(f"dot Product :- {np.dot(arr,arr.T)}") # dot product of array and transverse of array
# print(f"inverse :- {np.linalg.inv(arr)}")# inverse of matrix


# ------------------------------------------------------------------------
# 8. Random Numbers
# Generate random values.

# import numpy as np

# arr = np.random.rand(2,3) # generate any random arrays
# print(arr)

# arr = np.random.randn(5) # Standard normal distribution
# print(arr)

# ------------------------------------------------------------------------

# 9. Reshaping and Flattening
# Change the shape of arrays.

# import numpy as np

# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)

# reshaped = arr.reshape((3,2)) # reshaped array
# print(reshaped)

# flattened = arr.flatten() # make array flattend
# print(flattened)

# ---------------------------------------------------------------
# 10. Boolean Indexing and Filtering
# Filter arrays using conditions.

# import numpy as np
# arr = np.array([10,20,30,40,50])

# print(arr)

# fliterArr = arr[arr >= 40] # filter array
# print(fliterArr)

# ------------------------------------------------------------------------------

# 11. Concatenation and Splitting
# Combine or split arrays.

# import numpy as np

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# conca = np.concatenate((a,b)) # concatinate arrays
# print(conca)

# split = np.array_split(conca, 4) # splits array 
# print(split)

# -----------------------------------------------------------------------------
# 12. Saving and Loading
# Save and load arrays.

# import numpy as np

# arr = np.array([10, 20, 30, 40, 50])

# array_saved = np.save("my_array.npy", arr)        # Save array
# loaded_array = np.load("my_array.npy")# Load array
# print(array_saved)
# print(loaded_array)

# ----------------------------------------------------------------------------------------

# 13. Handling Missing Data
# Using np.nan to represent missing values.

# import numpy as np

# arr = np.array([1, 2, np.nan, 4])
# print("Mean ignoring NaN:", np.nanmean(arr))


