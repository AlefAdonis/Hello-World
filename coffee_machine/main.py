# Coffee Machine 4.0

def insuficiente():
    global water
    global milk
    global beans
    global cups
    

    if water <= 350:
        print("Sorry, not enough water!")
        return True
    if milk <= 100:
        print("Sorry, not enough milk!")
        return True
    if beans <= 20:
        print("Sorry, not enough coffee beans!")
        return True
    if cups < 1:
        print("Sorry, not enough disposable cups!")
        return True


def buy():
    
    global money
    global water
    global milk
    global beans
    global cups

    print()
    type_coffee = input("What do you want to buy? \n1 - Espresso \n2 - Latte \n3 - Cappuccino \nback - to main menu\n ")
    
    if insuficiente():
        return
    
    print("\nI have enough resources, making you a coffee!\n")
    if type_coffee == '1':
        water -= 250
        beans -= 16
        cups -= 1
        money += 4
        return

    elif type_coffee == '2':
        water -= 350
        milk -= 75
        beans -= 20
        cups -= 1
        money += 7
        return
    
    elif type_coffee == '3':
        water -= 200
        milk -= 100
        beans -= 12
        cups -= 1
        money += 6
        return
    
    elif type_coffee.lower() == 'back':
        return 


def fill():
    
    global water
    global milk
    global beans
    global cups

    add_water = int(input("Write how many ml of water do you want to add: "))
    add_milk = int(input("Write how many ml of milk do you want to add: "))
    add_beans = int(input("Write how many grams of coffee beans do you want to add: "))
    add_cups = int(input("Write how many disposable cups of coffee do you want to add: "))

    water += add_water
    milk += add_milk
    beans += add_beans
    cups += add_cups


def take():
    global money
    print(f"I gave you ${money}")
    money -= money


def remaining():
    global money
    global water
    global milk
    global beans
    global cups
    
    print(f"""\nThe coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{cups} of disposable cups
{money} of money\n""")


def main():
    
    while True:

        action = input("Write action (buy, fill, take, remaining, exit): \n")

        if action.lower() == "buy":
            buy()

        elif action.lower() == "fill":
            fill()

        elif action.lower() == "take":
            take()

        elif action.lower() == "remaining":
            remaining()

        elif action.lower() == "exit": break



money = 550
water = 400
milk = 540
beans = 120
cups = 9

main()
