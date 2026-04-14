import coffee_maker
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

resource = CoffeeMaker()
money = MoneyMachine()
order = Menu()

is_on = True

while is_on:
    choice = input(f"What would you like? {order.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        resource.report()
        money.report()
    else:
        drink = order.find_drink(choice)
        if drink:
            if resource.make_coffee(drink):
                if money.make_payment(drink.cost):
                    resource.make_coffee(drink)
