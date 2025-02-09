import math

# calculate the area of a circle
def area_of_circle(radius):
    return round(math.pi * radius ** 2, 2)

# calculate the total amount due with tax
def total_due(money, tax_rate):
    return round(money + (money * (tax_rate / 100)), 2)

#  convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * (5 / 9), 5)

# test the functions
def main():
    # Calculate the area of a circle
    print("Test Data - Area of a Circle")
    radii = [10, 6, 24, 2, 1]
    for r in radii:
        print(f"Input: {r}, Output: {area_of_circle(r)}")

    # Calculate the total due with tax
    print("\nTest Data - Taxes")
    tax_data = [(20, 6), (54, 4), (68, 8)]
    for money, tax_rate in tax_data:
        print(f"Input: Money = {money}, Tax Rate = {tax_rate}%, Output: {total_due(money, tax_rate)}")

    # Fahrenheit to Celsius conversion
    print("\nTest Data - Temperature")
    temperatures = [32, 80, 73, 42]
    for temp in temperatures:
        print(f"Input: {temp}, Output: {fahrenheit_to_celsius(temp)}")

# The program runs
if __name__ == "__main__":
    main()
