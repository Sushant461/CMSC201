"""
File:   day_of_the_week.py
Author:  Sushant Sharma
Date:    09/19/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description:  points out what weekday it is in the month of September  2023 with the correct suffix
  
"""

day = int(input("What day of September 2023 is it? "))

if day < 1 or day > 30:
    print("That", day, "is out of range, you must enter a number between 1 and 30")
else:
    remainder = day % 7
    if remainder == 1:
        weekday = "Friday"
    elif remainder == 2:
        weekday = "Saturday"
    elif remainder == 3:
        weekday = "Sunday"
    elif remainder == 4:
        weekday = "Monday"
    elif remainder == 5:
        weekday = "Tuesday"
    elif remainder == 6:
        weekday = "Wednesday"
    else:
        weekday = "Thrusday" 

    if day % 10 == 1 and day != 11:
        suffix = "st"
    elif day % 10 == 2 and day != 12:
        suffix = "nd"
    elif day % 10 == 3 and day != 13:
        suffix = "rd"
    else:
        suffix = "th"
    print("September ",day, suffix,"is a", weekday)
    





