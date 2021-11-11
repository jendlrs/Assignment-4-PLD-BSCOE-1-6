print ("\nWelcome to Jensen's fruit stand!")

def getMoney_andCostPerApple():
    moneyA= float(input("\nEnter the amount of money you have: \n> "))
    cost_per_appleA= float(input("\nPrice per apple: \n> "))
    return moneyA, cost_per_appleA

def max_apple_and_change (moneyA, cost_per_appleA):
    max_appleA = int(moneyA/cost_per_appleA)
    changeA = moneyA % cost_per_appleA
    short_moneyA = abs(money-cost_per_apple)
    return max_appleA, changeA, short_moneyA

def display(max_appleB, changeB, short_moneyB):
    if max_appleB > 1:
        print (f"\nYou can buy {max_appleB:,} apples and your change is {changeB:,.2f} pesos.\n")
    elif max_appleB == 1:
        print (f"\nYou can buy {max_appleB:,} apple and your change is {changeB:,.2f} pesos.\n")
    else:
        print (f"\nSorry, your money is not enough, you need atleast {short_moneyB:,.2f} to buy an apple\n")

money, cost_per_apple =getMoney_andCostPerApple()
max_apple, change, short_money = max_apple_and_change(money, cost_per_apple)
display(max_apple, change, short_money)