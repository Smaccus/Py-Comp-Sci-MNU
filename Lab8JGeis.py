# Date Last Modified: 10/19/2021
# Date Created: 10/19/2021
# Author: Jack Geis
# Program Name: Accountinator
# Descrpition/Algorithm: This program uses a function to calculate the ending balance and
#   total interest earned by first getting the principle balance and total years the 
#   account has been opened.    The program calls the function and passes the input,
#   then, the returned values are assigned to variables and printed out for the user.
#   all of this, except the function, are inside a while loop.  Lastly the program asks
#   the user if they want to run the program again and runs again if they dont enter 
#   'done' or 'Done'.



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
    print(format('Hello! Welcome to the Accountinator!',' ^45'))
    print(format('-','=^45'))
    print(' ', '\n')


# Function to claculate and return the total interest earned and the ending balance.
# Input: Principle balance and total years the account is opened, (pBalance and totYr).
# Return Value/Output: total interest earned and the ending balance, (interestEarned, endBal).

def balanceAndInterest(pBalance, totYr):
    interestRate = .04
    endBal = pBalance * ((1 + interestRate) ** totYr)
    interestEarned = endBal - pBalance
    return interestEarned, endBal


###########################
##### Main Program ########
###########################

# Calls greeting function

greeting()


# Sets the sentinel to its default so the while loop will run.

sen = 'Default'


# While loop that runs while the sentinel isnt == done or Done

while sen != 'Done' and sen != 'done':

    # Asks the user for the principle balance and total years the account has been open,
    # then assigns the inputs to their respective variables.

    pBalance = int(input('Please input principle balance here: '))

    totYr = int(input('Please input total years the account has been opened here: '))

    # Assigns the returned values of balanceAndInterest to global variables

    interestEarned, endBal = balanceAndInterest(pBalance, totYr)

    # Prints out the end balance and total interest in a nice format

    print('Ending Account Balance: ', format(endBal, '.2f'), '\n')

    print('Total Interest Earned: ',format(interestEarned, '.2f'), '\n')

    # Gives the user a sentinel

    sen = input('Enter "Done" to leave, to enter another account input anything: ')


# Calls farewell function

farewell()