from numpy import arange
from math import exp, sqrt, sin, log1p, pi

from matplotlib.pyplot import plot, ylabel, show


def fun_1(x):
    return (sin(2*x+(pi/3)))**2/sqrt((x+3)/4) + log1p((3*x+11)/(x+1))/3


def fun_2(x):
    if x < 0.6:
        return (0.9*x-0.4)**2-0.3*exp(x-1)
    return x-0.8


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
