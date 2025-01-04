# Basic Array Creation and Properties (20 Questions)
# -----------------------------------------------------------------------------------------------
#     1. Create a 1D NumPy array of numbers from 1 to 10.
import numpy as np

# arr = np.arange(1,11) # create arrays
# print(arr)
# # -----------------------------------------------------------------------------------------------
#     2. Create a 2D array of shape (3, 4) filled with zeros.
# arr = np.zeros((3,4))
# print(arr)
# # -----------------------------------------------------------------------------------------------

#     3. Create a 3D array of ones with shape (2, 3, 4).
# arr = np.ones((2,3,4))
# print(arr)
# # -----------------------------------------------------------------------------------------------

#     4. Generate an array of 20 random numbers between 0 and 1.
# arr = np.random.rand(20)
# print(arr)

# # -----------------------------------------------------------------------------------------------

#     5. Create an array of integers from 10 to 50, stepping by 5.
# arr = np.arange(10, 51, 5)
# print(arr)
# # -----------------------------------------------------------------------------------------------

#     6. Generate an array of 15 evenly spaced numbers between 0 and 10.
# arr = np.linspace(0,10,15)
# print(arr)
# # -----------------------------------------------------------------------------------------------

#     7. Create a NumPy array with the following shape and fill it with any values: (2, 2, 2).
# arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(arr)
# # -----------------------------------------------------------------------------------------------

#     8. Create an identity matrix of size 10.
# arr = np.eye(10)
# print(arr)
# # -----------------------------------------------------------------------------------------------

#     9. Determine the shape, size, and data type of the array np.array([1, 2, 3.0]).
# arr = np.array([1, 2, 3.0])
# print(arr.size)
# print(arr.shape)
# print(arr.dtype)
# # -----------------------------------------------------------------------------------------------

#     10. Convert a list [[1, 2], [3, 4]] into a NumPy array.
# arr = [[1, 2], [3, 4]]
# convert = np.array(arr)
# print(f"list:--{arr},Arrays:--{convert}")
# # -----------------------------------------------------------------------------------------------
#     11. Check if all elements in an array are non-zero using a NumPy function.
# arr = np.array([1, 2, 3, 4, 5])

# non_zero = np.all(arr !=0)
# print(non_zero)

# # -----------------------------------------------------------------------------------------------

#     12. Check if any element in an array is zero using a NumPy function.
# arr = np.array([1, 2, 0, 4, 5])

# zeros_ele = np.any(arr ==0)
# print(zeros_ele)
# # -----------------------------------------------------------------------------------------------

#     13. Reverse the order of elements in the array [1, 2, 3, 4, 5].
# arr = [1, 2, 3, 4, 5]
# print(arr[::-1])
# -----------------------------------------------------------------------------------------------

#     14. Reshape the array [1, 2, 3, 4, 5, 6] into a 2x3 matrix.
# arr = np.array([1, 2, 3, 4, 5, 6])
# reshaped = arr.reshape((2,3))
# print(reshaped)
# -----------------------------------------------------------------------------------------------

#     15. Create a 2D array of shape (4, 4) with random integers between 1 and 100.
# arr = np.random.randint(1,101, size=(4,4))
# print(arr)
# -----------------------------------------------------------------------------------------------

#     16. Get the dimensions and size of the array created in the previous question.
# arr = np.random.randint(1,101, size=(4,4))
# print(arr)
# print(arr.size)
# print(arr.shape)
# -----------------------------------------------------------------------------------------------

#     17. Convert a NumPy array of integers [1, 2, 3] into floats.
# arr = np.array([1, 2, 3])
# floats_arr = arr.astype(float)
# print(floats_arr)
# -----------------------------------------------------------------------------------------------

#     18. Change the data type of an array from float64 to int32.
# arr_float = np.array([1.5, 2.8, 3.1, 4.7], dtype=np.float64)

# # Convert the array to int32
# arr_int = arr_float.astype(np.int32)

# print(arr_int)

# -----------------------------------------------------------------------------------------------

#     19. Create a diagonal matrix with values [1, 2, 3] on the diagonal.
# arr = np.array([1,2,3])
# diagonals = np.diag(arr)
# print(diagonals)
# -----------------------------------------------------------------------------------------------

