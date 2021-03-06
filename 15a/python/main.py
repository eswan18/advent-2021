from dataclasses import dataclass, field
import heapq

from board import Board

@dataclass(order=True)
class Path:
    risk: int
    moves: tuple[tuple[int, int]] = field(compare=False)

 
with open('input.txt', 'rt') as f:
    board = Board(
        [[int(x) for x in list(l.strip())] for l in f.readlines()]
    )

final_square = (board.n_rows - 1, board.n_cols - 1)

heap: list[Path] = []
heapq.heappush(heap, Path(0, ((0,0),)))
seen: set[tuple[int, int]] = set()

i = 0
log = False

while True:
    path = heapq.heappop(heap)
    i += 1
    if i == 100000 and log:
        print(f'{len(path.moves)=}')
        print(f'{path.risk=}')
        i = 0
    current_square = path.moves[-1]
    # Get the squares reachable from the current point that aren't in the path already.
    next_squares = [
        point for point in board.neighbors(*current_square)
        if point not in path.moves
        and point not in seen
    ]
    # If we found an answer!
    if final_square in next_squares:
        final_path = path.moves + final_square
        final_risk = path.risk + board[final_square]
        break
    else:
        for point in next_squares:
            seen.add(point)
            new_path = Path(
                path.risk + board[point],
                path.moves + (point,)
            )
            heapq.heappush(heap, new_path)

    
#print(final_path)
print(final_risk)
