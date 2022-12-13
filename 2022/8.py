def parse_input(input_lines):
    return [list(map(int, line)) for line in input_lines]

def num_visible(grid):

    nrows = len(grid)
    ncols = len(grid[0])

    num = 2 * (nrows + ncols) - 4

    maxes = [[dict() for c in range(ncols)] for r in range(nrows)]

    for r in range(nrows):
        maxes[r][0]["LEFT"] = grid[r][0]
        for c in range(1, ncols):
            maxes[r][c]["LEFT"] = max(maxes[r][c-1]["LEFT"], grid[r][c])
        maxes[r][-1]["RIGHT"] = grid[r][-1]
        for c in range(ncols-2, -1, -1):
            maxes[r][c]["RIGHT"] = max(maxes[r][c+1]["RIGHT"], grid[r][c])

    for c in range(ncols):
        maxes[0][c]["UP"] = grid[0][c]
        for r in range(1, nrows):
            maxes[r][c]["UP"] = max(maxes[r-1][c]["UP"], grid[r][c])
        maxes[-1][c]["DOWN"] = grid[-1][c]
        for r in range(nrows-2, -1, -1):
            maxes[r][c]["DOWN"] = max(maxes[r+1][c]["DOWN"], grid[r][c])

    for r in range(1, nrows - 1):
        for c in range(1, ncols - 1):
            h = grid[r][c]
            if h > maxes[r][c-1]["LEFT"] or \
               h > maxes[r][c+1]["RIGHT"] or \
               h > maxes[r-1][c]["UP"] or \
               h > maxes[r+1][c]["DOWN"]:
               num += 1

    return num

def part1(input_lines):
    grid = parse_input(input_lines)
    return num_visible(grid)


def max_score(grid):
    best = 0
    nrows = len(grid)
    ncols = len(grid[0])
    for r in range(1, nrows - 1):
        for c in range(1, ncols - 1):
            up = 0
            for _r in range(r-1, -1, -1):
                up += 1
                if grid[_r][c] >= grid[r][c]:
                    break
            down = 0
            for _r in range(r+1, nrows):
                down += 1
                if grid[_r][c] >= grid[r][c]:
                    break
            left = 0
            for _c in range(c-1, -1, -1):
                left += 1
                if grid[r][_c] >= grid[r][c]:
                    break
            right = 0
            for _c in range(c+1, ncols):
                right += 1
                if grid[r][_c] >= grid[r][c]:
                    break
            score = up * down * left * right
            best = max(best, score)

    return best

def part2(input_lines):
    grid = parse_input(input_lines)
    return max_score(grid)

example_answers = [21, 8]