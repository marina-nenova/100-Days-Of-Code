from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while is_on:
    choice = input(f"What would you like {menu.get_items()}?").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            print(f"Your drink costs {drink.cost}")
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
