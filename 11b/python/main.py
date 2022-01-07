total_flashes = 0


class Octopi:

    def __init__(self, vals: list[list[int]]):
        self.vals = vals
        self.n_rows = len(vals)
        self.n_cols = len(vals[0])

    def __getitem__(self, key):
        if isinstance(key, tuple):
            x, y = key
            return self.vals[y][x]
        else:
            raise TypeError

    def neighbors(self, x, y):
        potential_n = [
            (x+dx, y+dy) for dx in range(-1, 2) for dy in range(-1, 2)
        ]
        real_n = [
            (x, y) for (x, y) in potential_n
            if 0 <= x < self.n_cols
            and 0 <= y < self.n_rows
        ]
        return real_n
        
    def turn(self):
        # First, the energy level of each octopus increases by 1.
        self.vals = [[x + 1 for x in row] for row in self.vals]
        # Then, any octopus with an energy level greater than 9 flashes. This increases
        # the energy level of all adjacent octopuses by 1, including octopuses that are
        # diagonally adjacent. If this causes an octopus to have an energy level greater
        # than 9, it also flashes. This process continues as long as new octopuses keep
        # having their energy level increased beyond 9. (An octopus can only flash at
        # most once per step.)
        past_flashers = []
        while True:
            flashers = [
                (x, y)
                for x in range(self.n_cols)
                for y in range(self.n_rows)
                if self[x, y] > 9 and (x, y) not in past_flashers
            ]
            if not flashers:
                break
            # Increment the neighbors
            for f in flashers:
                for x, y in self.neighbors(*f):
                    self.vals[y][x] += 1
            past_flashers.extend(flashers)
        # Finally, any octopus that flashed during this step has its energy level set to
        # 0, as it used all of its energy to flash.
        for x, y in past_flashers:
            self.vals[y][x] = 0
        global total_flashes 
        total_flashes += len(past_flashers)
        if len(past_flashers) == (self.n_rows * self.n_cols):
            return True
        else:
            return False
            

    def __repr__(self) -> str:
        s = f'Octopi([\n'
        for row in self.vals:
            s += f'    {row!r}\n'
        s += '])'
        return s


with open('input.txt', 'rt') as f:
    octo = Octopi(
        [list(int(x) for x in line.strip())
         for line in f.readlines()]
    )

for i in range(1, 2000):
    superflash = octo.turn()
    if superflash:
        print(i)
        break
