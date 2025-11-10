import array
import numpy as np

print("==============MultiDimensional Array=================")

arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr3)

print(arr3.dtype)
print(arr3.ndim)
print(arr3.shape)
print(arr3.size)
print(arr3.itemsize)
print(arr3.nbytes)
print(arr3[1,2])
for row in arr3:
    for val in row:
        print(val, end=" ")

arr4=np.linspace(1,10,5)
print(arr4)

arr5=np.arange(1,20,3)
print(arr5)
arr6=np.zeros((3,4),int)
print(arr6) 

arr7=np.array([2,1,4,3,5])
arr8=arr7.view()        #  Shallow Copy
print(arr7)
print(arr8)

arr9=arr7.copy()       # Deep Copy
print(arr9)

print(arr3.flatten())
print("=====================================================")
print("==============Array Operations=================")
arrA = np.array([1,2,3,4])
arrB = np.array([5,6,7,8])  
print("Array A: ", arrA)
print("Array B: ", arrB)
print("Addition: ", arrA + arrB)
print("Subtraction: ", arrB - arrA)
print("Multiplication: ", arrA * arrB)
print("Division: ", arrB / arrA)    
print("Exponentiation: ", arrA ** 2)
print("Square Root of Array B: ", np.sqrt(arrB))
print("=====================================================")
print("==============Matrix Operations=================")
matA = np.array([[1,2],[3,4]])
matB = np.array([[5,6],[7,8]])
print("Matrix A: \n", matA)
print("Matrix B: \n", matB)
print("Matrix Addition: \n", matA + matB)
print("Matrix Subtraction: \n", matB - matA)
print("Matrix Multiplication: \n", np.dot(matA, matB))
print("Element-wise Multiplication: \n", matA * matB)
print("Transpose of Matrix A: \n", matA.T)



