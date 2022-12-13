import re
from collections import namedtuple

#State = namedtuple('State', ['open_valves', 'locations'])

def parse_input(input_lines):
    valves = {}
    for line in input_lines:
        m = re.match('Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line)
        v = m.group(1)
        f = int(m.group(2))
        n = m.group(3).split(', ')
        valves.update({v:(f,n)})
    return valves

def solve(valves, open_valves: set, location: str, time_left: int, memo) -> int:
    if time_left == 0:
        return 0
    key = (serialize(open_valves), location, time_left)
    if key in memo:
        return memo[key]
    candidates = []
    for n in valves[location][1]:
        candidates.append(solve(valves, open_valves, n, time_left - 1, memo))
    if location not in open_valves and valves[location][0] != 0:
        candidates.append(solve(valves, open_valves | set([location]), location, time_left - 1, memo))
    winner = max(candidates)
    released = sum(valves[x][0] for x in open_valves)
    value = winner + released
    memo[key] = value
    return value


class Part2:

    def __init__(self):
        self.valves = None
        self.valve_indices = {}
        self.location_indices = {}
        self.memo = {}

    def _init_indices(self):
        valve_index = 0
        location_index = 0
        for valve, (flow, _) in self.valves.items():
            if flow != 0:
                self.valve_indices[valve] = valve_index
                valve_index += 1
            self.location_indices[valve] = location_index
            location_index += 1
        print(self.valve_indices)
        print(self.location_indices)            

    def _get_key(self, open_valves, locations, time_left):
        key = 0
        for v in open_valves:
            key |= (1 << self.valve_indices[v])
        key |= (self.location_indices[locations[0]] << 15)
        key |= (self.location_indices[locations[1]] << 21)
        key |= time_left << 27
        return key

    def solve(self, valves, start_locations, time_left: int) -> int:
        self.valves = valves
        self._init_indices()
        return self.solve_recursive(set(), start_locations, time_left)

    def solve_recursive(self, open_valves: set, locations, time_left: int) -> int:
        if time_left == 0:
            return 0 #(0, [State(open_valves, locations)])
        key = self._get_key(open_valves, locations, time_left)
        if key in self.memo:
            return self.memo[key]
        my_loc, eleph_loc = locations
        candidates = []
        for my_next, eleph_next in [(i,j) for i in (self.valves[my_loc][1] + [my_loc]) for j in (self.valves[eleph_loc][1] + [eleph_loc])]:
            new_open_valves = open_valves.copy()
            if my_loc == my_next:
                if my_loc not in open_valves and self.valves[my_loc][0] != 0:
                    new_open_valves.add(my_loc)
                else:
                    continue
            if eleph_loc == eleph_next:
                if eleph_loc not in open_valves and self.valves[eleph_loc][0] != 0:
                    new_open_valves.add(eleph_loc)
                else:
                    continue
            candidates.append(self.solve_recursive(new_open_valves, (my_next, eleph_next), time_left - 1))
        winner = max(candidates)
        released = sum(self.valves[x][0] for x in open_valves)
        value = winner + released
        self.memo[key] = value
        if(len(self.memo) % 1000000 == 0):
            print("Memo size:",len(self.memo))
        return value


def serialize(open_valves):
    return ''.join(open_valves)

def part1(input_lines):
    valves = parse_input(input_lines)
    memo = {}
    result = solve(valves, set(), 'AA', 30, memo)
    return result

def part2(input_lines):
    valves = parse_input(input_lines)
    result = Part2().solve(valves,  ('AA','AA'), 26)
    return result

example_answers = [ 1651, 1707 ]
skip_part1 = True
#only_test = True