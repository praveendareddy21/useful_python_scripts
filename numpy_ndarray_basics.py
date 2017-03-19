import numpy as np

a = np.arange(6) # create ndarray for 0,1,2,3,4,5
print(a)

b = np.array([0,1,2,3,4,5]) # create ndarray for 0,1,2,3,4,5
print(b)

"""
ndarray.ndim
the number of axes (dimensions) of the array. 
In the Python world, the number of dimensions is referred to as rank.
"""
print("ndim" + " : " + str(b.ndim))

"""
ndarray.shape
the dimensions of the array. 
This is a tuple of integers indicating the size of the array in each dimension. For a matrix with n rows and m columns, shape will be (n,m). The length of the shape tuple is therefore the rank, or number of dimensions, ndim.
"""
print("shape" + " : " + str(b.shape))

"""
ndarray.size
the total number of elements of the array.
This is equal to the product of the elements of shape
"""

print("size" + " : " + str(b.size))


"""
Reshaping , ndarray can be reshaped if total elements are not changed (size is same)

"""
b = b.reshape(2, 3)
print(b)
print("ndim" + " : " + str(b.ndim))
print("shape" + " : " + str(b.shape))
print("size" + " : " + str(b.size))

b = b.reshape(3, 2)
print(b)
print("ndim" + " : " + str(b.ndim))
print("shape" + " : " + str(b.shape))
print("size" + " : " + str(b.size))


"""
ndarray.dtype
an object describing the type of the elements in the array. One can create or specify dtype using standard Python types
Additionally NumPy provides 
 numpy.int32, numpy.int16, and numpy.float64 

"""

print("dtype" + " : " + str(b.dtype))