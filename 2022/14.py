def parse_input(input_lines: list[str]):
    all_points = set()
    for line in input_lines:
        points = line.split('->')
        for start, end in zip(points[:-1], points[1:]):
            s_x, s_y = tuple(map(int, start.split(',')))
            e_x, e_y = tuple(map(int, end.split(',')))
            if s_x == e_x:
                s_y, e_y = sorted([s_y, e_y])
                for y in range(s_y, e_y + 1):
                    all_points.add((s_x, y))
            else:
                s_x, e_x = sorted([s_x, e_x])
                for x in range(s_x, e_x + 1):
                    all_points.add((x, s_y))
    return all_points

class Simulation:
    STARTING_POS = (500, 0)
    def __init__(self, points, has_floor):
        self.has_floor = has_floor
        self.floor = max([p[1] for p in points]) + (2 if has_floor else 0)
        self.points = points
        self.num_sand = 0

    def _one_move(self, pos):
        pass

    def _add_sand(self):
        pos = Simulation.STARTING_POS
        while True:
            if self.has_floor and pos[1] == self.floor - 1:
                self.points.add(pos)
                self.num_sand += 1
                return True
            if not self.has_floor and pos[1] == self.floor:
                return False
            moved = False
            to_check = [(pos[0], pos[1] + 1), (pos[0] - 1, pos[1] + 1), (pos[0] + 1, pos[1] + 1)]
            for point in to_check:
                if point not in self.points:
                    pos = point
                    moved = True
                    break
            if not moved:
                self.points.add(pos)
                self.num_sand += 1
                return pos != Simulation.STARTING_POS
        
    def simulate(self):
        while True:
            if not self._add_sand():
                break
        return self.num_sand

def part1(input_lines):
    return Simulation(parse_input(input_lines), False).simulate()

def part2(input_lines):
    return Simulation(parse_input(input_lines), True).simulate()

example_answers = [ 24, 93 ]