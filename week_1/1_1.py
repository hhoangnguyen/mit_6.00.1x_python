"""
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print: 5
"""
string = 'azcbobobegghakl'


def is_valid_vowel(char):
    if char == 'a':
        return True
    if char == 'e':
        return True
    if char == 'i':
        return True
    if char == 'o':
        return True
    if char == 'u':
        return True
    return False


def get_num_vowels(s):
    num_vowels = 0
    for index in range(len(s)):
        if is_valid_vowel(s[index]):
            num_vowels += 1
    print(num_vowels)
    
get_num_vowels(string)
