from __future__ import annotations
from collections import Counter
from typing import Literal
from functools import reduce

pt = Literal['#', '.']

class Image:

    def __init__(self, pts: list[list[pt]], infinite_pt: pt = '.'):
        self.pts = pts
        self.n_rows = len(pts)
        self.n_cols = len(pts[0])
        self.infinite_pt = infinite_pt

    @classmethod
    def from_string(cls, s, infinite_pt: pt = '.') -> Image:
        lines = [l.strip() for l in s.split('\n')]
        pts = [list(l) for l in lines]
        return cls(pts, infinite_pt=infinite_pt)

    @property
    def n_lit(self) -> int:
        counter = reduce(lambda x, y: x + y, (Counter(row) for row in self.pts))
        return counter['#']

    def __getitem__(self, key: tuple[int, int]) -> pt:
        if isinstance(key, tuple):
            x, y = key
            if 0 <= x < self.n_cols and 0 <= y < self.n_rows:
                return self.pts[y][x]
            else:
                # Indexing to a location off the board just gets you the infinite point.
                return self.infinite_pt
        else:
            raise TypeError

    def enhance(self, key: str) -> Image:
        new_grid = ''
        for y in range(-1, self.n_rows+1):
            for x in range(-1, self.n_cols+1):
                window = [self[i, j] for j in (y-1, y, y+1) for i in (x-1, x, x+1)]
                bin_str = ''.join(window).replace('#', '1').replace('.', '0')
                loc = int(bin_str, 2)
                new_grid += key[loc]
            new_grid += '\n'
        if self.infinite_pt == '.':
            new_infinite_pt = key[0]
        else: # self.infinite_pt == '#'
            new_infinite_pt = key[511]
        return self.__class__.from_string(new_grid.strip(), infinite_pt=new_infinite_pt)


    def __repr__(self) -> str:
        s = f'{self.__class__.__name__}([\n'
        for row in self.pts:
            s += f'    {row!r}\n'
        s += '])'
        return s

    def __str__(self) -> str:
        return '\n'.join(
            ''.join(str(x) for x in row)
            for row in self.pts
        )
