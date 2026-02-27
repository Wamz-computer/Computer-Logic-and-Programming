# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 21:04:46 2026

@author: wamul
Enter a principle amount of a CD and year to maturity of CD. Determine the
interest rate based on the amount of the principle and maturity (see below).
Calculate first year interest (principle x interest rate). Display principle, interest
rate and the interest amount for first year.
Principle Years to Maturity Interest Rate
>$100,000 5 6%
$50,000 to $100,000 10 5%
$50,000 to $100,000 5 4%
Any other principle and years 2%
"""

# This program calculates first-year CD interest using compound conditions

# Input
principal = float(input("Enter the principal amount of the CD: "))
years = int(input("Enter years to maturity: "))

# Determine interest rate
if principal > 100000 and years == 5:
    interest_rate = 0.06
elif principal >= 50000 and principal <= 100000 and years == 10:
    interest_rate = 0.05
elif principal >= 50000 and principal <= 100000 and years == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02

# Calculation
interest_amount = principal * interest_rate

# Output (formatted and aligned)
print("\n--- CD Interest Summary ---")
print(f"{'Principal:':20s}${principal:10.2f}")
print(f"{'Interest Rate:':20s}{interest_rate * 100:9.2f}%")
print(f"{'First Year Interest:':20s}${interest_amount:10.2f}")