from __future__ import annotations
from dataclasses import dataclass, field
from itertools import product
from functools import cached_property

from bound import Bound


@dataclass(frozen=True)
class Cuboid:
    x: Bound
    y: Bound
    z: Bound
    dynamic_data: dict[str, Any] = field(default_factory=dict)

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

    def common(self, other: Cuboid) -> Optional[Cuboid]:
        '''
        Get the common space of two cuboids.
        '''
        bounds = []
        for bound_a, bound_b in zip(self.bounds, other.bounds):
            common = bound_a.common(bound_b)
            if common is None:
                return None
            else:
                bounds.append(common)
        return Cuboid(*bounds)

    def overlap(self, other: Cuboid) -> int:
        '''
        Get the volume of the overlap of two cuboids.
        '''
        common = self.common(other)
        if common is not None:
            return common.volume
        else:
            return 0
        running_overlap = 1
        for bound_a, bound_b in zip(self.bounds, other.bounds):
            overlap = bound_a.overlap(bound_b)
            if overlap == 0:
                return 0
            else:
                running_overlap *= overlap
        return running_overlap

    @property
    def bounds(self) -> tuple[Bound, Bound, Bound]:
        return (self.x, self.y, self.z)

    @classmethod
    def from_string(cls, s: str) -> Cuboid:
        bound_strs = (a.split('=')[1] for a in s.split(','))
        x, y, z = (Bound.from_string(b) for b in bound_strs)
        return cls(x=x, y=y, z=z)
    
    def __str__(self) -> str:
        return f'x={self.x},y={self.y},z={self.z}'
