from functools import wraps


def type_logger(f):

    @wraps(f)
    def wrapper(*args, **kwargs):
        nums = [i for i in (*args, *kwargs.values())]
        n = [f'{f.__name__}({el}: {type(el)})' for el in nums]
        print(*n, *f(*args, **kwargs), sep=',\n')

    return wrapper


@type_logger
def calc_cube(*a, **b):
    nums = [i for i in (*a, *b.values()) if isinstance(i, int) or isinstance(i, float)]
    return [el ** 3 for el in nums]


# a = calc_cube(4, {'str': 15}, (9, 'len'), {5, 10}, [12, 6], 'hello', firstname='Ruslan')
a = calc_cube(4, 125, 234.3, ui=23.2, io=2)
# print(calc_cube.__name__)
help(calc_cube)
