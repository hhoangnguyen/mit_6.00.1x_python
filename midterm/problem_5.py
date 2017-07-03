'''
Write a Python function that takes in a string and prints out a version of this string that does not contain any vowels,
according to the specification below. Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.

For example, if s = "This is great!" then print_without_vowels will print Ths s grt!.
If s = "a" then print_without_vowels will print the empty string .
'''


def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    vows = 'AaEeIiOoUu'
    new_string = ''
    for index in range(len(s)):
        is_vow = False
        for vow_index in range(len(vows)):
            if vows[vow_index] == s[index]:
                is_vow = True
        if not is_vow:
            new_string = new_string + s[index]
    print(new_string)

s = "This is great!"
print_without_vowels(s)
