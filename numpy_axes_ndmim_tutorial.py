import numpy as np


b = np.ones(24) # created 24 1's
print(b)

"""
numpy axes::
By definition, the axis number of the dimension is the index of that dimension within the array's shape.
It is also the position used to access that dimension during indexing.


For example, if a 2D array a has shape (5,6), then you can access a[0,0] up to a[4,5]. 
Axis 0 is thus the first dimension (the "rows"), and axis 1 is the second dimension (the "columns"). 
In higher dimensions, where "row" and "column" stop really making sense, try to think of the axes in terms of the shapes and indices involved.





"""




c = b.reshape(2,3,4)
print(c)
print("ndim" + " : " + str(c.ndim))
print("shape" + " : " + str(c.shape))
print("size" + " : " + str(c.size))


print("after sum along axis 0")  ## outermost dimension
d =  c.sum(axis = 0)
print(d)
print("shape" + " : " + str(d.shape))
print("ndim" + " : " + str(d.ndim))
print("----------------------")


print("after sum along axis 1")
d =  c.sum(axis = 1)
print(d)
print("shape" + " : " + str(d.shape))
print("ndim" + " : " + str(d.ndim))
print("----------------------")


print("after sum along axis 2")  ###inner most dimension (as ndim =3)
d =  c.sum(axis = 2)
print(d)
print("shape" + " : " + str(d.shape))
print("ndim" + " : " + str(d.ndim))
print("----------------------")


"""
e.shape == (2, 3, 4)
Sum over an axis is a reduction operation so the specified axis disappears. Hence,

e.sum(axis=0).shape == (3, 4)
e.sum(axis=1).shape == (2, 4)
e.sum(axis=2).shape == (2, 3)

"""