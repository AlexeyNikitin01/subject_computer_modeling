"""

Преобразовать заданную матрицу коэффициентов А и вектора свободных
членов В для решения системы линейных уравнений.
A * X = B итерационными методами.

"""
from typing import List, Union
from pprint import pprint

from numpy import array, around, matmul
from numpy.linalg import inv, solve

from gauss import gauss
from yacobi import yacobi
from gauss_seidel import gauss_seidel


MATRIX = List[List[int]]
VECTOR = List[int]


class Matrix:
    def __init__(self, matrix: MATRIX):
        self.matrix = matrix
        self.inv_matrix = inv(matrix)

    def __str__(self):
        for i in self.matrix:
            print(f'|| {" | ".join(map(str, i))} ||')
        return f'size matrix - {len(self.matrix)} and {len(self.matrix[0])}'

    def __repr__(self):
        return f'size matrix - {len(self.matrix)} x {len(self.matrix[0])}\ntype values {type(self.matrix[0][0])}' \
               f'\ntype matrix {type(self.matrix)}'

    def __matmul__(self, other: Union[MATRIX, VECTOR]):
        return around(matmul(self.matrix, other), 3)

    def is_invert(self):
        self.matrix, self.inv_matrix = self.inv_matrix, self.matrix

    def search_solve(self, other: Union[MATRIX, VECTOR]):
        return around(solve(self.matrix, other), 3)

    def method_gauss(self, vector):
        return gauss(self.matrix, vector)

    def method_yacobi(self, vector):
        return yacobi(self.matrix, vector, 0.001)

    def method_gauss_seidel(self, vector):
        return gauss_seidel(self.matrix, vector, 0.001)


if __name__ == '__main__':
    A = array([[1, 3, 9, 1],
               [1, 1, 2, 5],
               [2, 7, 3, 2],
               [4, 2, 1, 1]])
    B = array([[10], [6], [12], [9]])
    matrix = Matrix(A)
    matrix.is_invert()
    print(matrix @ B)
    matrix.is_invert()
    print(matrix.search_solve(B))
    print(around(matrix.method_gauss(array([[10.], [6.], [12.], [9.]])), 3))
    print(around(matrix.method_yacobi(B), 3))
    print(around(matrix.method_gauss_seidel(B), 3))
