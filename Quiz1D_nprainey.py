# -*- coding: utf-8 -*-
"""
Quiz version D

Author: Nathan Rainey
"""

#Problem: monthly mortgage payment calculator

# principal amount
p = float(input("What is the principal amount of the loan? "))

# Annual interest percentage
r = float(input("What is the annual interest percentage on the loan? "))

# Number of years on the loan
t = float(input("What is the length of the loan? "))


#Monthly mortgage payment calculator
monthly_payment = ((p * r) / 1200) * (1 / (1- (1+(r/1200))**(-12*t)))



print("The monthly mortgage payment is, $", float(round(monthly_payment, 2)))




