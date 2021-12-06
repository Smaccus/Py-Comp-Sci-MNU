#Date Last Modified: 9/28/2021
#Date Created: 9/27/2021
#Author: Jack Geis
#Program Name: Commissionator
#Program Description/Algoritm:

#Welcomes user.
print('Hello! Welcome to the Commissionator!')
print(' ''\n')

#Sets a variable so the while loop will emmediately begin running.
loop_going = 'Y'

#While loop that will run while var loop_going is == 'Y' or 'y'.
#The loop will run the inside code until the user gets to the last input
#   and enters something other than 'Y' or 'y'.
while loop_going == 'Y' or loop_going == 'y':
    #Assigns variables to user input after asking them to enter Info regarding the variable
    sales = input('Input amount of sales: ')
    comm_rate = int(input('What is your commision rate: '))
    #Calculates the amount made via commissions, then prints the product.
    #    in a format that includes 2 decimal points and a '$'.
    commission = comm_rate*sales
    print('Your commission is: $', format(commision,'.2f'))
    #Allows the user to exit the program by entering something other than 'y' or 'Y'.
    loop_going = input('Do you want to enter another commission y/n? ')

#Thanks the User and gives farewell.
print('Thank you for using the Commissionator! Have a wonderful day!')
