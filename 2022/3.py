from pathlib import Path

def get_item_priority(item: str):
    if item.isupper():
        return ord(item) - ord('A') + 27
    if item.islower():
        return ord(item) - ord('a') + 1
    assert False

def get_score(line: str):
    assert len(line) % 2 == 0
    left = set(line[:len(line)//2])
    right = set(line[len(line)//2:])
    common = left.intersection(right)
    assert len(common) == 1
    return get_item_priority(common.pop())

def part1(input_lines):
    return sum(get_score(line) for line in input_lines)

def get_badge(group):
    common = set(group[0]).intersection(*[set(group[x]) for x in [1,2]])
    assert len(common) == 1
    return common.pop()

def part2(input_lines):
    assert len(input_lines) % 3 == 0
    return sum(get_item_priority(get_badge(input_lines[i:i+3])) for i in range(0, len(input_lines), 3))

example_answers = [157, 70]