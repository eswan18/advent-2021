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

    def __repr__(self) -> str:
        s = f'{self.__class__.__name__}([\n'
        for row in self.vals:
            s += f'    {row!r}\n'
        s += '])'
        return s

