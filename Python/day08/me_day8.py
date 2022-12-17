import math

height_map = []
visible_number = 0

with open('input.txt') as f:
    for line in f:
        height_map.append(list(map(int, list(line)[:-1])))

visible_number = 4 * len(height_map) - 4
best_score = 0

for i in range(1, len(height_map) - 1):
    for j in range(1, len(height_map[i]) - 1):
        visible = 1111
        score = [0, 0, 0, 0]
        height = height_map[i][j]
        # For each interior tree
        # Loop up
        for up in reversed(range(i)):
            score[0] += 1
            if height_map[up][j] >= height:
                visible -= 1000
                break
        for right in range(j + 1, len(height_map[i])):
            score[1] += 1
            if height_map[i][right] >= height:
                visible -= 100
                break
        for down in range(i + 1, len(height_map[j])):
            score[2] += 1
            if height_map[down][j] >= height:
                visible -= 10
                break
        for left in reversed(range(j)):
            score[3] += 1
            if height_map[i][left] >= height:
                visible -= 1
                break
        if visible != 0:
            visible_number += 1
        if math.prod(score) >= best_score:
            best_score = math.prod(score)
# Part 1
print(visible_number)
# Part 2
print(best_score)
