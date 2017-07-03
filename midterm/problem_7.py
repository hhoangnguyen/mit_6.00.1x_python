"""
Write a function called dict_invert that takes in a dictionary with immutable values
 and returns the inverse of the dictionary.
 The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d.
 The value for a key in the inverse dictionary is
 a sorted list (increasing order) of all keys in d that have the same value in d.

Here are two examples:

If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
"""


def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    inverted_dict = {}
    for key, value in d.items():
        if not check_if_key_in_dict(value, inverted_dict):
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
            # sort the list in increasing order
            inverted_dict[value].sort()
    return inverted_dict


def check_if_key_in_dict(key, dictionary):
    if key in dictionary:
        return True
    return False

d = {8: 6, 2: 6, 4: 6, 6: 6}
print(dict_invert(d))
