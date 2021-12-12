class Board:
    def __init__(self, vals: list[list[int]]):
        self.vals = vals
        self.n_rows = len(vals)
        self.n_cols = len(vals[0])

    def __getitem__(self, key):
        if isinstance(key, tuple):
            x, y = key
            return self.vals[y][x]
        else:
            raise TypeError

    def neighbors(self, x, y):
        neighbors = []
        if x > 0:
            neighbors.append(self[x-1, y])
        if x < (self.n_cols - 1):
            neighbors.append(self[x+1, y])
        if y > 0:
            neighbors.append(self[x, y-1])
        if y < (self.n_rows - 1):
            neighbors.append(self[x, y+1])
        return neighbors

    def low_points(self):
        pts = []
        for x in range(self.n_cols):
            for y in range(self.n_rows):
                ns = self.neighbors(x, y)
                val = self[x, y]
                if all(val < n for n in ns):
                    pts.append(val)
        return pts

    def total_risk(self):
        pts = self.low_points()
        return sum(p + 1 for p in pts)


    def __repr__(self) -> str:
        s = f'Board([\n'
        for row in self.vals:
            s += f'    {row!r}\n'
        s += '])'
        return s

with open('input.txt', 'rt') as f:
    board = Board(
        [list(int(x) for x in line.strip())
         for line in f.readlines()]
    )


print(board.total_risk())
