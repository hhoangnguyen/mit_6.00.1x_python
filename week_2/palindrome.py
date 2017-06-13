def is_palindrome(string):
    # base cases
    # if string is of length <= 1, it is a palindrome
    if len(string) <= 1:
        return True

    # recursive case: first == last AND smaller sub-problem is palindrome
    return string[0] == string[-1] and is_palindrome(string[1:-1])

print('Palindrome: ', is_palindrome('cabcbac'))
