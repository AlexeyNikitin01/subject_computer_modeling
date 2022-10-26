from typing import List, Tuple

from numpy import array, around, take


MATRIX = List[List[int | float]]
VECTOR = List[int | float] | List[List[int | float]]


def yacobi(matrix: MATRIX, vector: VECTOR, epl: float, vector_init: VECTOR = None, gs=False) -> VECTOR:
    """
    A * x = B
    param: A - MATRIX, B - VECTOR
    return: x
    """
    matrix, vector = _process_matrix(matrix, vector)
    if vector_init:
        approximate_vector = vector_init.copy()
    else:
        approximate_vector = [val/matrix[i][i] for i, val in enumerate(vector)]

    cal_epl = epl + 1  # init epl
    result = []
    while cal_epl > epl:
        x0 = _cal_sum(matrix, approximate_vector, vector, gs)
        approximate_vector = x0
        result = _cal_sum(matrix, approximate_vector, vector, gs)
        cal_epl = _mul_norm(result, approximate_vector)
    return result


def _cal_sum(matrix: MATRIX, app_vector: VECTOR, vector: VECTOR, gs) -> VECTOR:
    result_vector = []
    for ind_matrix, row in enumerate(matrix):
        result = float(vector[ind_matrix])/matrix[ind_matrix][ind_matrix]
        for ind_vector, (val_mat, val_vec) in enumerate(zip(row, app_vector)):
            if ind_vector != ind_matrix:
                result -= val_mat * val_vec/matrix[ind_matrix][ind_matrix]
        if gs:
            app_vector[ind_matrix] = result
        result_vector.append(result)
    return result_vector


def _mul_norm(x1: VECTOR, x0: VECTOR) -> float:
    return max([abs(x1_val - x0_val) for x1_val, x0_val in zip(x1, x0)])


def _process_matrix(matrix: MATRIX, vector: VECTOR) -> Tuple[MATRIX, VECTOR]:
    buff_matrix, buff_vector = [], []
    for i in range(len(matrix[0])):
        col = take(matrix, [i], axis=1)
        ind = list(col).index(max(col))
        buff_matrix.append(matrix[ind])
        buff_vector.append(vector[ind])
    return buff_matrix, buff_vector


def _process_matrix_2(matrix: MATRIX, vector: VECTOR) -> Tuple[MATRIX, VECTOR]:
    for i in range(len(matrix)):
        ration = matrix[i][i]
        for j in range(len(matrix)):
            matrix[i][j] = 0 if i == j else -matrix[i][j]/ration
        vector[i] = vector[i]/ration
    return matrix, vector


if __name__ == '__main__':
    A = array([[1, 3, 9, 1],
               [1, 1, 2, 5],
               [2, 7, 3, 2],
               [4, 2, 1, 1]])
    B = array([[10], [6], [12], [9]])
    print(yacobi(A, B, 0.001))
