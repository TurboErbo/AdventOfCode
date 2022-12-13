# Template that can be run independently

import run_aoc

def parse_input(input_lines):
    pass

def part1(input_lines):
    parse_input(input_lines)

def part2(input_lines):
    parse_input(input_lines)

if __name__ == "__main__":
    input_lines = util.get_data(__file__, '.txt')
    example_input_lines = util.get_data(__file__, '.example.txt')

    assert part1(example_input_lines) == 2
    print(part1(input_lines))

    assert part2(example_input_lines) == 4
    print(part2(input_lines))