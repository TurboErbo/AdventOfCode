import collections
import re

Number = collections.namedtuple('Number', ['start_col', 'end_col', 'value'])
Symbol = collections.namedtuple('Symbol', ['row', 'col', 'value'])

def parse_input(input_lines: list[str]):
    numbers = [[] for _ in range(len(input_lines))]
    symbols = []
    for row, line in enumerate(input_lines):
        for m in re.finditer(r'\d+', line):
            numbers[row].append(Number(m.start(), m.end() - 1, int(m.group())))
        for m in re.finditer(r'[^\d.]', line):
            symbols.append(Symbol(row, m.start(), m.group()))
    return numbers, symbols

def has_overlap(span1, span2):
    return not ((span1[1] < span2[0]) or (span1[0] > span2[1]))

def extract_part_numbers(numbers: list[list[Number]], symbols: list[Symbol]):
    part_numbers = set()
    for symbol in symbols:
        for row in range(max(0, symbol.row - 1), min(len(numbers), symbol.row + 1) + 1):
            for n in numbers[row]:
                if has_overlap((n.start_col, n.end_col), (symbol.col - 1, symbol.col + 1)):
                    part_numbers.add(n)
    return [n.value for n in part_numbers]

def extract_gear_ratios(numbers: list[list[Number]], symbols: list[Symbol]):
    gear_ratios = []
    for symbol in symbols:
        if symbol.value == '*':
            adjacent_numbers = []
            for row in range(max(0, symbol.row - 1), min(len(numbers), symbol.row + 1) + 1):
                for n in numbers[row]:
                    if has_overlap((n.start_col, n.end_col), (symbol.col - 1, symbol.col + 1)):
                        adjacent_numbers.append(n.value)
            if len(adjacent_numbers) > 1:
                assert(len(adjacent_numbers) == 2)
                gear_ratios.append(adjacent_numbers[0] * adjacent_numbers[1])
    return gear_ratios

def part1(input_lines: list[str]):
    numbers, symbols = parse_input(input_lines)
    return sum(extract_part_numbers(numbers, symbols))

def part2(input_lines: list[str]):
    numbers, symbols = parse_input(input_lines)
    return sum(extract_gear_ratios(numbers, symbols))
