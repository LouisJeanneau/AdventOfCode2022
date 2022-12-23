# Parse input :
# Map first, created of good sized then filled with values
# -1 for void, 0 for walkable and 1 for wall ?
# instruction then : split digits and letters
# var : facing, position, instructions_pos
# every turn :
#   execute instru
#
# check of valid advance : go forward the number of time specified until wall or no more move. don't decrement if void

# final output : 1000 * row + 4 * column + facing
import re

import numpy as np

move = ((0, 1), (1, 0), (0, -1), (-1, 0))


def face_change(x, y, orientation):
    # 1
    if x == 199 and 50 <= y <= 99 and orientation == 3:
        x, y = 150 + y - 50, 0
        orientation = 0
        return x, y, orientation
    # 2
    if x == 199 and 100 <= y <= 149 and orientation == 3:
        x, y = 199, y - 100
        orientation = 3
        return x, y, orientation
    # 3
    if 0 <= x <= 49 and y == 49 and orientation == 2:
        x, y = 149 - x, 0
        orientation = 0
        return x, y, orientation
    # 4
    if 50 <= x <= 99 and y == 49 and orientation == 2:
        x, y = 100, x - 50,
        orientation = 1
        return x, y, orientation
    # 5
    if x == 99 and 0 <= y <= 49 and orientation == 3:
        x, y = y + 50, 50
        orientation = 0
        return x, y, orientation
    # 6
    if 100 <= x <= 149 and y == 149 and orientation == 2:
        x, y = 149 - x, 50
        orientation = 0
        return x, y, orientation
    # 7
    if 150 <= x <= 199 and y == 149 and orientation == 2:
        x, y = 0, x - 100
        orientation = 1
        return x, y, orientation
    # 8
    if x == 0 and 0 <= y <= 49 and orientation == 1:
        x, y = 0, y + 100
        orientation = 1
        return x, y, orientation
    # 9
    if 150 <= x <= 199 and y == 50 and orientation == 0:
        x, y = 149, x - 100
        orientation = 3
        return x, y, orientation
    # 10
    if x == 150 and 50 <= y <= 99 and orientation == 1:
        x, y = y + 100, 49
        orientation = 2
        return x, y, orientation
    # 11
    if 100 <= x <= 149 and y == 100 and orientation == 0:
        x, y = 149 - x, 149
        orientation = 2
        return x, y, orientation
    # 12
    if 50 <= x <= 99 and y == 100 and orientation == 0:
        x, y = 49, x + 50
        orientation = 3
        return x, y, orientation
    # 13
    if x == 50 and 100 <= y <= 149 and orientation == 1:
        x, y = y - 50, 99
        orientation = 2
        return x, y, orientation
    # 14
    if 0 <= x <= 49 and y == 0 and orientation == 0:
        x, y = 149 - x, 99
        orientation = 2
        return x, y, orientation
    assert 0, "oups"
    return x, y, orientation


def test():
    return 0

def forward(x, y, orientation, number) -> tuple[int, int, int]:
    while True:
        if map[x, y] == 0:
            a, b, old_or = x, y, orientation
        x += move[orientation][0]
        y += move[orientation][1]
        x %= max_height
        y %= max_width
        if map[x, y] == 0:
            number -= 1
        elif map[x, y] == -1:
            x, y, orientation = face_change(x, y, orientation)
            number -= 1
        if map[x, y] == 1:
            return a, b, old_or

        if number == 0:
            return x, y, orientation


# Parsing
with open("input.txt") as f:
    splitted = f.read().splitlines()
    global map, max_height, max_width
    max_height = len(splitted) - 2
    max_width = max(len(i) for i in splitted[:-2])

    map = np.full((max_height, max_width), -1)

    for h in range(max_height):
        for w in range(len(splitted[h])):
            if splitted[h][w] == ".":
                map[h, w] = 0
            elif splitted[h][w] == "#":
                map[h, w] = 1

    instructions = re.split(r'(\d+)', splitted[-1])[1:-1]

    # init position
    facing = 0
    y = list(map[0, :]).index(0)
    x = 0

    for inst in instructions:
        print(x, y, facing)
        if x==143 and y==50 and facing==1:
            print("ici")
        # print(inst)
        if inst == "R":
            facing = (facing + 1) % 4
        elif inst == "L":
            facing = (facing - 1) % 4
        else:
            (x, y, facing) = forward(x, y, facing, int(inst))
    x += 1
    y += 1
    print(x * 1000 + y * 4 + facing)
    # not 136230, too high
    # not 187158, too high
    # Part 2 178171 too high
    # Part 2 55283 too low
