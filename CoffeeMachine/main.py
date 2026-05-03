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

value = {
    "quarters" : 0.25,
    "dimes" : 0.10,
    "nickles" : 0.05,
    "pennies" : 0.01,
}


money = 0
earning = 0
machine_switch = False
# TODO: 1. Get prompt from the user about options to select from
# TODO: 2.

while not machine_switch:
    # TODO: 4. Print Insufficient if there's shortage of supply
    options = input("What are you ordering today?(espresso/latte/cappuccino)")
    if options == "off":
        machine_switch = True
    # TODO: 3. Print a report of all the coffee machine resources
    elif options == "report":
        print(f"Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: ${earning}")

    # TODO: 5. Insert coin
    elif options == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print(f"Sorry there is not enough water.")
        if resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print(f"Sorry there is not enough coffee.")
        if resources["water"]>=MENU["espresso"]["ingredients"]["water"] and resources["coffee"]>= MENU["espresso"]["ingredients"]["coffee"]:
            print("Please insert coins.")
            quarters = int(input("How many quarters: "))
            dimes = int(input("How many dimes: "))
            nickles = int(input("How many nickles: "))
            pennies = int(input("How many pennies: "))
            money += (quarters * value["quarters"]) + (dimes * value["dimes"]) + (nickles * value["nickles"]) + (
                        pennies * value["pennies"])
            if money == MENU["espresso"]["cost"]:
                earning += MENU["espresso"]["cost"]
                print("Here is your Espresso. Enjoy")
                resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]

            if money > MENU["espresso"]["cost"]:
                change = money - MENU["espresso"]["cost"]
                earning += MENU["espresso"]["cost"]
                print(f"Here is your Espresso. Enjoy. Here is your change of {round(change, 2)}")
                resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]

            if money < MENU["espresso"]["cost"]:
                print("You have insufficient fund. Try again")
            money = 0

    elif options == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print(f"Sorry there is not enough water.")
        if resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print(f"Sorry there is not enough milk.")
        if resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print(f"Sorry there is not enough coffee.")
        if resources["water"]>=MENU["latte"]["ingredients"]["water"] and resources["milk"]>=MENU["latte"]["ingredients"]["milk"] and resources["coffee"]>= MENU["latte"]["ingredients"]["coffee"]:
            print("Please insert coins.")
            quarters = int(input("How many quarters: "))
            dimes = int(input("How many dimes: "))
            nickles = int(input("How many nickles: "))
            pennies = int(input("How many pennies: "))
            money += (quarters * value["quarters"]) + (dimes * value["dimes"]) + (nickles * value["nickles"]) + (
                    pennies * value["pennies"])
            if money == MENU["latte"]["cost"]:
                earning += MENU["latte"]["cost"]
                print("Here is your Latte. Enjoy")
                resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]

            if money > MENU["latte"]["cost"]:
                change = money - MENU["latte"]["cost"]
                earning += MENU["latte"]["cost"]
                print(f"Here is your Latte. Enjoy. Here is your change of {round(change, 2)}")
                resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]

            if money < MENU["latte"]["cost"]:
                print("You have insufficient fund. Try again")
            money = 0

    elif options == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print(f"Sorry there is not enough water.")
        if resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print(f"Sorry there is not enough milk.")
        if resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print(f"Sorry there is not enough coffee.")
        if resources["water"]>=MENU["cappuccino"]["ingredients"]["water"] and resources["milk"]>=MENU["cappuccino"]["ingredients"]["milk"] and resources["coffee"]>= MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Please insert coins.")
            quarters = int(input("How many quarters: "))
            dimes = int(input("How many dimes: "))
            nickles = int(input("How many nickles: "))
            pennies = int(input("How many pennies: "))
            money += (quarters * value["quarters"]) + (dimes * value["dimes"]) + (nickles * value["nickles"]) + (
                    pennies * value["pennies"])
            if money == MENU["cappuccino"]["cost"]:
                earning += MENU["cappuccino"]["cost"]
                print("Here is your Cappuccino. Enjoy")
                resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
                resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]

            if money > MENU["cappuccino"]["cost"]:
                change = money - MENU["cappuccino"]["cost"]
                earning += MENU["cappuccino"]["cost"]
                print(f"Here is your Cappuccino. Enjoy. Here is your change of {round(change, 2)}")
                resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
                resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]

            if money < MENU["cappuccino"]["cost"]:
                print("You have insufficient fund. Try again")
            money = 0









