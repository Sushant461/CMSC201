"""
File:    pascal.py
Author:  Sushant Sharma
Date:    10/12/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description:  makking the pascals trinagle 
"""
def next_level(level):

    next_row = [1]

    i = 0 
    while i < len(level) - 1:
        total = level[i] + level[i+1]
        next_row.append(total)
        i += 1
    
    next_row.append(1)

    return next_row

if __name__ == "__main__":

    level = [1]
    i = 0

    while i < 10:
        
        for x in level:
            print(x, end = '\t')
        print()

        level = next_level(level)
        i += 1

        
