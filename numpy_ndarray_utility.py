import numpy as np

b = np.array([0,5,2,3,4,5]) # create ndarray for 0,1,2,3,4,5
print(b)

c = np.argmax(b)


print(c)
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




"""
np.mean


numpy.mean(a, axis=None, dtype=None, out=None, 

Compute the arithmetic mean along the specified axis.

Returns the average of the array elements. The average is taken over the flattened array by default,
 otherwise over the specified axis. float64 intermediate and return values are used for integer inputs.
"""
print("np.mean example")
a = np.array([[2, 2, 2], [4, 4,4]])
print(a)
print(np.mean(a, dtype = np.float64))  # mean of flattened array  , higher precision for accurate mean 

b = np.mean(a, axis=0) # mean along axis 0 i,e,,  col (2, 4) 
print(b)

c = np.mean(a, axis=1)   # mean along axis 1 i,e,,  row (2, 2, 2) 
print(c)