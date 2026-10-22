# 1.Write a Python program using NumPy to create a one-dimensional array containing 10 integers & 
# display the array, its size, data type, and number of dimensions.

import numpy as np

# arr=np.array([1,2,3,4,5,6,7,8,9,10])
# print("Array:",arr)
# print("Array size:",arr.size)
# print("Type:",arr.dtype)
# print("Dim:",arr.ndim)



# 2.Create two NumPy arrays of 5 integers each. Perform & display:
# •	Addition 
# •	Subtraction 
# •	Multiplication 
# •	Division 
# •	Modulus

# import numpy as np
# arr1=np.array([1,2,3,4,5])
# arr2=np.array([6,7,8,9,10])

# print("Addition:",arr1+arr2)
# print("Subtraction:",arr1-arr2)
# print("Multiplication:",arr1*arr2)
# print("Division:",arr1/arr2)
# print("Modulus:",arr1%arr2)


# 3.	Create a NumPy array containing 10 numbers. 
# Find and display the maximum, minimum, sum, and average of the elements.

# import numpy as np

# arr=np.array([1,2,3,4,5,6,7,8,9,10])

# print("Maximum:",arr.max())
# print("Minimum:",arr.min())
# print("Sum:",arr.sum())
# print("Avg:",arr.mean())


# 4.Create a NumPy array of integers from 1 to 20. 
# Use Boolean indexing to separate and display the even and odd numbers.

# import numpy as np
# arr=np.arange(1,21)
# even=arr[arr%2==0]
# odd=arr[arr%2!=0]
# print("Original",arr)
# print("Even",even)
# print("Odd",odd)


# 5.Create a one-dimensional array containing numbers from 1 to 12. Reshape it into:
# •	2 × 6 matrix 3 × 4 matrix  4 × 3 matrix

# import numpy as np

# arr=np.arange(1,13)
# print("Original:",arr)
# print("2 x 6",arr.reshape(2,6))


# 6.	Create two 3 × 3 NumPy matrices and perform matrix addition

# import numpy as np

# a=np.array([[1,2,3],
#            [4,5,6],
#            [7,8,9]])

# b=np.array([[9,8,7],
#            [6,5,4],
#            [3,2,1]])

# print("A:",a)
# print()
# print("B:",b)
# print()
# print("Addition:",a+b)

# 7.Create two compatible matrices using NumPy and perform matrix multiplication using an appropriate NumPy function.
# res=np.matmul(a,b)
# print("Multiplication:",res)

# 8.Create a 3 × 4 matrix and display its transpose.
# print(a.T)

# 9.	Create a 4 × 4 NumPy array and write a program to:
# •	Display the first row 
# •	Display the last column 
# •	Display the diagonal elements 
# •	Display the elements from the second and third rows

arr=np.array([[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12],
             [13,14,15,16]])

# print("First row:")
# print(arr[0,:])
# print("Last row:")
# print(arr[:-1])
# print("Diagonal:")
# print(np.diag(arr))
# print("Second and Third Rows:")
# print(arr[1:3, :])

# 10.Create a 4 × 4 matrix and calculate the sum of each row and each column separately
# print("Sum of 1 row",np.sum(arr[0,:]))
# print("Sum of 2 row",np.sum(arr[1,:]))
# print("Sum of 3 row",np.sum(arr[2,:]))
# print("Sum of 4 row",np.sum(arr[3,:]))
# print("Sum of 1st column:", np.sum(arr[:, 0]))
# print("Sum of 2nd column:", np.sum(arr[:, 1]))
# print("Sum of 3rd column:", np.sum(arr[:, 2]))
# print("Sum of 4th column:", np.sum(arr[:, 3]))

# 11.Create a NumPy array containing numbers from 1 to 20. Using slicing, display:
# •	First 5 elements 
# •	Last 5 elements 
# •	Alternate elements 
# •	Elements in reverse order
# arr=np.arange(1,21)
# print(arr[:5])
# print(arr[-5:])
# print(arr[0::2])
# print(arr[::-1])

# 12.	Create an array of 10 integers. Replace all elements greater than 50 with 0 using NumPy Boolean indexing.
# arr = np.array([10, 25, 60, 45, 75, 30, 90, 50, 65, 20])
# print("Original Array:", arr)
# arr[arr > 50] = 0
# print("Modified Array:", arr)


# 13.	Create an unsorted NumPy array and display it in:
# •	Ascending order 	Descending order
# arr = np.array([45, 12, 78, 23, 9, 56, 34, 90])
# print("Original Array:", arr)
# print("Ascending Order:", np.sort(arr))
# print("Descending Order:", np.sort(arr)[::-1])


# 14.Create an array containing duplicate values. Find and display only the unique elements.

# arr = np.array([10, 20, 30, 20, 40, 10, 50, 30, 60, 10])

# print("Original Array:", arr)
# print("Unique Elements:", np.unique(arr))


# 15.Create two NumPy arrays and concatenate them horizontally and vertically. 
# arr1 = np.array([[1, 2],
#                  [3, 4]])

