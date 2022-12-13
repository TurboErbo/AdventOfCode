def parse_input(input_lines):
    fs = {}
    cwd = fs
    for line in input_lines:
        tokens = line.split()
        if tokens[0] == "$":
            cmd = tokens[1]
            if cmd == "ls":
                pass
            elif cmd == "cd":
                arg = tokens[2]
                if arg == "/":
                    cwd = fs
                else:
                    cwd = cwd[arg]
        else:
            if tokens[0] == "dir":
                dirname = tokens[1]
                if dirname not in cwd:
                    cwd[dirname] = { ".." : cwd }
            else:
                size = int(tokens[0])
                filename = tokens[1]
                cwd[filename] = size
    return fs

def get_dir_sizes(dir):
    sum = 0
    sizes = []
    for name, item in dir.items():
        if type(item) == int:
            sum += item
        elif name != "..":
            size, subdir_sizes = get_dir_sizes(item)
            sum += size
            sizes += subdir_sizes
    sizes.append(sum)
    return sum, sizes

def part1(input_lines):
    fs = parse_input(input_lines)
    _, sizes = get_dir_sizes(fs)
    return sum(filter(lambda x: x <= 100000, sizes))

def part2(input_lines):
    fs = parse_input(input_lines)
    total, sizes = get_dir_sizes(fs)
    needed = total - 40000000
    return min(filter(lambda x: x >= needed, sizes))

example_answers = [95437, 24933642]