def find_first_unique_substring(s, n):
    for i in range(n, len(s)):
        if len(set(s[i-n:i])) == n:
            return i

def find_first_unique_substring2(s, n):
    x = {}
    for i in range(n):
        x[s[i]] = x.get(s[i], 0) + 1
    
    for i in range(n, len(s)):
        if len(x) == n:
            return i
        if x[s[i-n]] == 1:
            del x[s[i-n]]
        else:
            x[s[i-n]] -= 1
        x[s[i]] = x.get(s[i], 0) + 1

def part1(input_lines):
    return [find_first_unique_substring2(line, 4) for line in input_lines]

def part2(input_lines):
    return [find_first_unique_substring2(line, 14) for line in input_lines]

example_answers = [
    [7, 5, 6, 10, 11],
    [19, 23, 23, 29, 26]
]

if __name__ == "__main__":
    from util import Utils
    input_line = Utils.get_data("6.txt")[0]
    print("Naive implementation returned {}, took {} seconds".format(*Utils.timed(find_first_unique_substring, input_line, 100)))
    print("Improved implementation returned {}, took {} seconds".format(*Utils.timed(find_first_unique_substring2, input_line, 100)))
