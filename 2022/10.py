def parse_input(input_lines):
    program = []
    for line in input_lines:
        instruction = line.split()
        if len(instruction) == 2:
            instruction[1] = int(instruction[1])
        program.append(instruction)
    return program

def simulate(program, callback):
    regValue = 1
    cycle = 0
    for instruction in program:
        cmd = instruction[0]
        if cmd == "noop":
            cycle += 1
            callback(cycle, regValue)
        else: #addx
            callback(cycle + 1, regValue)
            cycle += 2
            callback(cycle, regValue)
            regValue += instruction[1]

def part1(input_lines):
    program = parse_input(input_lines)
    values = []
    def callback(cycle, regValue):
        if cycle % 40 == 20:
            values.append(cycle * regValue)
    simulate(program, callback)
    return sum(values)

def part2(input_lines):
    program = parse_input(input_lines)
    image = ''    
    def callback(cycle, regValue):
        nonlocal image
        horizontalPos = (cycle-1) % 40
        if horizontalPos >= regValue - 1 and horizontalPos <= regValue + 1:
            pixel = '#'
        else:
            pixel = '.'
        image += pixel
        if horizontalPos == 39:
            image += '\n'
    simulate(program, callback)
    return image

example_image=\
'##..##..##..##..##..##..##..##..##..##..\n' +\
'###...###...###...###...###...###...###.\n' +\
'####....####....####....####....####....\n' +\
'#####.....#####.....#####.....#####.....\n' +\
'######......######......######......####\n' +\
'#######.......#######.......#######.....\n'

example_answers = [13140, example_image]