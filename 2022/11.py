import math

class Monkey:
    def __init__(self, items, operation: str, test: int, trueTarget: int, falseTarget: int):
        self.items = items
        self.operation = operation
        self.test = test
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget
        self.numItemsInspected = 0

    @classmethod
    def parse(cls, input_lines):
        items = [int(x) for x in input_lines[1].partition('Starting items:')[2].split(',')]
        operation = input_lines[2].partition('new = ')[2]
        test = int(input_lines[3].partition('divisible by ')[2])
        trueTarget = int(input_lines[4].partition('throw to monkey ')[2])
        falseTarget = int(input_lines[5].partition('throw to monkey ')[2])
        return cls(items, operation, test, trueTarget, falseTarget)

    def one_turn(self, state):
        output = []
        for item in self.items:
            item = eval(self.operation, {'old':item})
            item = state.update_worry_level(item)
            target = self.trueTarget if item % self.test == 0 else self.falseTarget
            output.append((target, item))
        self.numItemsInspected += len(self.items)
        self.items = []
        return output


class State:

    def __init__(self, input_lines, reduction_factor=3):
        self.monkeys = [Monkey.parse(chunk) for chunk in [input_lines[i:i+6] for i in range(0,len(input_lines),7)]]
        self.reduction_factor = reduction_factor
        if not self.reduction_factor:
            self.custom_reduction_factor = math.prod(m.test for m in self.monkeys)
            
    def update_worry_level(self, level):
        if self.reduction_factor:
            newlevel = level // self.reduction_factor
        else:
            newlevel = level % self.custom_reduction_factor
        return newlevel

    def one_round(self):
        for monkey in self.monkeys:
            output = monkey.one_turn(self)
            for target, item in output:
                self.monkeys[target].items.append(item)  

    def simulate(self, rounds):
        for _ in range(rounds):
            self.one_round()

    def get_monkey_business(self):
        numsInspected = sorted([m.numItemsInspected for m in self.monkeys], reverse=True)
        return numsInspected[0] * numsInspected[1]


def part1(input_lines):
    state = State(input_lines)
    state.simulate(20)
    return state.get_monkey_business()

def part2(input_lines):
    state = State(input_lines, None)
    state.simulate(10000)
    return state.get_monkey_business()

example_answers = [ 10605, 2713310158 ]

if __name__ == "__main__":
    from util import Utils
    input_lines = Utils.get_data('11.txt')
    for n in range(150, 160):
        state = State(input_lines, None)
        _, t = Utils.timed(state.simulate, n)
        print("{} rounds with reduction, returned {} in {} seconds".format(n, [m.numItemsInspected for m in state.monkeys], t))
        state = State(input_lines, 1)
        _, t = Utils.timed(state.simulate, n)
        print("{} rounds w/o  reduction, returned {} in {} seconds".format(n, [m.numItemsInspected for m in state.monkeys], t))
