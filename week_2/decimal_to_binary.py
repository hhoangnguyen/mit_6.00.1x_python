# algorithm to convert decimal number to binary
# per: http://i.imgur.com/FAQLGyz.png
number = int(input('Input a decimal number: '))
binary = ''
while number > 0:
    # remainder of division by 2 to get the last digit
    remainder = number % 2
    # integer division to shift all digit to the left
    number = number // 2
    # accumulate binary
    binary = str(remainder) + binary
print('Binary: ' + binary)