# arr2 = np.array([[5, 6],
#                  [7, 8]])

# print("Array 1:")
# print(arr1)

# print("Array 2:")
# print(arr2)

# print("Horizontal Concatenation:")
# print(np.concatenate((arr1, arr2), axis=1))

# print("Vertical Concatenation:")
# print(np.concatenate((arr1, arr2), axis=0))


# 16.	Store marks of 10 students in a NumPy array. Calculate:
# •	Highest marks 
# •	Lowest marks 
# •	Average marks 
# •	Median 
# •	Standard deviation

# marks = np.array([75, 80, 65, 90, 85, 70, 95, 60, 88, 82])

# print("Student Marks:", marks)
# print("Highest Marks:", np.max(marks))
# print("Lowest Marks:", np.min(marks))
# print("Average Marks:", np.mean(marks))
# print("Median:", np.median(marks))
# print("Standard Deviation:", np.std(marks))

# 17.	Take marks of 20 students, calculate the class average and display the marks of students who scored above the average.

# marks = np.array([75, 80, 65, 90, 85, 70, 95, 60, 88, 82,
#                   78, 92, 55, 84, 76, 89, 68, 96, 73, 81])

# average = np.mean(marks)

# print("Student Marks:", marks)
# print("Class Average:", average)
# print("Marks Above Average:", marks[marks > average])


# 18.	Write a Python program using NumPy to 
# create a 3D array of shape (2, 3, 4) containing numbers from 1 to 24. Display the array and its: •	Number of dimensions  Shape  Size
# arr = np.arange(1, 25).reshape(2, 3, 4)

# print("3D Array:")
# print(arr)

# print("Number of Dimensions:", arr.ndim)
# print("Shape:", arr.shape)
# print("Size:", arr.size)


# 19.	Create a 3D array of shape (2, 3, 4) and write a program to access:
# •	First element 
# •	Last element 
# •	Element at index [0,1,2] 
# •	Element at index [1,2,3]

# arr = np.arange(1, 25).reshape(2, 3, 4)

# print("3D Array:")
# print(arr)

# print("First Element:", arr[0, 0, 0])
# print("Last Element:", arr[-1, -1, -1])
# print("Element at index [0,1,2]:", arr[0, 1, 2])
# print("Element at index [1,2,3]:", arr[1, 2, 3])


# 20.	Create a (2, 3, 4) array and calculate:
# •	Sum of all elements 
# •	Sum of each layer 
# •	Sum along rows 
# •	Sum along columns

# arr = np.arange(1, 25).reshape(2, 3, 4)

# print("3D Array:")
# print(arr)

# print("Sum of All Elements:", np.sum(arr))
# print("Sum of Each Layer:")
# print(np.sum(arr, axis=(1, 2)))

# print("Sum Along Rows:")
# print(np.sum(arr, axis=2))

# print("Sum Along Columns:")
# print(np.sum(arr, axis=1))

# PS: Create a 3D array of random integers between 1 and 100.
# Replace all values greater than 50 with 0.

# arr = np.random.randint(1, 101, size=(2, 3, 4))
# print("Original Array:\n", arr)

# arr[arr > 50] = 0
# print("Modified Array:\n", arr)


# PS: Generate a random 3D array of shape (3, 4, 5).
# Calculate mean, median, standard deviation, variance,
# minimum, and maximum.

# arr = np.random.randint(1, 101, size=(3, 4, 5))

# print("Array:\n", arr)
# print("Mean:", np.mean(arr))
# print("Median:", np.median(arr))
# print("Standard Deviation:", np.std(arr))
# print("Variance:", np.var(arr))
# print("Minimum:", np.min(arr))
# print("Maximum:", np.max(arr))


# PS: Create a 3D array of shape (2, 3, 4) containing
# numbers from 1 to 24. Display the original and flattened arrays.

# arr = np.arange(1, 25).reshape(2, 3, 4)

# print("Original Array:\n", arr)
# print("Flattened Array:", arr.flatten())

# PS: Create a 3D array containing numbers from 1 to 27.
# Flatten the array and calculate sum, average, maximum,
# and minimum.

# arr = np.arange(1, 28).reshape(3, 3, 3)
# flat = arr.flatten()

# print("Flattened Array:", flat)
# print("Sum:", np.sum(flat))
# print("Average:", np.mean(flat))
# print("Maximum:", np.max(flat))
# print("Minimum:", np.min(flat))

# PS: Create a random 3D array of shape (3, 4, 5).
# Flatten it and display elements greater than 50,
# even numbers, and elements less than the average.


# arr = np.random.randint(1, 101, size=(3, 4, 5))
# flat = arr.flatten()
# avg = np.mean(flat)

# print("Original Array:\n", arr)
# print("Flattened Array:", flat)
# print("Greater than 50:", flat[flat > 50])
# print("Even Numbers:", flat[flat % 2 == 0])
# print("Less than Average:", flat[flat < avg])

