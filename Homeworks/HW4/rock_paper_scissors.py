"""
File:    rock_paper_scissors.py
Author: Sushant Sharma
Date:    10/03/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description: 
  
"""
import sys
from random import choice, seed

if len(sys.argv) >= 2:
   seed(sys.argv[1])


if __name__ == "__main__":
    user_input = input("Enter rock, paper, or scissors to play, stop to end > ")

    while user_input != "stop":
        if user_input not in ["rock","paper","scissors"]:
            print("You need to select rock, paper or scissors.")
        else:
            computer = choice (["rock","paper","scissors"])

            if user_input == computer:
                print("Both", user_input + ",", "there is a tie.")
            elif user_input == "rock" and computer == "scissors":
                print("Rock crushes scissors, you win.")
            elif user_input == "rock" and computer == "paper":
                print("Paper covers rock, you lose.")
            elif user_input == "paper" and computer == "rock":
                print("Paper covers rock, you win.")
            elif user_input == "paper" and computer == "scissors":
                print("Scissors cut paper, you lose.")
            elif user_input == "scissors" and computer == "paper":
                print("Scissors cut paper, you win.")
            elif user_input == "scissors" and computer == "rock":
                print("Rock crushes scissors, you lose.")
        user_input = input("Enter rock, paper, or scissors to play, stop to end.")