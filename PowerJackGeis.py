#Date last modified: 9/14/2021
#Author: Jack Geis
#Name of program: The Power Raiser
#Discription: This program takes gets two numbers from the user and raises the power
#of the first number by the second number, then displays the resulting product.

#Greets the user and instructs them on how to use the program.
print('Hello! this is The Power Raiser. Input the number you want to raise, then the number you wish to be the exponent.')

#Gets input from the user and assigns the input to a variable.
coefficient = float(input('Input the coefficient here: '))

exponent = float(input('Input the exponent here: '))


#Cmputes the answer, assignes computed value to variable 'Product', then prints 'Product'
Product=coefficient**exponent

print('Your answer is: ', Product)

#Says goodbye and thanks the user for using the program.
print('Goodbye, and thank you for using The Power Raiser! Have a great day. :D')
