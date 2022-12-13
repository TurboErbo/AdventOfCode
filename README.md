See https://adventofcode.com/2022.

Solutions are organized by year, with example data and input data (which is unique to each user) in the `data` directory of each year.

Running `./util.sh [DAY] [YEAR]` initializes boilerplate code for the given day, defaulting to today.
It needs to read a COOKIE variable from credentials.sh (not commited to git). This can be obtained from the HTTP request headers in the browser tools.

Fill in `DAY`.example.txt manually by copy and pasting from the problem description, and update the variable `example_answers` in `DAY`.py. Then the fun part: implement part1() and part() in `DAY`.py!

To run the code, execute `python aoc.py YEAR/DAY`. It checks if example answers are correct, and if so prints out the answers.

If using vscode, there is a AdventOfCode debug configuration provided, and you can simply press F5 with the current day's file open to debug it.

Have fun!
