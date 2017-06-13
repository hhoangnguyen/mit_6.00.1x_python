def multi_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result
print('Multiplication Iterative:', multi_iter(3, 2))


def multi_recur(a, b):
    # base case, a * 0 = 0
    if b == 0:
        return 0
    # recursive steps a * b = (a * b-1) + a
    return multi_recur(a, b - 1) + a
print('Multiplication Recursive:', multi_recur(3, 2))


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print('Factorial', factorial(3))
