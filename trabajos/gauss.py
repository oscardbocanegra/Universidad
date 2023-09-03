import numpy as np 
A = np.array([[10., -5, -5], [-5, 12, -3], [-5, -3, 8]])
b = np.array([12, 0, -6])
x = np.linalg.solve(A,b)
print(x)