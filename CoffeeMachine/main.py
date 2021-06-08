MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine = "on"
money = 0


def available_ingredients(order_ingredients):  #order_ingredients = MENU[order]["ingredients"]
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def pay():
    print("Please insert coins.")
    quarters = float(input("How many quarters? ")) * .25
    dimes = float(input("How many dimes? ")) * .10
    nickels = float(input("How many nickels? ")) * .05
    pennies = float(input("How many pennies? ")) * .01
    return quarters + dimes + nickels + pennies


def issue_change():
    global money
    if paid >= cost:
        change = paid - cost
        money += cost
        print(f"Your change is ${change:.2f}.\nHere is your {order} ☕ Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


while machine == "on":
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
        continue
    elif order == "off":
        break
    else:
        drink = MENU[order]
        if available_ingredients(drink["ingredients"]):
            paid = pay()
            cost = float(MENU[order]["cost"])
            if issue_change():
                make_coffee(drink["ingredients"])


# TODO: 1. take customer order
# TODO: 1. machine on/ off
# TODO: 2. print report of resources
# TODO: 4. verify resources available for order
# TODO: 5. payment
# TODO: 6. verify success or not
# TODO: 7. make drink
# TODO figure out how to add ml to water, milk and g to coffee
# TODO update resources to remove expended resources


# ****************************************
# AY solution:
#
# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
#
# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True
#
#
# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total
#
#
# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
#
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")
#
#
# is_on = True
#
# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
