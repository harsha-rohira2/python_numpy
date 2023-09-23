import numpy as np

a = np.arange(8).reshape(2,4)
b = np.arange(8,16).reshape(4,2)
print(a)
"""output   [[0 1 2 3]
             [4 5 6 7]]
"""
print(b)
"""output   [[ 8  9]
             [10 11]
             [12 13]
             [14 15]]
 """

# Scalar Operation (Operation is perform by single operators)
# 1. Arithmetic operators

a1 = a*2
print(a1)
"""output   [[ 0  2  4  6]
             [ 8 10 12 14]]     """

a1 = a+2
print(a1)
"""output   [[2 3 4 5]
             [6 7 8 9]]     """

a1 = a/2
print(a1)
"""output   [[0.  0.5 1.  1.5]
             [2.  2.5 3.  3.5]]     """

a1 = a**2
print(a1)
"""output   [[ 0  1  4  9]
             [16 25 36 49]]     """

# 2. Relation operator

a1 = a>4
print(a1)
"""output   [[False False False False]
             [False  True  True  True]]     """

a1 = a==12
print(a1)
"""output   [[False False False False]
             [False False False False]]     """

a = np.arange(8).reshape(2,4)
b = np.arange(8,16).reshape(4,2)

# Vector operator ( operation is perform between 2 operands)
c = a @ b
print(c)
