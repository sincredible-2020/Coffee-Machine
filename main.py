import day15_data

espresso = day15_data.menu['espresso']
latte = day15_data.menu['latte']
cappuccino = day15_data.menu['cappuccino']

resources = {"water": 300, "milk": 200, "coffee": 100}


def check_resources():
    if answer == 'espresso':
        if resources["water"] < espresso['ingredients']['water']:
            print("Sorry there is not enough water")
        if resources['coffee'] < espresso['ingredients']['coffee']:
            print("Sorry there is not enough coffee")
        else:
            return 1
    elif answer == 'latte':
        if resources["water"] < latte['ingredients']['water']:
            print("Sorry there is not enough water")
        if resources['coffee'] < latte['ingredients']['coffee']:
            print("Sorry there is not enough coffee")
        if resources['milk'] < latte['ingredients']['milk']:
            print("Sorry there is not enough milk")
        else:
            return 1
    elif answer == 'cappuccino':
        if resources["water"] < cappuccino['ingredients']['water']:
            print("Sorry there is not enough water")
        if resources['coffee'] < cappuccino['ingredients']['coffee']:
            print("Sorry there is not enough coffee")
        if resources['milk'] < cappuccino['ingredients']['milk']:
            print("Sorry there is not enough milk")
        else:
            return 1


def calculate_change():
    change = 0
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if answer == 'espresso':
        if espresso['cost'] > total:
            print("Sorry that's not enough money")
            return 0
        else:
            change = total - espresso['cost']
            print(f"Here is your ${round(change, 2)} in change")
            return 1
    elif answer == 'latte':
        if latte['cost'] > total:
            print("Sorry that's not enough money")
            return 0
        else:
            change = total - latte['cost']
            print(f"Here is your ${round(change, 2)} in change")
            return 1
    elif answer == 'cappuccino':
        if cappuccino['cost'] > total:
            print("Sorry that's not enough money")
            return 0
        else:
            change = total - cappuccino['cost']
            print(f"Here is your ${round(change, 2)} in change")
            return 1


def make_drinks():
    if answer == 'espresso':
        resources["water"] = resources["water"] - espresso['ingredients']['water']
        resources['coffee'] = resources['coffee'] - espresso['ingredients']['coffee']
    elif answer == 'latte':
        resources["water"] = resources["water"] - latte['ingredients']['water']
        resources['coffee'] = resources['coffee'] - latte['ingredients']['coffee']
        resources['milk'] = resources['milk'] - latte['ingredients']['milk']
    elif answer == 'cappuccino':
        resources["water"] = resources["water"] - cappuccino['ingredients']['water']
        resources['coffee'] = resources['coffee'] - cappuccino['ingredients']['coffee']
        resources['milk'] = resources['milk'] - cappuccino['ingredients']['milk']
    print(f"Here is your {answer}☕. Enjoy!")


def report():
    print(f"RESOURCES LEFT:\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")


def refill():
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100


def main():
    global answer
    report()
    answer = input("What would you like? (espresso/latte/cappuccino): ")
    if answer == 'off':
        print("Turning off...\nBYE!")
    else:
        if check_resources() == 1:
            if calculate_change() == 1:
                make_drinks()
                main()
            else:
                main()
        else:
            answer2 = input("Do you want to refill the resources? y/n: ")
            if answer2 == 'y':
                refill()
                main()


main()
