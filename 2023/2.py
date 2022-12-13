import functools
import operator

def parse_game(game):
    draws = []
    for draw in game.partition(":")[2].split(';'):
        drawn_cubes = {}
        for num_color in draw.split(','):
            num, color = num_color.strip().split(' ')
            drawn_cubes[color] = int(num)
        draws.append(drawn_cubes)
    return draws

def part1(input_lines: list[str]):
    amounts = {
        'red' : 12,
        'green' : 13,
        'blue': 14
    }
    def is_possible(game: str):
        draws = parse_game(game)
        return all([draw.get(color, 0) <= amounts[color] for color in amounts.keys() for draw in draws])
    return sum([x[0] for x in filter(lambda x: is_possible(x[1]), enumerate(input_lines, start=1))])        

def part2(input_lines):
    def power(game):
        min_amounts = {}
        draws = game.partition(":")[2]
        for draw in draws.split(';'):
            for num_color in draw.split(','):
                num, color = num_color.strip().split(' ')
                min_amounts[color] = max(int(num), min_amounts.get(color, 0))
        return functools.reduce(operator.mul, min_amounts.values(), 1)
    return sum(power(game) for game in input_lines)