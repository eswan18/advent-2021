right_chars = {
    ')': '(',
    '}': '{',
    '>': '<',
    ']': '[',
}
left_chars = {v: k for (k, v) in right_chars.items()}

with open('input.txt', 'rt') as f:
    lines = [l.strip() for l in f.readlines()]

def is_corrupt(line):
    stack = []
    for c in line:
        if c not in right_chars:
            stack.append(c)
        else:
            topchar = stack.pop()
            if topchar != right_chars[c]:
                return True
    return False

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

incomplete_lines = [l for l in lines if not is_corrupt(l)]

def complete_line(line):
    stack = []
    for c in line:
        if c not in right_chars:
            stack.append(c)
        else:
            topchar = stack.pop()
            if topchar != right_chars[c]:
                raise ValueError
    # Now begin completion
    score = 0
    for c in reversed(stack):
        d = left_chars[c]
        score *= 5
        if d == ')':
            score += 1
        elif d == ']':
            score += 2
        elif d == '}':
            score += 3
        elif d == '>':
            score += 4
        else:
            raise ValueError
    return score

scores = [complete_line(line) for line in incomplete_lines]
index = len(scores) // 2
result = sorted(scores)[index]
print(result)
