# Date Last Modified: //
# Date Created: //
# Author: Jack Geis
# Program Name:
# Descrpition/Algorithm: This program uses a function (common) to compare to lists for any elements in both lists.
# The function returns false if there are no same elements in the lists.



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
    print(format('Hello! Welcome to a Class Exercise!',' ^45'))
    print(format('-','=^45'))
    print(' ', '\n')

# Function to check if two lists have any numbers in common.
# Input: Two individual lists.
# Return Value/Output: True or False.

def common(listX,listY):
    boolean = False
    for x in listX:
        if x in listY:
            boolean = True
        return boolean

    

            
        


            


###########################
##### Main Program ########
###########################

# Calls greeting function

greeting()

listA = [1,2,3,4]

listB = [10,5,6,7,9]

listC = [10,1,4]

boolean = common(listA,listB)

if boolean == True:
    print('List A and B have an element in common.')
else:
    print('List A and B do not have an element in common.')

boolean = common(listA,listC)

if boolean == True:
    print('List A and C have an element in common.')
else:
    print('List A and C do not have an element in common.')


boolean = common(listB,listC)

if boolean == True:
    print('List B and C have an element in common.')
else:
    print('List B and C do not have an element in common.')



# Calls farewell function

farewell()