# 20. Extract the diagonal of a matrix generated using np.random.rand(4, 4).
# arr = np.random.rand(4, 4)
# print(arr)
# dio_arr = arr.diagonal()
# print(dio_arr)
# -----------------------------------------------------------------------------------------------


# Indexing and Slicing (20 Questions)
# -----------------------------------------------------------------------------------------------

#     21. Access the second element in the array [10, 20, 30, 40].
# arr = np.array([10, 20, 30, 40])
# print(arr[1])
# -----------------------------------------------------------------------------------------------

#     22. Slice the first three elements from the array [10, 20, 30, 40, 50].
# arr = np.array([10, 20, 30, 40])
# print(arr[0:3])
# -----------------------------------------------------------------------------------------------

#     23. Extract all rows of the second column from a 3x3 array.
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr)
# print(arr[:,1])

# -----------------------------------------------------------------------------------------------

#     24. Retrieve the last row of a 2D array [[1, 2], [3, 4], [5, 6]].
# arr = np.array([[1, 2], [3, 4], [5, 6]])
# print(arr)
# print(arr[2,:])
# -----------------------------------------------------------------------------------------------

#     25. Change the second row of a 2D array to [7, 8].
# arr = np.array([[1, 2], [3, 4], [5, 6]])
# print(arr)
# arr[1,:] = [7,8]
# print(arr)
# -----------------------------------------------------------------------------------------------

#     26. Assign a value of 99 to the third column of a 2D array.
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# arr[:,2] = 99
# print(arr)
# -----------------------------------------------------------------------------------------------

#     27. Use slicing to reverse the rows of a 2D array.
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# rev_arr = arr[::-1]
# print(rev_arr)
# -----------------------------------------------------------------------------------------------

#     28. Extract the first two rows and the last two columns of a 3x3 array.
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr)
# print(arr[0:2,-2:])
# -----------------------------------------------------------------------------------------------

#     29. Use boolean indexing to filter out elements less than 50 from an array.
# arr = np.array([10, 30, 50, 60, 80, 90, 20, 45])
# filter_arr = arr[arr >=50]
# print(arr)
# print(filter_arr)
# -----------------------------------------------------------------------------------------------

#     30. Replace all negative values in an array with 0.
# arr = np.array([10, -5, 30, -2, 50, -8])
# arr [arr < 0] = 0
# print(arr)
# -----------------------------------------------------------------------------------------------

#     31. Find the indices of elements greater than 10 in an array.
# arr = np.array([5, 12, 8, 15, 3, 18])
# print(arr)
# indices = np.where(arr >10 )
# print(indices[0])
# -----------------------------------------------------------------------------------------------

#     32. Retrieve every other element from [0, 1, 2, 3, 4, 5, 6].
# arr = np.array([0, 1, 2, 3, 4, 5, 6])
# print(arr)
# print(arr[::2])
# -----------------------------------------------------------------------------------------------

#     33. Select elements at positions [0, 3, 4] from an array.
# arr = np.array([10, 20, 30, 40, 50, 60, 70])
# print(arr[[0, 3, 4]])
# -----------------------------------------------------------------------------------------------

#     34. Use slicing to reverse the elements of [1, 2, 3, 4, 5].
# arr = [1, 2, 3, 4, 5]
# print(arr[::-1])
# -----------------------------------------------------------------------------------------------

#     35. Slice a 2D array to extract a submatrix.
# arr = np.array([[1, 2, 3, 4, 5],
#                 [6, 7, 8, 9, 10],
#                 [11, 12, 13, 14, 15],
#                 [16, 17, 18, 19, 20],
#                 [21, 22, 23, 24, 25]])
# sliced = arr[1:3,2:4]
# print(sliced)
# -----------------------------------------------------------------------------------------------

#     36. Change all elements in a 2D array greater than 10 to 100.
# arr = np.array([[5, 12, 3], [15, 7, 10], [8, 9, 20]])
# arr[arr > 10] = 100

# print("Updated array:")
# print(arr)
# -----------------------------------------------------------------------------------------------

