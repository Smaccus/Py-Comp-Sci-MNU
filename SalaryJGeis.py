# Date Last Modified: 10/12/2021
# Date Created: 10/12/2021
# Author: Jack Geis
# Program Name: Salaryinator
# Descrpition/Algorithm: This program uses a main for loop to pass numbers to functions that calculate 
#                      two salary options, one that pays $100 a day, and a secind that pays one dollar
#                      a day but the salary doubles every day. There are two functions that calculate 
#                      each total using the number passed from the main for loop. 

# Function to print the lyrics for the program.
# Input: null.
# Return value: null.

def lyrics():
    print('Hi Ho')
    print('Hi Ho')
    print('It\'s off to work I go!')

# Function to Calculate the salary for Option 1.
# Input: Amount of days.
# Retrun Value: Total pay for each day passed to the function.

def Opt1(days):
    Tot1 = 100 * days
    return Tot1

# Function to calculate the salary for Option 2.
# Input: Amount of days.
# Return Value: Total pay for each day passed to the function.

def Opt2(days):
    Salary2 = 1
    Tot2 = 0
    for x in range(days):
        Tot2 += Salary2
        Salary2 += Salary2
    return Tot2

###########################
##### Main Program ########
###########################

# Prints a greeting.

print(format('-','=^45'))

print('Hello! Welcome to the Salaryinator!')

print(format('-','=^45'))

# For loop to pass the amount of days to each function.
# No Input
# Output: The lyrics, Amount of worked days, and Total pay for each option
#         according to the number of days.

for days in (1,5,10,15):
    print(' ''\n')
    
    lyrics()

    print('Days Worked: ',days)

    Opt1Salary = Opt1(days)
    
    print ('Option one paid',Opt1Salary)
    
    Opt2Salary = Opt2(days)
    
    print('Option two paid',Opt2Salary)


# Prints a farewell.

print(format('-','=^45'))

print('Thanks for using the Salaryinator! Goodbye!')

print(format('-','=^45'))