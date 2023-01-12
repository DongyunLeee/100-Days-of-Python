from coffeemachine_header import *
import sys


def admin_check():
    key = input("Please admin key:")
    if key == admin_key:
        return True
    else:
        return False


def admin_menu():
    a_menu = input("What would you like? (report/refill/off):")
    try:
        num = admin[a_menu]
        admin_func(num)
    except:
        print("Sorry, Not found admin function.")


def admin_func(num):
    if num == 1:
        print(f"""
        Water: {resources["water"]}ml
        Milk: {resources["milk"]}ml
        Coffee: {resources["coffee"]}g
        Money: ${resources["money"]}
        """)
    elif num == 2:
        print("Select refill")
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
        print(f"""
        <<<Refill complete>>>
        Water: {resources["water"]}ml
        Milk: {resources["milk"]}ml
        Coffee: {resources["coffee"]}g
        """)
    else:
        exit(0)


def menu_check(menu):
    try:
        if resources["water"] - MENU[menu]["ingredients"]["water"] < 0:
            print("Sorry, there is not enough water.")
            return False
        if resources["milk"] - MENU[menu]["ingredients"]["milk"] < 0:
            print("Sorry, there is not enough milk.")
            return False
        if resources["coffee"] - MENU[menu]["ingredients"]["coffee"] < 0:
            print("Sorry, there is not enough coffee.")
            return False
        return True
    except:
        print("Not found menu.")
        return False


def insert_coin():
    print("Please insert coin.")
    quarters = int(input("How many quarters?:")) * 0.25
    dimes = int(input("How many dimes?:")) * 0.10
    nickles = int(input("How many nickles?:")) * 0.05
    pennies = int(input("How many pennies?:")) * 0.01
    return round(quarters + dimes + nickles + pennies, 2)


def check_cost(menu, coin):
    change = round(coin - MENU[menu]["cost"], 2)
    if change >= 0:
        print(f"""
        Here is ${change} in change
        Here is your {menu}. Enjoy!
        """)
        resources["water"] -= MENU[menu]["ingredients"]["water"]
        resources["milk"] -= MENU[menu]["ingredients"]["milk"]
        resources["coffee"] -= MENU[menu]["ingredients"]["coffee"]
        resources["money"] += MENU[menu]["cost"]
    else:
        print("Sorry, that's not enough money. Money refunded.")


def main():
    menu = input("What would you like? (espresso/latte/cappuccino):")

    if menu == "admin":
        if admin_check():
            admin_menu()
        else:
            print("Sorry, Not matched admin key.")
        return

    else:
        if menu_check(menu):
            coin = insert_coin()
            check_cost(menu, coin)


while True:
    main()