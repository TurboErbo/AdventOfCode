def range_contains(first, second):
    return first[0] <= second[0] and first[1] >= second[1]

def full_overlap(first, second):
    return range_contains(first, second) or range_contains(second, first)

def any_overlap(first, second):
    return not (first[0] > second[1] or second[0] > first[1])

def parse_line(line):
    left, right = line.split(',')
    left = list(map(int, left.split('-')))
    right = list(map(int, right.split('-')))
    return left, right

def part1(input_lines):
    """In how many assignment pairs does one range fully contain the other"""
    return len(list(filter(lambda x: full_overlap(*parse_line(x)), input_lines)))

def part2(input_lines):
    """In how many assignment pairs do the ranges overlap?"""
    return len(list(filter(lambda x: any_overlap(*parse_line(x)), input_lines)))

example_answers = [2, 4]