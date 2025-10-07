"""
File:   ln2.py
Author:  Sushant Sharma
Date:    09/26/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description:  This program approximates ln(2) using the number that the user gives
  
"""

if __name__ == "__main__":
    n = int(input("How many terms do you want to calculate?"))

    total = 0.0

    for i in range(1, n +1):
        sign = (-1) ** (i+1)
        total += sign*(1/i)

    print("The approximation of ln(2) for", n, "terms is ", total)