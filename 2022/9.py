movements = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

def move(init_pos, displacement):
    return (init_pos[0] + displacement[0], init_pos[1] + displacement[1])

def get_displacement(a, b):
    return (a[0] - b[0], a[1] - b[1])

def follow(head, tail):
    d = get_displacement(head, tail)
    if all(abs(x) <= 1 for x in d):
        return tail
    movement = tuple(map(lambda x: x // 2 if abs(x) == 2 else x, d))
    return move(tail, movement)

def parse_input(input_lines):
    return list(map(lambda x: (x[0], int(x[1])), [line.split() for line in input_lines]))

def print_positions(positions):
    for y in range(10, -10, -1):
        print(''.join('#' if (x,y) in positions else '.' for x in range(-12, 12)))

def model(moves, rope_len):
    tail_positions = set()

    rope = [(0,0) for _ in range(rope_len)]

    for direction, magnitude in moves:
        displacement = movements[direction]
        for _ in range(magnitude):
            rope[0] = move(rope[0], displacement)
            for i in range(1, len(rope)):
                rope[i] = follow(rope[i -1], rope[i])
            tail_positions.add(rope[-1])

    return len(tail_positions)

def part1(input_lines):
    moves = parse_input(input_lines)
    return model(moves, 2)

def part2(input_lines):
    moves = parse_input(input_lines)
    return model(moves, 10)

example_answers = [13, 1]

def preprocess(utils):
    assert part2(utils.get_data('9.example.2.txt')) == 36
