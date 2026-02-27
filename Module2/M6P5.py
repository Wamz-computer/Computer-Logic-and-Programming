# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 21:19:10 2026

@author: wamul
The user will enter employee last name, salary and job level (as noted below). Use
the job level to determine the bonus rate. Then compute bonus to be salary times
bonus rate. Display employee last name and bonus.
Job Level Bonus Rate
10 and above 25%
5 to 9 20%
All others 10%
"""
# Get user input
last_name = input("Enter employee last name: ")
salary = float(input("Enter employee salary: "))
job_level = int(input("Enter job level: "))

# Determine bonus rate based on job level
if job_level >= 10:
    bonus_rate = 0.25
elif job_level >= 5:
     bonus_rate = 0.20
else:
    bonus_rate = 0.10

# Compute bonus amount 
bonus_amount = salary * bonus_rate

# Display results
print(f"\n--- Bonus Summary ---")
print(f"Employee: {last_name}")
print(f"Bonus Amount: ${bonus_amount:.2f}")
