import numpy as np

a = np.arange(1,7)
print(a)
print(a.shape)
b = a.reshape((2,3))
print(b)

c = a[np.newaxis, :]
print(c.shape)