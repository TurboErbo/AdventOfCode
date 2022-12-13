def part1(input_lines):
    def transform(line):
        filtered = list(filter(lambda x: x.isdigit(), line))
        return int(filtered[0] + filtered[-1])
    return sum(transform(line) for line in input_lines)

def part2(input_lines):
    targets = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] + list(map(str, range(1,10)))
    def transform(line: str):
        first = min(filter(lambda x: x[0] != -1, [(line.find(target), index) for index, target in enumerate(targets)]))[1] % 9 + 1
        last = max(filter(lambda x: x[0] != -1, [(line.rfind(target), index) for index, target in enumerate(targets)]))[1] % 9 + 1
        return first * 10 + last
    return sum(transform(line) for line in input_lines)


example_answers = [ 142, 281 ]