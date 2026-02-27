# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 11:16:00 2026

@author: wamul
Enter the number of books to order and cost per book. If the order total is over
$50.00 shipping is free. If the order total is $50.00 or under charge $25 shipping.
Display the order total and shipping charge (note 0 should display for a free
shipping charge)
"""
#Input
num_books = int(input("Enter the number of books to order: "))
cost_per_book = float(input("Enter the cost per book: "))

# Calculation
order_total = num_books * cost_per_book

# Determine shipping
if order_total > 50.00:
    shipping = 0.00
else:
    shipping = 25.00

# Output
print("\n--- Order Summary ---")
print(f"Order Total: ${order_total:.2f}")
print(f"Shipping Charge: ${shipping:.2f}")
