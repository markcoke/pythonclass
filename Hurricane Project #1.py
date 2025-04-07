#Create lists
rain_list = []
wind_list = []

# Greet user and ask for data
input_string = input(
    "Please enter the rain level and wind speed for today, separated by a space: \n")

while input_string != "-1.0":
    try:
        rain, wind = input_string.split()
        rain = float(rain)
        wind = float(wind)

        rain_list.append(rain)
        wind_list.append(wind)

    except ValueError:
        print("Invalid input. Please enter two numbers separated by a space.")

    input_string = input("Enter the rain level and wind speed reading for today: \n")

# Calculate average rain and wind
if len(rain_list) > 0:
    average_rain = sum(rain_list) / len(rain_list)
    average_wind = sum(wind_list) / len(wind_list)

    # Calculate weather severity
    severity = (average_rain * 10) + average_wind

    # Output results
    print(f"\nThe average rain is {average_rain:.1f} inches")
    print(f"The average wind is {average_wind:.1f} mph")
    print(f"The weather severity for these {len(rain_list)} readings is:  {severity:.1f}")
else:
    print("No data entered.")
