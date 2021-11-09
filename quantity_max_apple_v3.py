#Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
#Display the maximum number of apples that you can buy and the remaining money that you will have.
#Display the output in the following format.
#You can buy ___ apples and your change is ___ pesos.

def getMoney_andCostPerApple():
    moneyA= float(input("\nEnter the amount of money you have: \n>"))
    cost_per_appleA=float(input("\nPrice per apple: \n>"))
    return moneyA, cost_per_appleA

getMoney_andCostPerApple()