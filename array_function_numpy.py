import numpy as np

a = np.arange(8).reshape(2,4)
b = np.arange(8,16).reshape(4,2)
print(a)
print(b)

# 1. max
""""The np.max() function is used to find the maximum value in an array."""
a1= np.max(a)
a2 = np.max(a,axis = 1)                 # axis 0-> column & 1-> row
print("a1 :",a1,"a2 :",a2)              # output    a1 : 7 a2 : [3 7]

# 2. min
"""The np.min() function is used to find the minimum value in an array."""
a1= np.min(a)
a2 = np.min(a,axis = 0)
print("a1 :",a1,"a2 :",a2)          # output    a1 : 0 a2 : [0 1 2 3]

# 3. sum
"""The np.sum() function is used to calculate the sum of elements in a NumPy array."""
a1= np.sum(a)
a2 = np.sum(a,axis = 1)
print("a1 :",a1,"a2 :",a2)          # output    a1 : 28 a2 : [ 6 22]

# 4. prod
"""The np.prod() function is used to calculate the product of elements in a NumPy array. """
a1= np.prod(a)
a2 = np.prod(a,axis = 0)
print("a1 :",a1,"a2 :",a2)          # output    a1 : 0 a2 : [ 0  5 12 21]

# 5. mean
"""The np.mean() function is used to calculate the mean or average value of elements in a NumPy array. """
a1= np.mean(a)
a2 = np.mean(a,axis = 1)
print("a1 :",a1,"a2 :",a2)          # output   a1 : 3.5 a2 : [1.5 5.5]

# 6. median
"""the np.median() function is used to calculate the median value of elements in a NumPy array. 
The median is the middle value in a sorted list of numbers or the value that separates the higher half from the lower half"""
a1= np.median(a)
a2 = np.median(a,axis = 0)
print("a1 :",a1,"a2 :",a2)          #output  a1 : 3.5 a2 : [2. 3. 4. 5.]

# 7. std
"""the np.std() function is used to calculate the standard deviation of elements in a NumPy array. 
The standard deviation is a measure of the spread or dispersion of data points in a dataset."""
a1= np.std(a)
a2 = np.std(a,axis = 1)
print("a1 :",a1,"a2 :",a2)          # output   a1 : 2.29128784747792 a2 : [1.11803399 1.11803399]

# 8. var
"""the np.var() function is used to calculate the variance of elements in a NumPy array. 
Variance is a measure of how much individual data points deviate from the mean (average)."""
a1= np.var(a)
a2 = np.var(a,axis = 0)
print("a1 :",a1,"a2 :",a2)      # output  a1 : 5.25 a2 : [4. 4. 4. 4.]

# 9. trignometer
a1 = np.sin(a)
print(a1)
"""output       [[ 0.          0.84147098  0.90929743  0.14112001]
                 [-0.7568025  -0.95892427 -0.2794155   0.6569866 ]]     """

# 10. dot product
"""In NumPy, you can calculate the dot product of two arrays using the numpy.dot() function or the @ operator. 
The dot product is a mathematical operation that takes two arrays of the same shape and computes the sum of 
the products of their corresponding elements"""
print(np.dot(a,b))
"""output       [[ 76  82]
                 [252 274]]     """

# 11. log
print(np.log(a))
"""Output       [[      -inf 0.         0.69314718 1.09861229]
                 [1.38629436 1.60943791 1.79175947 1.94591015]]       """

# 12. exponent
print(np.exp(a))
"""output       [[1.00000000e+00 2.71828183e+00 7.38905610e+00 2.00855369e+01]
                 [5.45981500e+01 1.48413159e+02 4.03428793e+02 1.09663316e+03]]     """

# 13. round
"""n NumPy, you can round the elements of a NumPy array using the numpy.round() function. 
This function allows you to round the values to a specified number of decimal places or to the nearest integer. """
c = np.random.random([2,3])*100
print(c)
"""output       [[20.13977907 85.07529149 56.04775337]
                 [85.9120794  49.03205116 22.57044427]]"""
print(np.round(c))
"""output       [[20. 85. 56.]
                 [86. 49. 23.]]     """

# 14. floor
"""This function rounds down each element in a NumPy array to the nearest integer less than or equal to it."""
print(np.floor(c))
"""output       [[20. 85. 56.]
                 [85. 49. 22.]]     """

# 15. ciel
"""This function rounds up each element in a NumPy array to the nearest integer greater than or equal to it."""
print(np.ceil(c))
"""output       [[21. 86. 57.]
                 [86. 50. 23.]]         """



