from enum import Enum
import copy
import math

class Direction(Enum):
    LEFT = (0,-1)
    RIGHT = (0,1)
    DOWN = (-1,0)
    UP = (1,0)

class Rock:
    TYPES = [
        [(0,2),(0,3),(0,4),(0,5)],
        [(0,3),(1,2),(1,3),(1,4),(2,3)],
        [(0,2),(0,3),(0,4),(1,4),(2,4)],
        [(0,2),(1,2),(2,2),(3,2)],
        [(0,2),(0,3),(1,2),(1,3)]
    ]
    def __init__(self, type: int, height: int):
        self.components = Rock.TYPES[type]
        self.move(Direction.UP, height)

    def move(self, direction: Direction, magnitude=1):
        self.components = [(c[0] + direction.value[0] * magnitude, c[1] + direction.value[1] * magnitude) for c in self.components]

    def get_coordinates(self):
        return self.components

class WindPattern:
    def __init__(self, pattern):
        self.pattern = [Direction.LEFT if ch == '<' else Direction.RIGHT for ch in pattern]
        self.index = 0

    def get_direction(self):
        d = self.pattern[self.index]
        self.index = (self.index + 1) % len(self.pattern)
        return d

class Chamber:
    WIDTH = 7
    FALL_HEIGHT = 3
    def __init__(self, wind: WindPattern, max_height):
        self.wind = wind
        self.max_height = max_height
        self.matrix = [[False for _ in range(Chamber.WIDTH)] for _ in range(max_height)]
        self.height = 0
        self.current_rock_type = 0
        self.matrix_offset = 0

    def process_rock(self):
        r = Rock(self.current_rock_type, self.height + self.FALL_HEIGHT)
        self.current_rock_type = (self.current_rock_type + 1) % len(Rock.TYPES)
        while True:
            r, _ = self._try_move(r, self.wind.get_direction())
            r, moved = self._try_move(r, Direction.DOWN)
            if not moved:
                break
        self._add_rock(r)

    def _try_move(self, rock: Rock, direction: Direction):
        tentative = copy.copy(rock)
        tentative.move(direction)
        if self._legal_check(tentative):
            return tentative, True
        return rock, False

    def _legal_check(self, rock: Rock):
        for r, c in rock.get_coordinates():
            if c >= self.WIDTH or c < 0:
                return False
            if r < self.matrix_offset:
                return False
            if self.matrix[r - self.matrix_offset][c]:
                return False
        return True

    def _add_rock(self, rock: Rock):
        for r, c in rock.get_coordinates():
            self.matrix[r - self.matrix_offset][c] = True
            self.height = max(self.height, r + 1)

    def get_profile(self):
        p = []
        for c in range(Chamber.WIDTH):
            for h in range(self.height - 1, self.matrix_offset - 2, -1):
                if h == self.matrix_offset - 1 or self.matrix[h - self.matrix_offset][c]:
                    p.append(h)
                    break
        m = min(p)
        return tuple(h - m for h in p)

    def readjust(self, profile, height):
        m = max(profile)
        for r in range(m):
            for c in range(Chamber.WIDTH):
                self.matrix[r][c] = r < profile[c]
        for r in range(m, self.max_height):
            self.matrix[r] = [False for _ in range(Chamber.WIDTH)]
        self.matrix_offset = height - m
        self.height = height

def part1(input_lines):
    max_height = 5261 # ceil(2022 / 5 * 13) + 3
    c = Chamber(WindPattern(input_lines[0]), max_height)
    for _ in range(2022):
        c.process_rock()
    return c.height

def part2(input_lines):
    minor_period = math.lcm(len(Rock.TYPES), len(input_lines[0]))
    profiles = { (0 for _ in range(Chamber.WIDTH)) : (0, 0)}
    max_height = minor_period * 20 
    c = Chamber(WindPattern(input_lines[0]), max_height)
    rounds = 1000000000000
    for i in range(1, rounds):
        c.process_rock()
        if i % minor_period == 0:
            p = c.get_profile()
            print(p, c.height, i)
            if p in profiles:
                round, height = profiles[p]
                offset = round
                major_period = i - round
                height_offset = height
                height_per_period = c.height - height
                break
            profiles[p] = (i, c.height)
    num_major_periods = (rounds - offset) // major_period
    expected_height = height_offset + height_per_period * num_major_periods
    c.readjust(p, expected_height)
    remaining = (rounds - offset) % major_period
    for _ in range(remaining):
        c.process_rock()
    return c.height

example_answers = [ 3068, 1514285714288 ]
skip_part1 = True
#only_test = True