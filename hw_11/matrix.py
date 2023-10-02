"""Создайте класс Матрица. Добавьте методы для:
вывода на печать,
сравнения,
сложения,
*умножения матриц"""


class Matrix:
    def __init__(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if isinstance(matrix[i][j], int) or isinstance(matrix[i][j], float):
                    self.matrix = matrix
                else:
                    raise ValueError('Элементами матрицы должны быть только числа')

    def __str__(self):
        """Метод представления для пользователя"""
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __repr__(self):
        """Метод представления для создания экземпляра"""
        return f'Matrix({self.matrix})'

    def __eq__(self, other):
        """Сравнение двух матриц"""
        if not isinstance(other, Matrix):
            raise ValueError('Неверный формат, укажите 2 матрицы верного формата')
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return f'Нельзя сравнивать матрицы разных размеров'
        else:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        return False
            return True

    def __add__(self, other):
        """Сложение двух матриц"""
        if not isinstance(other, Matrix):
            raise ValueError('Неверный формат, укажите 2 матрицы верного формата')
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return f'Нельзя складывать матрицы разных размеров'
        else:
            result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                      range(len(self.matrix))]
        return Matrix(result)

    def __mul__(self, other):
        """Умножение двух матриц"""
        if not isinstance(other, Matrix):
            raise ValueError('Неверный формат, укажите 2 матрицы верного формата')
        if len(self.matrix[0]) != len(other.matrix):
            return f'Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы'
        else:
            result = [[0 for _ in range(len(other.matrix[0]))] for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(self.matrix[0])):
                        result[i][j] += (self.matrix[i][k] * other.matrix[k][j])
            return Matrix(result)
