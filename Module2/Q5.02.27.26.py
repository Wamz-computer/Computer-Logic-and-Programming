# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 11:25:03 2026

@author: wamul
Enter the user’s last name, number of dependents and gross income. Compute
adjusted gross income to be gross income minus dependents times $12000. Next
determine an income tax rate. Adjusted gross incomes over $50,000 have a tax
rate of 20%. Adjusted gross incomes $50,000 or under have or under have a tax rate of 10%
"""
last_name = input("Enter last name: ")
dependents = int(input("Enter number of dependents: "))
gross_income = float(input("Enter gross income: "))

adjusted_income = gross_income - (dependents * 12000)

if adjusted_income > 50000:
    tax_rate = 0.20
else:
    tax_rate = 0.10

income_tax = adjusted_income * tax_rate

if income_tax < 0:
    income_tax = 100

print("Last Name:", last_name)
print("Gross Income: $", gross_income)
print("Dependents:", dependents)
print("Adjusted Gross Income: $", adjusted_income)
print("Income Tax: $", income_tax)
