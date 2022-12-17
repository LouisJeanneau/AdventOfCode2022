from numpy import sign

# Part 1
'''
# Init positions
x_h, y_h, x_t, y_t = 0, 0, 0, 0
# Array of visited places for the tail, in order
visited_tail = [(0,0)]

with open('input.txt') as f:
    for line in f:
        direction, repeat = line.split()
        for i in range(int(repeat)):
            # Head movement
            x_h += ((direction == "R") - (direction == "L"))
            y_h += ((direction == "U") - (direction == "D"))
            # Euclidean distance between head and tail
            if (x_h - x_t)**2 + (y_h - y_t)**2 > 2:
                x_t += sign(x_h - x_t)
                y_t += sign(y_h - y_t)
            visited_tail.append((x_t, y_t))
'''

# Part 2
x, y = [0] * 10, [0] * 10
# Array of visited places for the tail, in order
visited_tail = [(0, 0)]

with open('input.txt') as f:
    for line in f:
        direction, repeat = line.split()
        for _ in range(int(repeat)):
            # Head movement
            x[0] += ((direction == "R") - (direction == "L"))
            y[0] += ((direction == "U") - (direction == "D"))
            # For each knots in order
            for i in range(1, 10):
                # Euclidean distance between leading knot and following one
                if (x[i-1] - x[i]) ** 2 + (y[i-1] - y[i]) ** 2 > 2:
                    x[i] += sign(x[i-1] - x[i])
                    y[i] += sign(y[i-1] - y[i])
            visited_tail.append((x[9], y[9]))

# Convert to set to get unique location / get rid of duplicate
print(len(set(visited_tail)))
