import re
from enum import Enum
import copy

class Resource(Enum):
    ORE = 0
    CLAY = 1
    OBSIDIAN = 2
    GEODE = 3

class State:
    def __init__(self):
        self.resource_count = [0 for _ in Resource]
        self.robot_count = [0 for _ in Resource]
        self.robot_count[Resource.ORE.value] = 1

    def can_build(self, robot_type: Resource, blueprint):
        return all([self.resource_count[r.value] >= blueprint.robot_costs[robot_type.value][r.value] for r in Resource])

    def build(self, robot_type: Resource, blueprint):
        self.robot_count[robot_type.value] += 1
        self.resource_count = [self.resource_count[r.value] - blueprint.robot_costs[robot_type.value][r.value] for r in Resource]

    def get_successors(self, blueprint):
        collect_amount = [self.robot_count[r.value] for r in Resource]
        no_build_state = copy.copy(self)
        no_build_state.resource_count = [no_build_state.resource_count[r.value] + no_build_state.robot_count[r.value] for r in Resource]
        s = [no_build_state]
        for r in Resource:
            if self.can_build(r, blueprint):
                c = copy.copy(self)
                c.build(r, blueprint)
                c.resource_count = [c.resource_count[r.value] + collect_amount[r.value] for r in Resource]
                s.append(c)
        return s

class Blueprint:
    def __init__(self, input):
        m = re.match('Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.', input)
        self.robot_costs = [[0 for _ in Resource] for _ in Resource]
        self.robot_costs[Resource.ORE.value][Resource.ORE.value] = int(m.group(1))
        self.robot_costs[Resource.CLAY.value][Resource.ORE.value] = int(m.group(2))
        self.robot_costs[Resource.OBSIDIAN.value][Resource.ORE.value] = int(m.group(3))
        self.robot_costs[Resource.OBSIDIAN.value][Resource.CLAY.value] = int(m.group(4))
        self.robot_costs[Resource.GEODE.value][Resource.ORE.value] = int(m.group(5))
        self.robot_costs[Resource.GEODE.value][Resource.OBSIDIAN.value] = int(m.group(6))

def parse_input(input_lines):
    return [Blueprint(line) for line in input_lines]

def get_max_geodes(blueprint):
    states = [State()]
    for _ in range(10):
        next_states = set()
        for s in states:
            for succ in s.get_successors(blueprint):
                next_states.add(succ)
        states = next_states
        print(len(states))
    return max([s.resource_count[Resource.GEODE.value] for s in states])

def part1(input_lines):
    blueprints = parse_input(input_lines)
    return sum(i * get_max_geodes(blueprint) for i, blueprint in enumerate(blueprints))

def part2(input_lines):
    parse_input(input_lines)

example_answers = [ 33, 'PART2_ANSWER' ]