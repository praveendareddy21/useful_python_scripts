import numpy as np

"""
numpy.transpose(a, axes=None) axes : list of ints, optional
Permute the dimensions of an array.
By default, reverse the dimensions, otherwise permute the axes according to the values given.

"""

a = np.arange(6).reshape((2,3))
print(a)
b = np.transpose(a)
print(b)

a = np.ones((1,2,3))
print(a)
print("shape" + " : " + str(a.shape))
b = np.transpose(a, (1,0,2))
print(b)
print("shape" + " : " + str(b.shape))

"""
numpy.ravel(a, order='C')
Return a contiguous flattened array.
A 1-D array, containing the elements of the input, is returned. A copy is made only if needed.

"""






"""
ndarray.flatten(order='C')
Return a copy of the array collapsed into one dimension.
"""
a = np.array([[1,2], [3,4]])
print(a)
print("shape" + " : " + str(a.shape))
b = a.flatten()
print(b)
print("shape" + " : " + str(b.shape))