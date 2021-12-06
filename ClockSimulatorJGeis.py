#Date Last Modified: 9/30/2021
#Date Created: 9/30/2021
#Author: Jack Geis
#Program Name: Clockinator
#Descrpition/Algorithm: This program uses loops to make a simulation of a clock.
#First the program welcomes the user. It then sets all variables to the default
#and asks the user if they want to run the program. if the input is not a n or N
#the program starts the while loop containing for loops that set the variables
#to the number corrosponding with the time and prints them.
#every cycle of 12 hours variable AM_PM changes to a 1 or a 2, if its a one
#the program prints 'AM' before the hours, minutes and seconds.
#If AM_PM != 1 the program will print 'PM' before it prints the hours, minutes
#and seconds.

#Welcome the user
print(format('=','=^40'))
print('Hello! Welcome to the Clockinator!')
print(format('=','=^40'))

#variables 
AM_PM = 1
hours = 1
minutes = 0
seconds = 0
sentinel = input('Would you like the clockinator to run, y/n? ')
while sentinel != 'n' and sentinel != 'N':
   for AM_PM in (1,3):
     for hours in range(1,12):
          for minutes in range(0,60):
            for seconds in range(0,60):
                if AM_PM == 1:
                    print('AM',hours,'.',minutes,'.',seconds)
                else:
                    print('PM',hours,'.',minutes,'.',seconds)
   sentinel = input('Would you like the clockinator to keep running, y/n? ')
