#Date Last Modified: 10/5/2021
#Date Created: 10/5/2021
#Author: Jack Geis
#Program Name: Numberator V2.0
#Descrpition/Algorithm: This program asks the user to enter a positive number
#   and stores it, it also starts a while loop with a -1 sentinel,
#   it sets a min and max variable in the loop aswell. Lastly it keeps a running total of
#   user inputs. When the user enters '-1' the while loop stops, and the average is calculated.
#   Lastly the min, max, number of inputs, and average are all printed in a nice format.

#Welcome the user
print(format('-','=^60'))
print(format('Hello! Welcome to the Numberator V2.0!',' ^60'))
print(format('-','=^60'))

total = 0

inp = 0

totalInputs = 0

inp = int(input('Enter a positive number here, enter -1 to exit: '))

klein = inp

groß = inp

#Runs while loop until the user enters a -1

while inp != -1:
    #calculates the total for averageing
    total += inp

    totalInputs += 1
    
    #Sets Min and Max (klein is small in german, and groß,
    #pronounced 'Grossah' is german for large.
    if groß < inp:
        groß = inp

    if klein > inp:
        klein = inp
    #Makes sure that inp is never set to the sentinel

    inp = int(input('Enter a positive number here, enter -1 to exit: '))
   

#protects against division by zero in the case of the loop
#being skipped.
if totalInputs != 0:
    avg = total/totalInputs
else:
    avg = -1

#Uses print statements to output the amount of numbers enetered,
#the min and max number entered, and the average number entered.
print('\n'' ')
print(format('=','-^60'))


print('This is the amount of times a number was entered',format('.','.>3'),format(totalInputs,'7.0f'))

print('This is the minimum input',format('.','.>26'),format(klein,'7.0f'))

print('This is the max input',format('.','.>30'),format(groß,'7.0f'))

print('This is the average input',format('.','.>26'),format(avg,'7.2f'))


print(format('=','-^60'))
print('\n'' ')

#Formatted Farewell.

print(format('Thank you for using the Nuberator V2.0!','♥^60'))
