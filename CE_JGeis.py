# Date Last Modified: 10/14/2021
# Date Created: 10/14/2021
# Author: Jack Geis
# Program Name: CE(inator) 
# Descrpition/Algorithm: This program uses two functions to check if any 3 intigers are = 0
#   The first function is the main and passes variables the the second and calls it, then the second function
#   checks if any of the passed variables are 0s and returns True if there are, and False if there are not.
#   


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


# Main function to 
# Input: Returned values from function zeroCheck
# Return Value/Output: Prints 'True' or 'False' depending on the input

def main():
    x = 1
    y = 0
    z = 10
    Var = zeroCheck(x,y,z)
    if Var == True:
        print('True')
    else:
        print('False')


# Function to check if x, y, or z are assigned a 0, and returns True if one is, and False if none are set to 0.
# Input: x, y, and z are passed from main() to this function
# Return Value/Output: Returns True or False depending on the input

def zeroCheck(x,y,z):
    if (x == 0 or y == 0) or z == 0:
        return True
    else:
        return False


# Function to tell the user what the output means
# Input: null
# Return Value/Output: Uses print staements to describe to the user what the different outputs mean.

def description():
    print(' ''\n')

    print('False output means there are no zeros in the inputted numbers.''\n'
    'True output means there are no zeros in the numbers you inputted.')

    print(' ''\n')




###########################
##### Main Program ########
###########################



# Calls greeting function

greeting()


# Prints out the numbers being passed to zeroCheck and the output from zeroCheck

description()

x = int(input('Input first number here: '))

y = int(input('Input your second numner here: '))

z = int(input('INput your thrid number here: '))

print(' ''\n')

print(zeroCheck(x,y,z))

# Calls farewell function

farewell()