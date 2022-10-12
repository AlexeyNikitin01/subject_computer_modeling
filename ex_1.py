from matplotlib.pyplot import plot, ylabel, show
from numpy import arange
import math


def fun_1(x):
    return math.exp(x)


def fun_2(x):
    return math.sqrt(x)


def output_data():
    xs = []
    ys_1 = []
    ys_2 = []
    for i in arange(0, 2, 0.1):
        xs.append(i)
        ys_1.append(fun_1(i))
        if i >= 1:
            ys_2.append(fun_2(i))
        else:
            ys_2.append(fun_2(i))
    return xs, ys_1, ys_2


if __name__ == '__main__':
    xs, ys_1, ys_2 = output_data()
    plot(xs, ys_1)
    plot(xs, ys_2)
    ylabel('gr')
    show()
