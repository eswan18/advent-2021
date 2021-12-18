from copy import copy
from itertools import product
from dataclasses import dataclass


with open('input.txt', 'rt') as f:
    coord_str = f.readline().split(':')[1].strip()
    x_str, y_str = [s.split('=')[1] for s in coord_str.split(', ')]
    x_min, x_max = [int(x) for x in x_str.split('..')]
    y_min, y_max = [int(y) for y in y_str.split('..')]

@dataclass
class Probe:
    dx: int = 0
    dy: int = 0
    x: int = 0
    y: int = 0

    def step(self):
        self.x += self.dx
        self.y += self.dy
        if self.dx > 0:
            self.dx -= 1
        elif self.dx < 0:
            self.dx += 1
        self.dy -= 1

    def in_target(self) -> bool:
        return (
            x_min <= self.x <= x_max
            and
            y_min <= self.y <= y_max
        )
    
    def ever_in_target(self, verbose: bool = False) -> bool:
        p = copy(self)
        while p.y > y_min or p.dy > 0:
            if verbose:
                print(p)
            p.step()
            if p.in_target():
                return True
        return False

    @property
    def path(self) -> list[tuple[int, int]]:
        result = []
        p = copy(self)
        result.append((p.x, p.y))
        while p.y > y_min or p.dy > 0:
            p.step()
            result.append((p.x, p.y))
            if p.in_target():
                break
        return result


# These maximum numbers are arbitrary and I feel bad about it.
dx_range = range(0, x_max+20)
dy_range = range(y_min, (100 + y_max + x_min))

all_time_high_y = y_min
i = 0
for dx, dy in product(dx_range, dy_range):
    p = Probe(dx=dx, dy=dy)
    if p.ever_in_target():
        high_y = max(y for (x, y) in p.path)
        print(f'found a high y ({high_y}) at {p}')
        all_time_high_y = max(high_y, all_time_high_y) 

print(all_time_high_y)
