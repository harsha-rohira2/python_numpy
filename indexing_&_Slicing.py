import numpy as np

a = np.arange(20)
b = np.arange(16,dtype = float).reshape(4,4)
c = np.arange(16).reshape(4,2,2)

print(a)
print(b)
print(c)

""""Indexing: Indexing refers to accessing individual elements of a NumPy array using their positions or indices. 
You can access elements by specifying their row and column indices in square brackets"""
# Indexing 1D
print(a[0])                 # First index position                  # output    0

print(a[-1] )               # last index position                 # output    19

# indexing with 2D
print(b[1][2])       # output    6

# indexing with 3D
print(c[1,0,1])      # output    5


"""Slicing: Slicing allows you to extract a portion of a NumPy array by specifying a range of indices. 
You can use slicing to create subarrays from the original array."""
# slicing 1D
print(a[2:5])       # output    [2 3 4]

# slicing with 2D
print(b[0,:])               # print 1st row                       # output    [0. 1. 2. 3.]

print(b[:,2])               # print 2nd colunm                    # output    [ 2.  6. 10. 14.]

print(b[1:,1:3])
"""output       [[ 5.  6.]
                 [ 9. 10.]
                 [13. 14.]]"""

print(b[::2,::3])           # corner element
"""output       [[ 0.  3.]
                 [ 8. 11.]]"""

# slicing 3D
print(c[1,:,1])             # Output    [5 7]

print(c[2,1:,1:])           # output    [[11]]


