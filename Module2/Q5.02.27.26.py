# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 11:25:03 2026

@author: wamul
Enter the user’s last name, number of dependents and gross income. Compute
adjusted gross income to be gross income minus dependents times $12000. Next
determine an income tax rate. Adjusted gross incomes over $50,000 have a tax
rate of 20%. Adjusted gross incomes $50,000 or under have or under have a tax rate of 10%
"""
# Input
last_name = input("Enter last name: ")
dependents = int(input("Enter number of dependents: "))
gross_income = float(input("Enter gross income: "))

# Calculate adjusted gross income
adjusted_gross_income = gross_income - (dependents * 12000)

# Determine tax rate
if adjusted_gross_income > 50000:
    tax_rate = 0.20
else:
    tax_rate = 0.10

# Calculate income tax
income_tax = adjusted_gross_income * tax_rate

# Output
print("\n--- Tax Summary ---")
print(f"Last Name: {last_name}")
print(f"Gross Income: ${gross_income:.2f}")
print(f"Adjusted Gross Income: ${adjusted_gross_income:.2f}")
print(f"Tax Rate: {tax_rate * 100:.0f}%")
print(f"Income Tax: ${income_tax:.2f}")