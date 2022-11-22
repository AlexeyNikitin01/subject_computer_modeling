from numpy import arange
from math import exp, sqrt, sin, log1p, pi, cos

from matplotlib.pyplot import plot, ylabel, show
from sympy import diff


def fun_1(x):
    return exp((2*x+pi/2)/(x+4)) - exp((x-pi/2)/(2*x+1))


def fun_2(x):
    if x < 1.6:
        return cos(0.8-1.2*x) - 0.2*exp(1-0.5*x)
    return 1.8-x


def output_data():
    xs, ys_1, ys_2 = [], [], []
    for i in arange(0, 2, 0.1):
        xs.append(round(i, 3))
        ys_1.append(round(fun_1(i), 3))
        ys_2.append(round(fun_2(i), 3))
    return xs, ys_1, ys_2


if __name__ == '__main__':
    xs, ys_1, ys_2 = output_data()
    print(f'xs - {xs}', f'ys_1 {ys_1}', f'ys_2 {ys_2}', sep='\n')
    plot(xs, ys_1)
    plot(xs, ys_2)
    ylabel('gr')
    show()
