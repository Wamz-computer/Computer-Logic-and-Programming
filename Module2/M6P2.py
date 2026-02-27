# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 20:55:45 2026

@author: wamul
Enter a part number and quantity Determine the cost per unit using the table
below. Then calculate the total cost (quantity x unit cost). Display the part
number, cost per unit and total cost. Note: Part number can be an integer but it can
also be a string because you are not doing arithmetic on it. However, in your code
if statement be sure to compare using consistency, that is, if item == “10” when
item is a string and if item == 10 when item is an integer.
Part Unit Cost
10 or 55 1.00
99 2.00
80 or 70 3.00
All others 5.00
"""
# This program calculates total cost using compound relational conditions

# Input
part_number = input("Enter the part number: ")
quantity = int(input("Enter the quantity: "))

# Determine unit cost
if part_number == "10" or part_number == "55":
    unit_cost = 1.00
elif part_number == "99":
    unit_cost = 2.00
elif part_number == "80" or part_number == "70":
    unit_cost = 3.00
else:
    unit_cost = 5.00

# Calculation
total_cost = quantity * unit_cost

# Output (formatted and aligned)
print("\n--- Part Cost Summary ---")
print(f"{'Part Number:':20s}{part_number}")
print(f"{'Unit Cost:':20s}${unit_cost:10.2f}")
print(f"{'Total Cost:':20s}${total_cost:10.2f}")
