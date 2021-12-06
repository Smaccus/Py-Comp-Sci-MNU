#Date Last Modified: 9/28/2021
#Date Created: 9/28/2021
#Author: Jack Geis
#Program Name: Numberator 1000
#Program Description/Algorithm: This program asks the user if they want to add numbers,
#    then takes and adds that number to any past inputs and prompts the user again if they want
#    to add a new number, once the user inputs 'N' the loop ends and the program displays the amount
#    of times the user entered a number, along with the total of all the numbers entered and the
#    average (mean) number entered.

#First thing to do in any program is to welcome the user :D
print('\n'' ')


print(format('Welcome to the Numberator 1000!','-^60'))


print('\n'' ')

#Sets variables to default to insure the while loop runs correctly.
loopy = 'y'

usrNum = 0

totalInputs = 0

#While loop that will run until the user input sets var 'loopy' to anything other than 'y' or 'Y'.
while loopy != 'n' and loopy != 'N':

    usrNum = usrNum+int(input('Enter number here: '))

    totalInputs = totalInputs+1

    loopy = input('Do you want to add a number Y/N? ')


#Calculates Average input number, then displays' variables totalInputs, usrNum and usrNumAvg.
#Note: Formatting is grouped seperate from other code.
usrNumAvg = usrNum/totalInputs

print('\n'' ')
print(format('=','-^60'))


print('This is the amount of times a number was entered',format('.','.>3'),format(totalInputs,'7.0f'))

print('This is the total of all entered numbers',format('.','.>11'),format(usrNum,'7.0f'))

print('This is the average input',format('.','.>26'),format(usrNumAvg,'7.2f'))


print(format('=','-^60'))

#Formatted Farewell.
print('\n'' ')


print(format('Thank you for using the Nuberator 1000!','♥^60'))
