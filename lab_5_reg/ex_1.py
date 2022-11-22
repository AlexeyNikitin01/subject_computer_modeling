from numpy import array, float_

from scipy.stats import linregress

from matplotlib.pyplot import show, plot, legend

from lab_9_2.ex_1 import search_r2, back_slash

from pprint import pprint

if __name__ == '__main__':
    xs = '0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95 1'.split(' ')
    xs = array([float_(x) for x in xs])
    ys = '0.35 0.33 0.5 0.37 0.81 0.8 0.53 0.63 0.96 0.93 1.32 1.04 1.47 1.36 1.66 2.12 2.37 2.14 2.31 ' \
         '2.91 2.84'.split(' ')

    ys = array([float_(y) for y in ys])

    res = linregress(xs, ys)
    pprint(res)
    print(f'r2 {res.rvalue}')

    print(search_r2(vals_y=ys, vals_x=xs, regress_vals=res))

    print(f'back slash {back_slash(vals_y=ys, vals_x=xs)}')

    # show graph
    plot(xs, ys, 'o', label='original data')
    plot(xs, res.intercept + res.slope * float_(xs), 'r', label='fitted line')
    legend()
    show()
