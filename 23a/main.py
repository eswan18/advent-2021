with open('test_input.txt', 'rt') as f:
    lines = f.readlines()

class Amphipod:
    def __init__(self, color: str, cost_counter: list, location: tuple[int, int]):
        '''
        Keep track of the color (and based on that, the energy use) of an amphipod,
        along with what room (0-3) it's in.

        Making cost_counter a list is a hack so that we get a reference, not a copy,
        and can modify it as the amphipod moves.
        '''
        self.color = color
        self.cost_counter = cost_counter
        self.location = location
        c = color[0].lower()
        if c == 'a':
            self.energy = 1
        elif c == 'b':
            self.energy = 10
        elif c == 'c':
            self.energy = 100
        elif c == 'd':
            self.energy = 1000

    def move(self, square=None, distance=None) -> None:
        # If we're just moving a set number of squares
        if distance is not None:
            self.cost_counter[0] += self.energy * distance
        # If we're moving to a new square ... that sounds hard.
        else:
            raise NotImplementedError

amphis = []
cost = [0]
ROOM1 = 3
ROOM2 = 5
ROOM3 = 7
ROOM4 = 9
for line_num in (2, 3):
    for room in [ROOM1, ROOM2, ROOM3, ROOM4]:
        loc = (line_num, room)
        amphis.append(
            Amphipod(color=lines[line_num][room], cost_counter=cost, location=loc)
        )
print(amphis)
