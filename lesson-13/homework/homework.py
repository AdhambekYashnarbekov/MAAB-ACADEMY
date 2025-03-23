import numpy as np

# 1. Create a vector with values ranging from 10 to 49.
vector = np.arange(10, 50)
print("Vector:", vector)

# 2. Create a 3x3 matrix with values ranging from 0 to 8.
matrix_3x3 = np.arange(9).reshape(3, 3)
print("3x3 Matrix:", matrix_3x3)

# 3. Create a 3x3 identity matrix.
identity_matrix = np.eye(3)
print("Identity Matrix:", identity_matrix)

# 4. Create a 3x3x3 array with random values.
random_3x3x3 = np.random.rand(3, 3, 3)
print("3x3x3 Random Array:", random_3x3x3)

# 5. Create a 10x10 array with random values and find min and max.
ten_by_ten = np.random.rand(10, 10)
print("Min:", ten_by_ten.min(), "Max:", ten_by_ten.max())

# 6. Create a random vector of size 30 and find the mean value.
vector_30 = np.random.rand(30)
print("Mean:", vector_30.mean())

# 7. Normalize a 5x5 random matrix.
matrix_5x5 = np.random.rand(5, 5)
norm_matrix = (matrix_5x5 - np.mean(matrix_5x5)) / np.std(matrix_5x5)
print("Normalized Matrix:", norm_matrix)

# 8. Multiply a 5x3 matrix by a 3x2 matrix.
matrix_5x3 = np.random.rand(5, 3)
matrix_3x2 = np.random.rand(3, 2)
product_5x2 = np.dot(matrix_5x3, matrix_3x2)
print("5x3 * 3x2 Product:", product_5x2)

# 9. Compute dot product of two 3x3 matrices.
matrix_A = np.random.rand(3, 3)
matrix_B = np.random.rand(3, 3)
dot_product = np.dot(matrix_A, matrix_B)
print("Dot Product:", dot_product)

# 10. Find transpose of a 4x4 matrix.
matrix_4x4 = np.random.rand(4, 4)
transpose_4x4 = matrix_4x4.T
print("Transpose:", transpose_4x4)

# 11. Calculate determinant of a 3x3 matrix.
matrix_3x3_det = np.random.rand(3, 3)
determinant = np.linalg.det(matrix_3x3_det)
print("Determinant:", determinant)

# 12. Compute matrix product of A (3x4) and B (4x3).
A = np.random.rand(3, 4)
B = np.random.rand(4, 3)
product_AB = np.dot(A, B)
print("Matrix Product AB:", product_AB)

# 13. Compute matrix-vector product.
matrix_3x3_rand = np.random.rand(3, 3)
vector_3x1 = np.random.rand(3, 1)
matrix_vector_product = np.dot(matrix_3x3_rand, vector_3x1)
print("Matrix-Vector Product:", matrix_vector_product)

# 14. Solve the linear system Ax = b.
A_system = np.random.rand(3, 3)
b_system = np.random.rand(3, 1)
x_solution = np.linalg.solve(A_system, b_system)
print("Solution x:", x_solution)

# 15. Compute row-wise and column-wise sums of a 5x5 matrix.
matrix_5x5_sum = np.random.rand(5, 5)
row_sums = np.sum(matrix_5x5_sum, axis=1)
col_sums = np.sum(matrix_5x5_sum, axis=0)
print("Row Sums:", row_sums, "Column Sums:", col_sums)
