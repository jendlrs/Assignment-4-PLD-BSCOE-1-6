#Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
#Display the maximum number of apples that you can buy and the remaining money that you will have.
#Display the output in the following format.
#You can buy ___ apples and your change is ___ pesos.

print ("\nWelcome to Jensen's fruit stand!")

def getMoney_andCostPerApple():
    moneyA= float(input("\nEnter the amount of money you have: \n> "))
    cost_per_appleA=float(input("\nPrice per apple: \n> "))
    return moneyA, cost_per_appleA

def max_apple_and_change (moneyA, cost_per_appleA):
    max_appleA = int(moneyA/cost_per_appleA)
    changeA = moneyA % cost_per_appleA
    return max_appleA, changeA

def display(max_appleB, changeB):
    if max_appleB > 1:
        print (f"\nYou can buy {max_appleB:,} apples and your change is {changeB:,.2f} pesos\n")
    elif max_appleB == 1:
        print (f"\nYou can buy {max_appleB:,} apple and your change is {changeB:,.2f} pesos\n")

money, cost_per_apple =getMoney_andCostPerApple()
max_apple, change = max_apple_and_change(money, cost_per_apple)
display(max_apple, change)