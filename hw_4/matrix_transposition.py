"""
✔ Напишите функцию для транспонирования матрицы
"""
my_matrix = [[1, 2, 3], [4, 5, 6]]
print(my_matrix)


def transp_matrix(matrix):
    transposed_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix


print(transp_matrix(my_matrix))
