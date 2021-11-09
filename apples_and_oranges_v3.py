def getApplesAndOranges():
    quantity_appleA= int(input("\nHow many apple do you want to buy?\n> "))
    quantity_orangeA= int(input("\nHow many orange do you want to buy?\n> "))
    return quantity_appleA, quantity_orangeA

def computeForTotalCost():
    totalA= 20*quantity_apple + 25*quantity_orange
    return totalA

def display(totalA):
    print (f"\nThe total amount is {totalA:,.0f}\n")
#steps
#ask how many apples and oranges the user wants to buy.

quantity_apple, quantity_orange =getApplesAndOranges()

#add the fix price and formula

total= computeForTotalCost()
#display total
display(total)