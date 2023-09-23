import numpy as np

a = np.arange(20)
b = np.arange(16,dtype = float).reshape(4,4)
c = np.arange(16).reshape(4,2,2)

print(a)
print(b)
print(c)


# ndim (number od dimensions)
"""In NumPy, ndim is an attribute of NumPy arrays that returns the number of dimensions or axes in the array."""
# 1D
print(a.ndim)        # output    1
# 2D
print(b.ndim)        # output    2
# 3D
print(c.ndim)        # output    3


# shape ( will count the numbers of rows and colunm )
"""In NumPy, the shape attribute of a NumPy array returns a tuple representing the dimensions or shape of the array. """
# 1D
print(a.shape)      # output    (20,)
# 2D
print(b.shape)       # output    (4, 4)
# 3D
print(c.shape)      # output    (4, 2, 2)


# Size
"""In NumPy, the size attribute of a NumPy array returns the total number of elements in the array."""
print(a.size)       # output    20

print(b.size)       # output    16

print(c.size)       # output    16


# itemsize ( How much size occupy in memory )
"""In NumPy, the itemsize attribute of a NumPy array returns the size (in bytes) of each individual element in the array. """
print(a.itemsize)        # output    4

print(b.itemsize)        # output    8

print(c.itemsize)        # output    4


# change the data type
print(a.dtype)          # output    int32
a1 = a.astype(np.int64)
print(a1.dtype)
