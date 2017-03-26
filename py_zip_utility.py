import numpy as np
trX = np.ones(100)

"""
zip takes a bunch of lists likes

a: a1 a2 a3 a4 a5 a6 a7...
b: b1 b2 b3 b4 b5 b6 b7...
c: c1 c2 c3 c4 c5 c6 c7...
and "zips" them into one list whose entries are 3-tuples (ai, bi, ci). Imagine drawing a zipper horizontally from left to right.




"""


batch_size = 2
print(range(0, len(trX), batch_size))
print(range(batch_size, len(trX)+1, batch_size))

## below loop can be used for batch processing of some iterable(start and end are indices for a single batch)
for start, end in zip(range(0, len(trX), batch_size), range(batch_size, len(trX)+1, batch_size)):
	print(str(start) + " : " + str(end))