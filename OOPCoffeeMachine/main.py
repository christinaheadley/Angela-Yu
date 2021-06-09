from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine = CoffeeMaker()
# machine.report()
latte = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
espresso = MenuItem(name="espresso", water=50, milk=0, coffee=24, cost=1.5)
cappuccino = MenuItem(name="cappuccino", water=150, milk=100, coffee=24, cost=3.0)
# print(latte.name)
# print(latte.cost)
# print(latte.ingredients)
# print(machine.is_resource_sufficient()
menu = Menu()

# print(menu.get_items())
# print(menu.find_drink("latte"))
# print(menu.find_drink("lae"))
#
# print(machine.is_resource_sufficient(latte))
# machine.make_coffee(latte)
money = MoneyMachine()
# money.report()
# money.make_payment(latte.cost)

# print(MenuItem.name)
# menu_item = MenuItem("latte")
# print(menu_item)
# print(menu.get_items())

is_on = True

while is_on:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        machine.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                machine.make_coffee(drink)


# TODO 1 Print report
# TODO 2 check resources
# TODO 3 process coins
# TODO 4 check transaction success
# TODO 5 make coffee
