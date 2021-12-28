from __future__ import annotations
from dataclasses import dataclass, field

from distance import nodes

@dataclass
class Board:
    _board: dict[str, Optional[str]]

    def __getitem__(self, key) -> Optional[str]:
        '''Pure delegation.'''
        return self._board[key]

    def get_str(self, key) -> str:
        '''Get the occupant of a space, or '.' if None.'''
        value = self._board[key]
        return value if value is not None else '.'

    @classmethod
    def from_string(cls, s: str) -> Board:
        lines = s.split('\n')
        ROOM1, ROOM2, ROOM3, ROOM4 = 3, 5, 7, 9
        locations = dict.fromkeys(nodes, None)
        for line_num in (2, 3):
            for room in [ROOM1, ROOM2, ROOM3, ROOM4]:
                if room == ROOM1:
                    if line_num == 2:
                        loc = 'l'
                    else:
                        loc = 'p'
                elif room == ROOM2:
                    if line_num == 2:
                        loc = 'm'
                    else:
                        loc = 'q'
                elif room == ROOM3:
                    if line_num == 2:
                        loc = 'n'
                    else:
                        loc = 'r'
                elif room == ROOM4:
                    if line_num == 2:
                        loc = 'o'
                    else:
                        loc = 's'
                color=lines[line_num][room]
                locations[loc] = color
        return Board(locations)



    def __str__(self) -> str:
        s = '#' * 13 + '\n'
        s += '#' + ''.join(self.get_str(l) for l in 'abcdefghijk') + '#\n'
        s += '###' + self.get_str('l') + '#' + self.get_str('m')
        s += '#' + self.get_str('n') + '#' + self.get_str('o') + '###\n'
        s += '  #' + self.get_str('p') + '#' + self.get_str('q')
        s += '#' + self.get_str('s') + '#' + self.get_str('s') + '###\n'
        s += '  ' + '#' * 9
        return s

    def __iter__(self):
        return iter(self._board)


@dataclass(order=True)
class BoardState:
    iterations: int
    board: Board = field(compare=False)

def locations_of(color: str, locations: Board) -> tuple[str, str]:
    return tuple(s for s in locations if locations[s] == color)
