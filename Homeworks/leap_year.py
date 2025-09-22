"""
File:    leap_year.py
Author:  Sushant Sharma
Date:    09/19/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description:  checking if a year is a leap year or not
  
"""
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("It is a leap year")
elif year % 100 == 0:
    print("It is not a leap year")
elif year % 4 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")

