print ("\nWelcome to Jensen's fruit stand!\n The price per apple is 20 PHP\n The price per orange is 25 PHP")

def getApplesAndOranges():
    quantity_appleA= int(input("\nHow many apple(s) do you want to buy?\n> "))
    quantity_orangeA= int(input("\nHow many orange(s) do you want to buy?\n> "))
    return quantity_appleA, quantity_orangeA

def computeForTotalCost(quantity_AppleB, quantity_OrangeB):
    totalA= 20*quantity_AppleB + 25*quantity_OrangeB
    print (f"\nThe total amount is {totalA:,.0f} PHP.\n")

quantity_apple, quantity_orange = getApplesAndOranges()
total=computeForTotalCost(quantity_apple, quantity_orange)
