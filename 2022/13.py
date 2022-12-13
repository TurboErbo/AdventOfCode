from functools import cmp_to_key

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right

    left, right = tuple(x if isinstance(x, list) else [x] for x in [left, right])
    for i in range(min(len(left), len(right))):
        diff = compare(left[i], right[i])
        if diff != 0:
            return diff
    return len(left) - len(right)

def part1(input_lines):
    pairs = [(eval(input_lines[i]), eval(input_lines[i+1])) for i in range(0,len(input_lines),3)]
    return sum(i for i, (left, right) in enumerate(pairs, 1) if compare(left, right) <= 0)

def part2(input_lines):
    extras = [[[2]],[[6]]]
    vals = sorted([eval(line) for line in input_lines if line] + extras,
                  key=cmp_to_key(compare))
    return (vals.index(extras[0]) + 1) * (vals.index(extras[1]) + 1)

example_answers = [ 13, 140 ]