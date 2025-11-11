"""
File:    checkerboard.py
Author:  Sushant Sharma
Date:    10/12/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description: getting two symbols and the length of how many combinations, and looping through them to generate random symbols based on the user info
"""


def checkerboard(size, symbol_1, symbol_2):
    row = 0
    while row < size:
        col = 0
        line = ""  

        # Inner loop: builds each line symbol by symbol
        while col < size:
            # Alternate between symbol_1 and symbol_2
            if (row + col) % 2 == 0:
                line = line + symbol_1
            else:
                line = line + symbol_2
            col += 1

        print(line)
        row += 1


if __name__ == "__main__":
    size = int(input("What size do you want? "))
    symbols = input("What symbols do you want? ").split()

    if len(symbols) != 2:
        print("Please enter exactly two symbols separated by a space.")
    else:
        symbol_1 = symbols[0]
        symbol_2 = symbols[1]
        checkerboard(size, symbol_1, symbol_2)



