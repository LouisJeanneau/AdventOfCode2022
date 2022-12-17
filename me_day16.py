import re
import time
from collections import deque
from typing import List

# file = "demo.txt"
file = "input.txt"

time_start = time.time()

class Node:
    where_been: List[str]
    where_actually: str
    time_left: int
    total_pressure: int

    def __init__(self, where_actually, time_left, total_pressure, where_been):
        self.where_actually = where_actually
        self.time_left = time_left
        self.total_pressure = total_pressure
        self.where_been = where_been


lines = [re.split("[,;  =]+", line) for line in open(file).read().splitlines()]
flows = {x[1]: int(x[5]) for x in lines if x[5] != "0"}  # Dict of flows for non-0 value
successors = {x[1]: set(x[10:]) for x in lines}  # Dict of direct successors
graph = {x: {y: 1 if y in successors[x] else float('inf') for y in successors} for x in
         successors}  # graph of shortest path from what we know
# complete the graph
for middle in graph:
    for start in graph:
        for end in graph:
            graph[start][end] = min(graph[start][end], graph[start][middle] + graph[middle][end])

# BFS now
flow_ordered = [x[0] for x in sorted(list(flows.items()), key=lambda x: x[1], reverse=True)]
total_nodes = len(flow_ordered)


def bfs(n: Node, ans):
    to_visit = deque()
    to_visit.append(n)
    ans = dict()
    while len(to_visit):
        node = to_visit.popleft()
        ans[frozenset(node.where_been)] = max(ans.get(frozenset(node.where_been), 0), node.total_pressure)
        if node.time_left < 0 or len(node.where_been) == total_nodes:
            continue
        for v in flow_ordered:
            if v not in node.where_been:
                t = node.time_left - graph[node.where_actually][v] - 1
                to_visit.append(Node(v, t, node.total_pressure + flows[v] * t, node.where_been | {v}))
    return ans


n = Node("AA", 30, 0, set())
ans = bfs(n, {})
print(sorted(ans.values(), reverse=True)[0])
print(f'total time elapsed : {time.time() - time_start} s')

time_start = time.time()
part2 = bfs(Node("AA", 26, 0, set()), {})
part2_ans = max(v1 + v2 for k1, v1 in part2.items()
                for k2, v2 in part2.items() if not k1 & k2)
print(f'total time elapsed : {time.time() - time_start} s')
print(part2_ans)