#     37. Find elements in an array divisible by both 3 and 5.
# arr = np.array([15, 30, 45, 60, 7, 25, 100, 50, 3, 90])

# # Find elements divisible by both 3 and 5
# divisible_by_3_and_5 = arr[(arr % 3 == 0) & (arr % 5 == 0)]

# print("Elements divisible by both 3 and 5:")
# print(divisible_by_3_and_5)
# -----------------------------------------------------------------------------------------------

#     38. Select all elements except the first and last in [10, 20, 30, 40].
# arr = [10, 20, 30, 40]
# selected_elements = arr[1:-1]
# print(selected_elements)
# -----------------------------------------------------------------------------------------------

#     39. Set all even elements of an array to -1.
# arr = np.array([10, 15, 20, 25, 30, 35])
# arr[arr % 2 == 0] = -1
# print(arr)
# -----------------------------------------------------------------------------------------------

#     40. Use np.where() to replace all elements greater than 50 with 1.
# arr = np.array([10, 60, 40, 80, 30, 55])
# updated_arr = np.where(arr > 50, 1, arr)
# print(updated_arr)
# -----------------------------------------------------------------------------------------------


# Mathematical Operations (20 Questions)
# -----------------------------------------------------------------------------------------------

#     41. Add two NumPy arrays element-wise.
# a= np.array([1,2,3])
# b=np.array([4,5,6])
# c = a+b
# print(c)
# -----------------------------------------------------------------------------------------------

#     42. Subtract one array from another element-wise.
# a= np.array([1,2,3])
# b=np.array([4,5,6])
# c = b-a
# print(c)
# -----------------------------------------------------------------------------------------------

#     43. Multiply two arrays element-wise.
# a= np.array([1,2,3])
# b=np.array([4,5,6])
# c = b*a
# print(c)
# -----------------------------------------------------------------------------------------------

#     44. Divide two arrays element-wise.
# a= np.array([1,2,3])
# b=np.array([4,5,6])
# c = b/a
# print(c)
# -----------------------------------------------------------------------------------------------

# #     45. Compute the dot product of two matrices.
# A = np.array([[1, 2, 3],
#               [4, 5, 6]])

# B = np.array([[7, 8],
#               [9, 10],
#               [11, 12]])
# c = np.dot(A,B)
# # print(A)
# # print(B)
# print(c)
# -----------------------------------------------------------------------------------------------

#     46. Perform matrix multiplication for two 2D arrays.
# A = np.array([[1, 2, 3],
#               [4, 5, 6]])

# B = np.array([[7, 8],
#               [9, 10],
#               [11, 12]])
# c = A@B #matrix multiplication
# print(c)
# -----------------------------------------------------------------------------------------------

#     47. Compute the square of each element in an array.
# A = np.array([[1, 2, 3],
#               [4, 5, 6]])
# square = A**2
# print(square)
# -----------------------------------------------------------------------------------------------

#     48. Take the square root of each element in an array.
# A = np.array([[1, 2, 3],
#               [4, 5, 6]])
# square = np.sqrt(A)
# print(square)
# -----------------------------------------------------------------------------------------------

#     49. Compute the exponential (e^x) of elements in [1, 2, 3].
# A = np.array([1, 2, 3])
# exp_res = np.exp(A)
# print(exp_res)
# -----------------------------------------------------------------------------------------------

#     50. Compute the natural logarithm (ln) of each element.
# A = np.array([1, 2, 3])
# exp_res = np.log(A)
# print(exp_res)
# -----------------------------------------------------------------------------------------------

#     51. Compute the mean of an array.
# A = np.array([1, 2, 3])
# exp_res = np.mean(A)
# print(exp_res)
# -----------------------------------------------------------------------------------------------

#     52. Find the maximum value in an array.
# A = np.array([1, 2, 3])
# exp_res = np.max(A)
# print(exp_res)
# -----------------------------------------------------------------------------------------------

#     53. Determine the minimum value in an array.
# A = np.array([1, 2, 3,0.5])
# exp_res = np.min(A)
# print(exp_res)
# -----------------------------------------------------------------------------------------------

