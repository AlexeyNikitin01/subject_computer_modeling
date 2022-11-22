"""
x1 >= 0 x2 >= -1
h1 = x1 h2 = x2 + 1
"""

from scipy.optimize import fmin

from numpy import sign, exp


def extend_fun1(x, b=2):
    return (2 * x[0] + 3.5 * x[1] + exp(x[0] ** 2 + 0.5 * x[1] ** 2))\
           + b*(x[0]**2 * (1-sign(x[0])) + (x[1] + 1)**2 * (1-sign(x[1]+1)))


def extend_fun10(x, b=20):
    return (2 * x[0] + 3.5 * x[1] + exp(x[0] ** 2 + 0.5 * x[1] ** 2))\
           + b*(x[0]**2 * (1-sign(x[0])) + (x[1] + 1)**2 * (1-sign(x[1]+1)))


def extend_fun100(x, b=200):
    return (2 * x[0] + 3.5 * x[1] + exp(x[0] ** 2 + 0.5 * x[1] ** 2))\
           + b*(x[0]**2 * (1-sign(x[0])) + (x[1] + 1)**2 * (1-sign(x[1]+1)))


def extend_fun1000(x, b=2000):
    return (2 * x[0] + 3.5 * x[1] + exp(x[0] ** 2 + 0.5 * x[1] ** 2))\
           + b*(x[0]**2 * (1-sign(x[0])) + (x[1] + 1)**2 * (1-sign(x[1]+1)))


if __name__ == '__main__':
    x1, y1 = fmin(func=extend_fun1, x0=[-1, -0.5])
    x2, y2 = fmin(func=extend_fun10, x0=[x1, y1])
    x3, y3 = fmin(func=extend_fun100, x0=[x2, y2])
    x4, y4 = fmin(func=extend_fun1000, x0=[x3, y3])
    print(f'{x1, y1}\n{x2, y2}\n{x3, y3}\n{x4, y4}')
