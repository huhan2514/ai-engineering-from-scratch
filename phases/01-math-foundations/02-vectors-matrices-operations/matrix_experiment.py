import numpy as np

# =========================
# 1. 基础矩阵
# =========================

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("A =")
print(A)

print("\nB =")
print(B)

# =========================
# 2. Element-wise 运算
# =========================

print("\nA + B =")
print(A + B)

print("\nA * B  # element-wise multiplication")
print(A * B)

# =========================
# 3. Matrix multiplication
# =========================

print("\nA @ B  # matrix multiplication")
print(A @ B)

# =========================
# 4. Transpose
# =========================

print("\nA.T =")
print(A.T)

# =========================
# 5. Determinant and inverse
# =========================

print("\ndet(A) =")
print(np.linalg.det(A))

print("\nA inverse =")
print(np.linalg.inv(A))

print("\nA @ A_inverse =")
print(A @ np.linalg.inv(A))

# =========================
# 6. Broadcasting
# =========================

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

bias = np.array([10, 20, 30])

print("\nBroadcasting example: matrix + bias")
print(matrix + bias)