#     54. Calculate the standard deviation of an array.
# A = np.array([1, 2, 3,0.5])
# exp_res = np.std(A)
# print(exp_res)
# -----------------------------------------------------------------------------------------------

#     55. Normalize an array to range 0–1.
# A = np.array([1, 2, 3,0.5])
# normalized_A = (A - np.min(A)) / (np.max(A) - np.min(A))
# print(normalized_A)
# -----------------------------------------------------------------------------------------------

# #     56. Calculate the sum of all elements in a 2D array.
# A = np.array([[1, 2, 3],
#               [4, 5, 6]])
# sum_A = np.sum(A)
# print(sum_A)
# -----------------------------------------------------------------------------------------------

#     57. Compute the cumulative sum of a 1D array.
# A = np.array([1, 2, 3, 4, 5, 6])
# sum_A = np.cumsum(A)
# print(sum_A)
# -----------------------------------------------------------------------------------------------

#     58. Calculate the element-wise product of an array and a scalar.([1, 2, 3, 4, 5, 6])
# A = np.array([1, 2, 3, 4, 5, 6])
# scalar = 2# Define the scalar
# # Calculate the element-wise product of the array and the scalar
# product_A = A * scalar
# print(product_A)
# -----------------------------------------------------------------------------------------------

#     59. Generate an array where each element is the sine of [0, π/2, π].
# A = np.array([0, np.pi/2, np.pi])
# sum_A = np.sin(A)
# print(sum_A)
# -----------------------------------------------------------------------------------------------

#     60. Compute the absolute values of the elements in an array.
# A = np.array([1, 2, 3, 4, 5, 6])
# product_A = np.absolute(A)
# print(product_A)
# -----------------------------------------------------------------------------------------------


# Random Numbers and Statistics (10 Questions)
# -----------------------------------------------------------------------------------------------

#     61. Generate an array of 10 random integers between 1 and 100.
# arr = np.random.randint(1, 101, size=10)
# print(arr)
# -----------------------------------------------------------------------------------------------

#     62. Create an array of 5 random numbers from a normal distribution.
# arr = np.random.randn(1,5)
# print(arr)
# -----------------------------------------------------------------------------------------------

#     63. Generate 10 random floats between 0 and 1.
# arr = np.random.rand(10)
# print(arr)
# -----------------------------------------------------------------------------------------------

#     64. Create a 2D array of shape (3, 4) with random integers.
# arr = np.random.randint(1, 11, size=(3, 4))
# print(arr)
# -----------------------------------------------------------------------------------------------

#  65. Find the index of the maximum element in a randomly generated array.
# arr = np.random.randint(1, 101, size=10)
# max_ele = np.argmax(arr)
# print(arr)
# print(max_ele)
# -----------------------------------------------------------------------------------------------

#     66. Compute the median of an array.
# arr = np.random.randint(1, 101, size=10)
# arr_res = np.median(arr)
# print(arr_res)
# -----------------------------------------------------------------------------------------------

#     67. Find the 25th, 50th, and 75th percentiles of an array.
# arr = np.random.randint(1, 101, size=10)
# arr_res1 = np.percentile(arr,25)
# arr_res2 = np.percentile(arr,50)
# arr_res3 = np.percentile(arr,75)
# print(arr_res1,arr_res2,arr_res3)
# -----------------------------------------------------------------------------------------------

#     68. Shuffle a 1D array randomly.
# arr = np.random.randint(1, 101, size=10)
# arr_res = np.random.shuffle(arr)
# print(arr)
# print(arr_res)
# -----------------------------------------------------------------------------------------------

#     69. Set the seed for reproducible random numbers.
# np.random.seed(42)
# arr = np.random.randint(1, 101, size=10)
# print(arr)
# -----------------------------------------------------------------------------------------------

#     70. Generate a random permutation of numbers from 1 to 10.
# arr = np.random.permutation(10)+1
# print(arr)
# -----------------------------------------------------------------------------------------------


# Reshaping and Concatenation (10 Questions)
# -----------------------------------------------------------------------------------------------

#     71. Reshape a 1D array of 12 elements into a 3x4 matrix.
# arr = np.arange(1,13)
# reshaped_arr = arr.reshape(3,4)
# print(reshaped_arr)
# -----------------------------------------------------------------------------------------------

