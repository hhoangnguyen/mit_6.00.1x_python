# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    # print("  ", len(wordlist), "words loaded.")
    print(len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    str = ''
    for char in secretWord:
        if char not in lettersGuessed:
            str = str + '_ ' # added a space per suggestion
        else:
            str = str + char
    return str


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


def welcome(secretWord):
    '''
    Helper function to print welcome strings
    :param secretWord:
    :return:
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', str(len(secretWord)), 'letters long')


def separator():
    '''
    Helper function to print a line separator after each guess
    :return:
    '''
    print('-------------')


def isGuessedCharInWord(char, word):
    '''
    Helper function to check if char is in a given word
    :param char:
    :param word:
    :return:
    '''
    if char in word:
        return True
    return False


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    welcome(secretWord)
    separator()

    # list contains all guessed chars
    lettersGuessed = []

    # start the game with 8 allowed wrong guesses
    numGuessLeft = 8

    while numGuessLeft > 0 and not isWordGuessed(secretWord, lettersGuessed):
        print('You have', numGuessLeft, 'guesses left.')
        print('Available letters: ', getAvailableLetters(lettersGuessed))

        # save user input
        guessedChar = input('Please guess a letter: ').lower()

        # if user input already in letterGuessed, let them know, keep their numGuessLeft the same
        if isGuessedCharInWord(guessedChar, lettersGuessed):
            print('Oops! You\'ve already guessed that letter:', getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guessedChar)

            # if input is in secretWord, good guess
            if isGuessedCharInWord(guessedChar, secretWord):
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            else:
                print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))

                # bad guess, decrease by 1
                numGuessLeft -= 1
        separator()

    if numGuessLeft > 0:
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was', secretWord)
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)

secretWord = 'huyhoangnguyen'
hangman(secretWord)
