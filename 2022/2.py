from enum import Enum

class Shape(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3

class Result(Enum):
    LOSS=0
    DRAW=3
    WIN=6

def parse_input_part1(input_lines: list[str]) -> list[tuple[Shape, Shape]]:
    return [(Shape(ord(x[0]) - ord('A') + 1), Shape(ord(x[1]) - ord('X') + 1)) for x in (line.split() for line in input_lines)]

def single_round(opponent: Shape, mine: Shape) -> Result:
    if opponent == mine:
        return Result.DRAW
    if opponent.value == mine.value % 3 + 1:
        return Result.LOSS
    return Result.WIN

def play(moves):
    return [single_round(opponent, mine) for (opponent, mine) in moves]

def get_score(moves, results):
    return sum(x.value for x in results) + sum(x[1].value for x in moves)

def calc_move(opponent: Shape, result: Result) -> Shape:
    # MAGIC
    return Shape((opponent.value + result.value // 3 - 2) % 3 + 1)

def parse_input_part2(input_lines: list[str]) -> list[tuple[Shape, Result]]:
    return [(Shape(ord(x[0]) - ord('A') + 1), Result((ord(x[1]) - ord('X')) * 3)) for x in (line.split() for line in input_lines)]

def part1(input_lines):
    moves = parse_input_part1(input_lines)
    results = play(moves)
    return get_score(moves, results)

def part2(input_lines):
    rounds = parse_input_part2(input_lines)
    moves = [(round[0], calc_move(round[0], round[1])) for round in rounds]
    results = [round[1] for round in rounds]
    return get_score(moves, results)

example_answers = [15, 12]