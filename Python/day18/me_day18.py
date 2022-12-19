from collections import deque

import matplotlib.pyplot as plt
import numpy as np

neighbours_shift = (
    (-1, 0, 0),  # left
    (1, 0, 0),  # right
    (0, -1, 0),  # down
    (0, 1, 0),  # up
    (0, 0, -1),  # back
    (0, 0, 1)  # front
)
max_x, max_y, max_z = 0, 0, 0


def bfs(start_x, start_y, start_z, grid, unchecked, ans):
    unchecked[start_x, start_y, start_z] = 0
    q = deque()
    q.append((start_x, start_y, start_z))
    while len(q):
        x, y, z = q.popleft()
        unchecked[x, y, z] = 0
        for a, b, c in neighbours_shift:
            new_x, new_y, new_z = (x + a) % max_x, (y + b) % max_y, (z + c) % max_z
            if grid[new_x, new_y, new_z] and unchecked[new_x, new_y, new_z]:
                unchecked[new_x, new_y, new_z] = 0
                q.append((new_x, new_y, new_z))
            elif not grid[new_x, new_y, new_z]:
                ans += 1
    return ans


with open("input.txt") as f:
    input = f.read().splitlines()
    points = (tuple(map(int, line.split(','))) for line in input)
    x, y, z = [int(o.split(',')[0]) for o in input], [int(o.split(',')[1]) for o in input], [int(o.split(',')[2]) for o
                                                                                             in input]

    max_x, max_y, max_z = max(x) + 2, max(y) + 2, max(z) + 2

    grid = np.ones((max_x, max_y, max_z), int)
    for i in range(len(input)):
        grid[x[i], y[i], z[i]] = 0

    free_faces = 0
    for i in range(len(input)):
        for a, b, c in neighbours_shift:
            free_faces += grid[x[i] + a, y[i] + b, z[i] + c]

    # Part 2
    ans = 0
    unchecked = np.ones((max_x, max_y, max_z), int)
    ans = bfs(0, 0, 0, grid, unchecked, ans)


    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    #
    # # Plot the points
    # ax.scatter(x, y, z)
    #
    # # Show the plot
    # plt.show()

    print(free_faces)
    print(ans)
