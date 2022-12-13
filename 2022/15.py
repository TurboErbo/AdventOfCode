import re

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def parse_input(input_lines):
    sensors = []
    beacons = set()
    for line in input_lines:
        m = re.match('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
        s_x, s_y, b_x, b_y = [int(x) for x in m.groups(tuple(range(1,5)))]
        sensors.append((s_x, s_y, distance((s_x, s_y), (b_x, b_y))))
        beacons.add((b_x, b_y))
    return sensors, beacons

def get_projection(s_x, s_y, distance, y):
    half = distance - abs(y - s_y)
    if half < 0:
        return None
    return s_x - half, s_x + half

def get_line2(sensors, beacons, y, minmax=None):
    beacon_x = sorted([b[0] for b in beacons if b[1] == y])
    projections = sorted(list(filter(lambda x: x, [get_projection(s_x, s_y, distance, y) for s_x, s_y, distance in sensors])))

    merged_segments = [list(projections[0])]
    for i in range(1, len(projections)):
        _, p_end = merged_segments[-1]
        start, end = projections[i]
        if start > p_end:
            merged_segments.append([start, end])
        else:
            merged_segments[-1][1] = max(merged_segments[-1][1], end)

    if not minmax:
        split_segments = []
        for start, end in merged_segments:
            for b in beacon_x:
                if b >= start and b <= end:
                    if b != start:
                        split_segments.append((start, b - 1))
                    start = b + 1
                elif b > end:
                    break
            if start <= end:
                split_segments.append((start, end))
        num_impossible = sum([e - s + 1 for s, e in split_segments])
        return num_impossible

    min_x, max_x = minmax
    for s, e in merged_segments:
        if e < min_x:
            continue
        if s > max_x:
            break
        if s > min_x:
            return min_x
        min_x = e + 1

def find_beacon(sensors, beacons, extent):
    for y in range(extent + 1):
        if y % 10000 == 0:
            print('.', end='')
        possible_x = get_line2(sensors, beacons, y, (0, extent))
        if possible_x:
            return (possible_x, y)

def is_example(input_lines):
    return len(input_lines) == 14

def part1(input_lines):
    sensors, beacons = parse_input(input_lines)
    y = 10 if is_example(input_lines) else 2000000
    return get_line2(sensors, beacons, y)

def part2(input_lines):
    extent = 20 if is_example(input_lines) else 4000000
    sensors, beacons = parse_input(input_lines)
    x, y = find_beacon(sensors, beacons, extent)
    return x * 4000000 + y


example_answers = [ 26, 56000011 ]