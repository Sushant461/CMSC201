"""
File:    gandalf.py
Author:  Sushant Sharma
Date:    09/17/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description: LORT guessing game 
  
"""

race = input("Which race are you? (human/dwarf/elf/maiar/hobbit)").lower()

if race == "human":
    king_or_not = input("Are you the true and rightful King of Gondor?").lower()
    if king_or_not == "yes":
        print("You are Aragorn son of Arathorn")
    else:
        ring_frodo = input("Did you try to take the ring from Frodo?").lower()
        if ring_frodo == "yes":
            print("You are Boromir, poor guy...")
        else:
            print("You are Theoden, probably.")
elif race == "elf":
    matrix = input("Were you in the matrix? ").lower()
    if matrix == "yes":
        print("You are Agent Smith, I mean... Elrond")
    else:
        print("You are Legolas.")
elif race == "maiar":
    good_evil = input("Are you good or evil? ").lower()
    if good_evil == "good":
        print("You are Gandalf")
    elif good_evil == "evil":
        forged_ring = input("Are you the one who Forged the One Ring?").lower()
        if forged_ring == "yes":
            print("You are Sauron")
        else:
            print("You are Saruman")   
elif race == "hobbit":
    ring_carry = input("Do you carry one ring?").lower()
    if ring_carry == "yes":
        print("Frodo Baggins")
    else:
        garnder = input("Are you a Gardner? ").lower()
        if garnder == "yes":
            print("You are Samwise.")
        else:
            print("You are either Merry or Pippin")
elif race == "dwarf":
    print("You are Gimli son of Gloin")
else:
    print("You are an Orc, sorry about that.")




