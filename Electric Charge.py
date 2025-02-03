# Electric Charge

# rate constants/cents
FIRST_1000 = 7.633  # cents per kWh for first 1000 kWh
RATE_OVER_1000 = 9.259   # cents per kWh for usage over 1000 kWh

# Ask user for kWh used
kw_hours = int(input("Enter the KW hours used: "))

# Calculate the total cost
if kw_hours <= 1000:
    total_cost_cents = kw_hours * FIRST_1000
else:
    # First 1000 kWh at the lower rate
    first_1000 = 1000 * FIRST_1000
    # Remaining kWh at the higher rate
    cost_over_1000 = (kw_hours - 1000) * RATE_OVER_1000
    # Total cost
    total_cost_cents = first_1000 + cost_over_1000

# Convert cents to dollars
total_cost_dollars = total_cost_cents / 100

# Print total cost
print(f"Amount owed is ${total_cost_dollars:.2f}")
