"""
Write a function called general_poly, that meets the specifications below. For example, general_poly([1, 2, 3, 4])(10)
should evaluate to 1234 because 1∗10^3+2∗10^2+3∗10^1+4∗10^0.
"""


def general_poly(L):
    def poly_x(base):
        sum = 0
        for index in range(len(L)):
            sum += L[index] * (base ** (len(L) - 1 - index))
        return sum
    return poly_x


print(general_poly([1, 2, 3, 4])(10))