#     72. Flatten a 2D array into a 1D array.
# A = np.array([[1, 2, 3],
#               [4, 5, 6]])
# arr = A.flatten()
# print(arr)
# -----------------------------------------------------------------------------------------------

#     73. Concatenate two 1D arrays.
# A = np.array([1, 2, 3])
# B = np.array([4, 5, 6])
# arr = np.concat((A,B))
# print(arr)
# -----------------------------------------------------------------------------------------------

#     74. Stack two 2D arrays vertically.
# a =np.array([[1,2,3],[4,5,6]])
# b =np.array([[7,8,9],[10,11,16]])
# stacked_arr = np.vstack((a, b))
# print(stacked_arr)
# -----------------------------------------------------------------------------------------------

#     75. Stack two 2D arrays horizontally.
# a =np.array([[1,2,3],[4,5,6]])
# b =np.array([[7,8,9],[10,11,16]])
# stacked_arr = np.hstack((a, b))
# print(stacked_arr)
# -----------------------------------------------------------------------------------------------

#     76. Split a 1D array of 10 elements into two equal halves.
# a =np.array([1,2,3,4,5,6,7,8,9,10])
# arr = np.array_split(a,2)
# print(arr)
# -----------------------------------------------------------------------------------------------

#     77. Split a 2D array into smaller subarrays along rows.
# a =np.array([[1,2,3],[4,5,6]])
# arr = np.array_split(a,2, axis=0)
# print(arr)
# -----------------------------------------------------------------------------------------------

#     78. Reshape a 3D array into a 2D array.
# arr_3d = np.array([
#     [[1, 2, 3], [4, 5, 6]],
#     [[7, 8, 9], [10, 11, 12]]
# ])
# print(arr_3d)
# arr_2d = arr_3d.reshape(4,3)
# print(arr_2d)
# -----------------------------------------------------------------------------------------------

#     79. Add a new axis to a 1D array to make it a 2D column vector.
# arr = np.array([1, 2, 3,4, 5, 6,7, 8, 9,10, 11, 12])
# arr_2d = arr.reshape(-1,1)
# print(arr_2d)
# -----------------------------------------------------------------------------------------------

#     80. Remove all single-dimensional axes from an array.
# arr = np.array([[[1, 2, 3]]])
# print(arr)
# res = np.squeeze(arr)
# print(res)
# -----------------------------------------------------------------------------------------------


# Advanced Topics (20 Questions)
# -----------------------------------------------------------------------------------------------

#     81. Generate an array of random numbers and sort it in ascending order.
# arr = np.random.randint(1,100, size=10) # generate any random arrays
# print(arr)
# arr_asc = np.sort(arr)
# print(arr_asc)
# -----------------------------------------------------------------------------------------------

#     82. Find unique elements in an array.
# arr = np.random.randint(1,100, size=10) 
# print(arr)
# arr_asc = np.unique(arr)
# print(arr_asc)
# -----------------------------------------------------------------------------------------------

#     83. Count the occurrences of each unique element in an array.
# arr = np.random.randint(1,100, size=10) 
# print(arr)
# unique_elements, counts = np.unique(arr, return_counts=True)
# for element, count in zip(unique_elements, counts):
#     print(f"{element} :-- {count}")
# -----------------------------------------------------------------------------------------------

#     84. Create a structured array with named fields.
# data_types = [('name','U10'), ('age','i4'),('height','f4')]
# arr = np.array([
#     ('ace',26, 5.5),
#     ('luffy',25, 5.3),
#     ('sabo',20, 5.1),
# ],dtype = data_types)
# print(arr)
# print(arr['name'])
# print(arr['age'])
# print(arr['height'])
# print(arr[0])

# -----------------------------------------------------------------------------------------------

#     85. Mask values in an array based on a condition.
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(arr)
# print(f"masked :-{arr[arr > 5]}")
# -----------------------------------------------------------------------------------------------

