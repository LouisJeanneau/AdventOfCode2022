import matplotlib.pyplot as plt
import numpy
from collections import deque
import cProfile

'''
Topography print
with open("input.txt") as f:
    input = f.read().splitlines()
    for i in range(len(input)):
        input[i] = [ord(c)-95 if (c!="S" and c!="E") else 0 for c in list(input[i])]
    im = numpy.array(input)
    plt.imshow(im)
    plt.colorbar()
    plt.show()
    plt.imsave("topography.png", im)
'''

# Part 1
def dijkstra(map, start, finish):
    to_visit = deque()
    to_visit.append(start)
    n, m = len(map), len(map[0])
    shortest = [[32767] * m for _ in range(n)]
    shortest[start[0]][start[1]] = 0
    while len(to_visit):
        i, j = to_visit.popleft()
        actual_height = map[i][j]
        actual_shortest = shortest[i][j]
        for a,b in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            if 0 < j + b < m-1 and 0 < i + a < n-1 and (map[i+a][j+b] <= actual_height + 1) and (shortest[i+a][j+b] > actual_shortest + 1):
                shortest[i+a][j+b] = actual_shortest + 1
                to_visit.append((i+a, j+b))
    print(shortest[finish[0]][finish[1]])
    return 0

def dijkstra_part2(map, start):
    to_visit = deque()
    to_visit.append(start)
    n, m = len(map), len(map[0])
    shortest = [[32767] * m for _ in range(n)]
    shortest[start[0]][start[1]] = 0
    while len(to_visit):
        i, j = to_visit.pop()
        actual_height = map[i][j]
        actual_shortest = shortest[i][j]

        for a,b in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            if 0 <= j + b <= m-1 and 0 <= i + a <= n-1 and (map[i+a][j+b] <= actual_height + 1) and (shortest[i+a][j+b] > actual_shortest + 1):
                shortest[i+a][j+b] = actual_shortest + 1
                to_visit.append((i+a, j+b))
    shortest_overall = 30000
    for i in range(n):
        for j in range(m):
            if map[i][j] == 26 and shortest[i][j] < shortest_overall:
                shortest_overall = shortest[i][j]
    print(shortest_overall)
    return



with open("input.txt") as f:
    input = f.read().splitlines()
    start, finish = 0, 0
    heightmap = [[] for _ in range(len(input))]
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == "S":
                start = (i,j)
            if input[i][j] == "E":
                finish = (i, j)
        heightmap[i] = [ord(c) - 96 if (c != "S" and c != "E") else 0 for c in list(input[i])]
    heightmap[start[0]][start[1]] = 1
    heightmap[finish[0]][finish[1]] = 26
    cProfile.run("dijkstra(heightmap, start, finish)")
    heightmap_inv = [[] for _ in range(len(input))]
    for i in range(len(input)):
        heightmap_inv[i] = [27-c for c in heightmap[i]]
    dijkstra_part2(heightmap_inv, finish)