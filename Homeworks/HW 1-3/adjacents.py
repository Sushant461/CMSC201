"""
File:   adjacents.py
Author:  Sushant Sharma
Date:    09/26/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description:   how many k adjacents pairs are in a string
  
"""
if __name__ == "__main__":
    text = input("Enter a string to check for k-adjacents: ")

    k = int(input("What is the jump distance k ? "))

    count = 0

    for i in range(len(text) - k):
        if text[i] == text[i+k]:
            count += 1
    print("The number of", k, "- adjacents  is", count)
