"""

File:    derangements.py
Author:  Sushant Sharma
Date:    10/28/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description: Computes the number of derangements Dn using a recursive formula.
  
"""

Even_sign = 1
Odd_sign = -1

def derangement(n):

    if n == 0:
        return 1
    

    # figure out the sign base

    if n % 2 == 0:
        sign = Even_sign        
    else:
        sign = Odd_sign

    #recusrive step
    return n * derangement(n - 1) + sign

if __name__ == "__main__":
    for i in range(20):
        print(i,derangement(i))        
