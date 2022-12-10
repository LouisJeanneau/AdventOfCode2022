sum = 0
X = 1
cycle = 1

'''
# Part 1
with open('input.txt') as f:
    for line in f:
        if (cycle + 20) % 40 == 0:
            sum += cycle * X
        if line.count("noop"):
            cycle += 1
        if line.count("addx"):
            cycle += 1
            if (cycle + 20) % 40 == 0:
                sum += cycle * X
            X += int(line.split()[1])
            cycle += 1
print(sum)
'''

# Part 2
screen = []
cycle = 0

with open('input.txt') as f:
    for line in f:
        duration = line.count("noop") + 2 * line.count("addx")
        for i in range(duration):
            if cycle % 40 == 0:
                screen.append(["."] * 40)
            if ((cycle % 40) - 1) <= X <= ((cycle % 40) + 1):
                screen[cycle // 40][cycle % 40] = "#"
            if i == 1:
                X += int(line.split()[1])
            cycle += 1

for l in screen:
    print("".join(l))
