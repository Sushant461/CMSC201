"""
File:   list_merge.py
Author:  Sushant Sharma
Date:    09/26/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description:  asking the user for what they want to put in the 1st and 2nd list and then merging  it, and prinig the raw 1st & 2nd and the merged one out
  
"""
if __name__ == "__main__":
    n = int(input("How many elements do you want in each list? "))
    first = []
    second = []
    merged = []
    #building first list
    for i in range(n):
        item = input("What do you want to put in the first list? ")
        first.append(item)
    # 2nd one
    for i in range(n):
        item = input("What do you want to put in the second list? ")
        second.append(item)

    for i in range(n):
        merged.append(first[i])
        merged.append(second[i])
    
    print("The first list is: ", first)
    print("The second list is: ", second)
    print("The merged list is: ",merged)