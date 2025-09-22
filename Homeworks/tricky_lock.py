"""
File:   tricky_lock.py
Author:  Sushant Sharma
Date:    09/17/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description:  trying to open a tricky lock, requires sum of two numbers to be 36 and exactly two switches to be up
  
"""


first_num = int(input("What is the first number in the combination lock? "))

second_num = int(input("What is the second number in the combination lock? ")) 

first_switch = (input("What is the position of the first switch(up/down)? "))

second_switch = (input("What is the position of the second switch(up/down)? "))

third_switch = (input("What is the position of the third switch(up/down)? "))

sum_ok = (first_num + second_num == 36)

first_up = (first_switch == 'up')
second_up = (second_switch == 'up')
third_up = (third_switch == 'up')

nump_ups = first_up + second_up + third_up
switches_ok = (nump_ups == 2)

if sum_ok and switches_ok:
    print("The lock opens, you gain access to the treasure.")
elif sum_ok or switches_ok:
    print("The lock clanks but does not open.")
else:
    print("The lock does not even budge, try again.")