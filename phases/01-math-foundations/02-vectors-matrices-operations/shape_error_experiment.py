import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6]])     # shape: 2x3


B = np.array([[1, 2],
              [3, 4]])        # shape: 2x2


# B = np.array([[1, 2],
#               [3, 4],
#               [5, 6]])        # shape: 3x2

print("A shape:", A.shape)
print("B shape:", B.shape)

print(A @ B)