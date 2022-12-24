import numpy as np

# WHAT IF i use a dict ?
# map = np.zeros((140, 140), int)
elves_pos = {}
temp_dict = {}

# (x, y) with x going south and y going east
#  0      y
#
#  x
directions = (
    (-1, 0),  # North
    (1, 0),  # South
    (0, -1),  # West
    (0, 1),  # East
)

neighbours = (
    ((-1, -1), (-1, 0), (-1, 1)),  # Whole North
    ((1, -1), (1, 0), (1, 1)),  # South
    ((-1, -1), (0, -1), (1, -1)),  # West
    ((-1, 1), (0, 1), (1, 1))  # East
)
neighbours_all = ((-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1),          ( 0, 1),
                  ( 1, -1), ( 1, 0), ( 1, 1))


def debug():
    max_x = max(elves_pos.keys(), key=lambda x: x[0])[0]
    min_x = min(elves_pos.keys(), key=lambda x: x[0])[0]
    max_y = max(elves_pos.keys(), key=lambda x: x[1])[1]
    min_y = min(elves_pos.keys(), key=lambda x: x[1])[1]
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            if elves_pos.get((x,y), 0):
                print("#", end='')
            else:
                print(".", end='')
        print("")
    print("\n\n")


with open("input.txt") as f:
    # parsing
    input = f.read().splitlines()
    i = 0
    for x, line in enumerate(input):
        for y, charac in enumerate(line):
            if charac == "#":
                elves_pos[(x, y)] = 1
                i += 1

    stop = True
    # STEPS
    for step in range(1000):
        # debug()
        temp_dict.clear()
        stop = True
        # propose
        for pos, elve_num in elves_pos.items():
            if not sum(elves_pos.get(tuple(np.add(pos, neighbours_all[n])), 0) for n in range(8)):
                l = temp_dict.get(pos, [])
                l.append(pos)
                temp_dict[pos] = l
                continue
            for try_number in range(4):
                stop = False
                res = sum(
                    elves_pos.get(tuple(np.add(pos, neighbours[(step + try_number) % 4][n])), 0) for n in range(3))

                # one = old_dict[np.add(pos, neighbours[(step+try_number)%4][0])]
                # two = old_dict[np.add(pos, neighbours[(step + try_number) % 4][1])]
                # three = old_dict[np.add(pos, neighbours[(step + try_number) % 4][2])]
                if not res:
                    new_pos = tuple(np.add(pos, directions[(step + try_number) % 4]))
                    l = temp_dict.get(new_pos, [])
                    l.append(pos)
                    temp_dict[new_pos] = l
                    break
                elif try_number==3:
                    l = temp_dict.get(pos, [])
                    l.append(pos)
                    temp_dict[pos] = l
        if stop:
            print(step+1)
            break
        elves_pos.clear()
        # move
        for grid_pos, elves in temp_dict.items():
            if len(elves) == 1:
                elves_pos[grid_pos] = 1
            else:
                for e in elves:
                    elves_pos[e] = 1

    # debug()
    max_x = max(elves_pos.keys(), key=lambda x: x[0])[0]
    min_x = min(elves_pos.keys(), key=lambda x: x[0])[0]
    max_y = max(elves_pos.keys(), key=lambda x: x[1])[1]
    min_y = min(elves_pos.keys(), key=lambda x: x[1])[1]
    print( (max_x - min_x + 1) * (max_y - min_y + 1) - i)
    # 3836 too high
