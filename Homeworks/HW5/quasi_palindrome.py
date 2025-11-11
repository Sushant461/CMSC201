"""
File:    quasi_palindrome.py
Author:  Sushant Sharma
Date:    10/12/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description:     Checks if a word is a quasi-palindrome within a given number of errors.
"""
def quasi_palindrome(word, errors):
    left = 0
    right = len(word) - 1
    mismatches = 0

    # Compare letters from both ends
    while left < right:
        if word[left] != word[right]:
            mismatches += 1
            # If mismatches exceed limit, it's not a quasi-palindrome
            if mismatches > errors:
                return False
        left += 1
        right -= 1

    # If mismatches <= errors, it qualifies
    return True


if __name__ == "__main__":
    done = False
    while not done:
        word = input("What word do you want to check? ")
        if word.lower() == "quit":
            done = True
        else:
            errors = int(input("How many errors do you want to allow? "))

            # Check if it is a quasi-palindrome
            if quasi_palindrome(word, errors):
                print("It was a ", errors, "-quasi-palindrome!", sep="")
            else:
                print("It was not a ", errors, "-quasi-palindrome!", sep="")



