from collections import namedtuple, Counter
from dataclasses import dataclass

Point = namedtuple('Point', 'x,y')


@dataclass
class Line:
    p1: Point
    p2: Point

    def __post_init__(self):
        # Fix non-integer coordinates
        self.p1 = Point(int(self.p1.x), int(self.p1.y))
        self.p2 = Point(int(self.p2.x), int(self.p2.y))

    @property
    def horizontal(self):
        return self.p1.y == self.p2.y

    @property
    def vertical(self):
        return self.p1.x == self.p2.x

    @property
    def slope(self):
        return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)

    @property
    def max_x(self):
        return max(self.p1.x, self.p2.x)

    @property
    def max_y(self):
        return max(self.p1.y, self.p2.y)

    def covered_points(self) -> list[Point]:
        if self.horizontal:
            next_pt = lambda x, y: (x+1, y)
        elif self.vertical:
            next_pt = lambda x, y: (x, y+1)
        elif self.slope == 1:
            next_pt = lambda x, y: (x+1, y+1)
        elif self.slope == -1:
            next_pt = lambda x, y: (x+1, y-1)
        else:
            raise ValueError
        # Necessary so we only have to work in one direction.
        current_pt, end_pt = sorted((self.p1, self.p2))

        pts = []
        while current_pt != end_pt:
            pts.append(current_pt)
            current_pt = Point(*next_pt(*current_pt))
        pts.append(end_pt)
        return pts


def line_from_line(line: str) -> Line:
    # Witty name, eh?
    point_a, point_b = [Point(*pt.split(',')) for pt in line.split(' -> ')]
    return Line(point_a, point_b)


with open('input.txt', 'rt') as f:
    lines = [line_from_line(line) for line in f.readlines()]

# Lines that are either vertical or horizontal
hv_lines = [line for line in lines if line.horizontal or line.vertical]

grid_size = (max(l.max_x for l in lines), max(l.max_y for l in lines))

grid = [
    [0 for _ in range(grid_size[0] + 1)]
    for _ in range(grid_size[1] + 1)
]

def print_grid(grid):
    return
    for row in grid:
        print(row)

covered_pts = [x for l in lines for x in l.covered_points()]

for point in covered_pts:
    grid[point.y][point.x] += 1
print_grid(grid)

pt_counts = Counter(covered_pts)

result = len([val for val in pt_counts.values() if val >= 2])
print(result)
