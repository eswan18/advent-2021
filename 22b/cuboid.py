from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Bound:
    start: int
    stop: int

    def __len__(self) -> int:
        '''Length, inclusive of endpoints. Bounds are weird.'''
        return self.stop - self.start + 1
    
    def contains(self, other: Bound) -> bool:
        return self.start <= other.start and self.stop >= other.stop

    @classmethod
    def from_string(cls, s: str) -> Bound:
        start, stop = (int(x) for x in s.split('..'))
        return cls(start, stop)


@dataclass(frozen=True)
class Cuboid:
    x: Bound
    y: Bound
    z: Bound

    @property
    def volume(self) -> int:
        return len(self.x) * len(self.y) * len(self.z)

    def contains(self, other: Cuboid) -> bool:
        return all((
            self.x.contains(other.x),
            self.y.contains(other.y),
            self.z.contains(other.z),
        ))

    @classmethod
    def from_string(cls, s: str) -> Cuboid:
        bound_strs = (a.split('=')[1] for a in s.split(','))
        x, y, z = (Bound.from_string(b) for b in bound_strs)
        return cls(x=x, y=y, z=z)
