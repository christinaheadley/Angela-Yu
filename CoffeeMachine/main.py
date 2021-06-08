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
starting_water = int(resources['water'])
starting_milk = int(resources['milk'])
starting_coffee = int(resources['coffee'])
money = 0
        # cost = float(MENU[order]["cost"])
        # remaining = list(calc_ingredients())


def calc_ingredients(drink):
    needed_water = starting_water - int(MENU[drink]["ingredients"]["water"])
    needed_milk = starting_milk - int(MENU[drink]["ingredients"]["milk"])
    needed_coffee = starting_coffee - int(MENU[drink]["ingredients"]["coffee"])
    return needed_water, needed_milk, needed_coffee


report = (
        f"Water: {starting_water}ml\n"
        f"Milk: {starting_milk}ml\n"
        f"Coffee: {starting_coffee}g"
        )


while machine == "on":
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "report":
        print(report)
        continue
    elif order == "off":
        break
    elif order == "espresso":
        needed = list(calc_ingredients("espresso"))
        for x in needed:
            if x < 0:
                print(f"Missing {x} to create {order}.")
                break
            else:
                continue

        def pay():
            print("Please insert coins.")
            quarters = float(input("How many quarters? ")) * .25
            dimes = float(input("How many dimes? ")) * .10
            nickels = float(input("How many nickels? ")) * .05
            pennies = float(input("How many pennies? ")) * .01
            return quarters + dimes + nickels + pennies
        paid = float(pay())
        cost = float(MENU[order]["cost"])

        def issue_change():
            if paid > cost:
                change = paid - cost
                print(f"Your change is ${change:.2f}.\nHere is your {order} ☕ Enjoy!")
            elif paid == cost:
                print(f"Here is your {order} ☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
                exit()
        issue_change()
        continue

    elif order == "latte":
        needed = list(calc_ingredients("latte"))
        for x in needed:
            if x < 0:
                print(f"Missing {x} to create {order}.")
                break
            else:
                continue

        def pay():
            print("Please insert coins.")
            quarters = float(input("How many quarters? ")) * .25
            dimes = float(input("How many dimes? ")) * .10
            nickels = float(input("How many nickels? ")) * .05
            pennies = float(input("How many pennies? ")) * .01
            return quarters + dimes + nickels + pennies

        paid = float(pay())
        cost = float(MENU[order]["cost"])

        def issue_change():
            if paid > cost:
                change = paid - cost
                print(f"Your change is ${change:.2f}.\nHere is your {order} ☕ Enjoy!")
                ending_water = starting_water - needed_water
            elif paid == cost:
                print(f"Here is your {order} ☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
                exit()
        issue_change()
        continue
    elif order == "cappuccino":
        needed = list(calc_ingredients("cappuccino"))
        for x in needed:
            if x < 0:
                print(f"Missing {x} to create {order}.")
                break
            else:
                continue

        def pay():
            print("Please insert coins.")
            quarters = float(input("How many quarters? ")) * .25
            dimes = float(input("How many dimes? ")) * .10
            nickels = float(input("How many nickels? ")) * .05
            pennies = float(input("How many pennies? ")) * .01
            return quarters + dimes + nickels + pennies

        paid = float(pay())
        cost = float(MENU[order]["cost"])

        def issue_change():
            if paid > cost:
                change = paid - cost
                print(f"Your change is ${change:.2f}.\nHere is your {order} ☕ Enjoy!")
            elif paid == cost:
                print(f"Here is your {order} ☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
                exit()
        issue_change()
        #
        # print(needed)
        # print(type(remaining))
        # for x in remaining:
        #     if x < 0:
        #         print(f"Missing {x} to create.")
        #         continue
        #     else:
        #         print("ok")

# while machine == "on":
#     def take_order():
#         order = input("What would you like? (espresso/latte/cappuccino): ").lower()
#         # cost = float(MENU[order]["cost"])
#         return order
#
#     if take_order() == "report":
#         # global report
#         # print(report)
#         # for key, value in resources.items():
#         #     print(key, ' : ', value, 'ml')
#         continue
#     elif take_order() == "off":
#         break
#     else:
#         def calc_ingredients(order) -> object:
#             remaining_water = 0 - MENU[order]["ingredients"]["water"]
#             remaining_milk = starting_milk - MENU[order]["ingredients"]["milk"]
#             remaining_coffee = starting_coffee - MENU[order]["ingredients"]["coffee"]
#             return int(remaining_water), int(remaining_milk), int(remaining_coffee)
#         remaining = list(calc_ingredients(take_order()))
#
#         print(remaining)
#         print(type(remaining))
#
#     for x in remaining:
#         if x < 0:
#             print(f"Missing {x} to create.")
#             continue
#         else:
#             print("ok")

    # report = (
    #     f"Water: {remaining[0]}ml\n"
    #     f"Milk: {remaining[1]}ml\n"
    #     f"Coffee: {remaining[2]}g"
    #     )

    # def pay():
    #     print("Please insert coins.")
    #     quarters = float(input("How many quarters? ")) * .25
    #     dimes = float(input("How many dimes? ")) * .10
    #     nickels = float(input("How many nickels? ")) * .05
    #     pennies = float(input("How many pennies? ")) * .01
    #     return quarters + dimes + nickels + pennies
    # paid = float(pay())

    # def issue_change():
    #     if paid > cost:
    #         change = paid - cost
    #         print(f"Your change is ${change:.2f}.\nHere is your {order} ☕ Enjoy!")
    #     elif paid == cost:
    #         print(f"Here is your {order} ☕ Enjoy!")
    #     else:
    #         print("Sorry that's not enough money. Money refunded.")
    #         exit()
    #

    #
    # elif order == "espresso":
    #     while paid >= cost:
    #         if remaining_water >= espresso_used_water:
    #             if remaining_coffee >= espresso_used_coffee:
    #                 # paid = float(pay())
    #                 # issue_change()
    #                 remaining_water -= espresso_used_water
    #                 remaining_coffee -= espresso_used_coffee
    #                 paid = float(pay())
    #                 issue_change()
    #             else:
    #                 print("Not enough ingredients available for selection.")
    #         else:
    #             print("Not enough ingredients available for selection.")
    # elif order == "latte":
    #     while paid >= cost:
    #         if remaining_water >= latte_used_water:
    #             if remaining_coffee >= latte_used_coffee:
    #
    #                 remaining_water -= latte_used_water
    #                 remaining_milk -= latte_used_milk
    #                 remaining_coffee -= latte_used_coffee
    #                 paid = float(pay())
    #                 issue_change()
    #             else:
    #                 print("Not enough ingredients available for selection.")
    #         else:
    #             print("Not enough ingredients available for selection.")
    # elif order == "cappuccino":
    #     while paid >= cost:
    #         if remaining_water >= cappuccino_used_water:
    #             if remaining_coffee >= cappuccino_used_coffee:
    #
    #                 remaining_water -= cappuccino_used_water
    #                 remaining_milk -= cappuccino_used_milk
    #                 remaining_coffee -= cappuccino_used_coffee
    #                 paid = float(pay())
    #                 issue_change()
    #             else:
    #                 print("Not enough ingredients available for selection.")
    #         else:
    #             print("Not enough ingredients available for selection.")
    #     else:
    #         print("Invalid request. Try again.")
    #         continue


# TODO: 1. take customer order
# TODO: 1. machine on/ off
# TODO: 2. print report of resources
# TODO: 4. verify resources available for order
# TODO: 5. payment
# TODO: 6. verify success or not
# TODO: 7. make drink
# TODO figure out how to add ml to water, milk and g to coffee
# TODO update resources to remove expended resources
