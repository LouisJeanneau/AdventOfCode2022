from collections import deque

import numpy as np
add_robot = np.eye(4)
blueprints = []

def bfs(init_robot, init_ressources, init_time, cost, ans):
    q = deque()
    q.append((init_robot, init_ressources, init_time))
    max_robots = tuple(max(cost[:,i]) if i < 3 else 99 for i in range(4))
    seen = set()
    while len(q):
        robots, ressources, time = q.popleft()

        # ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_clay
        # Co, Cc, Co1, Co2, Cg1, Cg2, T):

        #(ore, clay, obsidian, geodes, r1, r2, r3, r4, time)
        # o, c, ressources[2], g, r1, r2, r3, r4, t
        #(0, 0, 0,  0,  1,  0,  0, 0,  T)
        if robots[0] > max_robots[0]:
            robots[0] = max_robots[0]
        if robots[1] > max_robots[1]:
            robots[1] = max_robots[0]
        if robots[2] > max_robots[2]:
            robots[2] = max_robots[2]
        if ressources[0] >= time * max_robots[0] - robots[0] * (time - 1):
            ressources[0] = time * max_robots[0] - robots[0] * (time - 1)
        if ressources[1] >= time * cost[1][1] - robots[1] * (time - 1):
            ressources[1] = time * cost[1][1] - robots[1] * (time - 1)
        if ressources[2] >= time * cost[2][2] - robots[2] * (time - 1):
            ressources[2] = time * cost[2][2] - robots[2] * (time - 1)

        state = (robots , ressources, time)

        if state in seen:
            continue
        seen.add(state)


        ans = max(ans, ressources[3])

        if time == 25:
            continue


        for robot in range(3, -1, -1):
            if robots[robot] == max_robots[robot]:
                continue

            sub = np.subtract(ressources, cost[robot])
            if (sub < 0).any():
                continue
            q.append((np.add(robots, add_robot[robot]), np.add(sub, robots), time+1))
            break
        q.append((robots, np.add(ressources, robots), time+1))

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

    ans = 0
    bfs(robots, ressources, 1, blueprints[1], ans)
    print(ans)


