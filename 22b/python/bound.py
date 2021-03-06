from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Bound:
    start: int
    stop: int

    def __len__(self) -> int:
        '''Length, inclusive of endpoints. Bounds are weird.'''
        return self.stop - self.start + 1
    
    def contains(self, other: Union[Bound, int]) -> bool:
        '''
        Is a point or other bound fully within this bound?
        '''
        if isinstance(other, int):
            # Other is a point.
            return self.start <= other <= self.stop
        elif isinstance(other, Bound):
            return self.start <= other.start and self.stop >= other.stop
        else:
            raise TypeError

    def __contains__(self, other: Union[Bound, int]) -> bool:
        return self.contains(other)

    def common(self, other: Bound) -> Optional[Bound]:
        '''
        Get the common segment of two bounds.
        '''
        if self.stop < other.start or self.start > other.stop:
            return None
        start = self.start if self.start >= other.start else other.start
        stop = self.stop if self.stop <= other.stop else other.stop
        if stop >= start:
            return Bound(start, stop)
        else:
            return None

    def overlap(self, other: Bound) -> int:
        '''
        Get the volume of the overlap of two bounds.
        '''
        common = self.common(other)
        if common is not None:
            return (common.stop - common.start) + 1
        else:
            return 0

    

    @classmethod
    def from_string(cls, s: str) -> Bound:
        start, stop = (int(x) for x in s.split('..'))
        return cls(start, stop)

    def __iter__(self) -> Iterator[int]:
        yield self.start
        yield self.stop

    def __str__(self) -> str:
        return f'{self.start}..{self.stop}'
