#Create a program that will ask for name, age and address. 
#Display those details in the following format.
#Hi, my name is _____. I am ____ years old and I live in _____ .
def getNameAgeAddress():
    nameA= input ("\nWhat is your name? \n> ")
    ageA= input ("\nHow old are you? \n> ")
    addressA= input ("\nWhere do you live? \n> ")
    return nameA, ageA, addressA

#steps
#ask for name, age, and address
name, age, address =getNameAgeAddress()
#display