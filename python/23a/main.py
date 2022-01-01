from board import Board, BoardState
import heapq

with open('test_input.txt', 'rt') as f:
    board = Board.from_string(f.read())

heap: list[BoardState] = []
heapq.heappush(heap, BoardState(0, board))
seen = set[Board]

while True:
    board_state = heapq.heappop(heap)
    if board_state.board.is_solved:
        final_cost = board_state.cost
        break
    # If we can move an amphipod to its eventual home without blocking another, we
    # should always do that.
    available_moves = board_state.board.available_moves()
    for a in ('A', 'B', 'C', 'D'):
        a_at = locations_of(a)
        for l in locations:
            ...
    n_iter += 1
    if is_solved(locations):
        break
print(f'{n_iter=}')


def next_locs(locations: dict[str, Optional[str]]) -> list[dict[str, Optional[str]]]:
    n_iter += 1
    return min(fastest_solve(locations, n_iter))
