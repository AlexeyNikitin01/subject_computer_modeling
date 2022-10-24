"""

Построить таблицу значений функции f(x) на отрезке [-2;2] с шагом 0.2.
Выписать отрезки, на которых функция меняет знак.

"""

from numpy import cos, round, array, arange
from scipy.optimize import fsolve, newton
from matplotlib.pyplot import show, plot, grid


def fun(x: float) -> float:
    """
    Given value function
    """
    return (0.2*((x-0.7)**2)) - (cos(2*x+1)/(x+3))


def output_data(step: float, start: int, end: int) -> list:
    """
    Output data - table with values x and y for function
    """
    xs = [round(x, 5) for x in arange(start, end, step)]
    ys = [round(fun(x), 3) for x in xs]
    result = array([xs, ys])
    return result


def search_route_fsolve() -> tuple:
    """
    Searching route function by fsolve
    """
    return fsolve(fun, [-2, 4])


def search_route_method_newton() -> tuple:
    """
    Searching route function by method newton
    """
    return newton(fun, [-2, 2])


def search_route_method_dichotomy() -> tuple:
    """
    Searching route function by method dichotomy
    """
    return fsolve(fun, -1.4), fsolve(fun, 0.8)


def show_fun_graphic(data) -> None:
    """
    Show function on graphic
    """
    plot(*data)
    grid(True)
    show()


if __name__ == '__main__':
    print(output_data(0.2, -2, 2))
    print(search_route_fsolve())
    print(search_route_method_newton())
    print(*search_route_method_dichotomy())
    show_fun_graphic(output_data(0.2, -2, 2))
