#Create a program that will ask for name, age and address. 
#Display those details in the following format.
#Hi, my name is _____. I am ____ years old and I live in _____ .
def getNameAgeAddress():
    nameA= input ("\nWhat is your name? \n> ")
    while True:
        try:
          ageA= int(input("\nHow old are you? \n> "))
          break
        except ValueError:
            print("\nThe age you entered is invalid. Please enter your age in numbers only")
            continue
    addressA= input ("\nWhere do you live? \n> ")
    return nameA, ageA, addressA

def display(nameB, ageB, addressB):
    print(f"\nHi, my name is {nameB}. I am {ageB} years old and I live in {addressB} \n")

#steps
#ask for name, age (in numbers), and address
name, age, address = getNameAgeAddress()

#display
display(name, age, address)