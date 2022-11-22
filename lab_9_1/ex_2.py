from ex_1 import fun

from numpy import sqrt, exp

from scipy.optimize import fmin


def search_min(x1=-1, x2=-0.5, e=0.0001, d=float('inf')):
    print(x1, x2, fun(x1, x2))
    while d >= e:
        p1 = x1
        p2 = x2
        h = 0.01
        while abs(h) >= e:
            while fun(x1, x2) > fun(x1, x2+h):
                x2 += h
            x2 += h
            h /= -2

        h = 0.001
        while abs(h) >= e:
            while fun(x1, x2) > fun(x1+h, x2):
                x1 += h
            x1 += h
            h /= -2
        d = sqrt((p1-x1)**2+(p2-x2)**2)
    print(x1, x2, fun(x1, x2), d)


def fun_1(x):
    return 2 * x[0] + 3.5 * x[1] + exp(x[0] ** 2 + 0.5 * x[1] ** 2)


if __name__ == '__main__':
    search_min()
    print(fmin(func=fun_1, x0=[-1, -0.5]))
