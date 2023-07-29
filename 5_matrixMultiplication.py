def multiply_matrices(matrix1, matrix2):
    # Check if the matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in matrix1 must be equal to the number of rows in matrix2.")

    # Initialize an empty result matrix with the appropriate dimensions
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    # Perform matrix multiplication
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Test the function with two sample matrices
matrix1 = [[1, 2, 3],
           [4, 5, 6]]
matrix2 = [[7, 8],
           [9, 10],
           [11, 12]]

result_matrix = multiply_matrices(matrix1, matrix2)

# Display the result matrix
for row in result_matrix:
    print(row)
