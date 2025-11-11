"""
    File:    jmps_and_hlts.py
    Author:  Sushant Sharma
    Date:    10/11/2025
    Section: 42
    E-mail:  ssharm11@umbc.edu
    Description:   JMPs and HLTs a dice driven board game simulator.
    This program generates a random map, rolls a single six-sided dice each turn, moves the player with wrap-around,
    excutes the instruction on the landing square, prints the board once, logs each step, and ends on 'hlt'. 
    A replay loop lets the user run multiple games.
"""

import random

GRID_WIDTH = 8
GRID_HEIGHT = 3
DICE_SIDES = 6

CMD_ADD = 'add'
CMD_SUB = 'sub'
CMD_MUL = 'mul'

CMD_NOP = 'nop'
CMD_JMP = 'jmp'
CMD_HLT = 'hlt'

def apply_math_command(score, instruction):
    """
        :param score: current int score 
        :param instruction: string like 'add 5', 'sub 27', or 'mul 3'
        :return: a updated score after applying the math command 
    """   
    # split
    parts = instruction.strip().lower().split()
    if len(parts) != 2:
        return score  # do nothing
    
    cmd = parts[0]
    if parts[1].isdigit():
        value = int(parts[1])
    else:
        return score  

    if cmd == CMD_ADD:
        score = score + value
    elif cmd == CMD_SUB:
        score = score - value
    elif cmd == CMD_MUL:
        score = score * value

    return score

def handle_jump(game_map, position):
    """
        :game map: list of the strings aka the full map
        :param position: currenty int position ( where the jmp x was found)
        :return: the new position after the jump
    """
    parts = game_map[position].strip().lower().split()

    if len(parts) != 2 or parts[0] != 'jmp':
        return position # not a valid jump
    
    if not parts[1].isdigit():
        return position 

    jump_to = int(parts[1])
    # making sure its within the range

    if 0 <= jump_to < len(game_map):
        return jump_to
    else:
        return position  # the target is invalid so you have to stay put 

def display_board(game_map):
    """
        :game_map - list of the strings represnting the full board map 
        :return: (none) prints the boards neatly 
    """
    size = len(game_map)
    grid = make_grid(size)

    #filling in the squares with its index and command
    for i in range(size):
        fill_grid_square(grid, size, i, f"{i}\n{game_map[i]}")

    # print each row joined together for a clean look
    for row in grid:
        print(''.join(row))


def resolve_landing(game_map, position, score, rolled):
    """
    :param game_map: list of instructions
    :param position: current position AFTER moving by dice
    :param score: current score BEFORE applying the landed instruction
    :param rolled: the dice value used to arrive here (for logging)
    :return: the final position, updated score, and game_over status for this turn 
    """
    game_over = False
    keep_resolving = True  


    while keep_resolving:
        instruction = game_map[position].strip().lower()

        print(f"Pos: {position} Score: {score}, instruction {instruction} Rolled: {rolled}")

        if instruction.startswith(CMD_JMP):
            # Jump, then loop again to print the destination with same roll
            position = handle_jump(game_map, position)

        elif instruction.startswith(CMD_ADD) or instruction.startswith(CMD_SUB) or instruction.startswith(CMD_MUL):
            score = apply_math_command(score, instruction)
            keep_resolving = False  # end of turn on math

        elif instruction.startswith(CMD_NOP):
            keep_resolving = False  # end of turn on nop

        elif instruction.startswith(CMD_HLT):
            game_over = True
            keep_resolving = False  # game over

        else:
            # Unknown instruction > end turn safely
            keep_resolving = False

    return position, score, game_over

def play_game(game_map):
    """
    :param game_map: list of instruction strings
    :return: None

    """
    size = len(game_map)
    position = 0      # start at 0 per spec
    score = 0
    game_over = False

    # Print the board once
    display_board(game_map)

    while not game_over:
        rolled = roll_dice()
        position = move_position(position, rolled, size)  
        position, score, game_over = resolve_landing(game_map, position, score, rolled)

    final_instruction = game_map[position].strip().lower()
    print(f"Final Pos: {position} Final Score: {score}, Instruction {final_instruction}")
    

def move_position(position, rolled, board_size):
    """
    :param position: current integer position
    :param rolled: dice roll result
    :param board_size: length of the board
    :return:  position after moving
    """
    return (position + rolled) % board_size




def generate_random_map(length, the_seed=0):
    """
        :param length: the length of the map
        :param the_seed: the seed of the map
        :return: a randomly generated map based on a specific seed, and length.
    """
    if the_seed:
        random.seed(the_seed)
    map_list = []
    for _ in range(length - 2):
        random_points = random.randint(1, 100)
        random_position = random.randint(0, length - 1)
        map_list.append(random.choices(['nop', f'add {random_points}', f'sub {random_points}', f'mul {random_points}', f'jmp {random_position}', 'hlt'], weights=[5, 2, 2, 2, 3, 1], k=1)[0])

    return ['nop'] + map_list + ['hlt']


def make_grid(table_size):
    """
    :param table_size: this needs to be the length of the map
    :return: returns a display grid that you can then modify with fill_grid_square (it's a 2d-grid of characters)
    """
    floating_square_root = table_size ** (1 / 2)

    int_square_root = int(floating_square_root) + (1 if floating_square_root % 1 else 0)
    table_height = int_square_root
    if int_square_root * (int_square_root - 1) >= table_size:
        table_height -= 1

    the_display_grid = [[' ' if j % GRID_WIDTH else '*' for j in range(GRID_WIDTH * int_square_root + 1)]
                        if i % GRID_HEIGHT else ['*' for j in range(GRID_WIDTH * int_square_root + 1)]
                        for i in range(table_height * GRID_HEIGHT + 1)]
    return the_display_grid


def fill_grid_square(display_grid, size, index, message):
    """
    :param display_grid:  the grid that was made from make_grid
    :param size:  this needs to be the length of the total map, otherwise you may not be able to place things correctly.
    :param index: the index of the position where you want to display the message
    :param message: the message to display in the square at position index, separated by line returns.
    """
    floating_square_root = size ** (1 / 2)
    int_square_root = int(floating_square_root) + (1 if floating_square_root % 1 else 0)
    table_row = index // int_square_root
    table_col = index % int_square_root

    if table_row % 2 == 0:
        column_start = GRID_WIDTH * table_col
    else:
        column_start = GRID_WIDTH * (int_square_root - table_col - 1)

    for r, message_line in enumerate(message.split('\n')):
        for k, c in enumerate(message_line):
            display_grid[GRID_HEIGHT * table_row + 1 + r][column_start + 1 + k] = c


def roll_dice():
    """
        Call this function once per turn.

        :return: returns the dice roll
    """
    return random.randint(1, DICE_SIDES)


if __name__ == '__main__':
    play_again = True

    while play_again:
        user_input = input("Board Size and Seed: ").strip()
        parts = user_input.split()

        # validate
        valid = len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit()
        size = int(parts[0]) if valid else 0
        seed = int(parts[1]) if valid else 0
        valid = valid and size >= 2  # simple guard so the board can render        

        if valid:
            game_map = generate_random_map(size, seed)
            play_game(game_map)
            again = input("Play again? (y/n): ").strip().lower()
            if again != 'y':
                play_again = False
        else:
            print("Invalid input. Please enter two integers like: 10 17 (size at least 2).")






    
