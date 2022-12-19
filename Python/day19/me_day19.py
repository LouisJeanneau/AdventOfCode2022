from collections import deque

import numpy as np

add_robot = np.eye(4)
blueprints = []


def bfs(init_robot, init_ressources, init_time, cost, ans):
    q = deque()
    r1, r2, r3, r4 = init_robot
    ore, clay, obsi, geod = init_ressources
    q.append((r1, r2, r3, r4, ore, clay, obsi, geod, init_time))
    max_robots = tuple(max(cost[:, i]) if i < 3 else 99 for i in range(4))
    seen = set()
    while len(q):
        r1, r2, r3, r4, ore, clay, obsi, geod, time = q.popleft()

        if r1 > max_robots[0]:
            r1 = max_robots[0]
        if r2 > max_robots[1]:
            r2 = max_robots[0]
        if r3 > max_robots[2]:
            r3 = max_robots[2]
        if ore > time * max_robots[0] - r1 * (time - 1):
            ore = time * max_robots[0] - r1 * (time - 1)
        if clay > time * cost[2][1] - r2 * (time - 1):
            clay = time * cost[2][1] - r2 * (time - 1)
        if obsi > time * cost[3][2] - r3 * (time - 1):
            obsi = time * cost[3][2] - r3 * (time - 1)

        state = r1, r2, r3, r4, ore, clay, obsi, geod, time

        if state in seen:
            continue
        seen.add(state)

        ans = max(ans, geod)

        if time == 0:
            continue

        # for robot in range(3, -1, -1):
        #     if robots[robot] == max_robots[robot]:
        #         continue
        #
        #     sub = np.subtract(ressources, cost[robot])
        #     if (sub < 0).any():
        #         continue
        #     q.append((np.add(robots, add_robot[robot]), np.add(sub, robots), time + 1))
        #     break
        q.append((r1, r2, r3, r4, ore + r1, clay + r2, obsi + r3, geod + r4, time - 1))
        if ore >= cost[0][0]: # buy r1
            q.append((r1 + 1, r2, r3, r4, ore + r1 - cost[0][0], clay + r2, obsi + r3, geod + r4, time - 1))
        if ore >= cost[1][0]: # r2
            q.append((r1, r2 + 1, r3, r4, ore + r1 - cost[1][0], clay + r2, obsi + r3, geod + r4, time - 1))
        if clay >= cost[2][1] and ore >= cost[2][0]:
            q.append((r1, r2, r3 + 1, r4, ore + r1 - cost[2][0], clay + r2 - cost[2][1], obsi + r3, geod + r4, time - 1))
        if obsi >= cost[3][2] and ore >= cost[3][0]:
            q.append((r1, r2, r3, r4 + 1, ore + r1 - cost[3][0], clay + r2, obsi + r3 - cost[3][2], geod + r4, time - 1))




    return ans


with open("demo.txt") as f:
    input = f.read().splitlines()
    # Parse cost
    splitted_input = [l.split() for l in input]
    blueprints = [((int(line[6]), 0, 0, 0),
                   (int(line[12]), 0, 0, 0),
                   (int(line[18]), int(line[21]), 0, 0),
                   (int(line[27]), 0, int(line[30]), 0)) for line in splitted_input]
    blueprints = [np.array(l) for l in blueprints]
    # index 0 : cost ore robot in ore
    # index 1 : cost clay robot in ore
    # index 2 : cost obsi robot in ore and clay
    # index 3 : cost geode robot in ore and obsi

    # [ore, clay, obsi, geode]
    ressources = np.array([0, 0, 0, 0], int)
    robots = np.array([1, 0, 0, 0], int)

    sum = 0
    for i, b in enumerate(blueprints):
        print(i)
        sum += (i+1) * bfs(robots, ressources, 24, b, 0)
    print(sum)
