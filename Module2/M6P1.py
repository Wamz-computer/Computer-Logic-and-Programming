# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 17:41:30 2026

@author: wamul
The input to the problem is quantity of widgets. Your program should determine
the price to charge based on the schedule below. Calculate the extended price
(quantity x price). Calculate tax at 7%. Display the extended price, tax amount
and total.
Quantity Price
>10000 $10
5000 to 10000 $20
Below 5000 $30
"""
# This program calculates pricing using nested if statements

# Input
quantity = int(input("Enter the quantity of widgets: "))

# Determine price using nested if
if quantity > 10000:
    price = 10.00
else:
    if quantity >= 5000:
        price = 20.00
    else:
        price = 30.00

# Calculations
extended_price = quantity * price
tax = extended_price * 0.07
total = extended_price + tax

# Output (formatted, aligned)
print("\n--- Invoice Summary ---")
print(f"{'Extended Price:':20s}${extended_price:10.2f}")
print(f"{'Tax (7%):':20s}${tax:10.2f}")
print(f"{'Total:':20s}${total:10.2f}")
