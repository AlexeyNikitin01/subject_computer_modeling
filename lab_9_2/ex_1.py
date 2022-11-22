from scipy.stats import linregress

from numpy.linalg import lstsq
from numpy import sum, mean, float_, arange, array, ones

from matplotlib.pyplot import show, plot, legend


def search_r2(vals_y, vals_x, regress_vals) -> float:
    ym = regress_vals.intercept + regress_vals.slope * float_(vals_x)
    sse = sum((ym-vals_y)**2)
    s_main = sum((vals_y-mean(vals_y))**2)
    r2 = 1 - sse / s_main
    return r2


def back_slash(vals_y, vals_x):
    vals_x = array(vals_x)
    b = lstsq(array([ones(len(vals_y)), vals_x]).T, vals_y)
    ym = b[0][0] + b[0][1] * vals_x
    s_main = sum((vals_y - mean(vals_y)) ** 2)
    sse = sum((vals_y - ym) ** 2)
    r2 = 1 - sse / s_main
    return r2, b


if __name__ == '__main__':
    # data vals
    xs = '0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95 1'.split(' ')
    xs = list([float_(x) for x in xs])
    ys = '0.35 0.33 0.5 0.37 0.81 0.8 0.53 0.63 0.96 ' \
         '0.93 1.32 1.04 1.47 1.36 1.66 2.12 2.37 2.14 2.31 2.91 2.84'.split(' ')
    ys = list([float_(y) for y in ys])

    res = linregress(xs, ys)
    print(res)
    print(f"R-squared from linregress: {res.rvalue**2:.6f}")

    print(f'search r2 {search_r2(ys, xs, res)}')
    print(f'back slash {back_slash(ys, xs)}')

    # show graph
    plot(xs, ys, 'o', label='original data')
    plot(xs, res.intercept + res.slope * float_(xs), 'r', label='fitted line')
    legend()
    show()

