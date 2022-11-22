"""
1. Решить заданное дифференциальное уравнение для x = [1 , 2] методом
Эйлера и исправленным методом Эйлера с шагом 0.1 и 0.05, найти погрешность
решения. Вывести на экран таблицу значений, график функции – решения,
значения погрешности для обоих методов.
2. Для методов Эйлера и исправленного метода Эйлера найти шаг, при
котором погрешность решения будет меньше, чем 0.0001. Вывести на экран
полученные значения шага.
3. Решить заданное дифференциальное уравнение для x  [1 , 2], используя
встроенную функцию ode методами Рунге-Кутта и Адамса. Вывести на экран
таблицу значений и график функции – решения.
"""
from numpy import arange

from matplotlib.pyplot import plot, show

from scipy.integrate import solve_ivp, RK45


def fun(x, y):
    return y - 3 * y / x
    # return 0.25 * y**2 + x**2


def euler_with_err(x, xk, y, h=0.1, e=0.0001):
    """
    Method Euler with an error
    """
    x0 = x
    n = 2 * (xk - x0) / h
    D = float('inf')
    while D >= e:
        d = 0
        x = x0
        y1, y2 = y, y
        xs, ys = [], []
        for _ in arange(n):
            x += h / 2
            y1 += h / 2 * fun(x, y1)
            x += h / 2
            y1 += h / 2 * fun(x, y1)
            y2 += h * fun(x, y2)
            if d < abs(y2 - y1):
                d = abs(y2 - y1)
            xs.append(x), ys.append(y2)
        D = d
        h /= 2
        n = 2 * (xk - x0) / h
        # print(f'n {n} D {D} h/2 {h} y {y} xk {xk} x {x}')
    return x, y2, D, xs, ys, n


def euler_wo_err(x, xk, y, h=0.000098, e=0.0001):
    """
    Method Euler without an error
    """
    n = 2 * (xk - x) / h
    print(n)
    y1, y2 = y, y
    xs, ys = [], []
    d = 0
    for _ in arange(n):
        x += h / 2
        y1 += h / 2 * fun(x, y1)
        x += h / 2
        y1 += h / 2 * fun(x, y1)
        y2 += h * fun(x, y2)
        if d < abs(y2 - y1):
            d = abs(y2 - y1)
        xs.append(x), ys.append(y2)
    return x, y2, d, xs, ys


def correct_euler_with_err(x, xk, y, h=0.1, e=0.0001):
    """
    Correct method Euler with error
    """
    x0 = x
    n = 2 * (xk - x0) / h
    D = float('inf')
    while D >= e:
        d = 0
        x = x0
        y1, y2 = y, y
        xs, ys = [], []
        for _ in arange(n):
            x += h / 2
            k = fun(x, y1)
            F = 0.5 * (k + fun(x, y1 + k * h / 2))
            y1 += h / 2 * F
            x += h / 2
            k = fun(x, y1)
            F = 0.5 * (k + fun(x, y1 + k * h / 2))
            y1 += h / 2 * F
            k2 = fun(x, y2)
            F2 = 0.5 * (k2 + fun(x, y2 + k2 * h))
            y2 += F2 * h
            if d < abs(y2 - y1):
                d = abs(y2 - y1)
            xs.append(x), ys.append(y2)
        D = d
        h /= 2
        n = 2 * (xk - x0) / h
        # print(f'n {n} D {D} h/2 {h} y {y} xk {xk} x {x}')
    return x, y2, D, xs, ys, n


def correct_euler_wo_err(x, xk, y, h=0.1, e=0.0001):
    """
    Correct method Euler without error
    """
    n = 2 * (xk - x) / h
    d = 0
    y1, y2 = y, y
    xs, ys = [], []
    for _ in arange(n):
        x += h / 2
        y1 += _y1_05_h(x, y1, h)
        x += h / 2
        y1 += _y1_05_h(x, y1, h)
        y2 += _y2_05_h(x, y2, h)
        if d < abs(y2 - y1):
            d = abs(y2 - y1)
        xs.append(x), ys.append(y2)
    return x, y2, d, xs, ys


def _y1_05_h(x, y1, h):
    k = fun(x, y1)
    F = 0.5 * (k + fun(x, y1 + k * h / 2))
    return h / 2 * F


def _y2_05_h(x, y2, h):
    k2 = fun(x, y2)
    F2 = 0.5 * (k2 + fun(x, y2 + k2 * h))
    return h * F2


# def runge_kutta(f, t, x0):
#     n = len(t)
#     x = array([x0] * n)
#     for i in xrange(n - 1):
#         h = t[i + 1] - t[i]
#         k1 = h * f(x[i], t[i]) / 2.0
#         x[i + 1] = x[i] + h * f(x[i] + k1, t[i] + h / 2.0)
#
#     return x


if __name__ == '__main__':
    x0, xk = (1, 2)
    y0 = -2
    x, y, d, xs1, ys1, n = euler_with_err(x0, xk, y0)
    print(f'x {x}, y {y}, d {d} n {n}')
    x, y, d, xs2, ys2, n = correct_euler_with_err(x0, xk, y0)
    print(f'x {x}, y {y}, d {d} n {n}')
    _, _, _, xs1, ys1 = euler_wo_err(x0, xk, y0)
    _, _, _, xs2, ys2 = correct_euler_wo_err(x0, xk, y0)
    plot(xs1, ys1)
    plot(xs2, ys2)
    show()
