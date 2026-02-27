# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 10:29:49 2026

@author: wamul
The program asks the user for an item and quantity. Determine the unit price of
the item based on the chart below. Compute the extended price to be quantity x
unit price. Display the item, unit price and extended price. Note: if the item
entered is not A then assume the item is B. No need to check for B.
Item Unit Price
A $10.00
B $20.00
(Note: assume the user will enter the data correctly. Assume if they enter capital
A then $10.00 gets assigned to unit price variable. Any other entry is assumed to
be a capital B whether they enter B or not. Therefore, you only need a relational
condition for A. This makes the if statement easier and removes data validation
from the program which could get quite complex).
if item == “A”:
Unit_price = 10.00
else:
Unit_price = 20.00
"""
# Input
item = input("Enter the item (A or B): ")
quantity = int(input("Enter the quantity: "))

# Determine unit price
if item == "A":
    unit_price = 10.00
else:
    unit_price = 20.00

# Calculation
extended_price = quantity * unit_price

# Output
print("\n--- Order Summary ---")
print(f"Item: {item}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended Price: ${extended_price:.2f}")
