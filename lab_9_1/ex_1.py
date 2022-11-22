from matplotlib.pyplot import contour, figure, show, clabel

from numpy import exp, meshgrid, arange


def fun(x1: int | float, x2: int | float) -> int | float:
    return 2 * x1 + 3.5 * x2 + exp(x1 ** 2 + 0.5 * x2 ** 2)


def vals(start: int, stop: int):
    x = arange(start, stop, 0.08)
    y = arange(start, stop, 0.08)
    xgrid, ygrid = meshgrid(x, y)
    zgrid = fun(xgrid, ygrid)
    return xgrid, ygrid, zgrid


if __name__ == '__main__':
    x, y, z = vals(-2, 2)
    fig = figure()
    axes = fig.add_subplot(projection='3d')
    axes.plot_surface(x, y, z, edgecolor='k', linewidth=0.3)
    show()
    cs = contour(x, y, z, 50)
    clabel(cs)
    show()
