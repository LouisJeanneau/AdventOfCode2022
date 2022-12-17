import math
import queue

def day11(round):
    number_monkey = 0
    monkeys = []
    with open('input.txt') as f:
        input = f.read().splitlines()
        while input.count(""):
            input.remove("")
        # Number of monkeys
        number_monkey = len(input) // 6
        monkeys = [[] for _ in range(number_monkey)]
        for i in range(len(input) // 6):
            items = input[i * 6 + 1].split(": ")[1]
            items = items.split(", ")
            operations = input[i * 6 + 2].split("= ")[1]
            divisible = input[i * 6 + 3].split()[-1]
            false_true = (int(input[i * 6 + 5][-1:]), int(input[i * 6 + 4][-1:]))
            # 0 is items held
            q = queue.Queue()
            [q.put(int(value)) for value in items]
            monkeys[i].append(q)
            # 1 is operations
            monkeys[i].append(operations)
            # 2 is the division test
            monkeys[i].append(int(divisible))
            # 3 where to go if false and true
            monkeys[i].append(false_true)
            # 4 is number of items inspected
            monkeys[i].append(0)

    # Least common multiple, for part 2, to avoid getting huge numbers
    lcm = math.lcm(*[monkeys[i][2] for i in range(number_monkey)])
    # print(lcm)
    for t in range(round):
        for i in range(number_monkey):
            while len(monkeys[i][0].queue):
                old = monkeys[i][0].get_nowait()
                new = eval(monkeys[i][1])

                # Part 1
                # new //= 3

                # Part 2
                new %= lcm

                # a = 0 if not divisible
                a = int(new % monkeys[i][2] == 0)
                monkeys[monkeys[i][3][a]][0].put_nowait(new)
                monkeys[i][4] += 1

    l = [monkeys[i][4] for i in range(number_monkey)]
    l.sort()
    return l[-1] * l[-2]

print(day11(10000))