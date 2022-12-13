from pathlib import Path
import importlib
import sys
import time
import datetime

class Utils:
    def get_data(filename, year=datetime.date.today().year):
        return Utils.read_file_lines(Path('.') / str(year) / "data" / filename)
        
    def read_file_lines(file):
        with open(file) as f:
            return f.read().splitlines()

    def timed(func, *args, **kwargs):
        t = time.time()
        r = func(*args, **kwargs)
        t = time.time() - t
        return r, t

def process(year, day):
    module = importlib.import_module(year + '.' + day)

    input_lines = Utils.get_data(day + '.txt', year)
    example_input_lines = Utils.get_data(day + '.example.txt', year)

    part2_example_file = Path('.') / str(year) / "data" / f'{day}.example2.txt'
    part2_example_input_lines = Utils.read_file_lines(part2_example_file) if Path.exists(part2_example_file) else example_input_lines

    only_test = 'only_test' in dir(module)

    solution_file = Path('.') / str(year) / "data" / f'{day}.solution.txt'
    solutions = Utils.read_file_lines(solution_file) if Path.exists(solution_file) else module.example_answers

    if 'preprocess' in dir(module):
        module.preprocess(Utils)

    if 'skip_part1' not in dir(module):
        answer = str(module.part1(example_input_lines))
        assert answer == solutions[0], f"Part 1 failed! expected: {solutions[0]}, got: {answer}"
        if not only_test:
            print(module.part1(input_lines))

    if len(solutions) > 1:
        answer = str(module.part2(part2_example_input_lines))
        assert answer == solutions[1], f"Part 2 failed! expected: {solutions[1]}, got: {answer}"
        if not only_test:
            print(module.part2(input_lines))


if __name__ == "__main__":
    # Hack: you can pass either the full path of implementation file (easier to do in .vscode/launch.json), 
    #       or YEAR/DAY (if running manually)
    p = Path(sys.argv[1])
    process(p.parts[-2], p.parts[-1].partition('.')[0])

