def is_in(char, aStr):
    low = 0
    high = len(aStr)
    average = int((high + low) / 2)

    # base cases
    if len(aStr) == 0:
        return False
    if low > high:
        return False

    # recursive cases
    if char == aStr[average]:
        return True
    elif char < aStr[average]:
        return is_in(char, aStr[low:average])
    else:
        return is_in(char, aStr[average+1: high])

print('Is In: ', is_in('c', 'abbcde'))
