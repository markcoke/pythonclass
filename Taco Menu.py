# Taco Palace Ordering System

# Function to show the menu
def show_menu():
    print("\nTaco Palace Menu")
    print("1. Taco - $2.99")
    print("2. Burrito - $4.99")
    print("3. Nachos - $3.49")
    print("4. Soft Drink - $1.99")
    print("5. Quit")


# Function to get the price of an item
def get_price(choice):
    if choice == 1:
        return 2.99
    elif choice == 2:
        return 4.99
    elif choice == 3:
        return 3.49
    elif choice == 4:
        return 1.99
    else:
        return 0  # Default for invalid choices


# Main function
def main():
    print("Welcome to Taco Palace!")

    order = []  # List to store ordered items
    total = 0  # Total price

    while True:
        show_menu()
        choice = input("Enter the number of your choice: ")

        if choice.isdigit():  # Check if input is a number
            choice = int(choice)

            if choice == 5:  # Quit option
                break  # Exit the loop
            elif choice in [1, 2, 3, 4]:  # Valid choices
                if choice == 1:
                    item = "Taco"
                elif choice == 2:
                    item = "Burrito"
                elif choice == 3:
                    item = "Nachos"
                elif choice == 4:
                    item = "Soft Drink"

                order.append(item)  # Add item to list
                total += get_price(choice)  # Add price to total

                print(f"You selected {item}.")
            else:
                print("Invalid choice. Please pick a number from 1 to 5.")
        else:
            print("Invalid input. Please enter a number.")

    # Show final order summary
    if order:
        print("\nYou ordered:", " and ".join(order))
        print(f"Your total is: ${total:.2f}")
    else:
        print("\nNo items ordered. Thanks for visiting Taco Palace!")


# Run the program
main()
