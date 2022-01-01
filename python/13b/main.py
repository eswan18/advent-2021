with open('input.txt', 'rt') as f:
    lines = [l.strip() for l in f.readlines()]

blank_line = lines.index('')
dots = {tuple(int(x) for x in l.split(',')) for l in lines[:blank_line]}
instructions = lines[blank_line+1:]

def fold(
    dots: set[tuple[int, int]],
    axis: str,
    foldline: int,
) -> set[tuple[int, int]]:
    f = int(foldline)
    if axis == 'x':
        new_dots = {
            (x, y) if x < f else (2 * f - x, y)
            for (x, y) in dots
            if x != f
        }
    elif axis == 'y':
        new_dots = {
            (x, y) if y < f else (x, 2 * f - y)
            for (x, y) in dots
            if y != f
        }
    else:
        raise ValueError
    return new_dots

def show_dots(dots):
    max_x = max(d[0] for d in dots)
    max_y = max(d[1] for d in dots)
    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x, y) in dots:
                print('#', end='')
            else:
                print('.', end='')
        print()


for i in instructions:
    axis, foldline = i.split(' ')[-1].split('=')
    dots = fold(dots, axis=axis, foldline=foldline)

print(len(dots))
show_dots(dots)
