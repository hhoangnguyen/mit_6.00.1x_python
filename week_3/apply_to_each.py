def apply_to_each(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    print(L)


def apply_func(funs, x):
    for f in funs:
        print(f(x))


def invert(item):
    return item * -1


def decrease_by_1(item):
    return item - 1


def square(item):
    return item**2

L = [1, -2, 3, 4]
apply_to_each(L, invert)
apply_to_each(L, decrease_by_1)
apply_to_each(L, square)

funs = [invert, decrease_by_1, square]
apply_func(funs, 3)
