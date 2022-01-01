class Board:

    def __init__(self, vals: list[list[int]]):
        self.vals = vals
        self.n_rows = len(vals)
        self.n_cols = len(vals[0])

    def __getitem__(self, key: tuple[int, int]) -> int:
        if isinstance(key, tuple):
            x, y = key
            return self.vals[y][x]
        else:
            raise TypeError

    def neighbors(self, x: int, y: int) -> dict[tuple[int, int], [int]]:
        potential_n = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        real_n = [
            (x, y) for (x, y) in potential_n
            if 0 <= x < self.n_cols
            and 0 <= y < self.n_rows
        ]
        return {n: self[n] for n in real_n}

    def __add__(self, other: int) -> 'Board':
        raw_vals = [[(x + other) for x in row] for row in self.vals]
        # Numbers above 9 wrap around.
        vals = [[x if x <= 9 else (x % 9) for x in row] for row in raw_vals]
        return self.__class__(vals)

    def vertical_append(self, other: 'Board') -> 'Board':
        self_vals = [row[:] for row in self.vals]
        other_vals = [row[:] for row in other.vals]
        return self.__class__(self_vals + other_vals)

    def horizontal_append(self, other: 'Board') -> 'Board':
        new_vals = [row_a[:] + row_b[:] for row_a, row_b in zip(self.vals, other.vals)]
        return self.__class__(new_vals)

    def __repr__(self) -> str:
        s = f'{self.__class__.__name__}([\n'
        for row in self.vals:
            s += f'    {row!r}\n'
        s += '])'
        return s

    def __str__(self) -> str:
        return '\n'.join(
            ''.join(str(x) for x in row)
            for row in self.vals
        )

