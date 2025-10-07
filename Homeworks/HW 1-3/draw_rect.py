"""
File:    draw_rect.py
Author:  Sushant Sharma
Date:    09/26/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description:   draws a rectangle of stars (*) with the given height and width.
"""

if __name__ == "__main__":
    height =  int(input("What is the height of the rectangle? "))
    width = int(input("What is the width of the rectangle?" ))

    for row in range(height):
        if row == 0 or row == height - 1:
            print("*"*width)
        else:
            print("*"+" "*(width -  2)+"*")
