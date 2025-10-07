"""
File:    red_rover.py
Author: Sushant Sharma
Date:    10/03/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description:  simple red rover game with red and blue teams
  
"""
if __name__ == "__main__":

    red = []
    blue = []

    # Adding phase 
    adding = True
    turn = "Red"
    while adding:
        if turn == "Red":
            name = input("Who should we add to the Red team? ")
            if name == "begin the game":
                
                print("Who should we add to the Blue team?")
                adding = False
            else:
                if name != "":
                    red.append(name)
                turn = "Blue"
        else:
            name = input("Who should we add to the Blue team? ")
            if name == "begin the game":
                print("Who should we add to the Red team?")
                adding = False
            else:
                if name != "":
                    blue.append(name)
                turn = "Red"

    # Gameplay phase 
    current_team = "Red"   
    game_over = False

    while not game_over:
        if current_team == "Red":
            prompt = "Who should Red team send over? "
            team = red
            other = blue
            team_name = "Red"
            other_name = "Blue"
        else:
            prompt = "Who should Blue team send over? "
            team = blue
            other = red
            team_name = "Blue"
            other_name = "Red"

        cmd = input(prompt)

        if cmd == "display":
            if team_name == "Red":
                print("The Red Team is composed of:")
            else:
                print("The Blue Team is composed of:")

            # print names exactly like: Jim, Archie, Jill, Tim,
            i = 0
            line = ""
            while i < len(team):
                if i == 0:
                    line = team[i] + ","
                else:
                    line = line + " " + team[i] + ","
                i = i + 1
            print(line)
            # same team asks again next loop

        elif cmd in team:
            made_it = input("Did they make it through the line? ")
            if made_it == "yes":
                print(cmd + " stays on the " + team_name + " team")
            else:
                team.remove(cmd)
                other.append(cmd)
                print(cmd + " changes to the " + other_name + " team")

            
            if current_team == "Red":
                current_team = "Blue"
            else:
                current_team = "Red"

            # win check
            if len(red) == 1 or len(blue) == 1:
                if len(red) == 1 and len(blue) > 1:
                    print("Blue team wins!")
                elif len(blue) == 1 and len(red) > 1:
                    print("Red team wins!")
                else:
                    print("Game over.")
                game_over = True

        else:
            print("Type 'display' or a valid name on the " + team_name + " team.")