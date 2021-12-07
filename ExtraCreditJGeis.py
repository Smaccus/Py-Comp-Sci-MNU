# Date Last Modified: 12/7/2021
# Date Created: 12/7/2021
# Author: Jack Geis
# Program Name: Listinator
# Descrpition/Algorithm: This program gets a list of ten integers from the user and makes copies of that list.
# Then, the copies are changed. The first copy has all of the duplicate numbers removed, then the list is displayed.
# The next list is sorted into numerical order and then displayed. The 3rd list-copy is changed to only contain 
# odd numbers from the original list and displays it. Lastly a for loop gets the sum of all the numbers in 
# the original list and displays it.



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



###########################
##### Main Program ########
###########################

# Calls greeting function

greeting()

# Makes empty lists for each different variation of UsrList

UsrList = []

noDupesUsrList = []

numericalUserList = []

oddUsrList = []

# Creates duplicates of UsrList to use for each variation

noDupesUsrList += UsrList

numericalUserList += UsrList

oddUsrList += UsrList

sumOfUsrList = 0

# Gets ten numbers from the user and puts them into Usr List

selNum = int(input('Please input the first of 10 numbers: '))

minimum = selNum

UsrList.append(selNum)

for i in range(9):
    selNum = int(input('\n','Please input your next number: '))
    UsrList.append(selNum)

# Creates duplicates of UsrList to use for each variation

noDupesUsrList += UsrList

numericalUserList += UsrList

oddUsrList += UsrList

sumOfUsrList = 0

# Removes all duplicates from the copy of UsrList, noDupesUsrList

for i in noDupesUsrList:
    index = noDupesUsrList.index(i)
    while i in noDupesUsrList:
        noDupesUsrList.remove(i)
    noDupesUsrList.insert(index, i)

# prints out the users original list

print('Your List: ',UsrList)

print('\n')

# prints out the list with no duplicates

print('Your list of numbers with no duplicates: ',noDupesUsrList)

# Sorts the copy of UsrList

numericalUserList.sort()

print('\n')

# Prints out the sorted list

print('All the numbers you entered in numerical order: ',numericalUserList)

# Gets the sum of all numbers in the list

for i in UsrList:
    sumOfUsrList += i

print('\n')

# prints the sum if the list

print('The sum of all the numbers you entered: ',sumOfUsrList)

# removes all even numbers from the list

for i in oddUsrList:
    if i % 2 == 0:
        oddUsrList.remove(i)

print('\n')

# Prints out all even numbers from the list

print('All the odd numbers that you entered: ',oddUsrList)

print('\n')

# prints out the users original list

print('Your list: ', UsrList)

# Calls farewell function

farewell()