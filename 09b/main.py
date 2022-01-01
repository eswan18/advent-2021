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

    def neighbor_locs(self, x, y):
        neighbors = []
        if x > 0:
            neighbors.append((x-1, y))
        if x < (self.n_cols - 1):
            neighbors.append((x+1, y))
        if y > 0:
            neighbors.append((x, y-1))
        if y < (self.n_rows - 1):
            neighbors.append((x, y+1))
        return neighbors

    def low_points(self) -> list[int]:
        pts = []
        for x in range(self.n_cols):
            for y in range(self.n_rows):
                ns = self.neighbors(x, y)
                val = self[x, y]
                if all(val < n for n in ns):
                    pts.append(val)
        return pts

    def low_point_locs(self) -> list[tuple[int, int]]:
        pts = []
        for x in range(self.n_cols):
            for y in range(self.n_rows):
                ns = self.neighbors(x, y)
                val = self[x, y]
                if all(val < n for n in ns):
                    pts.append((x, y))
        return pts

    def total_risk(self):
        pts = self.low_points()
        return sum(p + 1 for p in pts)

    def basins(self) -> list[list[tuple[int, int]]]:
        return [self.basin_from_lpt(*lpt) for lpt in self.low_point_locs()]

    def basin_from_lpt(self, x, y) -> list[tuple[int, int]]:
        '''
        The basin of a given low point
        '''
        pts = [(x,y)]
        while True:
            new_pts = set()
            for pt in pts:
                ns = self.neighbor_locs(*pt)
                good_neighbors = [n for n in ns if self[n] != 9 and n not in pts]
                new_pts = new_pts.union(good_neighbors)
            if not new_pts:
                break
            else:
                pts.extend(list(new_pts))
        return pts

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


basin_sizes = [len(b) for b in board.basins()]
largest_basins = sorted(basin_sizes)[-3:]
print(largest_basins[0] * largest_basins[1] * largest_basins[2])
