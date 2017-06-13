"""
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print 2
"""
string = 'azcbobobegghakl'
string_to_find = 'bob'


def get_num_match_string(str_to_find, s):
    match_count = 0
    for index in range(len(s)):
        sub_str = s[index:index + len(str_to_find)]
        if sub_str == str_to_find:
            match_count += 1
    print(match_count)
    
get_num_match_string(string_to_find, string)
