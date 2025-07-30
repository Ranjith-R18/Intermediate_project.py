from main import *

def resources_sufficient(order):
    for item in order:
        if resources[item]-order[ item]<0:
            print("Sorry . There is not enough resources.  Sorry for the inconvenience")
            return False
        return True
        
def process_coins():
    print("please insert coins.")
    total = int(input("how many quarters? ")) * 0.25
    total += int(input("how many dimes? ")) * 0.10
    total += int(input("how many nickles? ")) * 0.05
    total += int(input("how many pennies? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} change")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry! that's not enough money. Money refunded ")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

is_on =True
while is_on:
        choice=input("What would you like?(espresso,latte,cappuccino) : ").lower()
        if choice =="off":
            is_on = False
        elif choice=="return":
            print(f"Water : {resources["water"]} ml")
            print(f"Milk : {resources["milk"]} ml")
            print(f"Coffee : {resources["coffee"]} ml")
            print(f"profit : {profit}")
        else:
           drink = MENU[choice]
           if resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])      