from dataclasses import dataclass, field

@dataclass(frozen=True)
class Amphipod:
    color: str
    location: str
    energy: str = field(init=False)

    def __post_init__(self):
        '''
        Keep track of the color (and based on that, the energy use) of an amphipod,
        along with what room (0-3) it's in.

        Making cost_counter a list is a hack so that we get a reference, not a copy,
        and can modify it as the amphipod moves.
        '''
        self.color = self.color.lower()
        c = self.color[0]
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

    #def available_moves(self) -> ?:
        ...

