import numpy as np

#1D
a = np.arange(20)
print(a)                # output     [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

for i in a:
    print(i)

# 2D
b = np.arange(16,dtype = float).reshape(4,4)
for i in b:
    print(i)
"""output        [ 0.  1.  2.  3.]
                 [ 4.  5.  6.  7.]
                 [ 8.  9. 10. 11.]
                 [12. 13. 14. 15.]    """

# 3D
c = np.arange(16).reshape(4,2,2)
for i in c:
    print(i)
"""output       [[0 1]
                 [2 3]]
                [[4 5]
                 [6 7]]
                [[ 8  9]
                 [10 11]]
                [[12 13]
                 [14 15]]          """

# print the indivisual in 3D
for i in np.nditer(c):
    print(i)