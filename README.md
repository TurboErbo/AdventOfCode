See https://adventofcode.com.

Solutions are organized by year, with example data and input data (which is unique to each user) in the `data` directory of each year.

Running `./genfiles.sh [DAY] [YEAR]` initializes boilerplate code for the given day, defaulting to today.
It needs to read a `COOKIE` variable from `credentials.sh` (not commited to git). This can be obtained from the HTTP request headers in the browser tools.

Example: COOKIE='session=abcdefg'

Fill in `DAY`.example.txt manually by copying and pasting from the problem description, and update the variable `example_answers` in `DAY`.py. Then the fun part: implement part1() and part2() in `DAY`.py!

To run the code, execute `python aoc.py YEAR/DAY`.

To debug with VS Code, simply press F5 with the current day's file open.

Happy Advent of Coding!