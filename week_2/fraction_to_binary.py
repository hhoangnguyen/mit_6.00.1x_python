# algorithm to convert fraction number to binary
# same idea with additional step to convert fraction to whole number
number = float(input('Input a float: '))

# convert to whole number using power of 2
power = 0
while (number * (2 ** power)) % 1 != 0:
    power += 1

number = int(number * (2 ** power))
binary = ''
while number > 0:
    # remainder of division by 2 to get the last digit
    remainder = number % 2
    # integer division to shift all digit to the left
    number = number // 2
    # accumulate binary
    binary = str(remainder) + binary

# pad 0s in front of binary if needed
for i in range(power - len(binary)):
    binary = '0' + binary

# make sure it also works with decimal number greater than 1
binary = binary[0:-power] + '.' + binary[-power:]

print('Binary: ' + binary)
