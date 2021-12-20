# Date Last Modified: 11/18/2021
# Date Created: 11/12/2021
# Author: Jack Geis
# Program Name: The Naminator
# Descrpition/Algorithm: This program copies two files into lists and asks the user for a name. It then checks if their name is in either
# of the lists and sets a variable to true if it is in the list. Then two if statements print that their name was a common boy/girl name 
# between 2000 and 2009, depending on which lists the name was in.



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
    print(format('Hello! Welcome to the Naminator!',' ^45'))
    print(format('-','=^45'))
    print(' ', '\n')


###########################
##### Main Program ########
###########################

# Calls greeting function

greeting()

# variables

bNames = 'BoyNames.txt'

gNames = 'GirlNames.txt'

openBNames = open(bNames, 'r')

openGNames = open(gNames, 'r')

# Sets varaibles to default.

commonBName = False

commonGName = False

index = 1

# Asks the user for a name and sets a variable to their input.

bList = []

gList = []

sentinel = 'y'

while sentinel == 'y':
    
    # Asks the use which gender their name is.

    select = input('Is your name a boy or girl name, b/g?: ')

    # Asks the user for a name and sets a variable to their input.

    name = input('Please input your name: ')

    # copies the BoyNames.txt file into bList.
    if select == 'b':
        for line in openBNames:
            bList.append(line)

        # Checks if the name is in bList.

        if (name + '\n') in bList:
            commonBName = True

    # copies the GirlNames.txt into gList.
    if select == 'g':
        for line in openGNames:
            gList.append(line)

    # Checks if the name is in gList.

        if (name + '\n') in gList:
            commonBName = True


    # Prints out that their name was a common boy or girl name 

    if commonBName == True:
        print('Your name was a common boy between 2000 and 2009.')

    if commonGName == True:
        print('Your name was a common girl name between 2000 an 2009.')

    # if their name is not in the list, prints out that it was not a common name between 2000 and 2009.

    if commonGName == False and commonBName == False:
        print('Your name was not a common name between 2000 and 2009.')
    
    sentinel = input('Would you like to enter another name, y/n?: ')

openBNames.close()

openGNames.close()

# Calls farewell function

farewell()