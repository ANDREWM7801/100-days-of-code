"""
Day 15 project - coffee machine - Andrew Marshall
"""

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
    },
    "super coffee": {
        "ingredients": {
            "water": 0,
            "milk": 1000,
            "coffee": 240,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "cash": 0,
}

def enough(coffee_type):
    if MENU[coffee_type]["ingredients"]["water"] > resources["water"]:
        print("not enough water")
        return "no"
    elif MENU[coffee_type]["ingredients"]["milk"] > resources["milk"]:
        print("not enough milk")
        return "no"
    elif MENU[coffee_type]["ingredients"]["coffee"] > resources["coffee"]:
        print("not enough coffee")
        return "no"
    else:
        return "yes"

def new_resources(coffee_type):
    resources["water"] = resources["water"] - MENU[coffee_type]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[coffee_type]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[coffee_type]["ingredients"]["coffee"]

def payment(coffee_type):
    pennies = int(input("how many pennies? "))
    dimes = int(input("how many dimes? "))
    nickels = int(input("how many nickels? "))
    quaters = int(input("how many quaters? "))
    total_paid = 0.01*pennies + 0.05*dimes + 0.1*nickels + 0.25*quaters
    if total_paid < MENU[coffee_type]["cost"]:
        print("Sorry thats not enough money. money refunded.")
        return "insufficient funds"
    elif total_paid >= MENU[coffee_type]["cost"]:
        change = total_paid - MENU[coffee_type]["cost"]
        resources["cash"] = resources["cash"] + MENU[coffee_type]["cost"]
        print("Your change is ", change)
        return "paid"

On = True

while On == True:
    Option = input("What would you like? (espresso/latte/cappuccino): ")
    if Option == 'report':
        print(resources)
    elif Option == 'off':
        On = False
    elif (Option =='espresso' or Option =='latte' or Option =='cappuccino'):
        if enough(Option) == "yes":
            if payment(Option) == 'paid':
                new_resources(Option)
    else:
        print("not an option, try again. ")
            
            
            
            

    
    
        
    
