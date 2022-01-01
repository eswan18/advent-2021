from __future__ import annotations
from dataclasses import dataclass, field
from itertools import product, combinations
from functools import cached_property, reduce

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

    def uncovered_volume(self, layers: Iterable[Cuboid]) -> int:
        '''
        How much of this cuboid's volume is left uncovered, given other cuboids?
        '''
        # Find the spaces where this cuboid overlaps with other, already-seen layers --
        # that volume shouldn't be included in the volume it covers.
        overlapping_cuboids = [
            l for l in (l.common(self) for l in layers) if l is not None
        ]

        naive_overlapping_volume = sum(oc.volume for oc in overlapping_cuboids)
        # Overlapping areas may overlap with each other, causing the overlap to be
        # double- (or triple-, or ...) counted.
        redundant_overlap_volume = 0
        for n in range(2, len(overlapping_cuboids) + 1):
            for combo in combinations(overlapping_cuboids, n):
                common = reduce(lambda a, b: a.common(b) if a and b else None, combo)
                if common:
                    # I hate that I don't know why this works.
                    if n % 2 == 0:
                        redundant_overlap_volume += common.volume
                    else:
                        redundant_overlap_volume -= common.volume

        overlapping_volume = naive_overlapping_volume - redundant_overlap_volume
        
        # Figure out how much volume this new cuboid covers.
        covered_volume = self.volume - overlapping_volume
        return covered_volume

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
