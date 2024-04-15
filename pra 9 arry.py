import numpy as np

# Create a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print(f"1D Array: {arr1}")

# Create a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2D Array: \n{arr2}")

# Add 5 to all elements of arr1
arr1 = arr1 + 5
print(f"\n1D Array after adding 5: {arr1}")

# Multiply all elements of arr2 by 2
arr2 = arr2 * 2
print(f"\n2D Array after multiplying by 2: \n{arr2}")

# Calculate the sum of all elements in arr1
sum_arr1 = np.sum(arr1)
print(f"\nSum of all elements in 1D array: {sum_arr1}")

# Calculate the mean of all elements in arr2
mean_arr2 = np.mean(arr2)
print(f"\nMean of all elements in 2D array: {mean_arr2}")
