# # # Constructing objects and accessing their attributes and methods
# # from turtle import Turtle, Screen
# #
# # timmy = Turtle()
# # print(timmy)
# # timmy.shape("turtle")
# # timmy.color("coral")
# # timmy.forward(100)
# #
# # my_screen = Screen()
# # print(my_screen.canvheight)
# # my_screen.exitonclick()
#
#
# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmendor"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
#
# table.align = "l"
#
# print(table)


from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True



while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)