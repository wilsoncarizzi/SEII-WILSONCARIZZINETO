import numpy as np

a = np.array([[1,2],[3,4]])
eigenvalues, eigenvectors = np.linalg.eig(a)

b = eigenvectors[:,0] * eigenvalues[0]
print(b)
c = a @ eigenvectors[:,0]
print(b)

print(np.allclose(b,c))