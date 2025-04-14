class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class VendingMachine:
    def __init__(self):
        self.beverages = [
            Beverage("Coke", 1.50),
            Beverage("Pepsi", 1.25),
            Beverage("Sprite", 1.00),
            Beverage("Water", 0.75),
            Beverage("Orange Juice", 2.00),
            Beverage("Iced Tea", 1.75)
        ]

    def display_menu(self):
        print("\n--- Vending Machine Menu ---")
        for idx, drink in enumerate(self.beverages, start=1):
            print(f"{idx}. {drink.name} - ${drink.price:.2f}")

    def vend(self, choice, money_inserted):
        drink = self.beverages[choice - 1]
        if money_inserted < drink.price:
            print(f"Not enough money. {drink.name} costs ${drink.price:.2f}. You entered ${money_inserted:.2f}.")
        else:
            change = money_inserted - drink.price
            print(f"Dispensing {drink.name}. Your change is ${change:.2f}. Enjoy!")

def run_machine():
    machine = VendingMachine()
    while True:
        machine.display_menu()
        try:
            choice = int(input("Select a beverage (1-6): "))
            if choice < 1 or choice > 6:
                print("Invalid selection. Please choose a number between 1 and 6.")
                continue

            money = float(input("Insert money: $"))
            machine.vend(choice, money)

        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the program
run_machine()
