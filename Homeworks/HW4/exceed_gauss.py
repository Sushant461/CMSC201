"""
File:    exceed_gauss.py
Author: Sushant Sharma
Date:    10/03/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description: Gauss sum until exceeding input
  
"""
if __name__ == "__main__":

    target = int(input("Enter a postive number > "))

    total = 0 
    k = 0

    while total <= target:
        k = k + 1
        total = total + k
    
    print("After",k, "iterations, the Gauss sum is", total,"which exceeds (or is eqal to) the number",target)

    
