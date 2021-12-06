# Date Last Modified: 11/15/2021
# Date Created: 11/11/2021
# Author: Jack Geis
# Program Name: The Passinator
# Descrpition/Algorithm: This program uses python functions and a for loop to check if the password that a user inputs has at least:
    # one number, one lowercase, and one uppercase letter, has no spaces, and is within 8-16 characters in length.
    # A variable is assigned to the True or False outputs of the conditions and used in an if statement. If one of the variables 
    # is True, excluding the range which is reversed, a dicision tree checks which parameters were not met and prints out to the
    # user which parts of their password need to change.



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
    print(format('Hello! Welcome to a Class Exercise!',' ^45'))
    print(format('-','=^45'))
    print(' ', '\n')






###########################
##### Main Program ########
###########################

# Calls greeting function

greeting()

password = input('Please input your password: ')

isUpper = password.isupper()

isLower = password.islower()

isSpace = False

for i in password:
    if i == ' ':
        isSpace = True

isNumber = password.isalpha()

if len(password) < 8 or  len(password) > 16:
    isInRange = False
else:
    isInRange = True

if ((isUpper == True or isLower == True) or (isSpace == True or isNumber == True)) or isInRange == False:
    print('Invalid Password')
    if isUpper  == False and isLower == True:
        print('Your password must have at least one uppercase letter.')
    if isLower == False and isUpper == True:
        print('You must include a lowercase letter in your password.')
    if isSpace == True:
        print('Your password cannot have any spaces.')
    if isNumber == True:
        print('Your password must have at least one number.')
    if isInRange == False:
        print('Your password must be between 8-16 characters.')

if ((isUpper == False and isLower == False) and (isSpace == False and isNumber == False)) and isInRange == True:
    print('Password accepted :D')



# Calls farewell function

farewell()