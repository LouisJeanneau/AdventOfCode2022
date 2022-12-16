import cProfile
import re
import matplotlib.pyplot as plt
import matplotlib as mpl
import z3
from matplotlib.patches import Polygon

mpl.use('Qt5Agg')


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def part1():
    with open("input.txt") as f:
        input = f.read().splitlines()
        sensors = []
        beacons = []
        for line in input:
            # Extract the integer values from the sentence using the regular expression
            values_string = re.findall(r'[+-]?\d+', line)
            sensor_x, sensor_y = int(values_string[0]), int(values_string[1])
            beacon_x, beacon_y = int(values_string[2]), int(values_string[3])
            dist = manhattan(sensor_x, sensor_y, beacon_x, beacon_y)
            sensors.append((sensor_x, sensor_y, dist))
            beacons.append((beacon_x, beacon_y))

        # print(sensors)
        sensors.sort(key=lambda x: x[0])
        min_x = sensors[0][0] - sensors[0][2]
        max_x = sensors[-1][0] + sensors[-1][2]
        max_dist = max(s[2] for s in sensors)

        beacons.sort(key=lambda x: x[0])

        y = 2000000
        sum = 0
        iter = max_x + 1 - min_x
        for x in range(min_x, max_x + 1):
            if x % 100000 == 0:
                percent = (x - min_x) / iter * 100
                print(f'{percent:.2f}%')
            if (x, y) in beacons:
                continue
            for s in sensors:
                sx, sy, d = s[0], s[1], s[2]
                if manhattan(x, y, sx, sy) <= d:
                    sum += 1
                    break

        print(sum)


def part2():
    with open("input.txt") as f:
        input = f.read().splitlines()
        sensors = []
        beacons = []
        for line in input:
            # Extract the integer values from the sentence using the regular expression
            values_string = re.findall(r'[+-]?\d+', line)
            sensor_x, sensor_y = int(values_string[0]), int(values_string[1])
            beacon_x, beacon_y = int(values_string[2]), int(values_string[3])
            dist = manhattan(sensor_x, sensor_y, beacon_x, beacon_y)
            sensors.append((sensor_x, sensor_y, dist))
            beacons.append((beacon_x, beacon_y))

        sensors.sort(key=lambda x: x[0])
        min_x = sensors[0][0] - sensors[0][2]
        max_x = sensors[-1][0] + sensors[-1][2]
        max_dist = max(s[2] for s in sensors)
        plt.interactive(True)
        for sx, sy, d in sensors:
            d += 1
            x = (sx, sx + d, sx, sx - d, sx)
            y = (sy + d, sy, sy - d, sy, sy + d)
            plt.plot(x,y)
        plt.axis([0, 4000000, 0, 4000000])
        # plt.axis('scaled')

        plt.show()

        # z3 solver seen on reddit
        s = z3.Solver()
        x, y = z3.Int("x"), z3.Int("y")
        s.add(0 <= x)
        s.add(x <= 4000000)
        s.add(0 <= y)
        s.add(y <= 4000000)

        def z3_abs(x):
            return z3.If(x >= 0, x, -x)

        for sx, sy, d in sensors:
            s.add(z3_abs(sx - x) + z3_abs(sy - y) > d)

        assert s.check() == z3.sat
        model = s.model()
        print(f'x : {model[x].as_long()}  y : {model[y].as_long()}')
        print("Part 2:", model[x].as_long() * 4000000 + model[y].as_long())

        plt.pause(1000)
        return


# cProfile.run("part2()")
part2()
