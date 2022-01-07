right_chars = {
    ')': '(',
    '}': '{',
    '>': '<',
    ']': '[',
}

with open('input.txt', 'rt') as f:
    lines = [l.strip() for l in f.readlines()]

def first_wrong(line):
    stack = []
    for c in line:
        if c not in right_chars:
            stack.append(c)
        else:
            topchar = stack.pop()
            if topchar != right_chars[c]:
                return c

def parse_pts(line):
    c = first_wrong(line)
    if not c:
        return 0
    else:
        if c == ')':
            return 3
        elif c == ']':
            return 57
        elif c == '}':
            return 1197
        elif c == '>':
            return 25137
        else:
            raise ValueError

print(sum(parse_pts(l) for l in lines))
