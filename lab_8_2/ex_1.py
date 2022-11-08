"""
Для заданной функции f(x) построить таблицу значений функции f(x) на
отрезке [-2;2] с шагом 0,2. Выбрать интервал, на котором функция имеет
только минимум, длиной 0,4.

2. Найти минимум функции f(x) с точностью 0.00001.
 методом дихотомии
 методом тяжелого шарика
 используя встроенную функцию fminseach
Вывести на экран полученные результаты в строку.

3. Для заданной функции f(x) найти минимум с учетом заданного
ограничения методом штрафных функций. Вывести на экран результаты
поиска условного минимума в виде таблицы.
"""
from numpy import sqrt, sin, round, sign

from scipy.optimize import fmin_cg, fmin, minimize


def fun_sx(x):
    return (x+0.5)**2 * (1-sign(x+1))


def fun(x: float | int, b=None) -> float | int:
    if b:
        return (0.3*sqrt(x+3) - (sin(1-x))**3) + (b*fun_sx(x))  # x >= -0.5
    return 0.3*sqrt(x+3) - (sin(1-x))**3


def dichotomy(start_slice: float | int, end_slice: float | int, e: float = 0.00001) -> None:
    h = e/3
    err = end_slice - start_slice
    while err >= e:
        avg = (start_slice + end_slice)/2
        x1 = avg-h
        x2 = avg+h
        if fun(x1) > fun(x2):
            start_slice = x1
        else:
            end_slice = x2
        err = end_slice - start_slice
        print(f'x {round(avg, 6)} function {round(fun(avg), 6)}'
              f' error {round(err, 6)}')
    return None


def method_hard_ball(start_slice: float | int, h: float = 0.001, e: float = 0.00001):
    x = start_slice
    while abs(h) >= e:
        while fun(x) > fun(x+h):
            x += h
        h /= -2
        x += h
        print(f'x {round(x, 6)} function {round(fun(x), 6)}'
              f' error {round(h, 6)}')
    return None


def method_(x0: float | int, b: float | int, h=0.01, e=0.0001, d=1) -> None:
    while d > e:
        x = x0
        while abs(h) >= e:
            while fun(x, b) > fun(x+h, b):
                x += h
            x += h
            h /= -2
        print(f'b {round(b, 6)} x {round(x, 6)}')
        b *= 100
        d = abs(x-x0)
        x0 = x
        h = 0.01
    return None


if __name__ == '__main__':
    a, b = [-2, 2]
    print('-'*50)
    dichotomy(a, b)
    print('-'*50)
    method_hard_ball(-1.8, b)
    print('-' * 50)
    print(f"\n{fmin_cg(fun, [-1.8])}\n{'-' * 50}")
    print(f"\n{fmin(fun, -1.8)}\n{'-' * 50}")
    print(f"\n{minimize(fun, -1.8, method='Nelder-Mead')}\n{'-' * 50}")  # dichotomy
    method_(-2, 1)
