import cProfile
import re

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
        sensors.sort(key=lambda x:x[0])
        min_x = sensors[0][0] - sensors[0][2]
        max_x = sensors[-1][0] + sensors[-1][2]
        max_dist = max(s[2] for s in sensors)

        beacons.sort(key=lambda x: x[0])

        y = 2000000
        sum = 0
        iter = max_x + 1 - min_x
        for x in range(min_x , max_x + 1):
            if x%100000==0:
                percent = (x - min_x) / iter * 100
                print(f'{percent:.2f}%')
            if (x,y) in beacons:
                continue
            for s in sensors:
                sx, sy, d = s[0], s[1], s[2]
                if manhattan(x, y, sx, sy) <= d:
                    sum += 1
                    break

        print(sum)

cProfile.run("part1()")