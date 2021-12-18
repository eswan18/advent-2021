from copy import copy
from dataclasses import dataclass


with open('test_input.txt', 'rt') as f:
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
