import copy
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

# Make the board 5x as big in each direction
board_copy = copy.deepcopy(board)
for i in range(1, 5):
    new_board = board + i
    board_copy = board_copy.horizontal_append(new_board)
board_copy2 = copy.deepcopy(board_copy)
for i in range(1, 5):
    new_board = board_copy + i
    board_copy2 = board_copy2.vertical_append(new_board)
board = board_copy2

final_square = (board.n_rows - 1, board.n_cols - 1)

heap: list[Path] = []
heapq.heappush(heap, Path(0, ((0,0),)))
seen: set[tuple[int, int]] = set()

i = 0
log = True

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

    
print(f'{len(final_path)=}')
print(f'{final_risk=}')
