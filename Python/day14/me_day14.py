import cProfile

from numpy import sign
import numpy as np

def physics(rocks: list, min_ver, max_ver, min_hor, max_hor):
    resting_sands = 0
    map = np.full((max_ver+4, max_hor-min_hor+4), 0)
    for rock in rocks:
        map[rock[1], rock[0]-min_hor+1] = 1
    void_not_encountered = True
    while void_not_encountered:
        can_move = True
        x,y = 500-min_hor+1,0
        while can_move:
            if y > max_ver:
                void_not_encountered = False
                can_move = False
            elif not map[y+1, x]:
                y += 1
            elif not map[y+1, x-1]:
                x -= 1
                y += 1
            elif not map[y+1, x+1]:
                x += 1
                y += 1
            else:
                resting_sands += 1
                map[y, x] = 1
                can_move = False
    print(resting_sands)

def physics_part2(rocks: list, min_ver, max_ver, min_hor, max_hor):
    map = np.full((max_ver + 3, max_ver*2+10), 0)
    for rock in rocks:
        map[rock[1], rock[0] - 500 + max_ver+1] = 1
    map[-1, :] = 1
    resting_sands = 0
    void_not_encountered = True
    while void_not_encountered:
        can_move = True
        x,y = max_ver+1,0
        while can_move:
            if not map[y + 1, x]:
                y += 1
            elif not map[y + 1, x - 1]:
                x -= 1
                y += 1
            elif not map[y + 1, x + 1]:
                x += 1
                y += 1
            elif x == max_ver+1 and y == 0:
                can_move = False
                void_not_encountered = False
                resting_sands += 1
            else:
                resting_sands += 1
                map[y, x] = 2
                can_move = False
    print(resting_sands)

with open("input.txt") as f:
    input = f.read().splitlines()
    rocks = []
    for line in input:
        coords_string = line.split(" -> ")
        coords = []
        for coord_string in coords_string:
            coords.append(eval(coord_string))
        for i in range(len(coords)-1):
            a, b, c, d = coords[i][0], coords[i+1][0], coords[i][1], coords[i+1][1],
            if a == b:
                for y in range(c, d + sign(d - c), sign(d - c)):
                    rocks.append((a,y))
            elif c == d:
                for x in range(a, b + sign(b - a), sign(b - a)):
                    rocks.append((x,c))
    # Sort by horizontal values to get min/max
    rocks.sort()
    min_hor, max_hor = rocks[0][0], rocks[-1][0]
    # Sort by vertical values to get min/max
    rocks.sort(key=lambda x: x[1])
    min_ver, max_ver = rocks[0][1], rocks[-1][1]
    cProfile.run("physics(rocks, min_ver, max_ver, min_hor, max_hor)")
    cProfile.run("physics_part2(rocks, min_ver, max_ver, min_hor, max_hor)")


