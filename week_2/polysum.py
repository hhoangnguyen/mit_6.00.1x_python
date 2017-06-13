import math


def polysum(n, s):
    """
    Sum the area and square of the perimeter of regular polygon
    :param n: number of sides
    :param s: length of each side
    :return: (float) sum the area and square of the perimeter rounded to 4 decimal places
    """

    # area of regular polygon
    area = 0.25 * n * (s**2) / math.tan(math.pi / n)

    # square perimeter of polygon
    square_perimeter = (n*s)**2

    # sum rounded to 4 decimal places, cast to float afterward
    return float("{0:.4f}".format(area + square_perimeter))
