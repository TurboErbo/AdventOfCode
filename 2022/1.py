def get_sums_per_elf(input_lines):
    boundaries = [-1] + [x for (x,line) in enumerate(input_lines) if not line] + [len(input_lines)]
    elves = [[int(x) for x in input_lines[boundaries[i]+1:boundaries[i+1]]] for i in range(len(boundaries)-1)]
    return [sum(x) for x in elves]

def part1(input_lines):
    return max(get_sums_per_elf(input_lines))

def part2(input_lines):
    return sum(sorted(get_sums_per_elf(input_lines), reverse=True)[:3])

example_answers = [24000, 45000]
