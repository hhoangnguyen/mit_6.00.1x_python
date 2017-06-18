import string


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # list to store alphabet
    letter_list = list(string.ascii_lowercase)

    # remove guessed chars from letter_list
    for char in lettersGuessed:
        if char in letter_list:
            letter_list.remove(char)

    # construct string of left over chars
    str = ''
    for char in letter_list:
        str = str + char
    return str

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
