from machine_menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def report():
    global resources

    r = resources

    water, milk, coffee, money = r["water"], r["milk"], r["coffee"], r["money"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")

def enough_resources(drink_selected):
    global resources

    drink = drink_selected["ingredients"]

    if resources["water"] < drink["water"]:
        print("Sorry there is not enough water.")
        return False
    elif resources["coffee"] < drink["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    
    if "milk" in drink:
        if resources["milk"] < drink["milk"]:
            print("Sorry there is not enough milk.")
            return False
        
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""

    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10 
    nickles = int(input("How many nickles?: ")) * 0.05 
    pennies = int(input("How many pennies?: ")) * 0.01

    return round(quarters + dimes + nickles + pennies, 2) 

def get_change(price, money_recieved):
    """Returns the total change for the user,
        if the money recieved is not enough returns -1
    """
    global resources

    if money_recieved < price:
        return -1
    
    resources["money"] += price
    return round(money_recieved - price, 2)

def update_resources(drink_selected):
    global resources

    drink = drink_selected["ingredients"]

    resources["water"] -= drink["water"]
    resources["coffee"] -= drink["coffee"]

    if "milk" in drink:
        resources["milk"] -= drink["milk"]

def main():
    user_drink = ''

    while user_drink != 'off':
        user_drink = input("What would you like? (espresso/latte/cappuccino): ")
        
        if user_drink == 'off':
            continue
        elif user_drink == 'report': 
            report()
            continue

        drink = MENU[user_drink]

        # check if there are enough resources
        if not enough_resources(drink):
            continue

        # get number of coins the user provides
        print("Please insert coins.")

        # process the payment
        payment = process_coins()

        # calculate the total change the user will recieve
        change = get_change(drink["cost"], payment)

        if change == -1:
            print("Sorry that's not enough money. Money refunded.")
        else:
            update_resources(drink)

            print(f"Here is ${change} in change.")
            print(f"Here is your {user_drink} ☕ Enjoy!")

if __name__ == '__main__':
    main()
