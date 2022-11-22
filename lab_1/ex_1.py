from numpy import arange
from math import exp, sqrt, sin, log1p

from matplotlib.pyplot import plot, ylabel, show
from sympy import diff


def fun_1(x):
    return (((3*x+1)**(2/3))/(x+2)) + (sin((2*x+1)/(x+1)))**2


def fun_2(x):
    if x < 1:
        return sin(1.9*x-0.5)+0.3*log1p(x+2.5)
    return x + 0.3


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
