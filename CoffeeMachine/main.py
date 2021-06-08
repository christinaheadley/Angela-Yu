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

starting_water = resources['water']
starting_milk = resources['milk']
starting_coffee = resources['coffee']

espresso_used_water = MENU["espresso"]["ingredients"]["water"]
espresso_used_coffee = MENU["espresso"]["ingredients"]["coffee"]

latte_used_water = MENU["latte"]["ingredients"]["water"]
latte_used_milk = MENU["latte"]["ingredients"]["milk"]
latte_used_coffee = MENU["latte"]["ingredients"]["coffee"]

cappuccino_used_water = MENU["cappuccino"]["ingredients"]["water"]
cappuccino_used_milk = MENU["cappuccino"]["ingredients"]["milk"]
cappuccino_used_coffee = MENU["cappuccino"]["ingredients"]["coffee"]

used_water = 0
used_milk = 0
used_coffee = 0

remaining_water = starting_water - used_water
remaining_milk = starting_milk - used_milk
remaining_coffee = starting_coffee - used_coffee

while machine == "on":
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    cost = float(MENU[order]["cost"])

    report = (
        f"Water: {remaining_water}ml\n"
        f"Milk: {remaining_milk}ml\n"
        f"Coffee: {remaining_coffee}g"
        )

    def pay():
        print("Please insert coins.")
        quarters = float(input("How many quarters? ")) * .25
        dimes = float(input("How many dimes? ")) * .10
        nickels = float(input("How many nickels? ")) * .05
        pennies = float(input("How many pennies? ")) * .01
        return quarters + dimes + nickels + pennies
    paid = float(pay())

    def issue_change():
        if paid > cost:
            change = paid - cost
            print(f"Your change is ${change:.2f}.\nHere is your {order} ☕ Enjoy!")
        elif paid == cost:
            print(f"Here is your {order} ☕ Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
            exit()

    if order == "report":
        print(report)
        # for key, value in resources.items():
        #     print(key, ' : ', value, 'ml')
        continue
    elif order == "off":
        break

    elif order == "espresso":
        while paid >= cost:
            if remaining_water >= espresso_used_water:
                if remaining_coffee >= espresso_used_coffee:
                    # paid = float(pay())
                    # issue_change()
                    remaining_water -= espresso_used_water
                    remaining_coffee -= espresso_used_coffee
                    paid = float(pay())
                    issue_change()
                else:
                    print("Not enough ingredients available for selection.")
            else:
                print("Not enough ingredients available for selection.")
    elif order == "latte":
        while paid >= cost:
            if remaining_water >= latte_used_water:
                if remaining_coffee >= latte_used_coffee:

                    remaining_water -= latte_used_water
                    remaining_milk -= latte_used_milk
                    remaining_coffee -= latte_used_coffee
                    paid = float(pay())
                    issue_change()
                else:
                    print("Not enough ingredients available for selection.")
            else:
                print("Not enough ingredients available for selection.")
    elif order == "cappuccino":
        while paid >= cost:
            if remaining_water >= cappuccino_used_water:
                if remaining_coffee >= cappuccino_used_coffee:

                    remaining_water -= cappuccino_used_water
                    remaining_milk -= cappuccino_used_milk
                    remaining_coffee -= cappuccino_used_coffee
                    paid = float(pay())
                    issue_change()
                else:
                    print("Not enough ingredients available for selection.")
            else:
                print("Not enough ingredients available for selection.")
        else:
            print("Invalid request. Try again.")
            continue


# TODO: 1. take customer order
# TODO: 1. machine on/ off
# TODO: 2. print report of resources
# TODO: 4. verify resources available for order
# TODO: 5. payment
# TODO: 6. verify success or not
# TODO: 7. make drink
# TODO figure out how to add ml to water, milk and g to coffee
# TODO update resources to remove expended resources
