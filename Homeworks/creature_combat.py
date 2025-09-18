"""
File:    creature_combat.py
Author:  Sushant Sharma
Date:    09/17/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description:  a battle between two creatures based on power toughness, and the program calculates the damage they deal to each other, and displays the result of the battle
  
"""
name1 = input("What is the name of the first creature? ")

power1 = int(input("What is the power of the first creature? "))

tough1 = int(input("What is the toughness of the first creature? "))

name2 = input("What is the name of the second creature? ")

power2 = int(input("What is the power of the second creature? "))

tough2 = int(input("What is the toughness of the second creature? "))

remaining1 = tough1 - power2 

remaining2 = tough2 - power1

print("The first creature now has (", power1, ",", remaining1, ")")

print("The second creature now has (", power2, ",", remaining2, ")")

if remaining1 <= 0 and remaining2 <= 0:
    print("Both creatures die in mutual combat.")
elif remaining1 <= 0:
    print(name1, "has died,", name2, "wins")
elif remaining2 <= 0:
    print(name2, "has died,", name1, "wins.")
else:
    print("Both creatures live to fight another day.")