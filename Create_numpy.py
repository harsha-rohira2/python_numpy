"""
1. NumPy is a general-purpose array-processing package.
2. It provides a high-performance multidimensional array object and tools for working with these arrays.
3. It is open-source software.

How to create Numpy in Python
"""
# import numpy
import numpy as np

# create numpy array
a = np.array([1,2,3,4,5])
print(a)                                    # output    [1 2 3 4 5]
print(type(a))                              # output    <class 'numpy.ndarray'>


# create 2D array
print(np.array([[1,2,3,4],[5,6,7,8]]))
""" Output      [[1 2 3 4]
                 [5 6 7 8]]
"""

# create 3D array
print(np.array([[1,2],[3,4],[5,6],[7,8]]))

"""output       [[1 2]
                 [3 4]
                 [5 6]
                 [7 8]]
"""

# Create Data type as your choice
print(np.array([1,2,3],dtype=float))         # output    [1. 2. 3.]

print(np.array([1,2,3],dtype=bool))         # output    [ True  True  True]

print(np.array([1,2,3],dtype=complex))      # output    [1.+0.j 2.+0.j 3.+0.j]

# np.arange (Loop)

# 1. print the range of 1 to 10
print(np.arange(1,10))        # output    [1 2 3 4 5 6 7 8 9]

# 2. print the odd no from range
print(np.arange(1,10,2))     # output    [1 3 5 7 9]

# reshape
print(np.arange(1,13).reshape(6,2))      # 5 i.e column & 2 i.e row
"""output   [[ 1  2]
             [ 3  4]
             [ 5  6]
             [ 7  8]
             [ 9 10]
             [11 12]]
"""

# np.ones (all item will be print 1)
print(np.ones([3,4]))
"""output   [[1. 1. 1. 1.]
            [1. 1. 1. 1.]
            [1. 1. 1. 1.]]
"""

# np.zeros (all item will be print 0)
print(np.zeros([3,4]))
"""output   [[0. 0. 0. 0.]
            [0. 0. 0. 0.]
            [0. 0. 0. 0.]]
"""

# np.random
print(np.random.random([2,3]))
"""output   [[0.52558439 0.82758992 0.42175295]
             [0.2644909  0.71697009 0.87542025]]
"""

# np.linspace
print(np.linspace(-10,10,10))
"""output   [-10.          -7.77777778  -5.55555556  -3.33333333  -1.11111111
             1.11111111   3.33333333   5.55555556   7.77777778  10.        ]
"""

# np.identity (diagonal are 1 remaining all are 0)
print(np.identity(3))
"""output   [[1. 0. 0.]
             [0. 1. 0.]
             [0. 0. 1.]]
"""



