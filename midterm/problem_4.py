'''
Write a function is_triangular that meets the specification below.
A triangular number is a number obtained by the continued summation of integers starting from 1.
For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.
'''


def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    # if k is not positive
    if k <= 0:
        return False

    # current sum
    sum = 0
    # loop through including k because 1 is a triangular
    for number in range(k+1):
        sum += number
        if sum == k:
            return True
        if sum > k:
            return False
    return False

k = 10
print(is_triangular(k))
