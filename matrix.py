import numpy as np
from scipy.linalg import lu

a = np.mat('1, 2; 3, 2; 2, 3')
print(a.shape)

at = a.transpose()
print(at)
print(at.shape)

b = 2*np.eye(3)
print(b.shape)
l = lu(a)
print(l)

