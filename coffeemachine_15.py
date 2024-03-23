MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
coins = {
    "one-rupee": 1,
    "two-rupee": 2,
    "five-rupee": 5,
    "ten-rupee": 10
}

transaction_complete = False
transaction = 0
earnings = 0
while not transaction_complete:
    coffee_type = input("What would you like (espresso/latte/cappuccino): ")


    money_inserted = 0
    if coffee_type == 'status':
        print("remaining resources: ", resources)
        print("earnings : ", earnings)
    else:
        water_r = MENU[coffee_type]["ingredients"]["water"]
        milk_r = MENU[coffee_type]["ingredients"]["milk"]
        coffee_r = MENU[coffee_type]["ingredients"]["coffee"]

        water_h = resources["water"]
        milk_h = resources["milk"]
        coffee_h = resources["coffee"]

        if water_r >= water_h or milk_r >= milk_h or coffee_r >= coffee_h:
            print("NOT enough resources")
            print(resources)
            print("Required", MENU[coffee_type]["ingredients"])
            transaction_complete = True
        else:
            price = MENU[coffee_type]["cost"]
            print(f"That would be {price} rupees")
            print("Please insert the coins")
            print("---------------------------------------")
            one = int(input("Insert one rupee coins: "))
            two = int(input("Insert two rupee coins: "))
            five = int(input("Insert five rupee coins: "))
            ten = int(input("Insert ten rupee coins: "))

            money_inserted = one * 1 + two * 2 + five * 5 + ten * 10

            while money_inserted < price:
                print("money is not enough")
                n_one, n_two, n_five, n_ten = 0
                state = input("Do you want to continue(y) or not(n): ")
                if state == 'y':
                    n_one = int(input("Insert one rupee coins: "))
                    n_two = int(input("Insert two rupee coins: "))
                    n_five = int(input("Insert five rupee coins: "))
                    n_ten = int(input("Insert ten rupee coins: "))

                    money_inserted += n_one * 1 + n_two * 2 + n_five * 5 + n_ten * 10
                if state == 'n':
                    transaction_complete = True
                    print("Thank you sir ")

            if money_inserted >= price:
                change = money_inserted - price
                if change != 0:
                    print(f"Here is your balance {change}")
                print(f"Here is your {coffee_type} sir, enjoy your coffee ")

                resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
                resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
                resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]

                earnings += price

                cont = input("Can i help you with something else(y/n): ")
                if cont == 'n':
                    transaction_complete = True
                    print("Thank you sir ")
