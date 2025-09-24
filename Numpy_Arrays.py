# Numpy:
# Numpy (Numerical Python) is a python library used for scientific and mathematical computing.
# It provides:
# -> powerfull array objects(more effective than python lists).
# -> vectorised operations (fast element-wise calculations).
# -> support for linear algebra,statistics,random number,operators etc...
# importing the numpy library.
import numpy as np
import array as arr
#creating an array with numpy:
# 1d aray:
A1D= np.array([1,2,3,4,5])
print(A1D)
#2d array:
A2D = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
print(A2D)
# [
#   123
#   456
#   789
# ]
 #methods and operations in numpy arrays:
 # 1. basic array information methods:
A = np.array([1,2,3,4,5])
 # ndim: returns the number of dimensions of the array.
print(A.ndim)
print(A2D.ndim)
#shape: returns a tuple showing the sizes of the array in each dimensions(rows,columns, etc..) 
print(A2D.shape) 
#size: returns the total number of elements in the array.
print(A2D.size)
# dtype: returns the datatype of the elements in the arraay.
print(A2D.dtype) #= type

# 2. crating an array with numpy:
# zeroes: creates an array of 6 zeros
print(np.zeros(6)) #
#ones:creates an array of 12ones
print(np.ones(12))
# arange:creates an array from 1-->10 based on the ranges. 
print(np.arange(1,11,1))  #1 2 3 4 5 6 7 8 9 10
print(np.arange(0,11,2)) # 0 2 4 6 8 10
print(np.arange(1,11,2)) # 1 3 5 7 9 
#linspace:creates 3 numbers evenly spaced between 0 and 1
print(np.linspace(0,1,3)) # 0 0.5 1

# Mathematical Operations:
A = np.array([1,2,3,4,5,])
L = [1,2,3,4,5]
print(A+6)
print(A-2)
print(A*2)
print(A/2)
print(A//2)
print(A**6)
print(A%2)

# Aggregate Functions:
a=np.array([1,2,3,4,5])
# sum():
print(np.sum(a))
# mean:
print(np.mean(a))
# max:
print(np.max(a))
# min:
print(np.min(a))
# median:
print(np.median(a))
#  std:
print(np.std(a))
# cumprod:
print(np.cumprod(a))

#matrix operations:
mat1=np.array([[1,2,3],[4,5,6],[7,8,9]])
mat2=np.array([[9,8,7],[6,5,4],[3,2,1]])
print(mat1+mat2)
print(mat1**2)
print(mat1*mat2)
#dot():
print(np.dot(mat1,mat2))
#transpose:
print(np.transpose(mat1))