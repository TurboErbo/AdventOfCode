from pathlib import Path
import importlib
import sys
import time
import datetime

class Utils:
    def get_data(filename, year=datetime.date.today().year):
        with open(Path('.') / str(year) / "data" / filename) as f:
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

    if 'preprocess' in dir(module):
        module.preprocess(Utils)

    answer = module.part1(example_input_lines)
    assert answer == module.example_answers[0], f"Part 1 failed! expected: {module.example_answers[0]}, got: {answer}"
    print(module.part1(input_lines))

    if module.example_answers[1] != "PART2_ANSWER":
        answer = module.part2(example_input_lines)
        assert answer == module.example_answers[1], f"Part 2 failed! expected: {module.example_answers[1]}, got: {answer}"
        print(module.part2(input_lines))


if __name__ == "__main__":
    # Hack: you can pass either the full path of implementation file (easier to do in .vscode/launch.json), 
    #       or YEAR/DAY (if running manually)
    p = Path(sys.argv[1])
    process(p.parts[-2], p.parts[-1].partition('.')[0])

