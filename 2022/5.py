from collections import defaultdict
from typing import List, Dict
import re

def parse_input(input_lines):
    stacks = defaultdict(list)
    moves = []
    stacks_complete = False
    for line in input_lines:
        if not line:
            continue        
        if len(line) > 1 and line[1] == '1':
            stacks_complete = True
            continue
        if not stacks_complete:
            for i in range(1, len(line), 4):
                if line[i] != ' ':
                    stacks[i//4 + 1].insert(0, line[i])
        else:
            moves.append(tuple(map(int, re.match(r'move (\d+) from (\d+) to (\d+)', line).group(1, 2, 3))))
    return stacks, moves

def apply_moves(stacks: Dict[int, List[int]], moves, reverse):
    for num, src, dst in moves:
        to_move = stacks[src][len(stacks[src])-num:]
        stacks[dst].extend(reversed(to_move) if reverse else to_move)
        stacks[src] = stacks[src][:len(stacks[src])-num]

def format_output(stacks):
    return ''.join(stacks[i][-1] for i in range(1, len(stacks) + 1))

def process(input_lines, reverse):
    stacks, moves = parse_input(input_lines)
    apply_moves(stacks, moves, reverse)
    return format_output(stacks)

def part1(input_lines):
    return process(input_lines, True)

def part2(input_lines):
    return process(input_lines, False)

example_answers = ['CMZ', 'MCD']