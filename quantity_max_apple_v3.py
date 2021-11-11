#Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
#Display the maximum number of apples that you can buy and the remaining money that you will have.
#Display the output in the following format.
#You can buy ___ apples and your change is ___ pesos.

def getMoney_andCostPerApple():
    moneyA= float(input("\nEnter the amount of money you have: \n>"))
    cost_per_appleA=float(input("\nPrice per apple: \n>"))
    return moneyA, cost_per_appleA

def max_apple_and_cost (moneyA, cost_per_appleA):
    max_apple = int(moneyA//cost_per_appleA)
    changeA = moneyA % cost_per_appleA
    print (f"\nYou can buy {max_apple:,} apple/s and your change is {changeA:,.2f}\n")

money, cost_per_apple =getMoney_andCostPerApple()
max_apple_and_cost(money, cost_per_apple)