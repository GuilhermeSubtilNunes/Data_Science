Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> soma = 0
>>> for i in range(1, 100000001):
	soma += i

	
>>> import numpy as np
>>> np.arange(1, 100000001).sum()
987459712
>>> 
