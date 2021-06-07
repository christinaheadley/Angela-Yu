MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
money = {"Money": 0}
# water = {"Water": 300}
# milk = {"Milk": 200}
# coffee = {"Coffee": 100}

while machine == "on":
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # remaining_water = resources["water"] - MENU[order]["ingredients"]["water"]
    # remaining_milk = resources["milk"] - MENU[order]["ingredients"]["milk"]
    # remaining_coffee = resources["coffee"] - MENU[order]["ingredients"]["coffee"]
    # print(remaining_water)
    # print(MENU[order]["ingredients"]["water"])
    # print(resources["water"])
    # report = (
    #     f"Water: {remaining_water}ml\n"
    #     f"Milk: {remaining_milk}ml\n"
    #     f"Coffee: {remaining_coffee}g"
    #     )
    if order == "off":
        break
    elif order == "report":
        # print(remaining_water)
        # for key, value in resources.items():
        #     print(key, ' : ', value, 'ml')
        continue
    elif order != "espresso" and order != "latte" and order != "cappuccino":
        print("Invalid request. Try again.")
        continue
    else:
        def pay():
            print("Please insert coins.")
            quarters = float(input("How many quarters? ")) * .25
            dimes = float(input("How many dimes? ")) * .10
            nickels = float(input("How many nickels? ")) * .05
            pennies = float(input("How many pennies? ")) * .01
            return quarters + dimes + nickels + pennies

        # paid = "${:,.2f}".format
        paid = float(pay())
        cost = float(MENU[order]["cost"])
        if paid >= cost:
            change = paid - cost
            print(f"Your change is ${change:.2f}.\nHere is your {order} ☕ Enjoy!")
        elif paid == cost:
            print(f"Here is your {order} ☕ Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")


    # def issue_change():
remaining_water = resources["water"] - order["water"]
print(remaining_water)
# TODO: 1. take customer order
# TODO: 1. machine on/ off
# TODO: 2. print report of resources
# TODO: 4. verify resources available for order
# TODO: 5. payment
# TODO: 6. verify success or not
# TODO: 7. make drink
# TODO figure out how to add ml to water, milk and g to coffee
# TODO update resources to remove expended resources
