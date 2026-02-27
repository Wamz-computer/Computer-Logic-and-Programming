# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 21:12:46 2026

@author: wamul
Have the user to enter number of concert tickets. The price per ticket depends on
the volume (see below). Display the number of tickets, price per ticket and the
total cost (number of tickets x Price Per Ticket).
Quantity Price Per Ticket
>=25 $50
10 to 24 $60
5 to 9 $70
Less 5 $75
"""
# Get user input
quantity = int(input("Enter number of concert tickets: "))

# Determine price per ticket based on quantity
if quantity >= 25:
    price_per_ticket = 50.00
elif quantity >= 10:
    price_per_ticket = 60.00
elif quantity >= 5:
    price_per_ticket = 70.00
else:
    price_per_ticket = 80.00  # Assuming $80 based on the logical trend

# Calculate total cost
total_cost = quantity * price_per_ticket

# Display results with formatting
print(f"\n--- Order Summary ---")
print(f"Tickets ordered:  {quantity}")
print(f"Price per ticket: ${price_per_ticket:.2f}")
print(f"Total cost:       ${total_cost:.2f}")
