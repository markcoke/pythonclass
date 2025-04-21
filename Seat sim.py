# Come Fly with Me - Airplane Seat Selection Simulator

TOTAL_SEATS = 20
FIRST_CLASS_SEATS = [1, 2, 3, 4]           # First-class
EMERGENCY_ROWS = [2, 3]                    # Emergency rows
seats = [False] * TOTAL_SEATS             # False means seat is available


def display_seats():
    print("\nSeat Map:")
    for i in range(TOTAL_SEATS):
        status = "X" if seats[i] else str(i + 1)
        print(f"[{status}]", end=" ")
        if (i + 1) % 5 == 0:
            print()
    print()


def is_emergency_seat(seat_number):
    row = (seat_number - 1) // 5 + 1
    return row in EMERGENCY_ROWS


def select_seat():
    try:
        seat = int(input("Enter seat number to book (1-20): "))
        if seat < 1 or seat > TOTAL_SEATS:
            print("Invalid seat number. Please choose between 1 and 20.")
            return

        if seats[seat - 1]:
            print("That seat is already taken.")
            return

        if seat in FIRST_CLASS_SEATS:
            confirm = input("This is a First-Class seat and costs $50. Confirm purchase? (yes/no): ").lower()
            if confirm != "yes":
                print("Purchase cancelled.")
                return

        if is_emergency_seat(seat):
            safety = input("This is an emergency exit seat. Do you accept responsibility in case of emergency? (yes/no): ").lower()
            if safety != "yes":
                print("You must accept to book this seat.")
                return

        seats[seat - 1] = True
        print(f"Seat {seat} successfully booked!\n")

    except ValueError:
        print("Please enter a valid number.")


def main():
    print("Welcome to Come Fly with Me - Seat Booking System!")

    while True:
        display_seats()
        select_seat()
        more = input("Do you want to book another seat? (yes/no): ").lower()
        if more != "yes":
            break

    print("\nFinal Seat Map:")
    display_seats()
    print("Thank you for flying with us!")


if __name__ == "__main__":
    main()
