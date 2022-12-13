def parse_depths(input_lines):
    return [int(line) for line in input_lines]

def rolling_window(lst, n):
    return [lst[i:i+n] for i in range(len(lst)-n+1)]

def count_increasing(lst):
    return len(list(filter(lambda x: x[0] < x[1], rolling_window(lst,2))))

def part1(input_lines):
    return count_increasing(parse_depths(input_lines))

def part2(input_lines):
    depths = parse_depths(input_lines)
    rolling_sums = [sum(window) for window in rolling_window(depths,3)]
    return count_increasing(rolling_sums)

example_answers = [ 7, 5 ]