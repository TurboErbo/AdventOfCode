class Node:
    def __init__(self, height, isEnd):
        self.neighbors: list[Node] = list()
        self.height = height # Only used as a helper during graph building
        self.isEnd = isEnd

def reachable(src, dst, reverse):
    if reverse:
        return ord(src) <= ord(dst) + 1
    return ord(dst) <= ord(src) + 1

def parse_input(input_lines, reverse):
    nrows = len(input_lines)
    ncols = len(input_lines[0])
    nodes: dict[tuple[int,int], Node] = {}
    UP = (-1,0)
    LEFT = (0,-1)
    start = None
    for r in range(nrows):
        for c in range(ncols):
            val = input_lines[r][c]
            if val == 'S':
                height = 'a'
            elif val == 'E':
                height = 'z'
            else:
                height = val
            node = Node(height, (height == 'a') if reverse else (val == 'E'))
            isStart = (val == 'E') if reverse else (val == 'S')
            if isStart:
                start = node
            for d in [UP, LEFT]:
                neighbor = (r+d[0],c+d[1])
                if neighbor[0] >= 0 and neighbor[0] < nrows and neighbor[1] >= 0 and neighbor[1] < ncols:
                    neighbor_node = nodes[neighbor]
                    neighbor_height = neighbor_node.height
                    if reachable(neighbor_height, height, reverse):
                        neighbor_node.neighbors.append(node)
                    if reachable(height, neighbor_height, reverse):
                        node.neighbors.append(neighbor_node)
            nodes[(r,c)] = node
    return start

def shortest_path(start: Node):
    q = [(start, 0)]
    parents = {start:None}
    while q:
        current, length = q.pop(0)
        for n in current.neighbors:
            if n.isEnd:
                path = [n]
                n = current
                while n:
                    path.append(n)
                    n = parents[n]
                return path[::-1]
            if n not in parents:
                parents[n] = current
                q.append((n, length + 1))
         
def part1(input_lines):
    start = parse_input(input_lines, False)
    return len(shortest_path(start)) - 1

def part2(input_lines):
    start = parse_input(input_lines, True)
    return len(shortest_path(start)) - 1

example_answers = [ 31, 29 ]