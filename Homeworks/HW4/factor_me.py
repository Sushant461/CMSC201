"""
File:    factor_me.py
Author: Sushant Sharma
Date:    10/03/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description: factors a number into its prime factors
  
"""

if __name__ == "__main__":

    # list of primes less than 50
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    num = int(input("Enter a number to factor: "))
    original = num
    factors = []

    # divide by each prime as many times as possible
    i = 0
    while i < len(primes):
        p = primes[i]
        # keep dividing while divisible
        while num % p == 0:
            factors.append(p)
            num = num // p
        i = i + 1

    # display results
    if len(factors) == 0:
        print("We didn't find any factors")
    else:
        # build string like 2*2*3*5
        text = str(factors[0])
        j = 1
        while j < len(factors):
            text = text + "*" + str(factors[j])
            j = j + 1
        print("The factors are:", text)

    # if leftover unfactorable part remains
    if num != 1:
        print("This part of the number couldn't be factored with primes less than 50:", num)
