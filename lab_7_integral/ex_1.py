"""

1. Построить таблицу значений функции f(x) на отрезке [-2;2] с шагом 0.2.
Выбрать интервал, на котором функция принимает положительные значения.

2. вычислить интеграл

"""

from typing import Tuple, List

from scipy.integrate import quad
from scipy.optimize import fsolve

from numpy import sqrt, sin, arange, float_, around


def fun(x: float) -> float:
    return (sin(1 - x)) ** 3 - 0.3 * sqrt(x + 3)


def output_data(start: float | int, end: float | int, rg: float | int) -> Tuple[List[float], List[float]]:
    xs, ys = [], []
    for x in arange(start, end, rg):
        xs.append(x)
        ys.append(fun(x))
    return xs, ys


def _general(x1: float, x2: float, end_iter, k=0, s_iter=0, result=None) -> float:
    h = (x2 - x1) / end_iter
    result = 0
    start = x1 + k * h / 2
    for i in arange(s_iter, end_iter):
        x = start + i * h
        result += fun(x)
    result *= h
    return result


def ave_rec(x1: float, x2: float, end_iter) -> float:
    return _general(x1, x2, end_iter, k=1)


def right_rec(x1: float, x2: float, end_iter) -> float:
    return _general(x1, x2, end_iter+1, s_iter=1)


def left_rec(x1: float, x2: float, end_iter) -> float:
    return _general(x1, x2, end_iter)


def _mp_rec(x1: float, x2: float, end_iter) -> float:
    return _general(x1, x2, end_iter, s_iter=1, k=1, result=((fun(x1) + fun(x2)) / 2))


def trapezoid(x1: float, x2: float, iters, rtol=1e-5) -> float:
    """
    Method trapezoid
    """
    h = (x2 - x1) / iters
    result = (fun(x1) + fun(x2)) / 2
    for i in arange(1, iters):
        result += fun(x1 + i * h)
    result *= h

    err = max(1, abs(result))
    n1 = iters
    while err > abs(rtol * result):
        result_buff = result
        result = (result + _mp_rec(x1, x2, n1)) / 2
        n1 *= 2
        err = abs(result - result_buff)
    return result


def parabola(x1: float, x2: float, iters) -> float:
    """
    Formula Simpsona
    """
    h = (x2 - x1) / iters
    result = fun(x1) + 4 * fun(x1 + h) + fun(x2)
    for i in arange(1, iters/2):
        result += 2 * fun(x1 + (2 * i) * h) + 4 * fun(x1 + (2 * i + 1) * h)
    result *= h / 3
    return result


if __name__ == '__main__':
    start, end, rg = (-2, 2.2, 0.2)
    xs, ys = around(output_data(start, end, rg), 3)
    print(xs, ys, sep='\n')
    x1, x2 = float_(fsolve(fun, -1.2)), float_(fsolve(fun, 0))
    print(f'roots function x1 - {x1}, x2 - {x2}')
    result = quad(fun, x1, x2)
    print(f'insert fun in scipy {result[0]}')
    iters = 100
    print(f'ave rec {ave_rec(x1, x2, iters)}')
    print(f'left rec {left_rec(x1, x2, iters)}\nright rec {right_rec(x1, x2, iters)} ')
    print(f'trapezoid {trapezoid(x1, x2, iters)}')
    print(f'parabola {parabola(x1, x2, iters)}')
