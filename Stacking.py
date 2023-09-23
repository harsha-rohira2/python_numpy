"""Stacking
In NumPy, stacking refers to the process of combining two or more arrays along a new axis. """

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a)
print(b)

# horizontal stacking
print(np.hstack((a,b)))

# Vertical Stacking
print(np.vstack((a,b)))

# depth- wise Stacking
print(np.dstack((a,b)))