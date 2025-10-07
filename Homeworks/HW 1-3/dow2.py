"""
File:   dow2.py
Author:  Sushant Sharma
Date:    09/26/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description:  calculating what weekday is it in september and addix a suffix to it
""" 

if __name__ == "__main__":
    day = int(input("What day of the month is it? "))
    if day < 1 or day > 30:
        print("That day", day, "is out of range you must enter a number between 1 and 30")
    else:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        index = (day-1) % 7
        weekday = days[index]

        if 11 <= day % 100 <= 19:
            suffix = "th"
        elif day % 10 == 1:
            suffix = "st"
        elif day % 10 == 2:
            suffix = "nd"
        elif day % 10 == 3:
            suffix = "rd"
        else:
            suffix = "th"
        print(f"The{day}{suffix} of September is a {weekday}")