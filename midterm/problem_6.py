def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    # dictionary to store each unique element (key) and their corresponding count (value)
    dictionary = list_to_element_count_dict(L)

    # flag to keep track whether we found target number
    found_largest_odd_times_number = False

    # start out with a very small number
    current_largest_number = float("-infinity")

    # loop through dictionary of (number, count) pairs
    for number, count in dictionary.items():
        # found a larger number which occurs odd times, this is our new target
        if number > current_largest_number and count % 2 == 1:
            current_largest_number = number
            found_largest_odd_times_number = True

    if found_largest_odd_times_number:
        return current_largest_number

    return None


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


def check_if_key_in_dict(key, dictionary):
    if key in dictionary:
        return True
    return False

L = [3, 0, 5, 3, 5, 3]
print(largest_odd_times(L))
