# define sprites
import math

import numpy as np

sprites = (
    (  # - flat
        0b111100,
    ),

    (  # cross
        0b010000,
        0b111000,
        0b010000
    ),

    (  # angle
        0b001000,
        0b001000,
        0b111000
    ),

    (  # |
        0b100000,
        0b100000,
        0b100000,
        0b100000
    ),

    (  # square
        0b110000,
        0b110000
    ),
)


# parse input
with open("input.txt") as f:
    global jets
    jets = f.read().strip()
    f.close()


# debug function to draw
def debug2(map, rock, index):
    for i in range(len(map) - 1, -1, -1):
        if index - len(rock) + 1 <= i <= index:
            print(f'{map[i] | rock[index - i]:0>9b}')
        else:
            print(f'{map[i]:0>9b}')
    print()


# create map of values
occupied_map = [0b111111111, 0b100000001, 0b100000001, 0b100000001, 0b100000001]
jets_index, total_rocks = 0, 0
jets_len = len(jets)
state, height = [], []
loops = 1_000_000_000_000
cycle_length, cycle_height, cycle_number = 0, 0, 0

while total_rocks < loops:
    rock = list(sprites[total_rocks % 5])

    # We append or remove line from the top of the map according to our needs
    a = occupied_map.index(257) + 3 + len(rock) - len(occupied_map)
    occupied_map.extend([257 for _ in range(a)])
    for _ in range(0, a, -1):
        occupied_map.pop()

    rock_ver_index = len(occupied_map) - 1

    can_fall = True
    while can_fall:
        # SOooooooo, i'm cheking through the full height of the rock if it can shift by using bitwise &
        # If it can shift, every bitwise & should be 0 and sum of those will be 0
        if not sum(
                occupied_map[rock_ver_index - h] & eval(str(rock[h]) + jets[jets_index % jets_len] * 2 + str(1)) for h
                in range(len(rock))):
            # Shift the rock
            for h in range(len(rock)):
                rock[h] = eval("rock[h]" + jets[jets_index % jets_len] * 2 + " 1")
        jets_index += 1

        # Checking if every line can shift by 1 vertically
        # if at any point I find a non-0 after a bitwise & : means i have contact
        if sum(occupied_map[rock_ver_index - len(rock) + h] & rock[-1 - h] for h in range(len(rock))):
            for x in range(len(rock)):
                occupied_map[rock_ver_index - x] |= rock[x]
            can_fall = False
            total_rocks += 1
            break
        rock_ver_index -= 1
    # Finger print the state to then find cycle
    height.append(occupied_map.index(257)-1)
    if total_rocks > jets_len and not cycle_length:
        current_state = (jets_index % jets_len, total_rocks % 5, occupied_map[occupied_map.index(257) - 1])
        if state.count(current_state) != 0:
            # print("jackpot " + str(total_rocks) + " - " + str(state[::-1].index(current_state)) + " = " + str(total_rocks - state[::-1].index(current_state)))
            cycle_length = state[::-1].index(current_state) + 1
            cycle_height = height[-1] - height[-1-cycle_length]
            cycle_number = math.floor((loops - total_rocks)/cycle_length)
            total_rocks += cycle_number * cycle_length
        state.append((jets_index % jets_len, total_rocks % 5, occupied_map[occupied_map.index(257) - 1]))
    else:
        state.append((0))

print(occupied_map.index(257) - 1 + cycle_number*cycle_height)
