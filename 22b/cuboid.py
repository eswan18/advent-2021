from __future__ import annotations
from dataclasses import dataclass
from itertools import product
from functools import cached_property

from bound import Bound


@dataclass(frozen=True)
class Cuboid:
    x: Bound
    y: Bound
    z: Bound

    @property
    def volume(self) -> int:
        return len(self.x) * len(self.y) * len(self.z)

    def contains(self, other: Union[Cuboid, tuple[int, int, int]]) -> bool:
        '''
        Is a point or other cuboid fully within this cuboid?
        '''
        if isinstance(other, tuple):
            # Other is a point.
            x, y, z = other
            return all((
                self.x.contains(x),
                self.y.contains(y),
                self.z.contains(z),
            ))
        elif isinstance(other, Cuboid):
            return all((
                self.x.contains(other.x),
                self.y.contains(other.y),
                self.z.contains(other.z),
            ))
        else:
            raise TypeError

    def __contains__(self, other: Union[Cuboid, tuple[int, int, int]]) -> bool:
        return self.contains(other)

    @cached_property
    def corners(self) -> tuple[tuple[int, int, int], ...]:
        return tuple(product(self.x, self.y, self.z))

    def overlap(self, other: Cuboid) -> int:
        '''
        Get the volume of the overlap of two cuboids.
        '''
        if other.volume > self.volume:
            bigger, smaller = other, self
        else:
            bigger, smaller = self, other
        # Check if any corners of the smaller cuboid are within the bigger.
        running_overlap = 1
        for bound_a, bound_b in zip(self.bounds, other.bounds):
            overlap = bound_a.overlap(bound_b)
            if overlap == 0:
                return 0
            else:
                running_overlap *= overlap
        return running_overlap
        # TODO: delete
        if any(bigger.contains(pt) for pt in smaller.corners):
            return reduce(lambda x, y: x * y, (
                self.x.overlap(other.x),
                self.y.overlap(other.y), 
                self.z.overlap(other.z), 
            ))
        else:
            return 0

    @property
    def bounds(self) -> tuple[Bound, Bound, Bound]:
        return (self.x, self.y, self.z)

    @classmethod
    def from_string(cls, s: str) -> Cuboid:
        bound_strs = (a.split('=')[1] for a in s.split(','))
        x, y, z = (Bound.from_string(b) for b in bound_strs)
        return cls(x=x, y=y, z=z)
