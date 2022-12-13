import math

def get_surfaces(point):
    x, y, z = point
    return [
        ((x,y,z), (x,y+1,z+1)),
        ((x,y,z), (x+1,y+1,z)),
        ((x,y,z), (x+1,y,z+1)),
        ((x+1,y,z), (x+1,y+1,z+1)),
        ((x,y+1,z), (x+1,y+1,z+1)),
        ((x,y,z+1), (x+1,y+1,z+1))
    ]

def num_surfaces(points):
    surfaces = set()
    for p in points:
        surfaces.symmetric_difference_update(get_surfaces(p))
    return len(surfaces)

def part1(input_lines):
    points = [list(map(int, line.split(','))) for line in input_lines]
    return num_surfaces(points)

def part2(input_lines):
    points = set(tuple(map(int, line.split(','))) for line in input_lines)
    mins = [min(p[i] for p in points) for i in range(3)]
    maxs = [max(p[i] for p in points) for i in range(3)]

    s = [(mins[0], y, z) for y in range(mins[1], maxs[1] + 1) for z in range(mins[2], maxs[2] + 1)] + \
        [(maxs[0], y, z) for y in range(mins[1], maxs[1] + 1) for z in range(mins[2], maxs[2] + 1)] + \
        [(x, mins[1], z) for x in range(mins[0], maxs[0] + 1) for z in range(mins[2], maxs[2] + 1)] + \
        [(x, maxs[1], z) for x in range(mins[0], maxs[0] + 1) for z in range(mins[2], maxs[2] + 1)] + \
        [(x, y, mins[2]) for x in range(mins[0], maxs[0] + 1) for y in range(mins[1], maxs[1] + 1)] + \
        [(x, y, maxs[2]) for x in range(mins[0], maxs[0] + 1) for y in range(mins[1], maxs[1] + 1)]

    reachable = set(s).difference(points)
    q = list(reachable)
    dirs = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
    while q:
        curr = q.pop()
        for d in dirs:
            neighbor = tuple(curr[x]+d[x] for x in range(3))
            out_of_range = False
            for i in range(3):
                if neighbor[i] < mins[i] or neighbor[i] > maxs[i]:
                    out_of_range = True
                    break
            if out_of_range:
                continue
            if neighbor in points or neighbor in reachable:
                continue
            q.append(neighbor)
            reachable.add(neighbor)
    #total = math.prod([maxs[i] - mins[i] + 1 for i in range(3)])
    #unreachable = total - len(explored) - len(points)
    all_points = set((x,y,z) for x in range(mins[0], maxs[0] + 1) for y in range(mins[1], maxs[1] + 1) for z in range(mins[2], maxs[2] + 1))
    unreachable = all_points - points - reachable
    return num_surfaces(points) - num_surfaces(unreachable)

def preprocess(utils):
    tiny_input = ['1,1,1','2,1,1']
    ans = part1(tiny_input)
    assert ans == 10


example_answers = [ 64, 58 ]
skip_part1 = True