# Date Last Modified: //
# Date Created: //
# Author: Jack Geis
# Program Name:
# Descrpition/Algorithm:



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

# Function to go through the shopping list
# Input: groceryList
# Return Value/Output: null

def shop(groceryList):
    for x in range(len(groceryList) - 1):
        print('Need: ', groceryList[x])
        input('Press Enter when ready for next item: ')



###########################
##### Main Program ########
###########################

# Calls greeting function

greeting()

groceryList = []

senAddRemove = (input('Please input the first item on your grocery list, input "done" when finished: '))

    
while senAddRemove != 'done' and senAddRemove != 'Done':

    groceryList.append(senAddRemove)
    
    senAddRemove = (input('Input the next item onto your grocery list, input "done" when finished: '))

print('Your list:')
for x in range(len(groceryList)):
    item = groceryList.__getitem__(x)
    print(item)

while senAddRemove != 'shop':
    senAddRemove = (input('Do you want to add/remove anything from your list?''\n''Or are you ready to shop?''\n''(Input "add", "remove", or "shop".): '))
    if senAddRemove == 'add':
        additionalItem = input('Input additional item: ')
        groceryList.append(additionalItem)
        print('Your list:')
        for x in range(len(groceryList)):
            item = groceryList.__getitem__(x)
            print(item)
    if senAddRemove == 'remove':
        remove = input('Input the item you want to remove: ')
        groceryList.remove(remove)
        print('Your list:')
        for x in range(len(groceryList)):
            item = groceryList.__getitem__(x)
            print(item)

shop(groceryList)
    


# Calls farewell function

farewell()