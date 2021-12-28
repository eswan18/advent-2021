from board import Board

with open('test_input.txt', 'rt') as f:
    board = Board.from_string(f.read())
print(board)
lksjdflksdjf

situations: tuple[int, dict[str, Optional[str]]] = [] # {distance, locations}
n_iter = 0
while True:
    # If we can move an amphipod to its eventual home without blocking another, we
    # should always do that.
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
