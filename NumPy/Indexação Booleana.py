Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> 
>>> a = np.array([[[1,2],[3,4],[5,6]])
	     
SyntaxError: invalid syntax
>>> a = np.array([[1,2],[3,4],[5,6]])
>>> 
>>> a
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> a[a>3]
array([4, 5, 6])
>>> a[a>1]
array([2, 3, 4, 5, 6])
>>> idx = (a > 2)
>>> idx
array([[False, False],
       [ True,  True],
       [ True,  True]])
>>> 
