# Date Last Modified: 12/6/2021
# Date Created: 12/3/2021
# Author: Jack Geis
# Program Name: Validinator 
# Descrpition/Algorithm: This program takes a credit card number from the user and reverses it, then it doubles
# every second number of the credit card number, and if this results in a two digit number, adds the two digits
# together to get a single digit number. Next the program adds all of these numbers together, along with the sum
# of every odd number in the reversed credit card number. If this number results in a number that is divisible 
# into a whole number

import stacks

# Function to say goodbye
# Input: null
# Return Value/Output: Uses print and format statements to thank and say goodbye to the user.
def farewell():
    print(' ', '\n')
    print(format('-','=^45'))
    print(format('Thank you for using my program!',' ^45'))
    print(format('Have a woderful day! :D',' ^45'))
    print(format('-','=^45'))
    print(' ', '\n')


# Function to greet the user.
# Input: null
# Return Value/Output: Uses print and format statements to greet the user

def greeting():
    print(' ', '\n')
    print(format('-','=^45'))
    print(format('Hello! Welcome to the Card Number Validinator!',' ^45'))
    print(format('-','=^45'))
    print(' ', '\n')



###########################
##### Main Program ########
###########################

# Calls greeting function

greeting()

# Gets the credit card number to verify

CreditNum = input('Please enter your card number: ')

# Creates a stack

stack1 = stacks.getStack()

# Reverses the credit card number

for i in CreditNum:
    stacks.push(stack1, i)

list1 = []

for i in CreditNum:
    x = stacks.pop(stack1)
    list1.append(x)

reversedCardNum = list1

# Doubles every 2nd number in the reversed list

doubledList = []

for i in range(1,(len(reversedCardNum)),2):
    Num = reversedCardNum[i]
    Num = int(Num)
    Num = Num * 2
    doubledList.append(Num)

squished2XList = []

# Squishes all two digit numbers down to one digit by adding the two digits together

for num in doubledList:
    if num >= 10:
        num = str(num)
        x = num[0]
        y = num[1]
        x = int(x)
        y = int(y)
        z = x + y
        squished2XList.append(z)
    else:
        squished2XList.append(num)

sumOfSquished = 0

sumOfReversed = 0

# Gets the sum of all the numbers in the squished list

for i in squished2XList:
    sumOfSquished += i

reversedCardNumInt = []

# Makes a copy of the reversed card number list and converts it to an integer

for i in reversedCardNum:
    i = int(i)
    reversedCardNumInt.append(i)

# Gets the sum of every odd index number in the converted, reversed, credit card number

for i in range(0,(len(reversedCardNum)),2):
    SelNum = reversedCardNumInt[i]
    sumOfReversed = sumOfReversed + SelNum

# Adds the two sums together

sumReversedAndSquished = sumOfReversed + sumOfSquished

# Devides the resulting sum by 10

Dev10 = sumReversedAndSquished/10

# Converts the devided number into a string

Dev10Str = str(Dev10)

# Finds the index of the decimal

PositionOfDecimal = Dev10Str.index('.')

# Sets a variable equal to the position of the number just past the decimal using the index of the decimal

posistionPastDecimal = PositionOfDecimal+1

# Checks if the number right after the decimal is a 0, which would mean the number was devided by 10 into a whole number.
# If it was a whole number after being devided, the card is valid and the print statement prints that it is.
# Else, the card is invalid and the print statement prints that it is invalid.
if Dev10Str[posistionPastDecimal] == '0':
    print('Valid card number! :D')
else:
    print('Invalid card number! D:')

# Calls farewell function

farewell()