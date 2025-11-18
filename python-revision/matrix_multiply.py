import numpy as np


print(np.arange(1, 11))

arr = np.arange(1, 21)
print(arr[arr % 2 == 0])


arr2 = np.array([1, -2, 3, -4, 5])
arr2[arr2 < 0] = 0
print(arr2)


A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])
print(A @ B)


arr3 = np.arange(12)
print(arr3.reshape(3, 4))
