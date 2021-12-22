from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Bound:
    start: int
    stop: int

    def __len__(self) -> int:
        '''Length, inclusive of endpoints. Bounds are weird.'''
        return self.stop - self.start + 1
    
    def contains(self, other: Bound) -> bool:
        return self.start <= other.start and self.stop >= other.stop


@dataclass
class Cuboid:
    x: Bound
    y: Bound
    z: Bound

    @property
    def volume(self) -> int:
        return len(self.x) * len(self.y) * len(self.z)

    def contains(self, other: Cuboid) -> bool:
        return all(
            self.x.contains(other.x),
            self.y.contains(other.y),
            self.x.contains(other.z),
        )

