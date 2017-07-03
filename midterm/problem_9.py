"""
Write a Python function that takes in two lists and calculates whether they are permutations of each other.
The lists can contain both integers and strings. We define a permutation as follows:
- the lists have the same number of elements
- list elements appear the same number of times in both lists

If the lists are not permutations of each other, the function returns False.
If they are permutations of each other, the function returns a tuple consisting of the following elements:
- the element occuring the most times
- how many times that element occurs
- the type of the element that occurs the most times

If both lists are empty return the tuple (None, None, None). If more than one element occurs the most number of times,
you can return any of them.

For example,

if L1 = ['a', 'a', 'b'] and L2 = ['a', 'b'] then is_list_permutation returns False
if L1 = [1, 'b', 1, 'c', 'c', 1] and L2 = ['c', 1, 'b', 1, 1, 'c']
    then is_list_permutation returns (1, 3, <class 'int'>) because the integer 1 occurs the most, 3 times,
    and the type of 1 is an integer (note that the third element in the tuple is not a string).
"""


def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    D1 = list_to_element_count_dict(L1)
    D2 = list_to_element_count_dict(L2)

    # if they don't have same number of element, False
    if len(D1) != len(D2):
        return False

    # if key in one list doesn't exist in another list, False
    for key in D1:
        if not check_if_key_in_dict(key, D2):
            return False
    for key in D2:
        if not check_if_key_in_dict(key, D1):
            return False

    # at this point, both dicts have same length AND each key in one list exists is a key in the other list
    for key in D1:
        # if count for each key doesn't match, False
        if D1[key] != D2[key]:
            return False

    return largest_count_times(L1)


def list_to_element_count_dict(L):
    """ Assumes L is a non-empty list of ints
        Returns a dictionary of each element as key and their corresponding count  as value """
    dictionary = {}
    for key in L:
        # if number not already in dict, add to dict by setting its to 1
        if not check_if_key_in_dict(key, dictionary):
            dictionary[key] = 1
        # otherwise, increase its count
        else:
            dictionary[key] += 1
    return dictionary


def largest_count_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    # dictionary to store each unique element (key) and their corresponding count (value)
    dictionary = list_to_element_count_dict(L)

    # flag to keep track whether we found target number
    found_count_times_item = False

    # start out with a very small number
    current_largest_item = None
    current_largest_count = 0

    # loop through dictionary of (number, count) pairs
    for number, count in dictionary.items():
        # found a larger number which occurs odd times, this is our new target
        if count > current_largest_count:
            current_largest_count = count
            current_largest_item = number
            found_count_times_item = True

    if found_count_times_item:
        return (current_largest_item, current_largest_count, type(current_largest_item))

    return (None, None, None)


def check_if_key_in_dict(key, dictionary):
    if key in dictionary:
        return True
    return False


L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']
print(is_list_permutation(L1, L2))
