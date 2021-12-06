# Date Last Modified: 11/1/2021
# Date Created: 10/26/2021
# Author: Jack (Main Program), Chloe (Function 1), Diego and Izan (Function 2), Gigi (Function 3).
# Program Name: BMI Calculator
# Descrpition/Algorithm: This program takes the users height and weight in pounds and inches,
# and converts it to kilograms and meters, then it uses the formula for calculating the BMI,
# and uses the calculated BMI to tell the user where they fall on the BMI index scale.


# Author of function: Jack
# Function to say goodbye.
# Input: null
# Return Value/Output: Uses print and format statements to thank and say goodbye to the user.

def farewell():
    print(' ', '\n')
    print(format('-','=^45'))
    print(format('Thank you for using Group 1\'s program!',' ^45'))
    print(format('Have a woderful day! :D',' ^45'))
    print(format('-','=^45'))
    print(' ', '\n')


# Author of function: Jack
# Function to greet the user.
# Input: null
# Return Value/Output: Uses print and format statements to greet the user.

def greeting():
    print(' ', '\n')
    print(format('-','=^45'))
    print(format('Hello! Welcome to the BMI Calculator!',' ^45'))
    print(format('-','=^45'))
    print(' ', '\n')

# Author of function: Diego and Izan
# Function to take the kilograms and meters of the function 1 and retrun the BMI of the person.
# Input: Kilograms and meters.
# Return Value/Output: BMI

def kilgmetBMI(kilograms, meters):
    bmi = kilograms / meters ** 2
    return bmi


# Author of function: Chloe
# Function to get the users height and weight and convert the height and weight to meters and kilos.
# Input: Null
# Return Value/Output: The coverted weight and height.

def convert():
    height = float(input(" Enter your height in inches: "))
    weight = float(input('\n'" Enter your weight in pounds: "))
    meters = height * 0.0254
    kilograms = weight * 0.453592
    return meters, kilograms


# Author of function: Angel
# Function to display the users BMI levels on the index.
# Input: The BMI calculated in the kilgmetBMI functioon.
# Return Value/Output: The users position on the BMI scale.

def category(bmi):
    if bmi >= 19 and bmi <= 24:
        print(" Your BMI is Normal.", '\n')
    if bmi >= 25 and bmi <= 29:
        print(" Your BMI is Overweight.", '\n')
    if bmi >= 30 and bmi <= 39:
        print(" Your BMI is Obese.", '\n')
    if bmi >= 40 and bmi <= 54:
        print(" Your BMI is Extreme Obesity.", '\n')



###########################
###### Main Program #######
####### Jack Geis #########
###########################

# Calls greeting function.

greeting()


# Sets variables equal to the returned values from the convert function.

meters, kilograms = convert()


# Sets a variable equal to the returned value from the kilgMetBMI function.

bmi = kilgmetBMI(kilograms, meters)


# Prints the users BMI.

print('\n','Your Body Mass Index is ', format(bmi,'.2f'),'\n')


# Calls the category function and passes it the bmi variable.

category(bmi)


# Calls farewell function.

farewell()