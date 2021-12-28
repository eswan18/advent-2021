from __future__ import annotations
from operator import xor
from functools import reduce
from dataclasses import dataclass, field

from locations import rooms
from distance import nodes

@dataclass(frozen=True)
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

    @cache
    def locations_of(color: str) -> tuple[str, str]:
        return tuple(s for s in self if self[s] == color)

    def with_move(_from: str, _to: str) -> Board:
        occupant = self[_from]
        if occupant is None:
            raise ValueError('Invalid move; no occupant of space')
        new_locations = self._board.copy()
        new_locations[_from] = None
        new_locations[_to] = occupant
        return Board(new_locations)

    def available_moves(self) -> list[tuple[tuple[str, str], int]]:
        '''
        Get a list of ((from, to), cost) tuples.
        '''
        moves = []
        a1, a2 = locations_of(a)
        b1, b2 = locations_of(b)
        c1, c2 = locations_of(c)
        d1, d2 = locations_of(d)


    def is_solved(self) -> bool:
        for loc, color in rooms.items():
            if self[loc] != color:
                return False
        return True

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

    def __eq__(self, other: Board) -> bool:
        if not isinstance(other, Board):
            return NotImplemented
        return self._board == other._board

    def __hash__(self) -> int:
        if hasattr(self, '_hash'):
            return self._hash
        else:
            b = self._board
            h = reduce(xor, hash(b[l]) for l in 'abcdefghijklmnopqrs')
            self._hash = h
            return h


@dataclass(order=True)
class BoardState:
    cost: int
    board: Board = field(compare=False)
