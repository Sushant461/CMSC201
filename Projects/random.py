"""
File:    jmps_and_hlts.py
Author:  Sushant Sharma
Date:   10/11/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description: DESCRIPTION OF WHAT THE PROGRAM DOES

"""

import random

GRID_WIDTH = 8
GRID_HEIGHT = 3
DICE_SIDES = 6


def generate_random_map(length, the_seed=0):
    """
        :param length - the length of the map
        :param the_seed - the seed of the map
        :return: a randomly generated map based on a specific seed, and length.
    """
    if the_seed:
        random.seed(the_seed)
    map_list = []
    for _ in range(length - 2):
        random_points = random.randint(1, 100)
        random_position = random.randint(0, length - 1)
        map_list.append(random.choices(['no', f'add {random_points}', f'sub {random_points}', f'mul {random_points}', f'jmp {random_position}', 'hlt'], weights=[5, 2, 2, 2, 3, 1], k=1)[0])

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
    map_length_str = input('Enter map length (>= 2): ').strip()
    seed_str = input('Enter seed (0 for random): ').strip()

    # the min
    if map_length_str.isdigit():
        map_length = int(map_length_str)
    else:
        print('Invalid length. Using 9.')
        map_length = 9

    if seed_str.lstrip('-').isdigit():
        the_seed = int(seed_str)
    else:
        print('Invalid seed. Using 0.')
        the_seed = 0

    if map_length < 2:
        print('Length too small. Using 9.')
        map_length = 9

#generating map 
the_map = generate_random_map(map_length, the_seed)

# building the display and grid
display = make_grid(len(the_map))

# filling it up, showing any number if it is present
for idx, instr in enumerate(the_map):
    parts = instr.split()
    op = parts[0].lower()

    if op = 'no':
        op = 'nop'
    short_op = op[:3]
    arg = parts[1] if len(parts) == 2 else ''

    # making a 2 line message, top = index, bottom = op/arg
    msg_top = f'{idx}'.ljust(3)[:3]
    msg_bot = (short_op +('' + arg else "")).ljst(7)[:7]