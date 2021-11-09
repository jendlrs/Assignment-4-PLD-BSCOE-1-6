print ("\nAdd your Personal Information\n")

def getNameAgeAddress():
    nameA= input ("What is your name? \n> ")
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
    print(f"\nHi, my name is {nameB}. I am {ageB} years old and I live in {addressB}. \n")

name, age, address = getNameAgeAddress()

display(name, age, address)