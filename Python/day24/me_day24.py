import numpy as np

# WHAT IF i use a dict ?
# map = np.zeros((140, 140), int)
user_pos_dict = {}
blizzards_dict = {}
temp_dict = {}
height = 0
width = 0
# (x, y) with x going south and y going east
#  0      y
#
#  x
directions = (
    (0, 1),  # East
    (1, 0),  # South
    (0, -1),  # West
    (-1, 0),  # North
)
moves = directions + ((0, 0),)
pointing = {">": 0, "v": 1, "<": 2, "^": 3}


def debug():
    print("#" * width)
    for x in range(1, height - 1):
        print("#", end='')
        for y in range(1, width - 1):
            a = blizzards_dict.get((x, y), [])
            if a:
                print(f'{len(a)}', end='')
            else:
                print(".", end='')
        print("#")
    print("#" * width)
    print("\n\n")


def part1():
    global blizzards_dict
    global user_pos_dict
    global height, width
    with open("input.txt") as f:
        # parsing
        input = f.read().splitlines()
        height = len(input)
        width = len(input[0])
        for x, line in enumerate(input):
            for y, charac in enumerate(line):
                if charac != "#" and charac != ".":
                    blizzards_dict[(x, y)] = [pointing[charac]]

        start = (0, input[0].index("."))
        finish = (height - 1, input[-1].index("."))
        user_pos_dict[start] = 0
        goal_reached = 0
        start_reached = 0

        while 1:
            # debug()

            # move blizzard
            temp_dict.clear()
            # For every grid cell with one (or more) blizz
            for grid_cell, blizzards in blizzards_dict.items():
                # for every blizzard
                for blizz in blizzards:
                    new_blizzard_pos = list(np.add(grid_cell, directions[blizz]))

                    # check boundaries
                    new_blizzard_pos[0] = (new_blizzard_pos[0] - 1) % (height - 2) + 1
                    new_blizzard_pos[1] = (new_blizzard_pos[1] - 1) % (width - 2) + 1
                    new_blizzard_pos = tuple(new_blizzard_pos)

                    l = temp_dict.get(new_blizzard_pos, [])
                    l.append(blizz)
                    temp_dict[new_blizzard_pos] = l
            blizzards_dict.clear()
            blizzards_dict = temp_dict.copy()

            # Move user
            temp_dict.clear()
            skip = False
            for grid_cell, time in user_pos_dict.items():
                for move in moves:
                    if skip:
                        break
                    new_user_pos = tuple(np.add(grid_cell, move))

                    # check end conditions
                    if new_user_pos == finish and goal_reached == 0:
                        goal_reached = 1
                        temp_dict.clear()
                        print("finish 1")
                        skip = True
                    elif new_user_pos == start and goal_reached == 1 and start_reached == 0:
                        start_reached = 1
                        temp_dict.clear()
                        print("start 1")
                        skip = True
                    elif new_user_pos == finish and goal_reached == 1 and start_reached == 1:
                        goal_reached = 2
                        temp_dict.clear()
                        print("finish 2")
                        skip = True
                    elif (new_user_pos != start and new_user_pos != finish) and (new_user_pos[0] % (height - 1) == 0 or new_user_pos[1] % (width - 1) == 0):
                        continue
                    if not blizzards_dict.get(new_user_pos, []):
                        temp_dict[new_user_pos] = time + 1
                if skip:
                    break

            if temp_dict.get(finish, []) and goal_reached == 2:
                print(temp_dict[finish])
            if goal_reached == 2:
                exit()
            user_pos_dict.clear()
            user_pos_dict = temp_dict.copy()


part1()