#     86. Replace missing values (np.nan) with the mean of the array.
# arr = np.array([1, 2, np.nan, 4, 5, np.nan, 7, 8])
# print(arr)
# mean_arr = np.nanmean(arr)
# print(mean_arr)
# arr[np.isnan(arr)] = mean_arr
# print(arr)
# -----------------------------------------------------------------------------------------------

#     87. Compute the inverse of a 3x3 matrix.
# matrix = np.array([[1, 2, 3],
#                    [0, 1, 4],
#                    [5, 6, 0]])
# print(matrix)
# inverse_matrix = np.linalg.inv(matrix)
# print(inverse_matrix)
# -----------------------------------------------------------------------------------------------

#     88. Compute the determinant of a 2D square matrix.
# matrix = np.array([[1, 2],
#                    [3, 4]])
# print(matrix)
# res = np.linalg.det(matrix)
# print(res)
# -----------------------------------------------------------------------------------------------

#     89. Find the eigenvalues of a matrix.
# matrix = np.array([[4, -2],
#                    [1,  1]])
# print(matrix)
# eigenvector, eigenvalues = np.linalg.eig(matrix)
# print(eigenvalues)
# print(eigenvector)
# ------- ----------------------------------------------------------------------------------------

#     90. Perform a matrix rank computation.
# matrix = np.array([[4, -2],
#                    [1,  1]])
# print(matrix)
# arr = np.linalg.matrix_rank(matrix)
# print(arr)
# -----------------------------------------------------------------------------------------------

#     91. Solve the system of linear equations Ax = b using NumPy.
# a = np.array([[3, 2],
#               [1, 2]])
# print(f"matrix a:-{a}")
# b = np.array([5, 5])
# print(f"matrix b:-{b}")

# x = np.linalg.solve(a,b)
# print(f"solution:-{x}")

# -----------------------------------------------------------------------------------------------

#     92. Compute the outer product of two vectors.
# a = np.array([1, 2, 3])
# b = np.array([4, 5])
# res = np.outer(a,b)
# print(res)
# -----------------------------------------------------------------------------------------------

#     93. Perform element-wise comparison of two arrays.
# a = np.array([1, 2, 3, 7, 11])
# b = np.array([4, 2, 6, 7, 8])
# print(a)
# print(b)
# arr = a == b
# print(arr)
# -----------------------------------------------------------------------------------------------

#     94. Clip values in an array to lie between a minimum and maximum value.
# a =np.array([1,2,3,4,5,6,7,8,9,10])
# arr  = np.clip(a, 3, 9)
# print(arr)

# -----------------------------------------------------------------------------------------------

#     95. Use np.histogram() to compute the histogram of a dataset.
# -----------------------------------------------------------------------------------------------

#     96. Generate a meshgrid of x and y values.
# x = np.linspace(-5, 5, 10)  # 10 points between -5 and 5 for x
# y = np.linspace(-5, 5, 10)  # 10 points between -5 and 5 for y

# # Generate the meshgrid
# X, Y = np.meshgrid(x, y)
# print(X)
# print(Y)
# -----------------------------------------------------------------------------------------------

#     97. Compute the gradient of a 1D array.
# arr = np.array([1, 2, 4, 7, 11, 16])

# # Compute the gradient of the array
# grad = np.gradient(arr)
# print(grad)
# -----------------------------------------------------------------------------------------------

#     98. Stack 1D arrays into a 2D grid using np.meshgrid().
# x = np.array([1, 2, 3])
# y = np.array([4, 5, 6])
# a,b = np.meshgrid(x,y)
# print(a,b)
# -----------------------------------------------------------------------------------------------

#     99. Create a checkerboard pattern using NumPy arrays.
# n = 8
# c_board = np.zeros((n, n), dtype= int)
# c_board[1::2, ::2] = 1  # Fill every other column starting from row 1
# c_board[::2, 1::2] = 1  # Fill every other row starting from column 1
# print(c_board)
# -----------------------------------------------------------------------------------------------

#     100. Build a 3x3 matrix where each row contains the same value (e.g., [1, 2, 3]).
# row = np.array([1, 2, 3])
# # Create a 3x3 matrix by repeating the row three times
# matrix = np.tile(row, (3, 1))
# print(matrix)
# -----------------------------------------------------------------------------------------------

