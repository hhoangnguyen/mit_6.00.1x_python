"""
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print 'beggh'
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print 'abc'
"""


def alphabet_to_array():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_array = {}
    for index in range(len(alphabet)):
        alphabet_array[alphabet[index]] = index
    return alphabet_array


def longest_alphabetical_substring(s):
    alphabet_array = alphabet_to_array()
    longest_length = 0    
    longest_substring = s[0]
    # loop through each char of the string
    for cur_index in range(len(s)):
        prev_index = cur_index
        cur_longest_length = 1 
        cur_str = s[cur_index]
        # at each char, loop through next char til end of string
        for index in range(cur_index + 1, len(s)):
            pre_index_char = s[prev_index]
            index_char = s[index]
            # compare with previous char
            if alphabet_array[pre_index_char] <= alphabet_array[index_char]:
                cur_longest_length += 1
                prev_index = index
                cur_str = cur_str + index_char
                if cur_longest_length > longest_length:
                    longest_substring = cur_str
                    longest_length = cur_longest_length
            else:
                break
    return longest_substring

string = 'ccdeabcee'
print(longest_alphabetical_substring(string))
