#Create a program that will ask how many apples and oranges you want to buy.
#Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
#Display the output in the following format.
#The total amount is ______.

def getApplesAndOranges():
    quantity_appleA= int(input("\nHow many apple do you want to buy?\n> "))
    quantity_orangeA= int(input("\nHow many orange do you want to buy?\n> "))
    return quantity_appleA, quantity_orangeA

def computeForTotalCost():
    totalA= 20*quantity_apple + 25*quantity_orange
    return totalA

#steps
#ask how many apples and oranges the user wants to buy.

quantity_apple, quantity_orange =getApplesAndOranges()

#add the fix price and formula

total= computeForTotalCost()
#display total
