from typing import List, Tuple

from numpy import array, append

MATRIX = List[List[int]]
VECTOR = List[int]


def gauss(matrix: MATRIX, vector: VECTOR) -> VECTOR:
    matrix = append(matrix, vector, axis=1)

    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            raise ZeroDivisionError

        for j in range(i+1, len(matrix)):
            ration = matrix[j][i] / matrix[i][i]
            for k in range(len(matrix[0])):
                matrix[j][k] -= ration*matrix[i][k]

    vector[-1] = matrix[-1][-1]/matrix[-1][-2]

    for i in range(len(matrix)-2, -1, -1):
        vector[i] = matrix[i][len(matrix)]
        for j in range(i+1, len(matrix)):
            vector[i] -= matrix[i][j]*vector[j]
        vector[i] = vector[i]/matrix[i][i]
    return vector


if __name__ == '__main__':
    A = array([[1., 3., 9., 1.],
               [1., 1., 2., 5.],
               [2., 7., 3., 2.],
               [4., 2., 1., 1.]])
    B = array([[10.], [6.], [12.], [9.]])

    result_vector = gauss(A, B)
    print(result_vector)
