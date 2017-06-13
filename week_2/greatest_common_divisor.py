def gcd_iter(a, b):
    guess = min(a, b)
    while ((a % guess) > 0) or ((b % guess) > 0):
        guess -= 1
    return guess

print('GCD iter: ', gcd_iter(8, 12))


def gcd_recur(a, b):
    """
    Per Euclid: https://en.wikipedia.org/wiki/Euclidean_algorithm#Worked_example
    """
    if b == 0:
        return a
    return gcd_recur(b, a % b)

print('GCD recur: ', gcd_recur(8, 12))
