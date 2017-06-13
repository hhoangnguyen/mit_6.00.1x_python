"""
In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search,
the computer will guess the user's secret number!

Note: your program should use input to obtain the user's input! Be sure to handle the case
when the user's input is not one of h, l, or c.

When the user enters something invalid, you should print out a message to the user explaining
you did not understand their input. Then, you should re-ask the question, and prompt again for input. For example:
"""

# initial setup
print('Please think of a number between 0 and 100!')
hint_string = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low" + \
              "Enter 'c' to indicate I guessed correctly."
low = 0
high = 100
answer = (high + low) / 2
print('Is your secret number ' + str(int(answer)) + '?')
print(hint_string, end=' ')

# initial input prompt
guess = input('')

while guess != 'c':
    if guess == 'h':
        # guess was too high
        high = answer
        answer = int((high + low) // 2)
    elif guess == 'l':
        # guess was too low
        low = answer
        answer = int((high + low) // 2)
    else:
        print('Sorry, I did not understand your input.')
        
    print('Is your secret number ' + str(answer) + '?')
    print(hint_string, end=' ')
    guess = input('')
print('Game over. Your secret number was: ' + str(answer))
