#Date: 9/13/2021
#Written by: Jack Geis, Stevo Fleuriot, and Wisdom Gibson.
#Group #: 4
#For: Professor Hale, Entry to Computer Science.

#Program: Drake Equation Claculator.
#Algorithm: N = R * p * n * f * i * c * L
#Goal: Calculate N



#Greeting the user.
print('Hello! this is the Drake Equation Calculator, Please input in float form: %10 input .10')


#Asks user for their desired input, then uses input to define the variables in the Drake Equation.
n=float(input('Input average number of planets that could potentially support life for each star with planets: '))

i=float(input('Input the percetage that will go on to develop intelligent life: '))

c=float(input('Input the percent of intelligent civilizations that will communicate with other planets: '))

l=float(input('Input expected lifetime of intelligent civilizations: '))

R=7

p=.40

f=.13


#Calculating the equation using the variables.
N=R*p*n*f*i*c*l

#Prints the claculated number.
print('This is your answer.')

print(N)


#Goodbye and thank you to user.
print('Thank you for using the Jack, Stevo, and Wisdom (JSW) version of the Drake Equation Calculator! Have a wonderful day! :D')
