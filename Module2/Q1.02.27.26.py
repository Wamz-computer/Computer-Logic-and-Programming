# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 19:26:40 2026

@author: wamul

Allow a user to enter a quantity of an item. If the quantity is greater than or equal
to 1000, the unit price should be $3.00. For quantities under 1000 the unit price is
$5.00. Compute extended price to be quantity x unit price. Compute tax to be 7%
of the extended price. The total is computed as extended price plus the tax.
Display the quantity, unit price, extended price, tax total

"""
SALES_TAX = 0.07 # 7%
#Get item- quantity from user 
print("enter quantity items")
item_quantity = int(input("enter quantity items:"))
#print(item_quantity)

# if item_quantity >= 1000 --> unity_price = 3.00
# Else if item_quantity < 100 --> unit_price = 5.00
if (item_quantity >= 1000) :
    unit_price = 3.00
else:
    unit_price = 5.00

# Compute extended_price = item_quantity * unit_price
extended_price = item_quantity * unit_price

# computer sales_tax = .07 * extended_price
sales_tax = SALES_TAX * extended_price

# Display the quantity, unit price, extendedd price, tax and total

total_sale = extended_price + sales_tax
print("\n--- Order Summary ---")
print(f"Quantity:{item_quantity}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended Price: ${extended_price:.2f}")
print(f"Tax (7%): ${sales_tax:.2f}")
print(f"Total:${total_sale:.2f}")
