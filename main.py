from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



def coffee_mahine(money_machine, menu, coffe_maker):
    on = True
    while on:
        print("Welcome to the coffee machine")
        choose = input(f"What would you like {menu.get_items()}: ")
        if choose == 'off':
            print("The machine is power off good bye")
            on = False
        else:
            drink = menu.find_drink(choose)
            if money_machine.make_payment(drink.cost):
                if coffe_maker.is_resource_sufficient(drink):
                    coffe_maker.report()
                    money_machine.report()
                    coffe_maker.make_coffee(drink)
                    coffe_maker.report()
            else:
                print("else")
    on = False

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()
coffee_mahine(money_machine, menu, coffee_maker)
