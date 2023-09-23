import numpy as np

a = np.arange(8,dtype = float).reshape(4,2)
print(a)

# Transpose
"""In NumPy, the T attribute or the transpose() function can be used to transpose a multi-dimensional array. 
Transposing an array means exchanging its rows with its columns, effectively changing the shape of the array 
while preserving the data"""

print(a.T)
print(np.transpose(a))


# ravel ( convert any dimension into 1D)
"""The ravel() method in NumPy is used to flatten a multi-dimensional array into a 1D array while keeping the element order. 
It unravels or flattens the array along its row-major (C-style) order, which means it iterates through the elements row by row."""

print(a.ravel())
