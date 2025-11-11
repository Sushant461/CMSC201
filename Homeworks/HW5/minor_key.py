"""
File:   minor_key.py
Author:  Sushant Sharma
Date:    10/12/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description:  Creates and prints the harmonic minor scale for a given musical note.
"""

# Constants  
FLAT = '\u266d'  # unicode for ♭
MUSICAL_NOTES = ['C', 'D' + FLAT, 'D', 'E' + FLAT, 'E', 'F',
                 'G' + FLAT, 'G', 'A' + FLAT, 'A', 'B' + FLAT, 'B']

HARMONIC_MINOR_STEPS = [2, 1, 2, 2, 1, 3, 1] # half step pattern


def normalize_input_to_note(user_text):

    s = user_text.strip().lower()
    if s == "quit":
        return "QUIT"


    flat_pos = s.find(" flat")
    if flat_pos != -1:
        base = s[:flat_pos].strip()
        if len(base) > 0:
            return base.upper() + FLAT
        # If user typed just "flat", treat as weird token
        return FLAT
    else:
        return s.upper()


def index_of_note(note):

    i = 0
    while i < len(MUSICAL_NOTES):
        if MUSICAL_NOTES[i] == note:
            return i
        i += 1
    return -1


def harmonic_minor_scale_from(start_idx):

    scale = [MUSICAL_NOTES[start_idx]]

    i = 0
    current_index = start_idx
    while i < len(HARMONIC_MINOR_STEPS):
        step = HARMONIC_MINOR_STEPS[i]
        current_index = (current_index + step) % len(MUSICAL_NOTES)
        scale.append(MUSICAL_NOTES[current_index])
        i += 1

    return scale


def main():

    done = False
    while not done:
        user = input("Enter a starting note (C, D flat): ")
        token = normalize_input_to_note(user)

        if token == "QUIT":
            # Exit the program
            done = True
        else:
            start_idx = index_of_note(token)
            if start_idx == -1:
                print("There is no starting note", token)
            else:
                scale = harmonic_minor_scale_from(start_idx)
                # Print notes space-separated
                i = 0
                line = ""
                while i < len(scale):
                    if i == 0:
                        line = scale[i]
                    else:
                        line = line + " " + scale[i]
                    i += 1
                print(line)


if __name__ == "__main__":
    main()



