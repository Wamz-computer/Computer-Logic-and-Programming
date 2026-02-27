# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 11:20:38 2026

@author: wamul
The warranty of an appliance depends on the cost of the appliance. For appliances
over $1,000 the warrantee cost is 10% of the price. For appliances $1,000 or less
the warranty cost is 5% of the price. The user will enter the name and cost of an
appliance. Display name and cost of appliance, the cost of the warrantee and the
total (cost of the appliance + warranty)
"""
# Input
appliance_name = input("Enter the name of the appliance: ")
appliance_cost = float(input("Enter the cost of the appliance: "))

# Determine warranty cost
if appliance_cost > 1000.00:
    warranty_cost = appliance_cost * 0.10
else:
    warranty_cost = appliance_cost * 0.05

# Calculate total
total_cost = appliance_cost + warranty_cost

# Output
print("\n--- Appliance Summary ---")
print(f"Appliance Name: {appliance_name}")
print(f"Appliance Cost: ${appliance_cost:.2f}")
print(f"Warranty Cost: ${warranty_cost:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
