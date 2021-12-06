#Date Last Modified: 9/14/2021
#Author: Jack Geis
#Name: The John Hancock Forcast Reader
#Discrpition: This Program takes input from the user on the color and mode of the light,
#i.e. Blue or Red, Flashing or Steady,
#and gives a weather forcast using the input from the user

#Greets the user
print('Hello! Welcome to the The John Hancock Forcast Reader')

#Gets input from user to assign to variables.
color=input('Input one of these colors, "red" or "blue": ')
mode=input('Input one of these modes, "steady" or "flashing": ')

#Logic tree that uses input from the user to tell them the weather forcast.
if color=='red' and mode=='flashing':
    print('Snow is forming.')

if color=='red' and mode=='steady':
    print('Rain will be falling.')

if color=='blue' and mode=='flashing':
    print('Clouds are on the way.')

if color=='blue' and mode=='steady':
    print('Clear Skys.')

#Displays error if an input is incorrect.
if color!='blue' and color!='red':
    print('Error, color input is incorrect. Make sure all inputs are in lowercase')

if mode!='flashing' and mode!='steady':
    print('Error, mode input is incorrect. Make sure all inputs are in lowercase')

#Says goodbye and thanks the user for using the program
print('Have a wonderful day! And thank you for using The John Hancock Forcast Reader by Jack Geis.')
