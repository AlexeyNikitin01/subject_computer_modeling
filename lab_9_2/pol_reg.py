from matplotlib import pyplot as plt

from numpy import poly1d, polyfit, float_, linspace, mean, sum, ones, array
from numpy.linalg import lstsq


def polyfit_(x, y, degree):
    results = {}
    coeffs = polyfit(x, y, degree)
    p = poly1d(coeffs)
    yhat = p(x)
    ybar = mean(y)
    ssreg = sum((yhat-ybar)**2)
    sstot = sum((y - ybar)**2)
    results['r_squared'] = ssreg / sstot
    return results


def backslash(vals_y, vals_x):
    b = lstsq(array([ones(len(vals_y)), vals_x, vals_x**2, vals_x**3]).T, vals_y)
    ym = b[0][0] + b[0][1]*vals_x + b[0][2]*vals_x**2 + b[0][3]*vals_x**3
    s_main = sum((vals_y-mean(vals_y))**2)
    sse = sum((vals_y-ym)**2)
    r2 = 1 - sse / s_main
    return r2, b


if __name__ == '__main__':
    xs = '0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95 1'.split(' ')
    xs = array([float_(x) for x in xs])
    ys = '0.35 0.33 0.5 0.37 0.81 0.8 0.53 0.63 0.96 ' \
         '0.93 1.32 1.04 1.47 1.36 1.66 2.12 2.37 2.14 2.31 2.91 2.84'.split(' ')

    ys = array([float_(y) for y in ys])

    print(backslash(ys, xs))
    print(polyfit_(xs, ys, 3))
    print(polyfit(xs, ys, deg=3))

    # show poly regression
    model = poly1d(polyfit(xs, ys, deg=3))
    polyline = linspace(0, 1, 50)
    plt.scatter(xs, ys)
    plt.plot(polyline, model(polyline))
    plt.show()
