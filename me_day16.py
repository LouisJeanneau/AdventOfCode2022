import re
import time
from collections import deque
from typing import List

# file = "demo.txt"
file = "input.txt"

time_start = time.time()

lines = [re.split("[,;  =]+", line) for line in open(file).read().splitlines()]
flows = {x[1]: int(x[5]) for x in lines if x[5] != "0"}  # Dict of flows for non-0 value
successors = {x[1]: set(x[10:]) for x in lines}  # Dict of direct successors
bit_order = {x: 1<<i for i, x in enumerate(flows)}
graph = {x: {y: 1 if y in successors[x] else float('inf') for y in successors} for x in
         successors}  # graph of shortest path from what we know
# complete the graph
for middle in graph:
    for start in graph:
        for end in graph:
            graph[start][end] = min(graph[start][end], graph[start][middle] + graph[middle][end])

# BFS now
flow_nodes = bit_order.keys()
total_nodes = len(flow_nodes)


def bfs(where_actually, time_left, total_pressure, where_been, ans):
    ans[where_been] = max(ans.get(where_been, 0), total_pressure)
    for v in flows:
        t = time_left - graph[where_actually][v] - 1
        if t < 0 or where_been & bit_order[v]:
            continue
        bfs(v, t, total_pressure + flows[v] * t, where_been | bit_order[v], ans)
    return ans

ans = bfs("AA", 30, 0, 0, {})
print(sorted(ans.values(), reverse=True)[0])
print(f'total time elapsed : {time.time() - time_start} s')

time_start = time.time()
part2 = bfs("AA", 26, 0, 0, {})
part2_ans = max(v1 + v2 for k1, v1 in part2.items()
                for k2, v2 in part2.items() if not k1 & k2)
print(f'total time elapsed : {time.time() - time_start} s')
print(part2_ans)
