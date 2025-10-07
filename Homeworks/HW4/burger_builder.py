"""
File:    burger_builder.py
Author:  Sushant Sharma
Date:    10/03/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description:  Builds a burger from user input and reports the layers.
"""
if __name__ == "__main__":

    burger_count = 0
    has_cheese = False
    condiments = []

    # force start with bottom bun
    item = input("What do you want to add? ")
    while item != "bottom bun":
        print("You must start with the bottom bun!")
        item = input("What do you want to add? ")

    building = True
    while building:
        item = input("What do you want to add? ")

        if item == "top bun":
            # stop building
            building = False
        elif item == "burger":
            burger_count = burger_count + 1
        elif item == "cheese":
            if not has_cheese:
                has_cheese = True
        else:
            # add condiment only if not already in the list
            if item != "bottom bun" and (item not in condiments):
                condiments.append(item)

   # final  
    print("Burger summary:")
    print(" Patties:", burger_count)
    if has_cheese:
        print(" Cheese: yes")
    else:
        print(" Cheese: no")

    if len(condiments) == 0:
        print(" Condiments: none")
    else:
        # simple comma-separated list
        text = ""
        i = 0
        while i < len(condiments):
            if i == 0:
                text = condiments[i]
            else:
                text = text + ", " + condiments[i]
            i = i + 1
        print(" Condiments:", text)