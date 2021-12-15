import random
from multiprocessing import Pool


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
 
with open('input.txt', 'rt') as f:
    board = Board(
        [[int(x) for x in list(l.strip())] for l in f.readlines()]
    )

final_square = (board.n_rows - 1, board.n_cols - 1)

def make_path(path: tuple[tuple[int, int]], score: int) -> tuple[list[int, int], int]:
    last_square = path[-1]
    # If next to the final square, go there.
    if (
        last_square[0] == final_square[0] and
        abs(last_square[1] - final_square[1]) == 1
        ) or (
        last_square[1] == final_square[1] and
        abs(last_square[0] - final_square[0]) == 1
    ):
        new_path = path + (final_square,)
        new_score = score + board[final_square]
        return new_path, new_score
    else:
        moves = board.neighbors(*last_square)
        moves = [
            (move, moves[move]) for move in moves
            if move not in path
        ]
        if len(moves) == 0:
            # Just an easy way to early terminate.
            return -1, -1
        if len(moves) == 1:
            (move, move_score), *_ = moves
            new_path = path + (move,)
            new_score = score + move_score
            return make_path(new_path, new_score)
        # "Randomly" select a move.
        rand_range = sum(1 / risk for _, risk in moves)
        # Random draw:
        draw = random.uniform(0, rand_range)
        if draw <= (1 / moves[0][1]):
            new_path = path + (moves[0][0],)
            new_score = score + moves[0][1]
        elif draw <= (1 / moves[0][1]) + (1 / moves[1][1]):
            new_path = path + (moves[1][0],)
            new_score = score + moves[1][1]
        elif len(moves) == 3:
            new_path = path + (moves[2][0],)
            new_score = score + moves[2][1]
        return make_path(new_path, new_score)

    
N = 1000000
paths = []
low_score = -1
for i in range(N):
    if (i % 100) == 0:
        print(f'Starting iteration {i}')
    starting_paths = ( (0, 0),)
    path, score = make_path(starting_paths, 0)
    if path != -1:
        print('FOUND A PATH')
        # paths.append((path, score))
        if low_score == -1 or score < low_score:
            low_score = score
            print(f'new low score! {low_score}')

print(min(p[1] for p in paths))
