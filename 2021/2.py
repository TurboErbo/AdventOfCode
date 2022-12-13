class Command:
    def __init__(self, direction, magnitude):
        self.direction = direction
        self.magnitude = magnitude

    @classmethod
    def parse(cls, input):
        x,y = input.split()
        return cls(x, int(y))

def solution(input_lines, sub):
    for line in input_lines:
        sub.execute(Command.parse(line))
    return sub.depth * sub.horizontal

class SubmarineBase:
    def __init__(self):
        self.depth = 0
        self.horizontal = 0

    def execute(self, cmd):
        self.__getattribute__(cmd.direction)(cmd.magnitude)
    
    def forward(self, magnitude):
        self.horizontal += magnitude

class Submarine(SubmarineBase):
    def up(self, magnitude):
        self.depth -= magnitude
    
    def down(self, magnitude):
        self.depth += magnitude

class Submarine2(SubmarineBase):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def up(self, magnitude):
        self.aim -= magnitude
    
    def down(self, magnitude):
        self.aim += magnitude

    def forward(self, magnitude):
        super().forward(magnitude)
        self.depth += self.aim * magnitude

def part1(input_lines):
    return solution(input_lines, Submarine())

def part2(input_lines):
    return solution(input_lines, Submarine2())

example_answers = [ 150, 900 ]